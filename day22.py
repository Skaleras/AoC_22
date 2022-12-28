data = open('input_day22.txt')
board, commands = data.read().split('\n\n')
#print(board)
path = board.split('\n')
# print(path)
for i, row in enumerate(path):
    for j, column in enumerate(row):
        if column == '':
            continue
        
        