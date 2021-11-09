
What  
This package contains multiple modules useful for building quizes

How to install it
pip install -i https://test.pypi.org/simple/ example-pkg-ShifraG

Example usage


How to set up the dev environment
coming soon...

How to ship a change
coming soon...


Change log
....coming soon 

License and author info
MIT Licence and author: Shifra Goldberg


details on files in the scr/ file:

In the python_quiz folder - 
-quiz_class -create a class to use variables prompt and answer in other modules
-quiz_bank - imports Question class from quiz class file and contains a variable for the list of question prompts and multi-choice answer options and another variable which identifies the answers  
-quiz_score takes user responses and checks them against the answers gives them a score
-quiz shuffle changes the prompt order

The slot machine is a game where user pulls lever and is given 3 numbers at random - they are given 5 changes to play - if they get two of the same numbers - its a partial win - if they get all three the same - they get "jackpot"

The math quiz uses random numbers to give user two number which they must sum - if they are correct they are told - if not they are given the opportunity to try again until they sum the numbers correctly. This can be built out in the future for other quiz like purposes.