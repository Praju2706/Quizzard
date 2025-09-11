import os 
import sys
from datetime import datetime
import pyfiglet
from colorama import Fore, Style, init
from rich.console import Console
from rich.panel import Panel
from rich.align import Align

console = Console()

init(autoreset=True)  

def welcome_screen():
    print(Fore.CYAN + "=" * 55)
    ascii_banner = pyfiglet.figlet_format("QUIZZARD")
    print(Fore.MAGENTA + ascii_banner + Style.RESET_ALL)
    print(Fore.YELLOW + "✨ Welcome to the QUIZZARD - The Console Quiz App! ✨" + Style.RESET_ALL)
    print(Fore.CYAN + "=" * 55 + Style.RESET_ALL)
    input(Fore.GREEN + "\n👉 Press Enter to Login..." + Style.RESET_ALL)

def logout_screen():
    print("\n")
    console.print(
        Panel(
            Align.center("✨ [cyan]See you soon, wizard![/cyan] ✨", vertical="middle"),
            border_style="bright_red",
            title="L O G G E D   O U T",
            title_align="center",
            width=55
        )
    )

def load_credentials(filepath):
    creds = {}
    if not os.path.exists(filepath):
        return creds
    
    with open(filepath, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 2:
                username, password = parts
                creds[username] = password
    return creds

def save_credentials(filepath, username, password):
    with open(filepath, "a") as f:
        f.write(f"{username},{password}\n")

def input_password(prompt="Enter password : "):
    console.print(f"[cyan]{prompt}[/cyan]", end="", style="cyan", highlight=False, soft_wrap=True)
    password = ""

    if os.name == "nt":  # Windows
        import msvcrt
        while True:
            char = msvcrt.getch()
            if char in {b"\r", b"\n"}:
                break
            elif char == b"\x08":
                if len(password) > 0:
                    password = password[:-1]
                    sys.stdout.write("\b \b")
                    sys.stdout.flush()
            elif char == b"\x03":
                raise KeyboardInterrupt
            else:
                password += char.decode("utf-8", errors="ignore")
                sys.stdout.write("*")
                sys.stdout.flush()
    else:  # Linux / Mac
        import termios, tty
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            while True:
                char = sys.stdin.read(1)
                if char in {"\r", "\n"}:
                    break
                elif char == "\x7f":
                    if len(password) > 0:
                        password = password[:-1]
                        sys.stdout.write("\b \b")
                        sys.stdout.flush()
                elif char == "\x03":
                    raise KeyboardInterrupt
                else:
                    password += char
                    sys.stdout.write("*")
                    sys.stdout.flush()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return password

def save_score(filepath, username, score, time_taken):
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(f"{username},{score},{time_taken},{datetime.now().strftime('%Y-%m-%d %H:%M')}\n")

def load_scores(filepath):
    if not os.path.exists(filepath):
        return []
    scores = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 4:
                username, score, time_taken, date = parts
                scores.append((username, int(score), int(time_taken), date))
    return scores

def load_achievements(filepath):
    if not os.path.exists(filepath):
        return {}
    achievements = {}
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 2:
                username, badges = parts
                achievements[username] = badges.split("|") if badges else []
    return achievements

def save_achievements(filepath, achievements):
    with open(filepath, "w", encoding="utf-8") as f:
        for username, badges in achievements.items():
            f.write(f"{username},{'|'.join(badges)}\n")

def show_question(q, idx, total):
    console.rule(f"[bold cyan] Question {idx}/{total}")
    panel = Panel.fit(
        f"[yellow]{q['question']}[/yellow]\n\n"
        f"A) {q['A']}\n"
        f"B) {q['B']}\n"
        f"C) {q['C']}\n"
        f"D) {q['D']}",
        title="📝 QUIZZARD",
        border_style="magenta"
    )
    console.print(panel)

def show_feedback(correct, ans=None, right=None):
    if correct:
        console.print(f"[bold green]✅ Correct![/bold green]\n")
    elif ans == "timeout":
        console.print(f"[bold yellow]⏰ Time’s up![/bold yellow]\n")
    elif ans:
        console.print(f"[bold red]❌ Wrong![/bold red] (Correct: [yellow]{right}[/yellow])\n")
    else:
        console.print(f"[bold yellow]⚠️ Invalid choice![/bold yellow]\n")

def show_summary(score, total, total_time):

    accuracy = f"{(score/total)*100:.1f} %"
    summary = (
        f"📋 [magenta]Total Questions:[/magenta] {total}\n"
        f"✅ [green]Correct Answers:[/green] {score}\n"
        f"❌ [red]Wrong Answers:[/red] {total - score}\n"
        f"⭐ [yellow]Final Score:[/yellow] {score}/{total}\n"
        f"⏱️  [cyan]Total Time:[/cyan] {total_time} sec\n"
        f"🎯 [bold blue]Accuracy:[/bold blue] {accuracy}"
    )

    console.print(Panel(Align.left(summary, vertical= "middle"), border_style="bright_magenta", width=55))
