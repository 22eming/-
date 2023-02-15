from collections import defaultdict, deque
N = int(input())
tree = defaultdict(list)
for i in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

root = set()
answer = [0]*(N+1)
stack = deque([])

def go_tree(q):
    for c in tree[q]:
        if c not in root:
            answer[c] = q
            root.add(c)
            stack.append(c)

stack.append(1)
while stack:
    q = stack.popleft()
    go_tree(q)

for a in answer[2:]:
    print(a)