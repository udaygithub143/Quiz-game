class QuizQuestion:
    def __init__(self, question, options, correct_option):
        self.question = question
        self.options = options
        self.correct_option = correct_option
 
class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
 
    def display_question(self, question_obj):
        print(question_obj.question)
        for index, option in enumerate(question_obj.options, start=1):
            print(f"{index}. {option}")
 
    def get_user_answer(self, question_obj):
        while True:
            try:
                user_answer = int(input("Your answer (enter the option number): "))
                if 1 <= user_answer <= len(question_obj.options):
                    return user_answer
                else:
                    print("Invalid input. Please enter a valid option number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
 
    def evaluate_answer(self, question_obj, user_answer):
        if user_answer == question_obj.correct_option:
            print("Correct!")
            self.score += 1
        else:
            print(f"Wrong! The correct answer was option {question_obj.correct_option}.")
 
    def play_game(self):
        for question_obj in self.questions:
            self.display_question(question_obj)
            user_answer = self.get_user_answer(question_obj)
            self.evaluate_answer(question_obj, user_answer)
            print()  # Add a newline for better readability
 
    def show_score(self):
        print(f"Your final score: {self.score}/{len(self.questions)}")
 
# Define quiz questions
question1 = QuizQuestion("What is the capital of France?", ["Paris", "Berlin", "Madrid"], 1)
question2 = QuizQuestion("Which programming language is this quiz written in?", ["Java", "Python", "C++"], 2)
question3 = QuizQuestion("What is 2 + 2?", ["3", "4", "5"], 2)
 
# Create a list of quiz questions
quiz_questions = [question1, question2, question3]
 
# Create a QuizGame instance
quiz_game = QuizGame(quiz_questions)
 
# Start the quiz game
quiz_game.play_game()
 
# Display the final score
quiz_game.show_score()