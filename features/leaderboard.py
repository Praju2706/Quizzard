
import os
from rich.table import Table
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from utils.helpers import load_scores

console = Console()
SCORES_FILE = os.path.join("quiz_data", "scores.txt")

# Displaying the leaderboard
def leaderboard():
    scores = load_scores(SCORES_FILE)
    if not scores:
        console.print("\n⚠️ [yellow]No leaderboard data available yet.[/yellow]")
        console.input("\n👉 [cyan]Press ENTER to return to dashboard...[/cyan]")
        return

    # Sort first by score DESC, then by time ASC
    leaderboard = sorted(scores, key=lambda x: (-x[1], x[2]))

    print("\n")
    console.print(Panel(Align.center("[bold magenta] L E A D E R B O A R D [/bold magenta]", vertical="middle"),
        border_style="bright_blue",
        width=55
    ))
    table = Table(style="magenta", header_style="bold cyan")
    table.add_column("Rank", justify="center")
    table.add_column("User", justify="left", style="bold yellow")
    table.add_column("Score", justify="center", style="green")
    table.add_column("Time (s)", justify="center", style="cyan")
    table.add_column("Date", justify="center", style="white")

    displayed = set()
    rank = 1
    for (u, s, t, d) in leaderboard:
        if u not in displayed:  # best performance per user
            table.add_row(str(rank), u, str(s), str(t), d)
            displayed.add(u)
            rank += 1
    console.print(table)
    console.input("\n👉 [cyan]Press ENTER to return to dashboard...[/cyan]")

