import os
from bootstrap import app

class Config:

    def __init__(self):
        return
    
    # To get the value of a key from the config file
    def get(self, key):
        # A sample of usage of the method
        # from laraflask.Helpers.config import config
        # config().get('app.app_name')
        # where app is the name of the file inside the config folder
        # app_name is the key

        # Split the key to get the file name and the key
        key = key.split('.')

        # Get the file name
        file_name = key[0]

        # Get the key
        key = key[1]

        # Get the file path
        file_path = os.path.join(app.AppBootstrap().app_config_path, file_name + '.py')

        # Import the class from the file
        file = __import__('config.' + file_name, fromlist=[file_name])

        # Create an instance of the class
        instance = key[0].upper() + key[1:] + 'Configuration'

        instance = getattr(file, instance)()

        # Get the value of the key
        return getattr(instance, key)
