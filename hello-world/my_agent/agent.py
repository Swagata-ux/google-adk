from typing import Dict
from google.adk.agents.llm_agent import Agent


def get_current_time(city: str) -> Dict[str, str]:
    """Returns the current time in a specified city.
    
    Args:
        city: Name of the city to get time for.
        
    Returns:
        Dictionary with status, city, and time information.
    """
    return {"status": "success", "city": city, "time": "10:30 AM"}


def get_current_weather(city: str) -> Dict[str, str]:
    """Returns the current weather in a specified city.
    
    Args:
        city: Name of the city to get weather for.
        
    Returns:
        Dictionary with status, city, and weather information.
    """
    return {"status": "success", "city": city, "weather": "Sunny and 75°F"}


root_agent = Agent(
    model='gemini-2.0-flash-exp',
    name='root_agent',
    description="Tells the current time and weather in a specific city",
    instruction=(
        "You are a helpful assistant that tells the current time or weather in cities. "
        "Use the 'get_current_time' tool to get the current time, "
        "use 'get_current_weather' to get the weather."
    ),
    tools=[get_current_time, get_current_weather],
)
