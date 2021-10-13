# Length of Last word
# Create a function that given a string as a parameter of upper/lower case letters
# and empty space characters (" "), return the length of the last word. 
# Meaning, the word that appears far most to the right if we loop through the words.

# Example Input: 
##s1 = "Oh My God Becky, Look at her butt"
# Example Output: 4

# Example Input:
#s2 = "One of those rap guys' girlfriends"
# Example Output: 11

# Example Input:
#s3 = "You other brothers can't deny"
# Example Output: 4

def length_of_word(string1):
    string1 = string1.split()
    return len(string1[-1])

print(length_of_word("You other brothers can't deny"))
print(length_of_word("One of those rap guys' girlfriends"))
