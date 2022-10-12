N, k = map(int, input().split())
people = []
for _ in range(N):
    s, t = input().split()
    people.append([s, float(t)])


people = sorted(people, key=lambda x: [x[0], -x[1]])
print('{0} {1:.2f}'.format(people[k-1][0], people[k-1][-1]))
