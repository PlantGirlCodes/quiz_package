import random 

def check_sum():
#create two numbers  
    num1 = random.randint(1, 100) #choose int bet 1 and ? 
    num2 = random.randint(1, 100) #choose int bet 1 and ? 
#calculate the addion and assign to var
    sum = num1 + num2

    is_answer_correct = False


    while is_answer_correct == False:
        user_sum = int(input(f'Please enter the sum of {num1} + {num2} ? '))


        if sum == user_sum:
            print (f' congrats! {sum} is the correct answer')
            is_answer_correct = True
            break 

        else:
            print(f'{user_sum} is not the sum of {num1}+{num2} please try again ')


check_sum()


