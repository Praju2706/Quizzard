import os
from auth.user import User
from utils.helpers import load_credentials, save_credentials, input_password
from rich.console import Console
from rich.panel import Panel
from rich.align import Align

console = Console()
CREDENTIALS_FILE = os.path.join("quiz_data", "credentials.txt")

# Asking user to login or register
def login_or_register():
    while True:
        print("\n")
        console.print(
            Panel(
                Align.center("[bold magenta]U S E R   L O G I N[/bold magenta]", vertical="middle"),
                border_style="bright_blue",
                width=55))

        text = ("[yellow]1.[/yellow] New User (Register)\n"
                "[yellow]2.[/yellow] Existing User (Login)")
        console.print(Panel(
            Align.left(text),
            width=55,
            border_style="bright_magenta"
            ))

        choice = console.input("👉 [cyan]Enter choice (1/2): [/cyan]").strip()
        if choice == "1":
            return register_user()
        elif choice == "2":
            return login_user()
        else:
            console.print("⚠️ [red] Invalid choice! Please enter 1 or 2.[/red]")

# Registering a new user
def register_user():
    creds = load_credentials(CREDENTIALS_FILE)
    while True:
        username = console.input("\n📝 [cyan]Enter username:[/cyan] ").strip()
        if not username:
            console.print("⚠️ [red] Username cannot be empty.[/red]")
            continue
        if username in creds:
            console.print("⚠️ [red] Username already taken. Try another.[/red]")
        else:
            break

    password = input_password("🔑 Enter a password: ").strip()
    if not password:
        console.print("\n⚠️ [red] Password cannot be empty. Try again.[/red]")
        return register_user()
    
    save_credentials(CREDENTIALS_FILE, username, password)
    print("\n")
    console.print(f"✅ [green]Account created successfully for [bold]{username}[/bold]![/green]")
    console.print(f"[cyan]=[/cyan]" * 55)
    return User(username, password)

# Logging in an existing user
def login_user():
    creds = load_credentials(CREDENTIALS_FILE)
    while True:
        username = console.input("\n👤 [cyan]Enter username:[/cyan] ").strip()
        if not username:
            console.print("⚠️ [red] Username cannot be empty.[/red]")
            continue
        if username not in creds:
            console.print("⚠️ [red] Username not found.[/red]")
            choice = console.input("👉 [yellow]Would you like to create a new account?(Y/N) : [/yellow]").lower()
            if choice == "y":
                return register_user()
            elif choice == "n":
                continue
        else:
            break
    
    while True:
        password = input_password("🔑 Enter a password: ").strip()
        if creds[username] == password:
            print("\n")
            console.print(f"✅ [green]Login successful! Welcome back, [bold]{username}[/bold]![/green]")
            console.print(f"[cyan]=[/cyan]" * 55)
            return User(username, password)
        else:
            console.print("\n❌ [red]Incorrect password. Try again.[/red]")
