from dotenv import load_dotenv
import os
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.agents import ChatAgent

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

# Create a model instance
model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI,
    model_type=ModelType.GPT_4O_MINI,
    model_config_dict={"temperature": 0.0},
    api_key=api_key  # Pass the API key as a separate parameter
)

# Create a basic agent
agent = ChatAgent(model=model)

# Test the agent
response = agent.step("Hello, I'm testing my CAMEL installation.")
print(response.msgs[0].content)