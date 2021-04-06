import UCS
import IDS
import ASTAR
import IDASTAR
# reading file and get data
file = open("input.txt", "r")
txt = file.read().split("\n")
algo = txt[0]
start = txt[1].split(',')
start = int(start[0]), int(start[1])
end = txt[2].split(',')
end = int(end[0]), int(end[1])
size = int(txt[3])
board = [0]*size
for i in range(size):
    board[i] = txt[i+4].split(',')
board = [[int(int(j)) for j in i] for i in board]
# choose the algorithm
if algo == 'UCS':
    solution = (UCS.uniform_cost_search(board, start, end))
if algo == 'IDS':
    solution = (IDS.iterative_deepening_search(board, start, end))
if algo == 'ASTAR':
    solution = (ASTAR.Astar(board, start, end))
if algo == 'IDASTAR':
    solution = IDASTAR.iterative_deepening_Astar(board, start, end)
# write the answer to txt file
output = open('output.txt', "w+")
if solution:
    for i, c in enumerate(solution[0]):
        if i != 0:
            output.write('-')
        output.write(c)
    output.write(" "+str(solution[1])+" "+str(solution[2]))
else:
    output.write("no path")
