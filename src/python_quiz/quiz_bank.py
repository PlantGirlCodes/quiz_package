from quiz_class import Question

question_prompts = [
 
    "What is correct syntax to output 'Hello World' in Python ?\na: print('Hello World')\nb:echo 'Hello World' \nc: p('Hello World')\nd: print(Hello World)\n\n",
    "How do you insert Comments in Python?\na: #this is a comment \nb://this us a comment \nc:/* This is a comment*/\n\n",
    "Which is the correct extention for Pything files? \na: .py \nb: .pyt \nd: .ipbny"
]

questions_answers = [
    Question(question_prompts[0], "a"),# index 0
    Question(question_prompts[1], "a"), # index 1
    Question(question_prompts[2], "a"), #index 2
]

