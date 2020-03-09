'''
https://www.codewars.com/kata/52bc74d4ac05d0945d00054e
'''

def first_non_repeating_letter(string):
    index_res = None
    letters = [i for i in string]
    letters_low = [i.lower() for i in letters]
    for i in letters_low:
        if letters_low.count(i) == 1:
            index_res = letters_low.index(i)
            return letters[index_res]
    return ''
