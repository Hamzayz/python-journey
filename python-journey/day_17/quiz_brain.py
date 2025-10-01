# This file contains the QuizzBrain class which manages the quiz functionality
# It handles asking questions, checking answers, and keeping track of the score

class QuizzBrain:
    # Constructor (__init__ method):
    # Initializes a new quiz with a list of questions
    # Parameters:
    #   - q_list: A list of Question objects
    def __init__(self, q_list):
        self.question_number = 0  # Keeps track of which question we're on
        self.question_list = q_list  # Stores all the questions
        self.score = 0  # Keeps track of the user's score

    # Method to check if there are more questions left
    # Returns True if there are more questions, False if we've reached the end
    def still_has_Questions(self):
        return self.question_number < len(self.question_list)

    # Method to ask the next question
    # Gets the current question, asks the user for their answer, and checks if it's correct
    def next_question(self):
        current_question = self.question_list[self.question_number]  # Get the current question
        self.question_number += 1  # Move to the next question
        # Ask the user for their answer
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        # Check if the answer is correct
        self.check_answer(user_answer, current_question.answer)

    # Method to check if the user's answer is correct
    # Parameters:
    #   - user_answer: The answer provided by the user
    #   - correct_answer: The correct answer to the question
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You are right!")
            self.score += 1  # Increase score if answer is correct
        else:
            print("You are wrong!")
        # Show the correct answer and current score
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")  # Add a blank line for better readability
