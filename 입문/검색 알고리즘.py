# 검색 알고리즘
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 보초법 : 검색하고자 하는 키값을 배열의 맨 끝에 저장하여 선형검색의 판단횟수를 반으로 줄이는 역할을 한다.
# 복잡도 : 알고리즘의 성능을 객관적으로 평가하는 기준
# 시간 복잡도 : 실행하는데 필요한 시간을 평가
# 공간 복잡도 : 메모리와 파일 공간이 얼마나 필요한지 평가
# 해시법 : 데이터를 저장할 위치 = '인덱스'를 간단한 연산으로 구하는 것 예를들어 원소의 개수가 13이라면 각 값을 13으로 나누고 나머지값에 해당하는 인덱스에 키값을 추가함
# 해시 충돌: 저장할 버킷이 충돌하는 현상
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# while 문으로 작성한 선형 검색 알고리즘

# from typing import Any, Sequence

# def seq_search( a: Sequence, key: Any) -> int:
#     # 시퀸스 a에서 key와 같이 값이 같은 원소를 검색
#     i = 0

#     while True:
#         if i == len(a):
#             return -1
#         if a[i] == key:
#             return i
#         i += 1

# if __name__ == '__main__':
#     num = int(input('원소 수를 입력하세요. :'))
#     x = [None] * num # 원소 수가 num인 배열 생성

#     for i in range(num):
#         x[i] = int(input(f'x[{i}]: '))
    
#     ky = int(input('검색할 값을 입력하세요.:'))

#     idx = seq_search(x, ky)

#     if idx == -1:
#         print('검색하는 원소가 존재하지 않습니다.')
#     else:
#         print(f'원소의 값은 x[{idx}] 입니다.')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# for 문으로 작성한 선형 검색 알고리즘

# from typing import Any, Sequence

# def seq_search(a: Sequence, key:Any) -> int:
#     for i in range(len(a)):
#         if i == key:
#             return i # 검색에 성공하여 인덱스를 반환

#     else:
#         return -1
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 이전에 작성한 함수를 import해서 실수 검색하기

# from search_while import seq_search

# print('실수를 검색합니다.')
# print('주의 : End를 입력하면 종료합니다.')

# number = 0
# x = []

# while True:
#     s = input(f'x[{number}]:')
#     if s == 'End' :
#         break
#     x.append(float(s)) # 배열 맨 끝에 원소 추가
#     number += 1

# ky = float(input('검색할 값을 입력하세요 :'))

# idx = seq_search(x, ky)
# if idx == -1:
#     print(' 검색값을 갖는 원소가 존재하지 않습니다.')
# else:
#     print(f'검색값은 x[{idx}]에 있습니다.')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# seq_search() 함수를 사용하여 특정 인덱스 검색하기

# from ssearch_while import seq_search

# t = (4,7,5.6,2,3.14,1)

# s = 'string'

# a = ['DTS','AAC','FLAC']

# print(f'{t}에서 5.6의 인덱스는 {seq_search(t,5.6})입니다.')
# print(f'{s}에서 n의 인덱스는 {seq_search(s,'n'})입니다.')
# print(f'{a}에서 5.6의 인덱스는 {seq_search(a,'DTS')}입니다.')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 선형 검색 알고리즘을 보초법으로 수정

# from typing import Any, Sequence 
# import copy

# def seq_search(seq : Sequence, key : Any) -> int:
#     # seq에서 key와 일치하는 원소를 검색 후 int형으로 반환
#     a = copy.deepcopy(seq) # seq를 복사
#     a.append(key) # 보초 키를 추가


#     i = 0
#     while True:
#         if a[i] == key:
#             break
#         i += 1

#     return -1 if i == len(seq) else i

# if __name__ == '__main__':
#     num = int(input('원소 수를 입력하세요 :'))
#     x = [None] * num

#     for i in range(num):
#         x[i] = int(input(f'x[{i}] :'))

#     ky = int(input('검색할 값을 입력하세요. :'))

#     idx = seq_search(x,ky)

#     if idx == -1:
#         print('검색값을 갖는 원소가 존재하지 않습니다.')
#     else:
#         print(f'검색할 값은 x[{idx}]에 있습니다.')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 이진 검색 알고리즘

# from math import trunc
# from typing import Any, Sequence

# def bin_search(a: Sequence, key : Any) -> int:
#     # 시퀸스 a에서 key와 일치하는 값 검색 이후 int형으로 반환

#     pl = 0 # 검색 범위 맨 앞 원소 인덱스
#     pr = len(a) -1 # 검색 범위 맨 뒤 원소 인덱스

#     while True:
#         pc = (pl + pr) // 2
#         if a[pc] == key:
#             return pc
#         elif a[pc] < key:
#             pl = pc +1
#         else:
#             pr = pc - 1
#         if pl > pr:
#             break
#     return -1
# if __name__ == '__main__':
#     num = int(input('원소 수를 입력하세요. :'))
#     x = [None] * num

#     print('배열 데이터를 오름차순으로 입력하세요.')

#     x[0] = int(input('x[0] :'))

#     for i in range(1,num):
#         while True:
#             x[i] = int(input(f'x[{i}]: '))
#             if x[i] >= x[i-1]:
#                 break
    
#     ky = int(input('검색할 값을 입력하세요. :'))
#     idx = bin_search(x,ky)

#     if idx == -1:
#         print('찾는 원소가 없음')
#     else:
#         print(f'검색값은 x[{idx}]에 있음')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 선형 검색의 시간 복잡도

# i = 0  # 0(1)

# while i < n: # 
#     if a[i] == key: 
#         return i
#     i += 1

# return -1
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 이진 검색의 시간 복잡도

# from typing import Any, Sequence


# def bin_search(a:Sequence, key:Any) -> int:
#     pl = 0 # 검색 범위 맨 앞 원소 인덱스
#     pr = len(a) - 1 # 검색 범위 맨 뒤 인덱스

#     while True:
#         pc = (pl + pr) //2
#         if a[pc] == key:
#             return pc
#         elif a[pc] < key:
#             pl = pc + 1
#         else:
#             pr = pc - 1
        
#         if pl > pr:
#             break
#     return -1 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 이진 검색 알고리즘의 실행 과정 출력  -- 코드 이해 못함

# from tkinter import W
# from typing import Any, Sequence

# def bin_search(a: Sequence, key:Any) -> int:
#     pl = 0
#     pr = len(a) -1

#     print('  |', end=" ")
#     for i in range(len(a)):
#         print(f'{i : 4}', end=' ')
#         print()
#         print('----+' + (4 * len(a) + 2) * '_')

#     while True:
#         pc = (pl + pr) // 2

#         print(' |', end=" ")
#         if pl != pc:
#             print((pl* 4 + 1) * ' ' + '<-' + ((pc-pl)*4)*' '+ '+', end=" ")
#         else:
#             print((pc * 4 + 1) * ' ' + '<+', end=' ')
        
#         if pc != pr:
#             print(((pr-pc) * 4 - 2) * ' ' + '->')
        
#         else:
#             print('->')
#         print(f'{pc:3}', end='')
#         for i in range(len(a)):
#             print(f'{a[i]:4}', end ='')
#         print('\n |' )

#         if a[pc] == key:
#             return pc
#         elif a[pc] < key:
#             pl = pc +1
#         else:
#             pr = pc - 1
#         if pl > pr:
#             break
#     return -1
# if __name__ == '__main__':
#     num = int(input('원소 수를 입력하세요. :'))
#     x = [None] * num

#     print('배열 데이터를 오름차순으로 입력하세요.')

#     x[0] = int(input('x[0] :'))

#     for i in range(1,num):
#         while True:
#             x[i] = int(input(f'x[{i}]: '))
#             if x[i] >= x[i-1]:
#                 break
    
#     ky = int(input('검색할 값을 입력하세요. :'))
#     idx = bin_search(x,ky)

#     if idx == -1:
#         print('찾는 원소가 없음')
#     else:
#         print(f'검색값은 x[{idx}]에 있음')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 체인법으로 해시 함수 구현하기
# from __future__ import annotations
# from typing import Any, Type
# import hashlib

# class Node:
#     def __init__(self, key: Any, value: Any, next: Node) -> None:
#         self.key = key
#         self.value = value
#         self.next = next



# class ChaineHash:
#     def __init__(self, capacity: int) -> None:
#         self.capacity = capacity # 해시 테이블 크기를 지정
#         self.table = [None] * self.capacity # 해시 테이블을 선언

#     def hash_value(self, key: Any) -> int:
#         # 해시값을 구한다
#         if isinstance(key, int):
#             return key % self.capacity
#         return(int(hashlib.sha256(str(key).encode()).hexdigest(),16) % self.capacity)

#     def search(self,key:Any) -> Any:
#         # 키가 key인 원소를 검색하여 값을 반환
#         hash = self.hash_value(key)
#         p = self.table[hash]

#         while p is not None:
#             if p.key == key:
#                 return p.value # 검색 성공
#             p = p.next  # 뒤쪽 노드를 주목

        
#         return  None # 검색 실패

#     def add(self, key:Any, value: Any) -> bool:
#         # 키가 key이고 값이 valule인 원소를 추가
#         hash = self.hash_value(key) # 추가하는 key의 해쉬값
#         p = self.table[hash]

#         while p is not None:
#             if p.key == key:
#                 return False
#             p = p.netx

#         temp = Node(key, value, self.table[hash])
#         self.table[hash] = temp
#         return True

#     def remove(self, key:Any) -> bool:
#         # 키가 key인 원소를 삭제
#         hash = self.hash_value(key) # 삭제할 key의 해시값
#         p = self.table[hash] # 노드를 주목
#         pp = None

#         while p is not None:
#             if p.key == key:
#                 if pp is None:
#                     self.table[hash] = p.next
#                 else:
#                     pp.next = p.next
#                 return True #삭제를 성공했다

#             pp = p
#             p = p.next
#         return False
    
#     def dump(self) -> None:
#         for i in range(self.capacity):
#             p = self.table[i]
#             print(i, end=' ')
#             while p is not None:
#                 print(f' ->{p.key} ({p.value})', end = '')
#                 p = p.next
#             print()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 체인법을 구현하는 해시 클래스 ChaninedHash 사용

# from enum import Enum

# Menu = Enum('Menu', ['추가','삭제','검색','덤프','종료']) # 메뉴를 선언

# def select_menu() -> Menu:
#     # 메뉴 선택
#     s = [f'({m.value}){m.name}' for m in Menu]
#     while True:
#         print(*s, sep = "  ", end=" ")
#         n = int(input(': '))
#         if 1 <= n <= len(Menu):
#             return Menu(n)

# hash = ChaineHash 
# hash = ChaineHash(13) # 크기가 13인 해시 테이블을 생성

# while True:
#     menu = select_menu()

#     if menu == Menu.추가: # 추가
#         key = int(input('추가할 키를 입력하세요.:'))
#         val = input('추가할 값을 입력하세요.:')
#         if not hash.add(key, val):
#             print('추가에 실패했습니다.')
        
#         elif menu == Menu.삭제 : 
#             key = int(input('삭제할 키를 입력하세요.:'))
#             if not hash.remove(key):
#                 print('삭제를 실패했습니다.')

#         elif menu == Menu.검색:
#             key = int(input('검색할 키를 입력하세요.:'))
#             if not hash.search(key):
#                 print('검색에 실패했습니다')
#             else:
#                 print('검색할 데이터가 없습니다')
#         elif menu == Menu.덤프:
#             hash.dump
#         else:
#             break
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 















































































































































































































































































































































































































































































































































































































































