from datetime import datetime
from langchain_openai import ChatOpenAI
from calendar_tool import get_calendar_tools, refresh_google_auth
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents.format_scratchpad.openai_tools import (
    format_to_openai_tool_messages,
)
from langchain.agents.output_parsers.openai_tools import OpenAIToolsAgentOutputParser
from langchain.agents import AgentExecutor

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
tools = get_calendar_tools()
llm_with_tools = llm.bind_tools(tools)

refresh_google_auth()

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a powerful assistant that schedules meetings. Today's date is {today}. 
            If the meeting cannot be scheduled at its particular time, find another time on the same day that works for the user.
            """,
        ),
        ("user", "{input}."),
        MessagesPlaceholder(variable_name="agent_tool_history"),
    ]
)

agent = (
    {
        "input": lambda x: x["input"],
        "today": lambda x: x["today"],
        "agent_tool_history": lambda x: format_to_openai_tool_messages(
            x["intermediate_steps"]
        ),
    }
    | prompt
    | llm_with_tools
    | OpenAIToolsAgentOutputParser()
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

list(agent_executor.stream(
    {
        "input": "Schedule my workout schedule this afternoon with a run, weights, and yoga", 
        "today": datetime.now().isoformat(),
    })
)
        # "input": "I need a brainstorming meeting this afternoon. Anytime would work, I just need 30 minutes. Schedule the first available time.", 
        # "input": "Schedule time at 1 pm for 1 hour to brainstorm awesome ideas", 
        # "input": "I need to find time for a taste testing meeting with the marketing team today. Aftewards, schedule an appointment with the pediatrician.", 