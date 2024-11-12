import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "mysecretkey")
    EXTERNAL_API_URL = os.getenv("EXTERNAL_API_URL", "https://api.example.com")
