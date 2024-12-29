# ChillBot.py
An API wrapper for ChillBot's API.

### Quick Example
Here's an example where you can get the user top 10 music data
```py
import asyncio
from ChillBot import Music

async def main():
    await Music.get_top_ten(123)

asyncio.run(main())
```