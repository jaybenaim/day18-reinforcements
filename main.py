def word_counter(string): 
    word_list = []
    
    for words in string: 
        each_word = string.split()
        if words == None: 
            return 0  
        else: 
            for word in each_word:  
                word_list.append(word)
        
        return len(word_list)
    

    

print(word_counter('this is a test'))

print(word_counter("Hello world") )# returns 2

print(word_counter("This is a sentence")) # returns 4

print(word_counter("")) # returns 0
