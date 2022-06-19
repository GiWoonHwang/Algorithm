#----------------------------------------------------------------------------------------------------------------------------------

# stack 구현하기

# from typing import Any

# class FixedStack:
    
#     class Empty(Exception):
#         pass
#     class Full(Exception):
#         pass

#     def __init__(self, capacity : int = 256) -> None:
#         self.stk = [None] * capacity
#         self.capacity = capacity
#         self.ptr = 0
        
#     def __len__(self) -> int:
#         return self.ptr
    
#     def is_empty(self) -> bool:
#         return self.ptr <= 0
    
#     def is_full(self) -> bool:
#         return self.ptr >= self.capacity
    
#     def push(self, value: Any) -> None:
#         # 스택에 데이터를 넣음
#         if self.is_full():
#             raise FixedStack.Full
#         self.stk[self.ptr] = value
#         self.ptr +=1
        
#     def pop(self) -> None:
#         if self.is_empty():
#             raise FixedStack.Empty
#         return self.stk[self.ptr-1]
    
#     def peek(self) -> Any:
#         if self.is_empty():
#             raise FixedStack.is_empty
#         return self.stk[self.ptr -1]
    
#     def clear(self)  -> None:
#         self.ptr = 0
        
#     def find(self, value: Any) -> Any:
#         for i in range(self.ptr-1, -1, -1):
#             if self.stk[i] == value:
#                 return i
#         return -1
                
#     def count(self, value: Any) -> int:
#         c = 0
#         for i in range(self.ptr):
#             if self.stk[i] == value:
#                 c +=1
#         return c
    
#     def __contains__(self, value: Any) -> bool:
#         return self.count(value) > 0
    
#     def dump(self) -> None:
#         if self.is_empty():
#             print('스택이 비어있습니다')
#         else:
#             print(self.stk[:self.ptr])
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 고정 길이 스택 클래스 사용해보기

# from enum import Enum

# Menu = Enum('Menu', ['푸시','팝','피크','검색','덤프','종료'])

# def select_menu() -> Menu:
#     s = [f'({m.value}){m.name}' for m in Menu]
#     while True:
#         print(*s, sep='  ', end=' ')
        
#         n = int(input(': '))
#         if 1 <= n <=  len(Menu):
#             return Menu(n)
#         s
# s = FixedStack(64)

# while True:
#     print(f'현재 데이터 개수: {len(s)} / {s.capacity}')
#     menu = select_menu()
    
#     if menu == Menu.푸시:
#         x = int(input('데이터를 입력하세요.:'))
#         try:
#             s.push(x)
#         except FixedStack.Full:
#             print('스택이 가득 찼습니다')
            
#     elif menu == Menu.팝:
#         try:
#             x = s.pop()
#             print(f'팝한 데이터는 {x}입니다')
#         except FixedStack.Empty:
#             print('스택이 비어 있습니다.')
#     elif menu == Menu.피크:
#         try:
#             x = s.peek()
#             print(f'피크한 데이터는 {x}입니다')
#         except FixedStack.Empty:
#             print('스택이 비어있습니다')
#     elif menu == Menu.검색:
#         x = int(input('검색할 값을 입력하세요:'))
#         if x in s:
#             print(f'{s.count(x)}개 포함되고, 맨 앞의 위치는 {s.find(x)}입니다')
#         else:
#             print('검색값을 찾을 수 없습니다')
#     elif menu == Menu.덤프:
#         s.dump()
    
#     else:
#         break
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 고정 길이 스택 클래스 구현하기

# from typing import Any
# from collections import deque

# class Stack:
#     def __init__(self, maxlen: int = 256) -> None:
#         # 스택 초기화
#         self.capacity = maxlen
#         self.__stk = deque([], maxlen)

#     def __len__(self) -> int:
#         # 스택에 쌓여있는 데이터 개수를 반환
#         return len(self.__stk)

#     def is_empty(self) -> bool:
#         return not self.__stk
    
#     def is_full(self) -> bool:
#         return len(self.__stk) == self.__stk.maxlen
    
#     def push(self, value: Any) -> None:
#         # 스택에 value를 푸시
#         self.__stk.append(value)
    
#     def pop(self) -> Any:
#         # 스택에서 데이터를 팝
#         return self.__stk.pop()

#     def peek(self) -> Any:
#         return self.__stk[-1]

#     def clear(self) -> None:
#         self.__stk.clear()
    
#     def find(self, value: Any) -> Any:
#         # 스택에서 value를 찾아 인덱스를 반환, 찾지 못하면 -1을 반환
#         try:
#             return self.__stk.index(value)
#         except ValueError:
#             return -1
    
#     def count(self, value: Any) -> int:
#         return self.__stk.count(value)

#     def __contains__(self, value: Any) -> bool:
#         return self.count(value)
    
#     def dump(self) -> int:
#         # 스택안에 있는 모든 데이터를 나열
#         print(list(self.__stk))
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 고정 길이 큐 클래스 FixedQueue 구현하기

# from signal import raise_signal
# from typing import Any

# class FixedQueue:
#     class Empty(Exception):
#         pass
#     class Full(Exception):
#         pass

#     def __init__(self, capacity : int) -> None:
#         self.no = 0 # 현재 데이터 개수
#         self.front = 0 # 맨 앞 원소 커서
#         self.rear = 0 # 맨 끝 원소 커서
#         self.capacity = capacity   # 큐의 크기
#         self.que = [None] * capacity # 큐의 본체

#     def __len__(self) -> int:
#         return self.no

#     def is_empty(self) -> bool:
#         return self.no <= 0

#     def is_full(self) -> bool:
#         return self.no >= self.capacity
    
#     def enque(self, x: Any) -> None:
#         # 데이터를 x에 인큐
#         if self.is_full():
#             raise FixedQueue.Full
#         self.que[self.rear] = x
#         self.rear += 1
#         self.no +=1
#         if self.rear == self.capacity:
#             self.rear = 0
#     def deque(self) -> Any:
#         # 데이터를 디큐
#         if self.is_empty():
#             raise FixedQueue.Empty
#         x = self.que[self.front]
#         self.front -= 1
#         if self.front == self.capacity:
#             self.front = 0
#         return x
#     def peek(self) -> Any:
#         # 큐에서 맨 앞 데이터를 들여다봄
#         if self.is_empty():
#             raise FixedQueue.Empty
#         return self.que[self.front]
    
#     def find(self, value: Any) -> Any:
#         for i in range(self.no):
#             idx = (1 + self.front) % self.capacity
#             if self.que[idx] == value:
#                 return idx
#             return -1
#     def count(self, value: Any) -> bool:
#         # 큐에 있는 value 개수를 반환
#         c = 0
#         for i in range(self.no):
#             idx = (i + self.front) % self.capacity
#             if self.que[idx] == value:
#                 return idx
#             return -1
#     def __contains__(self, value: Any) -> bool:
#         return self.count(value)
#     def clear(self) -> None:
#         self.no = self.front = self.rear = 0
#     def dump(self) -> None:
#         if self.is_empty():
#             print('큐가비었습니다')
#         else:
#             for i in range(self.no):
#                 print(self.que[(i + self.front) % self.capacity], end= '')
#             print()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 위에 작성함 함수를 사용하기

# from enum import Enum

# Menu = Enum('Menu', ['인큐', '디큐', '피크', '검색', '덤프', '종료'])

# def selcet_menu() -> Menu:
#     s = [f'({m.value}){m.name}' for m in Menu]
#     while True:
#         print(*s, sep=' ', end='')
#         n = int(input(': '))
#         if 1 <= n <= len(Menu):
#             return Menu(n)

# q = FixedQueue(64)

# while True:
#     print(f'현재 데이터 개수: {len(q)} / {q.capacity}')
#     menu = selcet_menu() # 메뉴 선택

#     if menu == Menu.인큐:
#         x = int(input('인큐할 데이터를 입력하세요.:'))
#         try:
#             q.enque(x)
#         except FixedQueue.Full:
#             print('큐가 가득찼습니다')
    
#     elif menu == Menu.피크:
#         try:    
#             x = q.peek()
#             print('피크한 데이터는 {x}입니다')
#         except FixedQueue.Empty:
#             print("큐가 비었습니다")
    
#     elif menu == Menu.검색:
        
#         x = int(input('검색할 값을 입력하세요'))
#         if x in q:
#             print(f'{q.count(x)}개 포함되고, 맨 앞의 위치는 {q.find(x)}입니다')
#         else:
#             print('검색값을 찾을 수 없습니다')
            
#     elif menu == Menu.덤프:
#         q.dump()
#     else:
#         break
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 오래된 데이터를 버리는 링 버퍼의 활용

# n = int(input('정수를 몇개 저장할까요? :'))

# a = [None] * n  # 입력받은값을 저장하는 배열 

# cnt = 0
# while True:
#     a[cnt % n] = int(input((f'{cnt +1}번째 정수를 입력하세요:')))
#     retry = input(f'계속 할까요? (Y, Yes / N No')
#     if retry in {'N', 'n'}:
#         break

# i = cnt - n
# if i < 0: i =0

# while i < cnt:
#     print(f'{i+1}번째 = {a[i%n]}')
#     i += 1
