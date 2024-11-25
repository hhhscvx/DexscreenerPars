from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    ZENROWS_API_KEY: str

    START_TEXT: str = r"""
 ____                                                   ____                    
|  _ \   ___ __  __ ___   ___  _ __   ___   ___  _ __  |  _ \   __ _  _ __  ___ 
| | | | / _ \\ \/ // __| / __|| '__| / _ \ / _ \| '_ \ | |_) | / _` || '__|/ __|
| |_| ||  __/ >  < \__ \| (__ | |   |  __/|  __/| | | ||  __/ | (_| || |   \__ \
|____/  \___|/_/\_\|___/ \___||_|    \___| \___||_| |_||_|     \__,_||_|   |___/
                    """


settings = Settings()
