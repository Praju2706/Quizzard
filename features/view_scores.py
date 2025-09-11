import os
from utils.helpers import load_scores
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.align import Align

console = Console()

SCORES_FILE = os.path.join("quiz_data", "scores.txt")

def view_scores(user):
    scores = load_scores(SCORES_FILE)

    user_scores = [(s, t, d) for (u, s, t, d) in scores if u == user.username]

    if not user_scores:
        console.print("\n⚠️ No scores found for your account.\n", style="yellow")
        console.input("\n👉 [cyan]Press ENTER to return to dashboard...[/cyan]")
        return

    print("\n")
    console.print(Panel(Align.center("[bold magenta] S C O R E   H I S T O R Y [/bold magenta]", vertical="middle"),
        border_style="bright_blue",
        width=55
    ))
    table = Table(style="magenta", header_style="bold cyan", width=55)
    table.add_column("Score", style="green", justify="center")
    table.add_column("Time Taken (s)", style="magenta", justify="center")
    table.add_column("Date", style="yellow", justify="center")

    for s, t, d in user_scores:
        table.add_row(str(s), str(t), d)
    
    console.print(table)
    console.input("\n👉 [cyan]Press ENTER to return to dashboard...[/cyan]")