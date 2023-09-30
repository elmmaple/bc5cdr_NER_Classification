from rich.console import Console
from rich.theme import Theme
from config import CONFIG

def print(text, style = ''):
    CUSTOM_THEME = Theme(CONFIG['CUSTOM_THEME'])
    console = Console(theme = CUSTOM_THEME)
    console.print(text, style = style)