# simple quiz game

questions = {
    "Capital of India? ": "delhi",
    "5 + 7 = ? ": "12",
    "Planet known as Red Planet? ": "mars"
}

score = 0

for q, ans in questions.items():
    user_ans = input(q).lower()
    if user_ans == ans:
        score += 1
        print("Correct!\n")
    else:
        print("Wrong!\n")

print("Your Score:", score)
