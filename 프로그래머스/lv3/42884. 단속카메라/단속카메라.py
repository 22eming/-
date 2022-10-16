def solution(routes):
    routes.sort(key= lambda x: (x[1], x[0]))
    answer = 1
    camera = routes[0][1]
    for x,y in routes[1:]:
        if x > camera:
            camera = y
            answer += 1
    return answer