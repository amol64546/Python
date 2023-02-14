from Question import Question

question_prompts = [
    "What is color of apple?\n(a) Yellow (b) green (c) Red\n",
    "What is color of banana?\n(a) Yellow (b) green (c) Red\n",
    "What is color of graph?\n(a) Yellow (b) green (c) Red\n"
]

questions = [
    Question(question_prompts[0],"c"),
    Question(question_prompts[1],"a"),
    Question(question_prompts[2],"b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if(answer==question.answer):
            score += 1
    
    print("You got",score,"/",len(questions),"correct")

run_test(questions)