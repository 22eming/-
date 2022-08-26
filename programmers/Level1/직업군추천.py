def solution(table, languages, preference):
    answer = ''
    cnt = 0
    for t in table:
        t = t.split()
        langCnt = 0
        for i, lang in enumerate(languages):
            if lang in t:
                langCnt += (6 - t.index(lang)) * preference[i]
    
        if langCnt > cnt:
            answer = t[0]
            cnt = langCnt
        elif langCnt == cnt:
            cnt = langCnt
            answer = sorted([t[0], answer])[0]
        
    return answer

solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
["JAVA", "JAVASCRIPT"], [7, 5])