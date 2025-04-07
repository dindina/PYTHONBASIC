import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)
    print("Data fetched!")
    return {"key": "value"}

async def process_data():
    print("Processing...")
    data = await fetch_data()  # Pause until fetch_data completes
    print(f"Data received: {data}")

async def main():
    await process_data()

asyncio.run(main())