# Hangman project
from hangman_art import logo
print(logo)
import random
from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
for _ in range(word_length):
    display += "_"
print(display)
end_of_game = False
lives = 6 

while not end_of_game:   
    guess = input("Guess a letter : ").lower()
    if guess in display:
        print(f"you have already guessed this word, try another one")
   
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position]= letter
            print(f"You guessed  '{guess}' , this letter is present in the word")
        
            
    print(display)
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed '{guess}', this is not in the word , you lose a life")
        print(f"you have {lives} lives left")
        if lives == 0:
            end_of_game = True
            print("YOU LOSE :(")
    print(f"{' '.join(display)}")
    if "_" not in display:
        print("YOU WIN!!!")
        end_of_game = True
    from hangman_art import stages
    print(stages[lives])  


     