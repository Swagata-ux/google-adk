from google.adk.agents.llm_agent import Agent

def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city."""
    return {"status": "success", "city": city, "time": "10:30 AM"}

def get_current_weather(city: str) -> dict:
    """Returns the current weather in a specified city."""
    return {"status": "success", "city": city, "weather": "Sunny and 75"}

root_agent = Agent(
    model='gemini-3-pro-preview',
    name='root_agent',
    description="Tells the current time in a specific city",
    instruction="You are a helpful assistant that tells the current time or weather in cities. Use the 'get_current_time' tool to get the current time, use 'get_current_weather' to get the weather",
    tools=[get_current_time,get_current_weather],
)
