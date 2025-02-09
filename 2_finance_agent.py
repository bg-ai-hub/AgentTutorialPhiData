from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.openai import OpenAIChat
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools

load_dotenv()

def get_company_symbol(company: str) -> str:
    """Use this function to get the symbol for a company

    Args:
        company (str): The name of the company

    Returns:
        str: The symbol for the company
    """
    symbols={
        "Phidata" : "MSFT",
        "Tesla" : "TSLA",
        "Infosys": "INFY",
        "Apple": "APPL",
        "Microsoft":"MSFT",
        "Amazon": "AMZN",
        "Google": "GOOGL"
    }

    return symbols.get(company, "Unknown")


agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True,
                         analyst_recommendations=True,
                         stock_fundamentals=True,
                         company_news=True), get_company_symbol],
    show_tool_calls=True,
    markdown=True,
    instructions=["Use tables to display data.",
                  "If you dont know the company symbol, please use get_company_symbol tool, even if it is not a public company"]
)

agent_openai = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[YFinanceTools(stock_price=True,
                         analyst_recommendations=True,
                         stock_fundamentals=True,
                         company_news=True), get_company_symbol],
    show_tool_calls=True,
    markdown=True,
    instructions=["Use tables to display data.",
                  "If you dont know the company symbol, please use get_company_symbol tool, even if it is not a public company"]
)

#agent.print_response("Summarise and compare analyst recommendations and fundamentals for TSLA and Phidata")
agent_openai.print_response("Summarise and compare analyst recommendations and fundamentals for TSLA and Phidata")
