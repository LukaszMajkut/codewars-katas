'''
https://www.codewars.com/kata/55983863da40caa2c900004e
'''
#first attempt using permutations - failed due to timeout error:

def next_bigger(n):
     from itertools import permutations
     combinations = permutations(str(n),len(str(n)))
     numbers = set()
     for i in combinations:
         numbers.add(int("".join(i)))
     numbers = sorted(numbers)
     if len(numbers) > 1 and max(numbers) != n:
         answer = numbers.index(n) + 1
     elif max(numbers) == n:
         return -1
     else:
         answer = numbers.index(n)
     return numbers[answer]
     
 #my final solution:
 
 def next_bigger(n):
    numbers = [int(i) for i in str(n)]
    to_change = []
    for i in range(len(numbers) - 1, 0, -1):
        if numbers[i - 1] < numbers[i]:
            to_change = numbers[i - 1:]
            good = numbers[:i - 1]
            
            check_smaller = to_change[1]
            for j in range(len(to_change)-1,1,-1):
                if to_change[j] < to_change[j-1] and to_change[j] < check_smaller and to_change[j] > to_change[0]:
                    to_change[1] = to_change[j]
                    to_change[j] = check_smaller

            tmp = to_change[1]
            to_change[1] = to_change[0]
            to_change[0] = tmp

            result = good + [to_change[0]] + sorted(to_change[1:])
            return int("".join([str(i) for i in result]))
        else:
            continue

    if len(to_change) == 0:
        return -1
