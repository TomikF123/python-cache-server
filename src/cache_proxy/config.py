class Settings:
    port:int = 3000
    origin:str = ''

    @classmethod
    def __repr__(cls) -> str:
        return f"origin:{cls.origin},port:{cls.port}"
    

settings = Settings()