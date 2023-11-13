import random


def generate_random_integer(min_range, max_range):
    """
    Generate a random integer within a specified range.

    Args:
    min_range (int): The minimum value of the range.
    max_range (int): The maximum value of the range.

    Returns:
    int: A random integer within the specified range.
    """
    return random.randint(min_range, max_range)


def choose_random_operator():
    """
    Randomly select an arithmetic operator.

    Returns:
    str: A randomly chosen operator from the set ['+', '-', '*'].
    """
    return random.choice(['+', '-', '*'])


def evaluate_expression(num1, num2, operator):
    """
    Evaluate the arithmetic expression based on two numbers and an operator.

    Args:
    num1 (int): The first number.
    num2 (int): The second number.
    operator (str): The arithmetic operator ('+', '-', '*').

    Returns:
    tuple: A tuple containing the expression as a string and its evaluated result.
    """
    expression = f"{num1} {operator} {num2}"
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    else:  # assuming multiplication
        result = num1 * num2
    return expression, result


def run_math_quiz():
    """
    Run a math quiz game where the user is presented with random arithmetic problems.
    """
    score = 0
    total_questions = 5  # Set the total number of questions for the quiz

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 10)
        operator = choose_random_operator()

        problem, correct_answer = evaluate_expression(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))
            if user_answer == correct_answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {correct_answer}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    run_math_quiz()
