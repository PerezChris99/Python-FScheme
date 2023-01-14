#anagram game
import json
import random
with open('D:\projects/data.json') as f:
    data = json.load(f)

def word_prompt(data, length):
    all_words = list(data.keys())
    while True:
        word = random.choice(all_words)
        if len(word) < length and len(word) > 2:
            return word
def shuffle_word(word):
    array - list(word)
    shuffled = word
    while True:
        random.shuffle(array)
        shuffled = ''.join(array)
        if shuffled != word:
            return shuffled
print("Welcome to the Anagram Game!")
while(True):
    word = word_prompt(data, 5)
    question = shuffle_word(word)
    meaning = data[word]

    question = question.lower()
    word = word.lower()

    print("\nSolve:", question)
    print("Hint:", meaning)

    for i in range(5, 0, -1):
        print("\nAttempts Left:", i)
        quess = input('Make a guess: ').lower()
        if guess == word:
            print("Correct!")
            break
        if i == 1:
            print("\nCorrect Answer:", word)

    choice = input("\nContinue? [y/n: ")
    print('-'*50)
    if choice == 'n':
        print("\nThank you for playing!")
        break