word = list(set([input() for i in range(int(input()))]))
print('\n'.join([i for i in sorted(sorted(word) ,key=len)]))