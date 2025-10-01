# This file defines the Question class which serves as a blueprint for creating question objects
# Each question object will have two attributes: text (the question) and answer (the correct answer)

class Question:
    # Constructor (__init__ method):
    # This method is automatically called when a new Question object is created
    # Parameters:
    #   - q_text: The actual question text (e.g., "Is the sky blue?")
    #   - a_answer: The correct answer to the question (e.g., "True" or "False")
    def __init__(self, q_text, a_answer):
        # self.text and self.answer are instance variables
        # They store the question text and answer for each Question object
        self.text = q_text
        self.answer = a_answer
        
