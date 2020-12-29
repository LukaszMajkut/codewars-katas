'''
https://www.codewars.com/kata/5765870e190b1472ec0022a2
'''
def path_finder(maze):
    maze = list(map(list, maze.split("\n")))

    from collections import deque
    
    start_position = [0,0]
    finish = [len(maze)-1,len(maze[0])-1]
    positions = deque()
    positions.append(start_position)
    
    def is_valid(maze, position):

        y = position[0]
        x = position[1]

        test_moves = [[y,x + 1], [y,x - 1], [y - 1,x], [y + 1,x]]
        good_moves = []
    
        for i in test_moves:
            if not (0 <= i[0] < len(maze) and 0 <= i[1] < len(maze[0])):
                continue
            elif maze[i[0]][i[1]] == 'W':
                continue
            else:
                good_moves.append(i)

        return good_moves

    while len(positions) > 0:
    
        position = positions.pop()

        y = position[0]
        x = position[1]
        
        if position == finish:
            return True

        if maze[y][x] == 'W':
            continue

        maze[y][x] = 'W'

        positions.extendleft(is_valid(maze,position))
    
    return False
