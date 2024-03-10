from dotenv import dotenv_values

class Env:

    """
    Get the value of a key from the .env file
    :param key: The key to get
    :param default: The default value if the key is not found
    :return: The value of the key
    """
    def get(key: str, default: str = None) -> str:    
        # Get the value of the key from the .env file
        return dotenv_values('.env').get(key, default)