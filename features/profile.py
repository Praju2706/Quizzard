import os
from rich.table import Table
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from utils.helpers import load_scores, load_achievements

console = Console()

SCORES_FILE = os.path.join("quiz_data", "scores.txt")
ACH_FILE = os.path.join("quiz_data", "achievements.txt")

def view_profile(username):
    scores = [(u, s, t, d) for (u, s, t, d) in load_scores(SCORES_FILE) if u == username]
    achievements = load_achievements(ACH_FILE)

    if not scores:
        console.print("\n⚠️ [yellow] No quiz history found for this user.[/yellow]")
        console.input("\n👉 [cyan]Press ENTER to return to dashboard...[/cyan]")
        return

    quizzes_played = len(scores)
    total_score = sum(s for (_, s, _, _) in scores)
    total_time = sum(t for (_, _, t, _) in scores)
    avg_score = round(total_score / quizzes_played, 2)
    avg_time = round(total_time / quizzes_played, 2)
    best_score = max(s for (_, s, _, _) in scores)

    leaderboard = load_scores(SCORES_FILE)
    leaderboard_sorted = sorted(leaderboard, key=lambda x: (-x[1], x[2]))
    rank = next((i+1 for i, (u, _, _, _) in enumerate(leaderboard_sorted) if u == username), "-")

    if rank == 1:
        rank_display = "🥇 1 (Gold)"
    elif rank == 2:
        rank_display = "🥈 2 (Silver)"
    elif rank == 3:
        rank_display = "🥉 3 (Bronze)"
    else:
        rank_display = str(rank)

    print("\n")
    console.print(Panel(Align.left(
        f"👤 [bold cyan]{username}[/bold cyan]\n🏆 Rank: [bold magenta]{rank_display}[/bold magenta]", vertical= "middle"),
        title="P L A Y E R   P R O F I L E",
        border_style="bright_blue",
        width=55
    ))

    stats_table = Table(show_header= False,style="magenta", header_style="bold cyan", width= 55)

    stats_table.add_row("Quizzes Played", str(quizzes_played))
    stats_table.add_row("Average Score", str(avg_score))
    stats_table.add_row("Average Time", f"{avg_time} sec")
    stats_table.add_row("Best Score", str(best_score))

    console.print(stats_table)

    if achievements.get(username):
        ach_text = "\n".join([f"🏅 [green]{b}[/green]" for b in achievements[username]])
    else:
        ach_text = "❌ [yellow] None yet... Keep playing![/yellow]"
    
    console.print(Panel(
        Align.left(ach_text),
        title="Achievements",
        border_style="magenta",
        width=55
    ))

    console.input("\n👉 [cyan]Press ENTER to return to dashboard...[/cyan]")
