from config import RICH_CONFIG, PATH_CONFIG
from rich.console import Console
from rich.theme import Theme
from rich.traceback import install
install()

def console(text):
    console = Console()
    console.log(text, log_locals = True)
    
def save_and_print(text, style):
    CURRENT_DATE_TIME = RICH_CONFIG['DATE_TIME']
    CUSTOM_THEME = Theme(RICH_CONFIG['CUSTOM_THEME'])
    console = Console(record = True, theme = CUSTOM_THEME)
    # console.log(text, log_locals = True)
    RESULT_HTML = PATH_CONFIG['RESULT_HTML']
    console.print(text, style = style)
    # 打開 HTML 文件以追加内容
    console_output = console.export_html() 
    with open(RESULT_HTML + str(CURRENT_DATE_TIME) +'.html',"a", encoding="utf-8") as html_file:
        # 将包装后的内容追加到HTML文件中
        html_file.write(console_output)