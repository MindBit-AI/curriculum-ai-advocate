import os
from urllib.request import Request
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from langchain_openai import ChatOpenAI
from datetime import datetime, timedelta
import pytz
import json
from typing import Dict, Any, List
from langchain.agents import Tool
from langchain.tools import tool

SCOPES = ["https://www.googleapis.com/auth/calendar"]

credentials_path = "token.json"
timezone = "America/Denver"
openai_client = ChatOpenAI(model="gpt-4o-mini")

def refresh_google_auth():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds


@tool("check_calendar_availability")
def check_calendar_availability(start_time: str, duration_minutes: int) -> bool:
    """Check if a given time slot is available in the calendar."""
    try:
        creds = refresh_google_auth()
        service = build('calendar', 'v3', credentials=creds)

        # Parse the input start_time and convert it to UTC
        start_datetime = datetime.fromisoformat(start_time).astimezone(pytz.timezone(timezone))
        end_datetime = start_datetime + timedelta(minutes=duration_minutes)

        events_result = service.events().list(
            calendarId='primary',
            timeMin=start_datetime.isoformat(),
            timeMax=end_datetime.isoformat(),
            singleEvents=True,
            orderBy='startTime'
        ).execute()
        events = events_result.get('items', [])

        return len(events) == 0  # True if no events (available), False otherwise
    except HttpError as error:
        print(f"An error occurred: {error}")
        return False  # Assume not available in case of error

@tool("extract_calendar_info")
def extract_calendar_info(text: str) -> Dict[str, Any]:
    """Extract calendar event information from user input."""
    functions = [
        {
            "name": "create_calendar_event",
            "description": "Create a new calendar event",
            "parameters": {
                "type": "object",
                "properties": {
                    "summary": {"type": "string", "description": "The title of the event"},
                    "start_time": {"type": "string", "description": "The start time of the event in ISO format (YYYY-MM-DDTHH:MM:SS)"},
                    "duration_minutes": {"type": "integer", "description": "The duration of the event in minutes"},
                    "description": {"type": "string", "description": "Optional description of the event"}
                },
                "required": ["summary", "start_time", "duration_minutes"]
            }
        }
    ]

    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that extracts calendar event information from user input."},
            {"role": "user", "content": text}
        ],
        functions=functions,
        function_call={"name": "create_calendar_event"}
    )

    function_call = response.choices[0].message.function_call
    return function_call

@tool("create_calendar_event")
def create_calendar_event(summary: str, start_time: str, duration_minutes: int, description: str = "") -> str:
    """Create a new calendar event."""
    try:
        creds = refresh_google_auth()
        service = build('calendar', 'v3', credentials=creds)

        start_datetime = datetime.fromisoformat(start_time).astimezone(pytz.timezone(timezone))
        end_datetime = start_datetime + timedelta(minutes=duration_minutes)

        event = {
            'summary': summary,
            'description': description,
            'start': {
                'dateTime': start_datetime.isoformat(),
                'timeZone': timezone,
            },
            'end': {
                'dateTime': end_datetime.isoformat(),
                'timeZone': timezone,
            },
        }

        event = service.events().insert(calendarId='primary', body=event).execute()
        return f"Event '{summary}' has been created for {start_datetime.strftime('%Y-%m-%d %H:%M')}."
    except HttpError as error:
        print(f"An error occurred: {error}")
        return f"Failed to create the event due to an error: {error}"

@tool("calendar_event_tool")
def calendar_event_tool(text: str) -> str:
    """Process user input to create a calendar event or suggest alternatives."""
    event_info = extract_calendar_info(text)
    if event_info:
        if event_info['is_available']:
            result = create_calendar_event(
                event_info['summary'],
                event_info['start_time'],
                event_info['duration_minutes'],
                event_info.get('description', '')
            )
            return result
        else:
            return f"The requested time is not available. Here are some alternative suggestions:\n{event_info['alternative_suggestions']}"
    else:
        return "Sorry, I couldn't extract the necessary information to create a calendar event."

def get_calendar_tools() -> List[Tool]:
    """Get a list of all available tools in this class."""
    return [
        check_calendar_availability,
        extract_calendar_info,
        create_calendar_event
    ]
    
# Usage example:
# calendar_tool = CalendarTool('path/to/your/credentials.json', 'Your/Timezone')
# tools = calendar_tool.get_tools()
# Use these tools with your LangGraph setup