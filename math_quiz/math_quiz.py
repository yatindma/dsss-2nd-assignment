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

    for _ in range(t_q):
        n1 = function_A(1, 10); n2 = function_A(1, 5.5); o = function_B()

        PROBLEM, ANSWER = function_C(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
