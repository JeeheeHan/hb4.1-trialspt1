"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items: 
        print (item)


def get_all_evens(nums):
    even_list = [num if num % 2 == 0 for num in nums]
    return even_list

def get_odd_indices(items):
    result = []
    for i in items:
        if i % 2 != 0:
            result.append(i)
    return result


def print_as_numbered_list(items):
    pass  # TODO: replace this line with your code


def get_range(start, stop):
    pass  # TODO: replace this line with your code


def censor_vowels(word):
    pass  # TODO: replace this line with your code


def snake_to_camel(string):
    pass  # TODO: replace this line with your code


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
