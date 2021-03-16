"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items: 
        print (item)


def get_all_evens(nums):
    even_list = [num for num in nums if num % 2 == 0]
    return even_list

def get_odd_indices(items):
    result = []
    for i in items:
        if i % 2 != 0:
            result.append(i)
    return result


def print_as_numbered_list(items):
    i = 1
    for item in items:
        print(f"{i}. {item}")
        i += 1


def get_range(start, stop):
    nums = [num for num in range(start, stop)]

    return nums


def censor_vowels(word):
    """ 

    >>> censor_vowels('cat')
    'c*t'
    
    """
    char = ''
    for letter in word:
        if letter in 'aeiou':
            letter = '*'
        char += letter

    return char


def snake_to_camel(string):
    camelCase = []
    for word in string.split('_'):
        word.title()
    
    return word 



def longest_word_length(words):
    len_longest_word = len(words[0])
    for word in words:
        if len(word) > len_longest_word:
            len_longest_word = len(word)
    return len_longest_word


def truncate(string):
    result = []

    for char in string:
        if len(result) == 0 or char not in result[-1]:
            result.append(char)
    return "".join(result)
    #in JS:  return result.join('');


def has_balanced_parens(string):
    parens = 0

    if string[0] == ')':
        return False #counting for if string has an unbalanced word
    for char in string:
        if char == '(':
            parens += 1
        else:
            if char == ')':
                parens -= 1

    return parens == 0 

def compress(string):
   compressed = []

   current_char = ''
   char_count = 0

   for char in string:
       
