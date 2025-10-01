# This is the main program file that ties everything together
# It imports the necessary modules and runs the quiz

# Import required modules
from question_model import Question  # Import the Question class
from data import question_data  # Import the question data
from quiz_brain import QuizzBrain  # Import the QuizzBrain class

# Create a list to store Question objects
question_bank = []

# Convert the question data into Question objects
for question in question_data["results"]:
    # Extract the question text and answer from the data
    question_text = question["question"]
    question_answer = question["correct_answer"]
    # Create a new Question object and add it to the question bank
    new_question = Question(q_text=question_text, a_answer=question_answer)
    question_bank.append(new_question)

# Create a new quiz with the question bank
quiz = QuizzBrain(question_bank)

# Run the quiz until all questions are answered
while quiz.still_has_Questions():
    quiz.next_question()

# Show the final results
print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")