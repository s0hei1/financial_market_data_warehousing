from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    
    database_url : str = ''
    python_path : str = ''
    
    @property
    def database_url_without_asyncpg(self):
        return self.database_url.replace("+asyncpg", "")

    class Config:
        env_file = r"C:\Users\Soheil\PycharmProjects\financial_market_data_warehousing\src\tools\config\.env"

settings = Settings()