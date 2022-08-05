from trivia_pkg.questions import history_questions, music_questions, sports_questions, general_questions

print(f"Welcome to Trivia- presented by your quizmaster, Jose!")

player = input(f"Please enter your name: ")
print(f"Welcome to the trivia game, {player}!")
print(f"""
Here are the rules for this game:
\t1. There are 4 rounds, each with a different category of questions.
\t2. Spelling counts, capitalization does not!
\t3. Each question is worth 10 points.""")

categories = ["History", "Music", "Sports", "General"]
print("The 4 categories of questions for this game will be:")
for category in categories:
    print(f"\t{category}")


# Player enters start to begin the game, or exit/quit to exit the game. If an invalid response is entered, will ask the player to enter a valid response.
while True:
    start = input(
        "To begin the 1st round, type start. To exit the game, type exit or quit:\t")
    if start.lower() == "start":
        break
    elif start.lower() == "quit" or start.lower() == "exit":
        quit()
    else:
        print("Please enter a valid response:\t")
        continue


score = 0
first_round_score = 0
print(f"**********1st Round*********")
print(f"The 1st Round category will be: {categories[0]}!")

for question in history_questions:
    answer = input(history_questions[question]["question"])
    if answer.lower() == history_questions[question]["answer"].lower():
        first_round_score += 10
    else:
        continue

score += first_round_score
print(f"\nYour total score for round one is: {first_round_score}.\n")
'''
for question, answer in history_questions.items():
    print(question, answer)
'''
print(f"\nYour total score is: {score}.\n")

print(f"**********2nd Round*********")
print(f"The 2nd Round category will be: {categories[1]}!")

second_round_score = 0

for question in music_questions:
    answer = input(music_questions[question]["question"])
    if answer.lower() == music_questions[question]["answer"].lower():
        second_round_score += 10
    else:
        continue

score += second_round_score
print(f"\nYour total score for round two is: {second_round_score}.\n")

'''for question, answer in music_questions.items():
    print(question, answer)
'''
print(f"\nYour total score is: {score}.\n")

print(f"**********3rd Round*********")
print(f"The 3rd Round category will be: {categories[2]}!")

third_round_score = 0

for question in sports_questions:
    answer = input(sports_questions[question]["question"])
    if answer.lower() == sports_questions[question]["answer"].lower():
        third_round_score += 10
    else:
        continue

score += third_round_score
print(f"\nYour total score for round three is: {third_round_score}.\n")

'''for question, answer in sports_questions.items():
    print(question, answer)'''

print(f"\nYour total score is: {score}.\n")

print(f"**********4th Round*********")
print(f"The 4th Round category will be: {categories[3]}!")

fourth_round_score = 0

for question in general_questions:
    answer = input(general_questions[question]["question"])
    if answer.lower() == general_questions[question]["answer"].lower():
        fourth_round_score += 10
    else:
        continue

score += fourth_round_score
print(f"\nYour total score for round four is: {fourth_round_score}.\n")

'''for question, answer in general_questions.items():
    print(question, answer)'''

print(f"\nYour final score is: {score}.\n")
print(f"Thank you for playing!")
