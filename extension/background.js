/* CompanyCard extension — background service worker (MV3).
   Holds the user's cards in chrome.storage.local. No network access at all:
   the extension has no host permissions and never calls an API. */

async function saveCards(cards) {
  if (!Array.isArray(cards) || !cards.length) return { ok: false, error: "no cards" };
  const clean = cards.filter(c => c && c.id).slice(0, 25);
  const prev = await chrome.storage.local.get(["activeId"]);
  const stillThere = clean.some(c => c.id === prev.activeId);
  await chrome.storage.local.set({
    cards: clean,
    updated: Date.now(),
    activeId: stillThere ? prev.activeId : clean[0].id
  });
  return { ok: true, count: clean.length };
}

/* From the content script on company-card.com/app/*. */
chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
  (async () => {
    try {
      if (!msg || !msg.type) return sendResponse({ ok: false, error: "bad message" });
      if (msg.type === "syncCards") return sendResponse(await saveCards(msg.cards));
      if (msg.type === "setActive") {
        await chrome.storage.local.set({ activeId: msg.id });
        return sendResponse({ ok: true });
      }
      if (msg.type === "status") {
        const o = await chrome.storage.local.get(["cards", "activeId", "updated"]);
        return sendResponse({ ok: true, cards: o.cards || [], activeId: o.activeId || "", updated: o.updated || 0 });
      }
      return sendResponse({ ok: false, error: "unknown type" });
    } catch (e) { return sendResponse({ ok: false, error: String((e && e.message) || e) }); }
  })();
  return true; // async response
});

/* From company-card.com pages (externally_connectable) — lets the site push a
   card straight to the extension and check whether it is installed. */
chrome.runtime.onMessageExternal.addListener((msg, sender, sendResponse) => {
  (async () => {
    try {
      if (!msg || !msg.type) return sendResponse({ ok: false, error: "bad message" });
      if (msg.type === "ping") return sendResponse({ ok: true, installed: true, id: chrome.runtime.id });
      if (msg.type === "syncCards") return sendResponse(await saveCards(msg.cards));
      return sendResponse({ ok: false, error: "unknown type" });
    } catch (e) { return sendResponse({ ok: false, error: String((e && e.message) || e) }); }
  })();
  return true;
});
