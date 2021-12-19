"""
Game - "Rock, Paper, Scissors, Lizard, Spock".
Stanislav Zelenyi. 2021.
"""
import random
answer_options = ('rock', 'paper', 'scissors', 'lizard', 'spock')#options of choice in game
rules_dict = {#dictionary of winner combinations
    'rock': ('lizard', 'scissors'),
    'spock': ('scissors', 'rock'),
    'paper': ('rock', 'spock'),
    'scissors': ('paper', 'lizard'),
    'lizard': ('paper', 'paper')
}


def player_answer(options):
    """
    А function that takes variations of shapes as a parameter, compares it with input text from console.
    If the test matches the shapes in the list, the function returns the shape,
    if not, the function calls itself again.
    :param options: options of choice in game
    :return: inputed text
    """
    answer = input().lower()
    if answer in options:
        print(f'Player: {answer}')
        return answer
    else:
        print(f'Invalid input: {answer}')
        print('Your choice (rock paper scissors lizard spock)?')
        return player_answer(options)


def computer_answer(options):
    """
    А function that takes variations of shapes as a parameter and return random one of them.
    :param options: options of choice in game
    :return: random one choice
    """
    comp = random.choice(options)
    print(f'Computer: {comp}')
    return comp


def check_winner(human, comp, rules):
    """
    A function that takes two choices from human and computer and return winner.
    :param human: choice of human
    :param comp: choice of computer
    :param rules: options of choice in game
    :return: Bool. If true - human is win, if not - computer
    """
    return comp in rules[human]


def repeat_answer():
    """
    A function that checking player want to play again or not.
    :return: answer from player - 'y' or 'n'
    """
    print('Repeat (Y/N)?')
    answer = input().lower()
    if answer == 'y' or answer == 'n':
        return answer
    else:
        print(f'Invalid input: {answer}, need (Y/N)')
        return repeat_answer()


if __name__ == '__main__':
    repeat_answer_str = 'y'
    comp_counter = 0
    player_counter = 0
    while repeat_answer_str == 'y':
        print('Your choice (rock paper scissors lizard spock)?')
        player_answer_str = player_answer(answer_options)
        computer_answer_str = computer_answer(answer_options)
        if player_answer_str == computer_answer_str:
            print('DRAW!')
            comp_counter += 1
            player_counter += 1
        elif check_winner(player_answer_str, computer_answer_str, rules_dict):
            print('Player WIN!')
            player_counter += 1
        else:
            print('Player LOSE!')
            comp_counter += 1
        print(f'Counter: Player - {player_counter}   Computer - {comp_counter}')
        repeat_answer_str = repeat_answer()
    print('Thanks for playing. Goodbye!')
