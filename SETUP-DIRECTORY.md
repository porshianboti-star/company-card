# חיבור אמיתי לספריית עובדים — Google Workspace / Microsoft 365

עד עכשיו כפתורי "Connect" הביאו משתמשי דמו. עכשיו הם עושים **חיבור OAuth אמיתי מהדפדפן**: האדמין של הארגון מתחבר ומאשר, והמערכת מושכת את המשתמשים האמיתיים ישירות מ־Google Directory API / Microsoft Graph. אין שרת ואין סוד — רק **Client ID ציבורי** אחד לכל ספק, שמדביקים ב־`app/config.js`.

חשוב: את שני השלבים האלה חייב לבצע **אדמין של הארגון** (Workspace admin / Entra admin), כי משיכת ספריית המשתמשים דורשת הרשאת אדמין ואישור (admin consent). זה חד־פעמי.

---

## Google Workspace (5–10 דקות, אדמין)

1. היכנס ל־**console.cloud.google.com** → צור/בחר פרויקט.
2. **APIs & Services → Library** → הפעל את **Admin SDK API**.
3. **APIs & Services → OAuth consent screen** → סוג **Internal** (לארגון שלך) → מלא שם אפליקציה ואימייל תמיכה → שמור.
4. **APIs & Services → Credentials → Create credentials → OAuth client ID** → סוג **Web application**.
   - תחת **Authorized JavaScript origins** הוסף את כתובות האתר:
     `https://company-card.com` , `https://www.company-card.com` , וגם `https://steady-cendol-c884c0.netlify.app` (הכתובת הזמנית), ולפיתוח מקומי `http://localhost:8787`.
   - צור — תקבל **Client ID** (מחרוזת שנגמרת ב־`.apps.googleusercontent.com`).
5. פתח `app/config.js` והדבק: `googleClientId: "‏…‎.apps.googleusercontent.com",`

עכשיו הכפתור "Connect Google Workspace" יפתח חלון התחברות אמיתי של Google; אחרי שהאדמין מאשר — כל המשתמשים בארגון נמשכים אוטומטית (שם, תפקיד, אימייל, טלפון, מחלקה).

## Microsoft 365 / Entra ID (5–10 דקות, אדמין)

1. היכנס ל־**entra.microsoft.com** (או portal.azure.com → Microsoft Entra ID).
2. **App registrations → New registration** → תן שם (למשל CompanyCard) → תחת **Redirect URI** בחר פלטפורמה **Single-page application (SPA)** והזן את כתובת האתר, למשל `https://company-card.com/app/onboarding.html` (וגם כתובת ה־Netlify הזמנית).
3. אחרי היצירה, בעמוד **Overview** העתק את **Application (client) ID**.
4. **API permissions → Add a permission → Microsoft Graph → Delegated** → הוסף **User.Read.All** ו־**Directory.Read.All** → לחץ **Grant admin consent**.
5. פתח `app/config.js` והדבק: `msClientId: "‏…‎",` (ה־Application client ID).

עכשיו הכפתור "Connect Microsoft 365" יפתח התחברות אמיתית; אחרי אישור האדמין — המשתמשים נמשכים מ־Microsoft Graph.

---

## הערות

- **בלי Client ID** — הכפתורים לא מביאים דמו יותר; הם מציגים את שלבי ההקמה הקצרים האלה. שום נתון מזויף לא נכנס למערכת.
- **אבטחה** — ה־Client ID הוא ציבורי לפי התכנון (אין client secret). ההתחברות והאישור קורים בצד Google/Microsoft; אנחנו רק מקבלים token זמני בדפדפן וקוראים איתו את רשימת המשתמשים.
- **CSV / הוספה ידנית** — עובדים כמו קודם, בלי צורך בהקמה.
- אחרי הדבקת ה־Client IDs, בצע commit/deploy (או תן לי לעשות זאת) כדי שהחיבור יעבוד גם באתר החי.
