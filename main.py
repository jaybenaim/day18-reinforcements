def word_counter(string): 
    words = []

    for word in string:
        each_word = word.split()
        words.append(each_word)
        
    for word in words: 
        length = len(word)

    return length 

print(word_counter(['this is a test']) )