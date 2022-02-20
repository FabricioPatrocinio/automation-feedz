# External modules
from dotenv import find_dotenv
from pydantic import BaseSettings, Field


class GlobalSettings(BaseSettings):
    '''Application settings.'''

    SITE: str = Field(..., env='SITE')
    EMAIL: str = Field(..., env='EMAIL')
    PASSWORD: str = Field(..., env='PASSWORD')

    class Config:
        '''Loads the dotenv file.'''

        env_file: str = find_dotenv('.env')


settings = GlobalSettings()
