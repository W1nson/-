

# Auestion 1A
def reverse(word): 
    ans = ""
    for i in range(len(word)-1, -1, -1): #O(n) 
        ans = ans + word[i] 

    return ans 
# total run time is O(n)


# testing 
a_word = "junyiacademy"
print(reverse(a_word))


# Question 1B 
def flip_sentence(sentence): 
    
    ans = "" 
    prev = 0

    for i in range(len(sentence)):  # O(n)
        if sentence[i] == " ": 
            temp = sentence[prev:i] 
            ans = ans + reverse(temp) + " " # O(n)
            prev = i + 1

    temp = sentence[prev:len(sentence)]
    ans = ans + reverse(temp)

    return ans 
    
#total run time is O(n^2) 


# testing
a_sentence = "flipped class room is important"
print(flip_sentence(a_sentence))


