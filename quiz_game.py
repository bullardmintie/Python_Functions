# Task 1 -- Develop a list of questions and answers

question_prompts = [
    "What is your favorite color? (a) red (b) purple (c) green (d) blue ",
    "What is your favorite food? (a) lasagna (b) pizza (c) tacos (d) spaghetti ",
    "What is your favorite hobby? (a) drawing (b) puzzles (c) reading (d) coloring ",
    "What is your favorite season? (a) fall (b) winter (c) summer (d) spring ",
    "What is your favorite time of day? (a) morning (b) afternoon (c) night (d) noon ",
    "What is your favorite sport? (a) basketball (b) football (c) golf (d) soccer "
    ]


# Task 2 -- Write a function that quizzes the user and takes their answers

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "a"),
    Question(question_prompts[5], "b")
    ]


# Task 3 -- Score the quiz and give the user feedback on their performance

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + " questions correct!")

run_test(questions)