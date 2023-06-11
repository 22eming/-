def solution(elements):
    sum_elements = elements + elements
    set_elements = set()
    for i in range(1, len(elements)+1):
        for j in range(len(elements)):
            set_elements.add(sum(sum_elements[j:j+i]))

    return len(set_elements)