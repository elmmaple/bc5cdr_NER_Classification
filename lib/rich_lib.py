from config import RICH_CONFIG
from rich.console import Console
from rich.theme import Theme
from rich.traceback import install
install()

def print(text, style = ''):
    CUSTOM_THEME = Theme(RICH_CONFIG['CUSTOM_THEME'])
    console = Console(theme = CUSTOM_THEME)
    console.print(text, style = style)
    
def console(text):
    console = Console()
    console.log(text, log_locals = True)