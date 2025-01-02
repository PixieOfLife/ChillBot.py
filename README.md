# ChillBot.py
An API wrapper for ChillBot's API.

[![ChillBot.py](https://snyk.io/advisor/python/ChillBot.py/badge.svg)](https://snyk.io/advisor/python/ChillBot.py)

### Installation
`pip install -U ChillBot.py`

### Quick Example
Here's an example where you can get the user top 10 music data
```py
import asyncio
from ChillBot import Music

async def main():
    data = await Music.get_top_ten("123") # Replace 123 with Discord user ID
    print(data)

asyncio.run(main())
```
