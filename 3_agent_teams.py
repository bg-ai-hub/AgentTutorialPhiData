from openai import models
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

web_agent = Agent(
    name="Web Agent",
    #model=Groq(id="llama-3.3-70b-versatile"),
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    markdown=True
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    #model=Groq(id="llama-3.3-70b-versatile"),
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[YFinanceTools(stock_price=True,
                         analyst_recommendations=True,
                         stock_fundamentals=True,
                         company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls = True,
    markdown=True
)

agent_team = Agent(
    #model=Groq(id="llama-3.3-70b-versatile"),
    model=OpenAIChat(id="gpt-4o-mini"),
    team=[web_agent,finance_agent],
    instructions=["Always include sources","Use tables to display data"],
    show_tool_calls=True,
    markdown=True
)

agent_team.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)