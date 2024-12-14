#Even or Odd
def even_or_odd(number): 
    if number % 2 == 0: 
        return "Even" 
    else:
        return "Odd"

#Number to string
def number_to_string(num):
    # Return a string of the number here!
    return str(num)

#Vowel count
def get_count(sentence):
    count = 0
    vowels = 'aeiou'
    for vowel in sentence:
        if vowel in vowels:
            count += 1
    return count