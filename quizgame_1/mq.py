#!/usr/bin/env python3

# Quiz game to practice different sums or anagrams

import random
import os
import operator

def print_main_menu():
    # Clear the screen
    os.system("cls")

    # Print the main menu
    print ("""
    **************************************************
    *                                                *
    *           Fancy playing a cool game?           *
    *                                                *
    *     What type of game do you want to play?     *
    *                                                *
    *                 1. Addition                    *
    *                 2. Subtraction                 *
    *                 3. Multiplication              *
    *                 4. Division                    *
    *                 5. Remainders                  *
    *                 6. Anagrams                    *
    *                                                *
    *                 99. Exit                       *
    *                                                *
    *   !PLEASE SELECT WHICH GAME YOU WANT TO PLAY!  *
    *                                                *
    **************************************************
    """)


def get_game_type():

    # Wait on user input. This function is only called after the print_main_menu function
    selection = input()

    # Assigns value to game_type depending on user input
    if selection == "1":
        game_type = "+"
    elif selection == "2":
        game_type = "-"
    elif selection == "3":
        game_type = "*"
    elif selection == "4":
        game_type = "/"
    elif selection == "5":
        game_type = "mod"
    elif selection == "6":
        game_type = "anagrams"
    elif selection == "99":
        os.system("cls")
        print("Come back soon!!\n\n\n\n\n")
        exit()
    else:
        os.system("cls")
        print_main_menu()
        get_game_type()

    return game_type


def get_question_settings():

    # Prestages some variables
    question_count = ""
    question_difficulty = ""

    # Gets a valid value from user for number of questions
    while not question_count:
        os.system("cls")
        try:
            question_count = int(input("How many questions would you like? (5-20)"))
        except ValueError:
            question_count = ""
        else:
            if question_count < 5 or question_count > 20:
                question_count = ""

    # Gets a valid value from user for difficulty of questions
    while not question_difficulty:
        os.system("cls")
        try:
            question_difficulty = int(input("What difficulty would you like? (1-Easy, 2-Medium, 3-Hard)"))
        except ValueError:
            question_difficulty = ""
        else:
            if question_difficulty not in [1,2,3]:
                question_difficulty = ""

    return question_count, question_difficulty


def set_questions(game_type, question_difficulty, question_count):

    # For maths games, assigns operator string to actual operator to be used in calculation
    ops = {"+": operator.add,
       "-": operator.sub,
       "*": operator.mul,
       "/": operator.floordiv,
       "mod": operator.mod
       }

    # Prestages question_pack as an empty list. The final pack will be a list of dictionaries
    # with each dictionary containing all the relevant items for a specific question
    question_pack = []

    # Based on question difficulty, sets boundaries for sum numbers or size of words for anagrams
    if question_difficulty == 1:
        lower, upper, letters = 1, 11, 5
    elif question_difficulty ==2:
        lower, upper, letters = 1, 100, 8
    elif question_difficulty ==3:
        lower, upper, letters = 10, 1000, 100

    # This code block gets valid word list based on max number of letters
    # and then chooses the correct number based on question count
    if game_type == "anagrams":
        with open('mywords.txt', 'r') as file:
            full_word_list = [x.strip('\n') for x in file.readlines()]
        file.close()

        valid_word_list = []

        for word in full_word_list:
            if len(word) <= letters and word.lower() == word:
                valid_word_list.append(word)

        words = random.sample(valid_word_list, question_count)
        anagram = ""
        anagrams = []

        for word in words:
            while word:
                position = random.randrange(len(word))
                anagram += word[position]
                word = word[:position] + word[(position + 1):]
            anagrams.append(anagram)
            anagram = ""

        for i in range(len(words)):
            question_pack.append({'word' : words[i], 'anagram' : anagrams[i]})
    # Generates questions based on count, difficulty parameters and operator
    else:
        maths_operator = ops[game_type]
        for i in range(question_count):
            number1 = random.randint(lower, upper)
            number2 = random.randint(lower, upper)
            number1, number2 = max(number1, number2), min(number1, number2)
            question_pack.append({'high' : number1, 'low' : number2, 'operator' : game_type, 'sum' : maths_operator(number1, number2)})

    return question_pack


def get_answers(game_type, question_pack):

    # Poses the relevant question and adds the user's answer to the question pack
    if game_type == 'anagrams':
        for question in question_pack:
            os.system("cls")
            question['answer'] = input("What word is " + question['anagram'] + " an anagram of? ")
    else:
        for question in question_pack:
            os.system("cls")
            question['answer'] = input("What is " + str(question['high']) + " " + question['operator'] + " " + str(question['low']) + "? ")

    return question_pack


def get_score(game_type, answers):

    # Checks given answer to correct one and updates question pack with score for each question
    if game_type == 'anagrams':
        for answer in answers:
            if answer['answer'] == answer['word']:
                answer['score'] = 'correct'
            else:
               answer['score'] = 'incorrect'
    else:
        for answer in answers:
            if answer['answer'] == str(answer['sum']):
                answer['score'] = 'correct'
            else:
               answer['score'] = 'incorrect'

    return answers


def print_score(question_count, score):

    # Counts the number of correct answers and prints relevant message
    total_score = 0

    for each in score:
        if each['score'] == 'correct':
           total_score += 1

    os.system("cls")

    print("You answered " + str(question_count) + " questions and got " + str(total_score) + " correct!\n")

    if total_score == question_count:
        print("\nWell done! You got them all right!!\n")


def main():

    # The main function which uses the other functions as a workflow
    print_main_menu()
    game_type = get_game_type()
    question_count, question_difficulty = get_question_settings()
    question_pack = set_questions(game_type, question_difficulty, question_count)
    answers = get_answers(game_type, question_pack)
    score = get_score(game_type, answers)
    print_score(question_count, score)

if __name__ == "__main__":
    main()
