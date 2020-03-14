'''
https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8
'''

def tickets(people):
    clerk_cash = {25:0,
                  50:0,
                  100:0
        }
    for i in people:
        if i == 100:
            if clerk_cash[50] >= 1 and clerk_cash[25]>=1:
                clerk_cash[100] += 1
                clerk_cash[50] -= 1
                clerk_cash[25] -= 1
            elif clerk_cash[25] >= 3:
                clerk_cash[100] += 1
                clerk_cash[25] -= 3
            else:
                return 'NO'
        elif i == 50:
            if clerk_cash[25] >= 1:
                clerk_cash[50] += 1
                clerk_cash[25] -= 1
            else:
                return 'NO'    
        elif i == 25:
            clerk_cash[25] += 1
    return 'YES'
