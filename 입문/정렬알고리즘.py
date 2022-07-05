9# 셰이커 정렬: 홀수 패스에서는 가장 작은 원소를 맨 앞으로 이동시키고, 짝수 패스에서는 가장 큰 원소를 맨 뒤로 이동시킨다.
# 셸 정렬: 정렬할 배열의 원소를 그룹으로 나눠 각 그룹별로 정렬을 수행한 후, 그룹을 합치는 작업을 반복하여 원소의 이동횟수를 줄임
# 4-정렬: 4칸씩 떨어진 원소를 꺼내어 그룹별로 나누고 정렬한다
# 2-정렬: 2칸씩 떨어진 원소를 꺼내어 그룹별로 나누고 정렬한다
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 버블정렬 알고리즘 구현하기

# from typing import MutableSequence

# def bublle_sort(a : MutableSequence) -> None:
#     n = len(a)
#     for i in range(n-1):
#         for j in range(n-1, i, -1):
#             if a[j-1] > a[j]:
#                 a[j-1], a[j] = a[j], a[j-1]

# if __name__ == '__main__':
#     print('버블 정렬을 수행합니다')
#     num = int(input('원소 수를 입력하세요:'))
#     x = [None] * num

#     for i  in range(num):
#         x[i] = int(input(f'x[{i}]: '))
#         bublle_sort(x)

#         print('오름차순으로 정렬했습니다.')
#         for i in range(num):
#             print(f'x[{i}] = {x[i]}')
# ------------------------------------------------------------------------------------------------

# 버블 정렬로 알고리즘 구현하기

# from typing import MutableSequence

# def bubble_sort(a: MutableSequence)-> None:
#     n = len(a)
#     for i in range(n-1):
#         for j in range(n-1, i, -1): # 왜 n-1인지 모르겠음
#             if a[j-1] > a[j]:
#                 a[j-1], a[j] = a[j], a[j-1]
                
# if __name__ == '__main__':
#     print('버블 정렬을 수행합니다')
#     num = int(input('원소 수를 입력하세요.:'))
#     x = [None] * num
    
#     for i in range(num):
#         x[i] = int(input(f'[{i}]:'))
    
#     bubble_sort(x)
    
#     print('오름차순으로 정렬했습니다.')
#     for i in range(num):
#         print(f'[{i}] = {x[i]}')
# ------------------------------------------------------------------------------------------------

# 버블 정렬 알고리즘 구현하기(정렬 과정을 출력)

# from typing import MutableSequence

# def bubble_sort_verbose(a : MutableSequence) -> None:
#     # 버블 정렬 과정을 출력
#     ccnt = 0 # 비교횟수
#     scnt = 0 # 교환횟수
    
#     n = len(a)
#     for i in range(n-1):
#         print(f'패스{i + 1}')
#         for j in range(n-1, i, -1):
            
#             for m in range(0, n-1):
#                 print(f'{a[m]:2}' +  ('  ' if m != j-1 else
#                                       '+' if a[j-1] > a[j] else ' -'),
#                                             end=' ')
#             print(f'{a[n-1]:2}')
#             ccnt +=1
            
#             if a[j-1] > a[j]:
#                 scnt +=1
#                 a[j-1], a[j] = a[j], a[j-1]
#         for m in range(0, n-1):
#             print(f'{a[m]:2}', end=' ')
#         print(f'{a[n-1]:2}')
#     print(f'비교를 {ccnt}번 했습니다')
#     print(f'교환을 {scnt}번 했습니다.')

# if __name__ == '__main__':
#     print('버블 정렬을 수행합니다')
#     num = int(input('원소 수를 입력하세요.:'))
#     x = [None] * num

#     for i in range(num):
#         x[i] = int(input(f'[{i}]:'))

#     bubble_sort_verbose(x)

#     print('오름차순으로 정렬했습니다.')
#     for i in range(num):
#         print(f'[{i}] = {x[i]}')

# ------------------------------------------------------------------------------------------------

# 버블 정렬 알고리즘 구현하기(알고리즘의 개선1)

# from typing import MutableSequence

# def bubble_sort(a : MutableSequence) -> None:
#     n = len(a)
#     for i in range(n-1):
#         exchang = 0  #패스에서 교환 횟수
#         for j in range(n-1, i, -1):
#             if a[j-1] > a[j]:
#                 a[j -1], a[j] = a[j], a[j-1]
#                 exchang += 1
#         if exchang == 0:
#             break

# if __name__ == '__main__':
#     print('버블 정렬을 수행합니다')
#     num = int(input('원소 수를 입력하세요.:'))
#     x = [None] * num

#     for i in range(num):
#         x[i] = int(input(f'[{i}]:'))

#     bubble_sort(x)

#     print('오름차순으로 정렬했습니다.')
#     for i in range(num):
#         print(f'[{i}] = {x[i]}')
# ------------------------------------------------------------------------------------------------

# 버블 정렬 알고리즘을 구현하기(알고리즘 개선2)

# from typing import MutableSequence

# def bubble_sort(a: MutableSequence) -> None:
#     n = len(a)
#     k = 0
#     while k  < n-1:
#         last = n-1
#         for j in range(n-1, k, -1):
#             if a[j-1] > a[j]:
#                 a[j-1], a[j] = a[j], a[j-1]
#                 last = j
#         k = last
        
# if __name__ == '__main__':
#     print('버블 정렬을 수행합니다')
#     num = int(input('원소 수를 입력하세요.:'))
#     x = [None] * num

#     for i in range(num):
#         x[i] = int(input(f'[{i}]:'))

#     bubble_sort(x)

#     print('오름차순으로 정렬했습니다.')
#     for i in range(num):
#         print(f'[{i}] = {x[i]}')
# ------------------------------------------------------------------------------------------------

# 셰이커 정렬 알고리즘 구하기

# from typing import MutableSequence

# def shaker_sort(a:MutableSequence) -> None:
#     left = 0
#     right = len(a) -1
#     last = right
#     while left < right:
#         for j in range(right, left, -1):
#             if a[j-1] > a[j]:
#                 a[j-1], a[j] = a[j], a[j-1]
#                 last = j
#         left = last
                
#         for j in range(left,right):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]
#                 last = j
#         right = last

# if __name__ == '__main__':
#     print('버블 정렬을 수행합니다')
#     num = int(input('원소 수를 입력하세요.:'))
#     x = [None] * num

#     for i in range(num):
#         x[i] = int(input(f'[{i}]:'))

#     shaker_sort(x)

#     print('오름차순으로 정렬했습니다.')
#     for i in range(num):
#         print(f'[{i}] = {x[i]}')
# ------------------------------------------------------------------------------------------------

# 단순 선택정렬 알고리즘 구현하기

# from typing import MutableSequence

# def selection_sort(a: MutableSequence) -> None:
#     n = len(a)
#     for i in range(n-1):
#         min = i # 정렬할 부분에서 가장 작은 인덱스
#         for j in range(i + 1, n):
#             if a[j] < a[min]:
#                 min = j
#         a[i], a[min] = a[min], a[i]
# ------------------------------------------------------------------------------------------------

# from typing import MutableSequence

# def insertion_sort(a: MutableSequence) -> None:
#     # 단순 삽입 정렬
#     n = len(a)
#     for i in range(1,n):
#         j = i
#         tmp = a[i]
#         while j > 0 and a[j-1] > tmp:
#             a[j] = a[j-1]
#             j -= 1
#         a[j] = tmp
        

# if __name__ == '__main__':
#     print('단순 삽입 정렬을 수행합니다')
#     num = int(input('원소 수를 입력하세요. :'))
#     x = [None] * num
    
#     for i in range(num):
#         x[i] = int(input(f'x[{i}]:' ))
    
#     insertion_sort(x)
    
#     print('오름차순으로 정렬했습니다.')
#     for i in range(num):
#         print(f'x[{i}] = {x[i]}')
    
# ------------------------------------------------------------------------------------------------

# # 이진 삽입 정렬 알고리즘 구현하기

# from typing import MutableSequence

# def binary_insertion_sort(a : MutableSequence) -> None:
#     n = len(a)
#     for i in range(1,n):
#         key = a[i]
#         pl = 0 # 검색 범위의 맨 앞 원소 인덱스
#         pr = i -1 # 검색 범위의 맨 끝 원소 인덱스
        
#         while True:
#             pc = (pl + pr) //2 # 검색 범위의 한 가운데 원소 인덱스
#             if a[pc] == key:
#                 break
#             elif a[pc] < key:
#                 pl = pc+1
#             else:
#                 pr = pc -1
#             if pl > pr:
#                 break
            
#         pd = pc + 1 if pl < pr else pr +1
        
#         for j in range(i, pd, -1):
#             a[j] = a[j-1]
#         a[pd] = key

# if __name__ == '__main__':
#     print('이진 삽입 정렬을 수행합니다.')
#     num = int(input('원소 수를 입력하세요. : '))
#     x = [None] * num
    
#     for i in range(num):
#         x[i] = int(input(f'x[{i}]: '))
        
#     binary_insertion_sort(x)
    
#     print('오름차순으로 정렬했습니다')
    
#     for i in range(num):
#         print(f'x[{i}] = {x[i]}')
# ------------------------------------------------------------------------------------------------

# 셸 정렬 알고리즘 구현하기 (코드가 이해 안됨)

# from typing import MutableSequence

# # def shell_sort(a: MutableSequence) -> None:
# a = [5,3,2,6,8,7,1,4]    

# n = len(a)

# h = n // 2 # 초깃값. 전체 배열에 절반으로 나눠준다
# print('dkdk', h)
# while h > 0:
#     for i in range(h,n):
#         j = i - h
#         print('1.',j)
#         tmp = a[i]
#         print(i)
#         while j>=0 and a[j] > tmp:
#             a[j + h] = a[j]
#             print('2.', a[j])
#             j -= h
#             print('3.',j)
#         a[j+h] = tmp
#         print('4.',tmp)
#     h // 2
#     print('5.',h)


# # if __name__=='__main__':
# #     print('셸 정렬을 수행합니다.')
# #     num = int(input('원소 수를 입력하세요.:'))
# #     x = [None] * num

# #     for i in range(num):
# #         x[i] = int(input(f'x[{i}]:'))


# #     shell_sort(x)

# #     print('오름차순으로 정렬했습니다.')
# #     for i in range(num):
# #         print(f'x[{i}] = {x[i]}')
# ------------------------------------------------------------------------------------------------

# 셸 정렬 알고리즘 구현하기:h * 3 + 1의 수열 사용 (이해못함)

# from typing import MutableSequence

# def shell_sort(a : MutableSequence) -> None:
#     n = len(a)
#     h = 1

#     while h < n // 9:
#         h =h*3+1

#     while h > 0:
#         for i in range(h,n):
#             j = i -h
#             tmp = a[i]
#             while j >=0 and a[j] > tmp:
#                 a[j+h] = a[j]
#                 j -= h 
#                 a[j+h] = tmp
#         h //=3

# if __name__ == "__main__":
#     print('셸 정렬을 수행합니다')
#     num = int(input('원소 수를 입력하세요'))
#     x = [None] * num

#     for i in range(num):
#         x[i] = int(input(f'x[{i}]: '))

#     shell_sort(x)

#     print('오름차순으로 정렬했습니다.')
#     for i in range(num):
#         print(f'x[{i}] = {x[i]}')
# ------------------------------------------------------------------------------------------------

# 퀵 정렬 : 배열을 두 그룹으로 나누기

# from re import X
# from typing import MutableSequence

# def partition(a: MutableSequence) -> None:
#     n = len(a)
#     pl = 0
#     pr = n -1
#     x = a[n // 2] # 피벗(가운데 원소)

#     while pl <= pr:
#         while a[pl] <x: pl +=1
#         while a[pr] > x: pr -=1
#         if pl <= pr:
#             a[pl], a[pr] = a[pr], a[pl]
#             pl += 1
#             pr -= 1
#     print(f'피벗은 {x}입니다')

#     print('피벗 이하인 그룹입니다')
#     print(*a[0 :pl])

#     if pl > pr+1:
#         print('피벗과 일치하는 그룹입니다.')
#         print(*a[pr + 1 : pl])


#         print('피벗 이상인 그룹입니다.')
#         print(*a[pr +1 : n])

# if __name__ == '__main__':
#     print('배열을 나눕니다.')
#     num = int(input('원소 수를 입력하세요 :'))
#     x = [None] * num

#     for i in range(num):
#         x[i] = int(input(f'x[{i}]: '))
    
#     partition(x)
# ------------------------------------------------------------------------------------------------

# 배열을 두 그룹으로 나누기

# from typing import MutableSequence

# def partition(a: MutableSequence) -> None:
#     # 배열을 나누어 출력
#     n = len(a) 
#     pl = 0
#     pr = n -1
    
#     x = a[n // 2] # 피벗
    
#     while pl <= pr:
#         while a[pl] < x: pl +=1
#         while a[pr] > x: pr -= 1
#         if pl <= pr:
#             a[pl], a[pr] = a[pr], a[pl]
#             pl += 1
#             pr -= 1
            
#     print(f'피벗은 {x}입니다.')
    
#     print(f'피벗 이하인 그룹입니다.')
#     print(*a[0 : pl]) 
    
#     if pl > pr + 1:
#         print('피벗과 일치하는 그룹입니다,')
#         print(*a[pr + 1 : pl ]) # a[pr+1] ~ a[pl-1]
        
#     print('피벗 이상인 그룹입니다.')
#     print(*a[pr + 1 : n]) # a[pr +1] ~ a[n-1]
        
# if __name__ == '__main__':
#     print('배열을 나눕니다.')
#     num = int(input('원소 수를 입력하세요.: '))
#     x = [None] * num
    
#     for i in range(num):
#         x[i] = int(input(f'x[{i}]: '))
        
#     partition(x)
# ----------------------------------------------------------------------------------------

# 퀵 정렬 알고리즘 구현하기

# from typing import MutableSequence

# def qsort(a: MutableSequence, left: int, right: int) -> None:
#     pl = left
#     pr = right
#     x = a[(left + right) // 2 ]
    
#     while pl <= pr:
#         while a[pl] < x: pl +=1
#         while a[pr] < x: pr -=1
        
#         if pl <= pr:
#             a[pl], a[pr] = a[pr], a[pl]
#             pl += 1
#             pr -= 1
    
#     if left < pr: qsort(a, left, pr)
#     if pl < right: qsort(a, pl, right)

# def quick_sort(a: MutableSequence) -> None:
    
#     qsort(a, 0, len(a)-1)

# if __name__ == '__main__':
#     print('퀵 정렬을 수행합니다.')
#     num = int(input('원소 수를 입력하세요.: '))
#     x = [None] * num
    
#     for i in range(num):
#         x[i] = int(input(f'x[{i}]: '))
        
#     quick_sort(x)
    
#     print('오름차순으로 정렬합니다.')
#     for i in range(num):
#         print(f'x[{i}] = {x[i]}')
# ----------------------------------------------------------------------------------------

# 비 재귀적인 퀵 정렬 구현하기

# from stack import Stack # 전에 작성한 코드를 임포트 해옴
# from typing import MutableSequence

# def qsort(a : MutableSequence, left : int, right: int) -> None:
#     range = Stack(right - left +1) # 스택 생성
    
#     range.push((left,right))
    
#     while not range.is_empty():
#         pl , pr = left, right = range.pop()           
#         x = a[(left + right) //2]
        
#         while pl <= pr:
#             while a[pl] < x: pl +=1
#             while a[pr] > x: pr -=1
#             if pl < pr:
#                 a[pl], a[pr] = a[pr], a[pl]
#                 pl += 1
#                 pr -= 1
                
#         if left < pr: range.push((left, pr)) # 왼쪽 그룹의 커서 저장
#         if pl < right: range.push((pl, right))
# 이하 생략
# ----------------------------------------------------------------------------------------

# 퀵 정렬 알고리즘 구현하기(원소수가 9 미만이면 단순 삽입 정렬)

# from typing import MutableSequence

# def sort3(a: MutableSequence, idx1: int, idx2: int, idx3: int):
#     # a[idx], a[idx2], a[idx3]를 오름차순으로 정렬하고 중앙값의 인덱스를 반환
#     if a[idx2] < a[idx1] : a[idx2], a[idx1] = a[idx1], a[idx2]
#     if a[idx3] < a[idx2] : a[idx3], a[idx2] = a[idx2], a[idx3]
#     if a[idx2] < a[idx1] : a[idx2], a[idx1] = a[idx1], a[idx2]

# def insertion_sort(a :MutableSequence, left : int, right: int) -> None:
#     # a[left] ~ a[right]를 단순 삽입 정렬
#     for i in range(left +1, right +1):
#         j = i
#         tmp = a[i]
#         while j > 0 and a[j-1] > tmp:
#             a[j] = a[j-1]
#             j -= 1
#         a[j] = tmp

# def qsort(a :MutableSequence, left: int, right: int)-> None:
#     if right - left < 9:  # 원소 수가 9 미만이면 삽입 정렬로 전환
#         insertion_sort(a, left, right)
#     else:
#         pl = left
#         pr = right
#         m = sort3(a, pl, (pl+pr) // 2, pr)
#         x = a[m]
        
#         a[m], a[pr -1] = a[pr -1], a[m]
#         pl += 1
#         pr -= 2
#         while pl <= pr:
#             while a[pl] < x: pl += 1
#             while a[pr] > x: pr -= 1
#             if pl <= pr:
#                 a[pl], a[pr] = a[pr], a[pl]
#                 pl += 1
#                 pr -= 1
        
#         if left < pr: qsort(a, left, pr)
#         if pl < right: qsort(a, pl, right)

# def quick_sort(a:MutableSequence) -> None:
    
#     qsort(a, 0, len(a)-1)

# if __name__ == '__main__':
#     print('퀵 정렬을 합니다.(원소수가 9 미만이라면 단순 삽입 정렬을 합니다')
#     num = int(input('원소 수를 입력하세요.: ' ))
#     x = [None] * num
    
#     for i in range(num):
#         x[i] = int(input(f'x[{i}]: '))
        
#     quick_sort(x)
    
#     print('오름차순으로 정렬했습니다')
    
#     for i in range(num):
#         print(f'x[{i}] = {x[i]}')
# ----------------------------------------------------------------------------------------

# sorted() 함수를 사용하여 정렬하기

# print('sorted() 함수를 사용하여 정렬하기')
# num = int(input('원소 수를 입력하세요,:'))
# x = [None] * num
        
# for i in range(num):
#     x[i] = int(input(f'x[{i}]: '))          
    
# # 배열 x를 오름차순으로 정렬
# x = sorted(x)
# print('오름차순으로 정렬했습니다')
# for i in range(num):
#     print(f'x[{i}] = {x[i]}')
    
# # 배열 x를 내림차순으로 정렬
# x =sorted(x, reverse= True)
# print('내림차순으로 정렬했습니다.')
# for i in range(num):
#     print(f'x[{i}] = {x[i]}')
    
# ----------------------------------------------------------------------------------------

# 정렬을 마친 두 배열을 병합하기

# from typing import Sequence, MutableSequence

# def merge_sorted_list(a: Sequence, b: Sequence, c: MutableSequence) -> None:
#     # 정렬을 마친 배열 a와 b를 병합하여 c에 저장
#     pa, pb, pc = 0,0,0,

#     na, nb, nc = len(a), len(b), len(c) # 각 배열의 원소수

#     while pa < na and pb < nb:  # pa와 pb를 비교하여 작은 값을 pc에 저장
#         if a[pa] < b[pb]:
#             c[pc] = a[pa]
#             pa += 1
#         else:
#             c[pc] = b[pb]
#             pb += 1
#         pc +=1

#     while pa < na: # a에 남은 원소를 c에 복사
#         c[pc] = a[pa]
#         pa +=1
#         pc +=1

#     while pb < nb:
#         c[pc] = b[pb]
#         pb +=1
#         pc +=1

# if __name__ == '__main__':
#     a = [2,4,6,8,11,13]
#     b = [1,2,3,4,9,16,21] # 임의의 배열 생성
#     c = [None] * (len(a)+len(b))
    
#     print('정렬을 마친 두 배열의 병합을 구합니다')

#     merge_sorted_list(a,b,c)

#     print('배열 a와 b를 병합하여 배열 c에 저장했습니다')
#     print(f'배열 a: {a}')
#     print(f'배열 b: {b}')
#     print(f'배열 c: {c}')
# ----------------------------------------------------------------------------------------

# 병합 정렬 알고리즘 구현하기

# from tkinter import N
# from typing import MutableSequence

# def merge_sort(a: MutableSequence) -> None:

#     def _merge_sorted(a: MutableSequence, left: int, right: int) -> None:
#         # a[left] - a[right]를 재귀적으로 병합 정렬
#         if left < right:
#             center = (left + right) // 2

#             _merge_sorted(a, left, center) # 배열 앞부분을 병합정렬
#             _merge_sorted(a, center+1, right) # 배열 뒷부분을 병합정렬

#             p = j = 0
#             i = k = left

#             while i <= center:
#                 buff[p] = a[i]
#                 p +=1
#                 i +=1

#             while i <= right and j < p:
#                 if buff[j] <= a[i]:
#                     a[k] = buff[j]
#                     j += 1
#                 else:
#                     a[k] = a[i]
#                     i +=1
#                 k +=1
#             while j < p :
#                 a[k] = buff[j]
#                 k +=1
#                 j +=1
    
#     n = len(a)
#     buff = [None] * n  # 작업용 배열을 생성
#     _merge_sorted(a, 0, n-1) # 배열 전체를 병합 정렬

#     del buff

# if __name__ == '__main__':
#     print('병합 정렬을 수행합니다')
#     num = int(input('원소 수를 입력하세요.: '))
#     x = [None] * num

#     for i in range(num):
#         x[i] = int(input(f'x[{i}]: '))

#     merge_sort(x)

#     print('오름차순으로 정렬')
#     for i in range(num):
#         print(f'x[{i}] = {x[i]}')
# ----------------------------------------------------------------------------------------

# 힙 정렬 알고리즘 구현하기

from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:

    def down_heap(a: MutableSequence, left: int, right: int) -> None:

        temp = a[left] # 루트

        parent = left

        while parent < (right +1) // 2 :
            cl = parent * 2 + 1 #왼쪽자식
            cr = cl + 1 # 오른쪽 자식
            child = cr if cr <= right and a[cr] > a[cl] else cl
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = temp

    n = len(a)
    
    for i in range((n-1) //2, -1, -1):
        down_heap(a,i,n-1)
    
    for i in range(n-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        down_heap(a,0,i-1)

if __name__ == '__main__':
    print('힙 정렬을 수행합니다')
    num = int(input('원소 수를 입력하세요:'))
    x = [None] * num
    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
        
    heap_sort(x)
    print('오름차순으로 정렬했습니다')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

