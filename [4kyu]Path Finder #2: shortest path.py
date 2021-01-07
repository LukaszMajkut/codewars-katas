'''
https://www.codewars.com/kata/57658bfa28ed87ecfa00058a
'''

def path_finder(maze):
    maze = list(map(list,maze.split("\n")))
    start = [0,0]
    finish = [len(maze)-1,len(maze[0])-1]

    moves = []
    moves.append(start)
    reps = 0
    
    def check(moves):
        next_moves = []
        for i in moves:

            y = i[0]
            x = i[1]

             #check right
            if 0 <= y < len(maze) and 0 <= x + 1 < len(maze) and maze[y][x+1] != 'W':
                if [y,x+1] in next_moves:
                    pass
                else:
                    next_moves.append([y,x+1])
             #check left
            if 0 <= y < len(maze) and 0 <= x - 1 < len(maze) and maze[y][x-1] != 'W':
                if [y,x-1] in next_moves:
                    pass
                else:
                    next_moves.append([y,x-1])
             #check down
            if 0 <= y + 1 < len(maze) and 0 <= x < len(maze) and maze[y+1][x] != 'W':
                if [y+1,x] in next_moves:
                    pass
                else:
                    next_moves.append([y+1,x])
             #check up
            if 0 <= y - 1 < len(maze) and 0 <= x < len(maze) and maze[y-1][x] != 'W':
                if [y-1,x] in next_moves:
                    pass
                else:    
                    next_moves.append([y-1,x])

            maze[y][x] = 'W'

        return next_moves
    
    while len(moves) > 0:
        
        reps += 1
        for i in check(moves):
            if i == finish:
                return reps

        moves = check(moves)  
        
    return False
