from enum import Enum


class Config(Enum):
    desired_capabilities = {
        # "app": "C:\\Users\\anduser\\AppData\\Local\\Reverso\\Reverso\\Reverso.exe"  # path to application ".exe" file
    }
    command_executor = 'http://127.0.0.1:4723/wd/hub'
