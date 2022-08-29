chess_input = [input() for _ in range(36)]
prev_loc = chess_input[0]

if len(set(chess_input)) != 36:
    print("Invalid")
    exit(0)

def check_valid(prev_loc, next_loc):
    abs_x = abs( ord(prev_loc[0]) - ord(next_loc[0]))
    abs_y = abs( int(prev_loc[1]) - int(next_loc[1]))
    return [abs_x, abs_y] != [2,1] and [abs_x, abs_y] != [1, 2]

for next_loc in chess_input[1:]:
    if check_valid(prev_loc, next_loc):
        print("Invalid")
        break
    prev_loc = next_loc
    
else:
    if check_valid(prev_loc, chess_input[0]):
        print("Invalid")
    else:
        print("Valid")