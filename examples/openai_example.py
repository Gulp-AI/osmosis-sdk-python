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
    # Import OpenAI after osmosis_ai is initialized
    from openai import OpenAI

    # Get API key from environment
    api_key = os.environ.get("OPENAI_API_KEY")

    # Create the OpenAI client
    client = OpenAI(api_key=api_key)

    # Make a request to GPT
    print("Making request to GPT...")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=150,
        messages=[
            {
                "role": "user",
                "content": "Hello, GPT! What are three interesting applications of machine learning in healthcare?",
            }
        ],
    )

    # Print the response
    print("\nResponse from GPT:")
    print(response.choices[0].message.content)

    print("\nAll interactions above have been logged via osmosis_ai!")

except Exception as e:
    print(f"Error: {str(e)}")
    import traceback

    traceback.print_exc()
