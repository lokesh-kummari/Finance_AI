from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


web_search_agent=Agent(
    name='web_search_agent',
    role='search',
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=[
        "search for 'llama' on DuckDuckGo",
        "Always include sources",
    ],
    show_tool_calls=True,
    markdown=True
)

financial_agent=Agent(
    name='financial_agent',
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True,company_news=True)],
    instructions=[
       "use tables to display the data",
    ],
    show_tool_calls=True,
    markdown=True
)

multi_ai_agent=Agent(
    team=[web_search_agent,financial_agent],
    instructions=[
        "Use the web_search_agent to search for 'llama'",
        "Use the financial_agent to get the stock price, analyst recommendations, stock fundamentals, and company news for 'AAPL'",
        "Always include sources",
    ],
    show_tool_calls=True,
    markdown=True
)

multi_ai_agent.print_response("Summarize the stock price, analyst recommendations, stock fundamentals, and company news for 'NVDA'",stream=True)