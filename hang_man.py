secret_word = 'HelloWorld'
word_try = []
chances = ()
dif = input('How hard can you handle? Easy / Medium / Hard: ')
if dif == 'Easy':
    chances = 6
elif dif == 'Medium':
    chances = 4
elif dif == 'Hard':
    chances = 3
print(f'Lets GO! You will have {chances} chances! Good Luck')
while True:
    letter = input('Please insert a letter: ')
    word_try.append(letter)
    if len(letter) == 1:
        if letter in secret_word:
            print(f'Uhhhh gotcha! The {letter} is good!')
        else:
            chances -= 1
            word_try.pop()
            print(f'HAHAHAHA you got it wrong, try again! You still have {chances} chances')
    else:
        print('WOAH one letter only brodah!')
        word_try.pop()
    temp_secret = ''
    for secret_letter in secret_word:
        if secret_letter in word_try:
            temp_secret += secret_letter
        else:
            temp_secret += '*'
    if temp_secret == secret_word:
        print('That is great! You gotcha')
        break
    else:
        print(f'The secret word is still {temp_secret}')
