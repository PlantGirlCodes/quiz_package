from quiz_bank import questions_answers
from quiz_class import Question

def run_test(list_of_q_a): #this arg reoresents the answers
    score=0
    for q_a in list_of_q_a:
        #create variable to store user input
        user_response = input(q_a.prompt)
        #check to see response is rights 
        if user_response == q_a.answer:
            score +=1

    print("Score:" + str(score) + " out of " + str(len(list_of_q_a)))

run_test(questions_answers)