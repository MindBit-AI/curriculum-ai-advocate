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
from typing import List
from langchain.agents import Tool
from langchain.tools import tool
from langchain.pydantic_v1 import BaseModel, Field

timezone = "America/Denver"

# Initialize the LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def get_google_calendar_service():
    SCOPES = ["https://www.googleapis.com/auth/calendar"]
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
    return build('calendar', 'v3', credentials=creds)

class CalendarEvent(BaseModel):
    """Schema for a calendar event."""
    summary: str = Field(..., description="The title of the event")
    start_time: str = Field(..., description="The start time in ISO format (YYYY-MM-DDTHH:MM:SS)")
    duration_minutes: int = Field(..., description="Duration of the event in minutes")
    description: str = Field("", description="Optional description of the event")

@tool # Main Task
def create_calendar_event(event: CalendarEvent) -> str:
    """Create a new calendar event."""
    try:
        service = get_google_calendar_service()

        start_datetime = datetime.fromisoformat(event.start_time).astimezone(pytz.timezone(timezone))
        end_datetime = start_datetime + timedelta(minutes=event.duration_minutes)

        event_body = {
            'summary': event.summary,
            'description': event.description,
            'start': {
                'dateTime': start_datetime.isoformat(),
                'timeZone': timezone,
            },
            'end': {
                'dateTime': end_datetime.isoformat(),
                'timeZone': timezone,
            },
        }

        event = service.events().insert(calendarId='primary', body=event_body).execute()
        return f"Event '{event['summary']}' has been created for {start_datetime.strftime('%Y-%m-%d %H:%M')}."
    except HttpError as error:
        print(f"An error occurred: {error}")
        return f"Failed to create the event due to an error: {error}"

@tool # Context
def check_calendar_availability(start_time: str, duration_minutes: int) -> bool:
    """Check if a given time slot is available in the calendar."""
    try:
        service = get_google_calendar_service()

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

def get_calendar_tools() -> List[Tool]:
    """Get a list of all available tools."""
    return [
        check_calendar_availability,
        create_calendar_event
    ]
    
# Usage example:
# calendar_tool = CalendarTool('path/to/your/credentials.json', 'Your/Timezone')
# tools = calendar_tool.get_tools()
# Use these tools with your LangGraph setup