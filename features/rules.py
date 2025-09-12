from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
console = Console()

# Displaying the quiz rules
def show_rules():
    console.print("\n")
    console.print(Panel(Align.center("[bold magenta] Q U I Z   R U L E S [/bold magenta]", vertical="middle"), border_style="bright_blue", width=55))

    rules_text = (
        "1️⃣  Each question has 4 options [yellow](A/B/C/D)[/yellow].\n"
        "2️⃣  Only one option is correct.\n"
        "3️⃣  You have [cyan]10 seconds[/cyan] to answer each question ⏱.\n"
        "4️⃣  Each correct answer gives [green]+1 point[/green].\n"
        "5️⃣  No negative marking ❌.\n"
        "6️⃣  Your score and time will be recorded 📊.\n"
        "7️⃣  Each attempt includes [bold yellow]10 random questions[/bold yellow].")

    console.print(Panel(
        Align.left(rules_text),
        width=55,
        border_style="bright_magenta"
    ))
    console.input("\n👉 [cyan]Press M to return to menu...[/cyan]")
