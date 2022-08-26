# print('www.example.com'.lstrip('ewxa.'))
# #istrip 선행문자 제거된 문자열 (모든 값 조합 제거)
# .removefrefix("")
# #removefrefix 단일 접두사 문자열 제거
# .replace(old, new[, count])
# #모든 부분 문자열 old 가 new 로 치환된 문자열의 복사본을 돌려줍니다
# .rfind(sub[, start[, end]])
# #부분 문자열 sub 가 s[start:end] 내에 등장하는 가장 큰 문자열의 인덱스를 돌려줍니다
# .zfill
# # 하나의 리스트에서 모든 조합
# permutations, combinations
# # 두개의 리스트 조합
# product 
# 배열 x,y축 교체
# np.transpose(a)
# 가장 큰수
# min_val = float('inf')


import itertools

list1 = [[1, 10], [2, 22], [3, 19]]
list2 = [[4, 2], [5, 9], [6, 3]]

list3 = list(map(list.__add__, list1, list2))
list4 = list(itertools.chain(*list3))
print(list4)


import re

st = [m.start() for m	in re.finditer('test', 'test test test test')]

print(st)
