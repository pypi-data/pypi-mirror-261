### PyWebSolutions API Python Library

This is a Python library for interacting with the PyWeb Moderator API. The library provides both synchronous and asynchronous methods for making requests to the PyWeb Moderator API, allowing you to easily integrate PyWebSolutions functionality into your Python applications.

## Usage
Synchronous API:

```python
import pyweb_moderator_api

text = "Example text"

with pyweb_moderator_api.SyncAPI(token="your_api_token") as client:
    result = client.getClass(text)

text_class = result.text_class
time_taken = result.time_taken
confidence = result.confidence
unique_id = result.unique_id
balance = result.balance
label = result.label

print(f"Text class: {text_class}\nLabel: {label}\nTime taken: {time_taken}\nConfidence: {confidence}\nId: {unique_id}\nRemaining balance: {balance}")
```

Asynchronous API:

```python
import pyweb_moderator_api
import asyncio

async def main():
    text = "Example text"

    async with pyweb_moderator_api.AsyncAPI(token="your_api_token") as client:
        result = await client.getClass(text)

    text_class = result.text_class
    time_taken = result.time_taken
    confidence = result.confidence
    unique_id = result.unique_id
    balance = result.balance
    label = result.label

    print(f"Text class: {text_class}\nLabel: {label}\nTime taken: {time_taken}\nConfidence: {confidence}\nId: {unique_id}\nRemaining balance: {balance}")

asyncio.run(main())
```

Replace "your_api_token" with your actual API key from telegram bot https://t.me/RuModeratorAI_API_Bot.

API endpoint URL: http://pywebsolutions.ru:30
API documentation: http://pywebsolutions.ru:30/docs