import openai
import os
from dotenv import load_dotenv
from loguru import logger

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def call_ai(system_prompt: str, user_prompt: str, max_tokens: int = 150, temperature: float = 0.3):
    """
        TODO: Check documentation of OpenAI API - https://platform.openai.com/docs/api-reference/chat?lang=python. Use the function parameters. Use the API key defined in .env file

    """


