import requests
import webbrowser
import time
import sys
import os
import random

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
║  🧪 BRUTEFORCE PROXY SIMULATOR (SAFE)     ║
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

# Inputs
username = input("👤 Enter simulated username: ")
wordlist_path = input("📁 Enter path to your wordlist (e.g., w.txt): ")
proxy_file = input("🌐 Enter path to proxy list (e.g., proxies.txt): ")

# Load passwords
try:
    with open(wordlist_path, "r") as f:
        passwords = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print("❌ Wordlist file not found.")
    exit()

# Load proxies
try:
    with open(proxy_file, "r") as f:
        proxies_list = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print("❌ Proxy list file not found.")
    exit()

# Simulated brute force loop
def get_random_proxy():
    proxy = random.choice(proxies_list)
    return {
        "http": proxy,
        "https": proxy
    }

correct_password = "admin123"  # For simulation only

print("\n🚀 Starting brute-force simulator...\n")
attempt = 0
session = requests.Session()

for password in passwords:
    attempt += 1
    proxy = get_random_proxy()

    print(f"🔐 Attempt {attempt}: Trying '{password}' using proxy {proxy['http']}")

    time.sleep(1)  # Delay to simulate request

    if password == correct_password:
        print(f"\n✅ SUCCESS: Correct password found: {password}")
        break
    else:
        print("❌ Incorrect password.\n")

    if attempt % 3 == 0:
        print("🔁 Switching proxy for next attempts...\n")
