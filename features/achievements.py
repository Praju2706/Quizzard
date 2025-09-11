import os
from utils.helpers import load_scores, save_achievements, load_achievements

SCORES_FILE = os.path.join("quiz_data", "scores.txt")
ACH_FILE = os.path.join("quiz_data", "achievements.txt")

def check_achievements(username, latest_score):
    achievements = load_achievements(ACH_FILE)
    unlocked = []

    # Already unlocked badges for this user
    current_badges = set(achievements.get(username, []))

    # Load score history
    scores = [(u, s, t, d) for (u, s, t, d) in load_scores(SCORES_FILE) if u == username]
    attempts = len(scores)
    best_score = max([s for (_, s, _, _) in scores], default=0)

    # Badge conditions
    if attempts == 1 and "Rookie" not in current_badges:
        current_badges.add("Rookie")
        unlocked.append("Rookie")

    if latest_score == 10 and "Sharp Shooter" not in current_badges:
        current_badges.add("Sharp Shooter")
        unlocked.append("Sharp Shooter")

    if attempts >= 3 and "Consistent" not in current_badges:
        current_badges.add("Consistent")
        unlocked.append("Consistent")

    if latest_score > best_score and "Climber" not in current_badges:
        current_badges.add("Climber")
        unlocked.append("Climber")

    # Save back
    achievements[username] = list(current_badges)
    save_achievements(ACH_FILE, achievements)

    return unlocked
