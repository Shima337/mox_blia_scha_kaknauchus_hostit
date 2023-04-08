from langchain import OpenAI
from dotenv import load_dotenv
import os 
from langchain.callbacks import get_openai_callback
from langchain.agents import Tool
from langchain.agents import load_tools, initialize_agent

from langchain import SerpAPIWrapper

load_dotenv()

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


llm = OpenAI(
    openai_api_key=OPENAI_API_KEY,
    temperature=0
)


def count_tokens(agent, query):
    with get_openai_callback() as cb:
        result = agent(query)
        print(f'Spent a total of {cb.total_tokens} tokens')

    return result


search = SerpAPIWrapper(serpapi_api_key='397205ae820bcae8152be0d274966df1e529386ba82dc4ef3c89f9ac44c2942e')
tools = [
    Tool(
        name="Intermediate Answer",
        func=search.run,
        description='google search'
    )
]

self_ask_with_search = initialize_agent(tools, llm, agent="self-ask-with-search", verbose=True)

# result= count_tokens(self_ask_with_search, "GDP of the US 2022 multiplying by 3")

def run_llm(query):
    result = count_tokens(self_ask_with_search, query)
    return result