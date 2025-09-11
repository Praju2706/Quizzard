from features.quiz import start_quiz
from features.view_scores import view_scores
from features.leaderboard import leaderboard
from features.rules import show_rules
from features.profile import view_profile
from utils.helpers import logout_screen
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text

console = Console()

def print_dashboard(user):
    header_text = Text.from_markup(
        f"[bold magenta]D A S H B O A R D[/bold magenta]\nLogged in as [cyan]{user.username}[/cyan]",
        justify="center"
        )
    print("\n")
    console.print(Panel(
        header_text,
        border_style="bright_blue",
        width=55
    ))
    options_text = (
        "[yellow]1.[/yellow] Start Quiz\n\n"
        "[yellow]2.[/yellow] View Scores (History)\n\n"
        "[yellow]3.[/yellow] Leaderboard\n\n"
        "[yellow]4.[/yellow] Quiz Rules\n\n"
        "[yellow]5.[/yellow] Profile / Stats\n\n"
        "[yellow]6.[/yellow] Logout"
    )
    console.print(Panel(
        Align.left(options_text),
        width=55,
        border_style="bright_magenta",
        title="📌 Options"
    ))

def dashboard(user):
    print_dashboard(user)

    while True:
        choice = console.input("\n👉 [cyan]Select an option:[/cyan] ").strip()

        if choice == "1":
            start_quiz(user)
            print_dashboard(user)
        elif choice == "2":
            view_scores(user)
            print_dashboard(user)
        elif choice == "3":
            leaderboard()
            print_dashboard(user)
        elif choice == "4":
            show_rules()
            print_dashboard(user)
        elif choice == "5":
            view_profile(user.username)
            print_dashboard(user)
        elif choice == "6":
            choice = console.input("👉 [yellow]Do you want to logout of the current session? (Y/N) : [/yellow]").lower()
            if choice == "y":
                logout_screen()
                break
            elif choice == "n":
                console.print("[green]✅ Logout cancelled. Returning to dashboard...[/green]")
                print_dashboard(user)
        else:
            console.print("⚠️ [bold red] Invalid option. Please try again.[/bold red]")
