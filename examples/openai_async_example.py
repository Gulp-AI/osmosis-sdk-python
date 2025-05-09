"""
Example demonstrating how to use osmosis-ai with OpenAI
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Import and initialize osmosis_ai
import osmosis_ai

# Initialize with OSMOSIS API key
osmosis_api_key = os.environ.get("OSMOSIS_API_KEY")
osmosis_ai.init(osmosis_api_key)

# Print messages to console for demonstration
osmosis_ai.set_log_destination(osmosis_ai.LogDestination.STDOUT)

print("OpenAI Integration Example\n")

try:
    # Get API key from environment
    api_key = os.environ.get("OPENAI_API_KEY")

    # Example with async client (commented out by default)

    print("\nAsync Client Example")
    from openai import AsyncOpenAI
    import asyncio

    async def call_openai_async():
        async_client = AsyncOpenAI(api_key=api_key)
        response = await async_client.chat.completions.create(
            model="gpt-4o-mini",
            max_tokens=150,
            messages=[
                {
                    "role": "user",
                    "content": "Hello, async GPT! What are three emerging trends in data science?",
                }
            ],
        )
        print("\nAsync Response from GPT:")
        print(response.choices[0].message.content)
        return response

    # Run the async example
    asyncio.run(call_openai_async())

    print("\nAll interactions above have been logged via osmosis_ai!")

except Exception as e:
    print(f"Error: {str(e)}")
    import traceback

    traceback.print_exc()
