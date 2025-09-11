from auth.login import login_or_register
from features.dashboard import dashboard
from utils.helpers import welcome_screen

if __name__ == "__main__":
    welcome_screen()
    user = login_or_register()

    if user:
        dashboard(user)
    else:
        print("❌ Something went wrong. Exiting...")
