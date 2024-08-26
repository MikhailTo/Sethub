# import sys
# import os
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# import init_env

# required_vars = ['DB_USERNAME', 'DB_PASSWORD', 'DB_HOST', 'DB_PORT', 'DB_NAME']
# missing_vars = [var for var in required_vars if var not in os.environ]
# if missing_vars:
#     raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")

# import os
# from pathlib import Path
# from dotenv import load_dotenv

# dotenv_path = os.path.join(Path(__file__).resolve().parents[3], '.env.example')

# if os.path.exists(dotenv_path):
#     load_dotenv(dotenv_path)