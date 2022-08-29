R_dict = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
a, b, c = R_dict.index(input()), R_dict.index(input()), R_dict.index(input())
print(int(str(a) + str(b) + "0"*c))