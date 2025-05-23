# osmosisExamples

This directory contains example code demonstrating how to use osmosis-ai with various LLM libraries.

## Prerequisites

Before running these examples, make sure you have:

1. Installed osmosis-ai and its dependencies
2. Set up environment variables for your API keys

```bash
# Copy the sample .env file (from the project root)
cp ../.env.sample .env

# Edit the .env file with your API keys
```

Edit the `.env` file to add your API keys:

```
# Required for logging
OSMOSIS_API_KEY=your_osmosis_api_key_here

# Optional: Only needed if you're using these services
ANTHROPIC_API_KEY=your_anthropic_key_here
OPENAI_API_KEY=your_openai_key_here
```

## Examples

### Comprehensive Example

`combined_example.py` provides a full demonstration of osmosis-ai with multiple LLM providers:

```bash
python examples/combined_example.py
```

This example:
- Initializes osmosis-ai
- Makes API calls to Anthropic Claude (if available)
- Makes API calls to OpenAI GPT (if available)
- Demonstrates LangChain integration (if available)
- Shows how to toggle OSMOSIS logging on and off

### Performance Profiler

`profiler_example.py` measures and compares the execution times for different integrations with and without osmosis-ai:

```bash
python examples/profiler_example.py
```

This example:
- Tests OpenAI, Anthropic, LangChain-OpenAI, and LangChain-Anthropic
- Runs each integration with and without osmosis-ai
- Calculates performance differences and provides a detailed comparison
- Helps identify any overhead introduced by osmosis-ai

### Individual Provider Examples

Each example demonstrates osmosis-ai with a specific provider:

- **Anthropic**: `anthropic_example.py` - Shows how to use osmosis-ai with the Anthropic Claude API
- **OpenAI**: `openai_example.py` - Shows how to use osmosis-ai with the OpenAI API
- **LangChain**: `langchain_example.py` - Shows how to use osmosis-ai with LangChain

Run any example with:

```bash
python examples/[example_file].py
```

### Tests

`test_examples.py` contains unit tests for osmosis-ai functionality. Run with:

```bash
pytest examples/test_examples.py
```

## Troubleshooting

If you encounter errors:

1. **API Key Issues**: Make sure you've set up all required API keys in the `.env` file
2. **Missing Dependencies**: Install dependencies for the LLM provider you want to use:
   ```bash
   # For Anthropic
   pip install anthropic
   
   # For OpenAI
   pip install openai
   
   # For LangChain
   pip install langchain-core
   ```
3. **OSMOSIS Connectivity**: Ensure your OSMOSIS API key is valid and the service is accessible 