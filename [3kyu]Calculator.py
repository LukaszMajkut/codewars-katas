'''
https://www.codewars.com/kata/5235c913397cbf2508000048/train/python
'''

class Calculator(object):
    def evaluate(self, math_str):
        operation = [int(i) if i.isdigit() else i for i in math_str.split()]
        first_iter = []
        second_iter = []
        for i in range(0,len(operation)-1):
            if operation[i] == '/' and operation[i-2] == '/' or operation[i] == '/' and operation[i-2] == '*':
                first_iter.append(first_iter[-1]/operation[i+1])
                del first_iter[-2]
            elif operation[i] == '*' and operation[i-2] == '*' or operation[i] == '*' and operation[i-2] == '/':
                first_iter.append(first_iter[-1]*operation[i+1])
                del first_iter[-2]
            elif operation[i] == '/':
                first_iter.append(operation[i-1]/operation[i+1])
            elif operation[i] == '*':
                first_iter.append(operation[i-1]*operation[i+1])
            elif operation[i+1] == '/' or operation[i-1] == '/' or operation[i+1] == '*' or operation[i-1] == '*':
                pass    
            else:
                first_iter.append(operation[i])
        first_iter.append(operation[-1])

        for i in range(0,len(first_iter)):
            if first_iter[i] == '+' and len(second_iter)>0:
                second_iter.append(second_iter[0]+first_iter[i+1])
                del second_iter[0]
            elif first_iter[i] == '-' and len(second_iter)>0:
                second_iter.append(second_iter[0]-first_iter[i+1])
                del second_iter[0]
            elif first_iter[i] == '+':
                second_iter.append(first_iter[i-1]+first_iter[i+1])
            elif first_iter[i] == '-':
                second_iter.append(first_iter[i-1]-first_iter[i+1])
            else:
                pass
        
        return second_iter[0]
