import random 

def slot_machine():

    turns = 0

    while turns <5:

        slot1 = random.randint(1,5)
        slot2 = random.randint(1,5)
        slot3 = random.randint(1,5)

        display = input('Play slot machine - hit enter')
        print (f' slot machine display: {slot1} {slot2} {slot3}')

        if slot1 == slot2 and slot2 == slot3:
            print(f' jackpot you won')
            break
        elif slot1 == slot2 or slot2 == slot3 or slot1 == slot3:
            print(f' partial win')
            turns += 1
        else:
            print(f'try again')
            turns += 1
            
    if turns == 5:
            print('you have already tried five time - stop gambling - go do something useful')

slot_machine()