#!/bin/bash
# CompanyCard — start the local server (double-click me)
cd "$(dirname "$0")"

if ! command -v node >/dev/null 2>&1; then
  echo ""
  echo "  Node.js is not installed on this Mac."
  echo "  Opening the download page — install the LTS version, then run me again."
  echo ""
  open "https://nodejs.org/en/download"
  read -n 1 -s -r -p "  Press any key to close..."
  exit 1
fi

# open the browser once the server is up
( sleep 1.5; open "http://localhost:8787" ) &

echo ""
echo "  Starting CompanyCard…  (close this window to stop the server)"
echo ""
exec node server/app-server.js
