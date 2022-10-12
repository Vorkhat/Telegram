import os
from src.tokens import Tokens
from typing import Optional
from dotenv import load_dotenv

load_dotenv()


class Config:
    HOST_URL = ""

    TELEGRAM_SET_WEBHOOK_URL: Optional[str] = f"https://api.telegram.org/bot{Tokens.TELEGRAM_TOKEN}/setWebhook"
