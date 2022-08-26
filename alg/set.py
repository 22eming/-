#  update
>>> k = {1, 2, 3}
>>> k.update([3, 4, 5])
>>> k
{1, 2, 3, 4, 5}

#원소 제거
>>> k.remove(3)
>>> k.discard(3) # 에러발생 안함

#set 복사
t = s.copy()

#연산자
| - 합집합 연산자
& : 교집합 연산자
- : 차집합 연산자
^ : 대칭차집합 연산자(합집합 - 교집합)

#메소드
union - 합집합
intersection - 교집합
difference - 차집합
symmetric_difference : 대칭차집합 연산자(합집합 - 교집합)
issubset : 부분집합 여부 확인
issuperset : issubset과 반대 superset인지 확인
isdisjoint : 교집합이 없으면 True, 있으면 False
