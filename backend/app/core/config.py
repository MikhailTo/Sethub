from pathlib import Path
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = 'Sethub'

     # path to src folder
    MAIN_PATH: Path = Path(__file__).resolve().parent.parent.parent
    # path to app folder
    APP_PATH: Path = MAIN_PATH / 'app'
    # name of media folder
    MEDIA_FOLDER: Path = Path('media')
    # path to media folder
    MEDIA_PATH: Path = MAIN_PATH / MEDIA_FOLDER
    # name of static folder
    STATIC_FOLDER_NAME: Path = Path('static')
    # path to static folder
    STATIC_FOLDER: Path = MAIN_PATH / STATIC_FOLDER_NAME

settings = Settings()