import os, random, time
from inputimeout import inputimeout, TimeoutOccurred
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from utils.helpers import save_score, show_question, show_feedback, show_summary
from features.achievements import check_achievements

console = Console()

QUESTIONS_FILE = os.path.join("quiz_data", "questions.txt")
SCORES_FILE = os.path.join("quiz_data", "scores.txt")

def start_quiz(user):
    questions = load_questions(QUESTIONS_FILE)
    if not questions:
        print("\n⚠️ No questions available. Please add questions to 'questions.txt'.")
        console.input("\n👉 [cyan]Press ENTER to return to dashboard...[/cyan]")
        return

    random.shuffle(questions)
    selected = questions[:10] if len(questions) >= 10 else questions

    print("\n📝 Quiz Started! Answer with A/B/C/D (15 seconds per question)\n")

    score = 0
    total_time = 0

    for idx, q in enumerate(selected, start=1):
        show_question(q, idx, len(selected))

        start_time = time.time()
        ans = None

        try:
            user_input = inputimeout(prompt=f"👉 Your answer (A/B/C/D): ", timeout=10).strip().upper()
            if user_input in {"A", "B", "C", "D"}:
                ans = user_input
            else:
                ans = None
        except TimeoutOccurred:
            ans = "timeout"

        q_time = int(time.time() - start_time)
        total_time += q_time

        if ans and ans == q["answer"]:
            show_feedback(True)
            score += 1
        elif ans:
            show_feedback(False, ans, q["answer"])
        else:
            show_feedback(False)

    console.print(Panel(Align.center("[bold magenta] Q U I Z   F I N I S H E D [/bold magenta]", vertical="middle"),
        border_style="bright_blue",
        width=55
    ))
    show_summary(score, len(selected), total_time)

    save_score(SCORES_FILE, user.username, score, total_time)

    unlocked = check_achievements(user.username, score)
    if unlocked:
        print("\n🏅 New Achievements Unlocked:")
        for badge in unlocked:
            print(f"   - {badge}")

    console.input("\n👉 [cyan]Press ENTER to return to dashboard...[/cyan]")

def load_questions(filepath):
    if not os.path.exists(filepath):
        return []
    questions = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 6:
                q, A, B, C, D, ans = parts
                questions.append({
                    "question": q,
                    "A": A,
                    "B": B,
                    "C": C,
                    "D": D,
                    "answer": ans.upper()
                })
    return questions
