from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.style import Style
from rich.panel import Panel as RichPanel
import json

def Panel():
    with open("./utils/config.json", "r") as json_file:
        data = json.load(json_file)
    print(" ")
    # Define custom styles for ON and OFF
    on_style = Style(color="green")
    off_style = Style(color="red")

    # Create a table with 2 columns
    table = Table(title="Discord Server Cloner", style="red")
    table.add_column("Setting", style="cyan", width=31)
    table.add_column("Status", justify="center", width=10)

    for setting, status in data["copy_settings"].items():
        table.add_row(setting.capitalize(), Text("ON" if status else " OFF", style=on_style if status else off_style))

    console = Console()
    console.print(table)

    # Paragraph with change logs
    paragraph = """Discord Guild Cloner by RaysDev.            ©️ 2022 Rays Developer - All Rights Reserved."""
    console.print(RichPanel(paragraph, style="green", width=48))
    
    # Version information
    version = "2.0.1"
    console.print(RichPanel(f"Version: {version}", style="red", width=48))


def Panel_Run(guild, user):
    with open("./utils/config.json", "r") as json_file:
        data = json.load(json_file)
    print(" ")
    # Define custom styles for ON and OFF
    on_style = Style(color="green")
    off_style = Style(color="red")

    # Create a table with 2 columns
    table = Table(title="Discord Server Cloner", style="red")
    table.add_column("Cloner is Running...", style="cyan", width=31)
    table.add_column("Status", justify="center", width=10)

    for setting, status in data["copy_settings"].items():
        table.add_row(setting.capitalize(), Text("ON" if status else " OFF", style=on_style if status else off_style))

    # Stick a new table in the footer
    footer = Table(show_header=False, show_lines=False, width=48)
    footer.add_column(justify="center")
    footer.add_row(f"[red]Server ID: [red]{guild}")
    footer.add_row(f"[red]Logged in as: [red]{user}")

    console = Console()
    console.print(table)
    console.print(footer)

    # Paragraph with change logs
    paragraph = """Discord Guild Cloner by RaysDev.            ©️ 2022 Rays Developer - All Rights Reserved."""
    console.print(RichPanel(paragraph, style="green", width=48))
    
    # Version information
    version = "2.0.1"
    console.print(RichPanel(f"Version: {version}", style="red", width=48))
