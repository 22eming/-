from collections import Counter


def solution(n, wires):
    answer = n
    for i in range(len(wires)):
        node_list = [0 for _ in range(n+1)]
        con_num = 0
        lint_num = 1
        for node1, node2 in wires:
            num1 = node_list[node1]
            num2 = node_list[node2]
            if con_num == i:
                con_num += 1
                continue
            if num1 == 0 and num2 == 0:  # 둘 다 없음
                node_list[node1] = lint_num
                node_list[node2] = lint_num
                lint_num += 1
            elif num1 != 0 and num2 != 0:  # 둘 다 존재
                node_list = [num1 if value == num2
                             else value for value in node_list]
            else:
                if num1 > num2:
                    node_list[node2] = num1
                else:
                    node_list[node1] = num2
            con_num += 1
        res = Counter(node_list[1:]).most_common()
        if len(res) > 1:
            if res[1][0] == 0:
                answer = min(res[0][1]-1, answer)
            else:
                answer = min(abs(res[0][1] - res[1][1]), answer)

    return answer


print(solution(3, [[1, 2], [2, 3]]))
