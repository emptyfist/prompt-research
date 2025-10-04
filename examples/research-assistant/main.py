from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool  # your custom tools

load_dotenv()

# Structured output model with source attribution
class ResearchResponse(BaseModel):
    top: str
    summary: str
    source: list[str]
    tools_used: list[str]
    source_attribution: dict[str, str]  # NEW: key=piece of info, value=source

llm = ChatAnthropic(model="claude-sonnet-4-5-20250929", temperature=0)

parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that generates research notes.

            Always consider THREE sources when answering:
            1. Your own internal knowledge (Anthropic model reasoning).
            2. The Search tool (for the latest info).
            3. The Wiki tool (for background knowledge).

            For every fact in your summary:
            - Clearly record its source in `source_attribution` as a key-value pair.
              Example: {{ "Eiffel Tower is in Paris": "Wiki", "Ethereum Shanghai upgrade 2023": "Search" }}

            Wrap the final output strictly in this format:\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

tools = [search_tool, wiki_tool, save_tool]

agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

query = input("Enter your research topic: ")
raw_response = agent_executor.invoke({"query": query})

# Try to parse into structured object
try:
    structured_response = parser.parse(raw_response.get("output")[0]["text"])
    print("\n=== Structured Research Response ===")
    print(structured_response.json(indent=2))
except Exception as e:
    print("Error parsing response:", e, "\nRaw response:", raw_response)
