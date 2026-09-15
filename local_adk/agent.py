from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

root_agent = Agent(
    name="local_agent",
    model=LiteLlm(
        model="ollama/your-model-name"
    ),
    instruction="""
    You are a helpful AI assistant.
    Answer questions clearly and concisely.
    """
)
