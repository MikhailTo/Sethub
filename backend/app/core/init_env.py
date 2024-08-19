import os
from pathlib import Path
from dotenv import load_dotenv

dotenv_path = os.path.join(Path(__file__).resolve().parents[3], '.env.example')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)