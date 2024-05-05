#1
def smallestMultiple(N, S):
    numbers_queue = [(0,0)]
    numbers_list = sorted(list(S))
    queue_start = 0
    checked = set()
    while queue_start < len(numbers_queue):
        number, answer = numbers_queue[queue_start]
        queue_start += 1
        if answer == 0 and number != 0:
            return number
        for i in numbers_list:
            new_number = number * 10 + i
            new_answer = (answer * 10 + i) % N


            if new_answer not in checked:
                checked.add(new_answer)
                numbers_queue.append((new_number, new_answer))
    return None

3.
#Performs Reversals and poping characters between the strings to create a new string
#P = number of Ps in the operations, R = number of Rs in the operations
#Runtime should be R * n + P, which is O(n)
def StringOperator(string, operations):
    print(string)
    outputString = ""
   
    #string = reverse(string)
    #newStrings = pop(string, outputString)


    #string = newStrings[0]
    #outputString = newStrings[1]
    #string = reverse(string)


    for letter in operations:
        if letter == "P":
            newStrings = pop(string, outputString)


            string = newStrings[0]
            outputString = newStrings[1]
        elif letter == "R":
            string = reverse(string)


   
    return outputString
   
   


#Reverses the string by pushing it into a stack and popping it off again
#Runtime should be 2 * the number of letters in th sring so O(n)
def reverse(string):
    reverseLetters = Stack()
    tempStack = Stack()


    for letter in string:
        tempStack.push(letter)


    outputString = ""
    for x in range(tempStack.size()):
        outputString = outputString + tempStack.peek()
        tempStack.pop()


    return outputString
#Removes th first element from the string and adds it to the end of the output string
#Constant runtime
def pop(string, outputString):
    letter = string[0]
    string = string[1:]
    outputString = outputString + letter


    return(string, outputString)

#2 
#You are designing a maze-solving robot that, given a description of a maze
#structure, and an intended destination within that maze, should determine the
#shortest path from the starting point to the destination. The maze description
#is given as a 2-dimensional list called M of 0’s and 1’s, where 0 indicates a
#dead end, and 1 indicates a path to follow. Your starting position is always at
#position (0,0), and the destination position is given as a tuple D. If the
#shortest path from the starting position exists, return it as a list of tuples
#indicating the path to be followed. Implement your solution as MazeSolver(M,D).
#Example inputs are provided in the text file ‘MazeSamples.txt’ on Canvas. 


#a. M = [[1,1,0,0,0], D = (4,0) , Answer =
#[(0,0),(1,0),(2,0),(2,1),(3,1),(4,1),(4,0)]
#[1,0,1,1,1],
#[1,1,0,1,0],
#[0,1,0,1,1],
#[1,1,1,1,0]]
#b. M =[[1,1,0,0,0], D = (3,4), Answer =
#[(0,0),(1,0),(2,0),(2,1),(3,1),(4,1),(4,2),(4,3),(3,3),(3,4)]
#[1,0,1,1,1],
#[1,1,0,1,0],
#[0,1,0,1,1],
#[1,1,1,1,0]]
#c. M =[[1,1,1,0,0], D = (3,4), Answer =
#[(0,0),(0,1),(0,2),(1,2),(1,3),(2,3),(3,3),(3,4)]
#[1,0,1,1,1],
#[1,1,0,1,0],
#[0,1,0,1,1],
#[1,1,1,1,0]]


from collections import deque

def MazeSolver(M, D):
    # Define possible moves: up, down, left, right
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # Initialize the queue with starting position (0, 0)
    queue = deque([(0, 0)])
    
    # Initialize a dictionary to keep track of visited positions and their parent positions
    visit = {(0, 0): None}
    
    while queue:
        cur_p = queue.popleft()
        
        # Check if we have reached the destination
        if cur_p == D:
            break
        
        # Explore possible moves
        for move in moves:
            n_position = (cur_p[0] + move[0], cur_p[1] + move[1])
            
            # Check if the new position is within the maze boundaries and is a valid path (1)
            if 0 <= n_position[0] < len(M) and 0 <= n_position[1] < len(M[0]) and M[n_position[0]][n_position[1]] == 1:
                # Check if the new position has not been visited yet
                if n_position not in visit:
                    visit[n_position] = cur_p
                    queue.append(n_position)
    
    # If the destination was not found, return None
    if D not in visit:
        return None
    
    # Reconstruct the shortest path
    path = []
    cur = D
    while cur is not None:
        path.append(cur)
        cur = visit[cur]
    path.reverse()
    
    return path

# test case 
maze = [
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1]
]
destination = (4, 4)
print(MazeSolver(maze, destination))  # Output: [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (3, 3), (4, 3), (4, 4)]
print(maze)
