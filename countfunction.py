def count(word,letter):
    counter = 0
    for character in word:
        if character == letter:
            counter = counter + 1
    print (counter)
input_word = input ('enter word: ')
input_letter = input ('enter letter: ')

count (input_word,input_letter)