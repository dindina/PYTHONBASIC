import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = [
        "https://www.example.com",
        "https://www.python.org",
        "https://www.google.com"
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)  # Run all fetches concurrently

        for url, response_text in zip(urls, responses):
            print(f"Content from {url[:30]}: {response_text[:50]}...")

if __name__ == "__main__":
    asyncio.run(main())