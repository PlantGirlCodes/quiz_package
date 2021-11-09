import random
from quiz_bank import questions_answers
from quiz_class import Question
from quiz_score import run_test

random.shuffle(questions_answers) 

run_test(questions_answers)