# Research Assistant Chatbot

An intelligent research assistant powered by LangChain and Anthropic's Claude that helps you conduct research and generate structured research papers. The chatbot uses web search, Wikipedia, and custom tools to gather information and format it into a structured output.

## Features

- **Web Search**: Uses DuckDuckGo to search the web for current information
- **Wikipedia Integration**: Fetches relevant information from Wikipedia
- **Structured Output**: Returns research results in a structured format with:
  - Top findings
  - Summary
  - Sources
  - Tools used
- **Save Functionality**: Automatically saves research output to text files
- **Agent-based Architecture**: Uses LangChain agents for intelligent tool selection

## Prerequisites

- Python 3.8 or higher
- Anthropic API key (Claude)

## Installation

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd chatbot
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root and add your Anthropic API key:
   ```env
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   ```

## Usage

1. **Activate your virtual environment** (if not already activated)

   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Run the chatbot**

   ```bash
   python main.py
   ```

3. **Enter your research query**
   The chatbot will prompt you with: "What can i help you research?"

   Example queries:

   - "Research the impact of artificial intelligence on healthcare"
   - "Find information about climate change effects on agriculture"
   - "What are the latest developments in quantum computing?"

4. **View the results**
   The chatbot will:
   - Search the web and Wikipedia for relevant information
   - Structure the findings into a research format
   - Display the results in the terminal
   - Save the output to `research_output.txt`

## Project Structure

```
chatbot/
├── main.py              # Main application file
├── tools.py             # Custom tools and utilities
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore rules
├── README.md           # This file
├── .env                # Environment variables (create this)
└── venv/               # Virtual environment (created during setup)
```

## Tools Available

The research assistant has access to three main tools:

1. **DuckDuckGo Search** (`ddg_search`)

   - Searches the web for current information
   - Useful for finding recent developments and news

2. **Wikipedia Query** (`wiki_tool`)

   - Fetches information from Wikipedia
   - Provides reliable, encyclopedic information

3. **Save Tool** (`save_to_txt`)
   - Saves research output to a text file
   - Includes timestamps for organization

## Output Format

The chatbot returns structured research data in the following format:

```python
class ResearchResponse(BaseModel):
    top: str           # Key findings
    summary: str       # Comprehensive summary
    source: list[str]  # List of sources used
    tools_used: list[str]  # Tools that were utilized
```

## Dependencies

- **langchain**: Core framework for building LLM applications
- **langchain-anthropic**: Integration with Anthropic's Claude models
- **langchain-community**: Community-contributed tools and utilities
- **python-dotenv**: Environment variable management
- **pydantic**: Data validation and parsing
- **wikipedia**: Wikipedia API wrapper
- **duckduckgo-search**: Web search functionality

## Configuration

### Model Configuration

The chatbot uses Claude Sonnet 4 (claude-sonnet-4-5-20250929) by default. You can modify this in `main.py`:

```python
llm = ChatAnthropic(model="claude-sonnet-4-5-20250929")
```

### Wikipedia Configuration

Wikipedia results are limited to 1 result with a maximum of 100 characters. You can adjust this in `tools.py`:

```python
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
```

## Troubleshooting

### Common Issues

1. **API Key Error**

   - Ensure your `.env` file contains a valid `ANTHROPIC_API_KEY`
   - Check that the API key has sufficient credits

2. **Import Errors**

   - Make sure all dependencies are installed: `pip install -r requirements.txt`
   - Verify your virtual environment is activated

3. **Search Issues**
   - Check your internet connection
   - Some search queries might be rate-limited

### Getting Help

If you encounter issues:

1. Check that all dependencies are properly installed
2. Verify your API key is correct and has credits
3. Ensure your internet connection is stable
4. Check the console output for detailed error messages

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- [LangChain](https://langchain.com/) for the framework
- [Anthropic](https://www.anthropic.com/) for Claude
- [DuckDuckGo](https://duckduckgo.com/) for search functionality
- [Wikipedia](https://www.wikipedia.org/) for encyclopedic information
