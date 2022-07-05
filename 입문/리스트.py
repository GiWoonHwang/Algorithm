# 이터러블 : str형 문자형, list형 리스트, tuple형 튜플등은 반복가능하다는 공통점이 있다. 이터러블 객체는 원소를 1개씩 꺼내는 구조의 객체이다.
# 이터러블 객체를 내장 함수인 iter()함수에 인수로 전달하면 그 객체에 대한 이터레이터(반복자)를 반환한다
# 이터레이터: 데이터가 줄지어 늘어선것을 표현하는 객체이다. 이터레이터의 __next__() 함수를 꺼내서 호출하거나, 내장함수인 next()함수에 반복자를 전달하면
# 줄지어 늘어선 원소를 순차적으로 꺼냅니다. 꺼낼 원소가 없으면 StopIteration 예외 처리를 보냅니다.

# 포인터로 연결 리스트 구현하기

# from __future__ import annotations
# import imp
# from re import M
# from typing import Any,Type

# class Node:
#     def __init__(self, data: Any = None, next: Node = None):
#         #  초기화
#         self.data = data
#         self.next = next
        

# class LinkednList:
#     def __init__(self) -> None:
#         self.no = 0 # 노드의 개수
#         self.head = None # 머리노드
#         self.current = None # 주목노드
        
#     def __len__(self) -> int:
#         # 연결 리스트의 노드 개수를 반환
#         return self.no
    
#     def search(self, data: Any) -> int:
#         # data와 값이 같은 노드를 검색
#         cnt = 0
#         ptr = self.head
#         while ptr is not None:
#             if ptr.data == data:
#                 self.current = ptr
#                 return cnt
#             cnt += 1
#             ptr = ptr.next
#         return -1
    
#     def __contains__(self, data: Any) -> bool:
#         # 연결 리스트에 data가 포함되어 있는지 확인
#         return self.search(data) >= 0

#     def add_first(self, data:Any) -> None:
#         # 맨 앞에 노드를 삽입
#         ptr = self.head # 삽입하기 전의 머리노드
#         self.head = self.current = Node(data,ptr)
#         self.no += 1
    
#     def add_last(self, data: Any):
#         # 맨 끝에 노드를 삽입
#         if self.head is None: #리스트가 비어있으면
#             self.add_first(data) # 맨 앞에 노드를 삽입
#         else:
#             ptr = self.head
#             while ptr.next is not None:
#                 ptr = ptr.next
#             ptr.next = self.current = Node(data, None)
#             self.no +=1
            
#     def remove_first(self) -> None:
#         # 머리 노드를 삭제
#         if self.head is not None:
#             self.head = self.current = self.head.next
#         self.no -=1
        
#     def remove_last(self) -> None:
#         # 꼬리 노드를 삭제
#         if self.head is not None:
#             if self.head.next is None:
#                 self.remove_first()
#             else:
#                 ptr = self.head # 스캔중인 노드
#                 pre = self.head # 스캔중인 노드의 앞쪽 노드
                
#                 while ptr.next is not None:
#                     pre = ptr
#                     ptr = ptr.next
                
#                 pre.next = None
#                 self.current = pre
#                 self.no -= 1
                
#     def remove(self, p: None) -> None:
#         # 노드 p를 삭제
#         if self.head is not None:
#             if p is self.head: # 지우려는 노드가 머리노드이면
#                 self.remove_first() # 머리노드 삭제
#             else:
#                 ptr = self.head
                
#                 while ptr.next is not p:
#                     ptr = ptr.next
#                     if ptr is None:
#                         return
#                 ptr.next = p.next
#                 self.current = ptr
#                 self.no -= 1
                
#     def remove_current_node(self) -> None:
#         # 주목 노드 삭제
#         self.remove(self.current)
        
#     def clear(self) -> None:
#         # 전체 노드를 삭제
#         while self.head is not None: # 전체가 비어 있을 때까지
#             self.remove.first() # 머리 노드를 삭제
#         self.current = None
#         self.no = 0
    
#     def next(self) -> bool:
#         # 주목 노드를 한칸 뒤로 이동
#         if self.current is None or self.current.next is None:
#             return False
#         self.current = self.current.next
#         return True
    
#     def print_current_node(self) -> None:
#         # 주목 노드를 출력
#         if self.current is None:
#             print('주목 노드가 존재하지 않습니다.')
#         else:
#             print(self.current.data)
            
#     def print1(self) -> None:
#         ptr = self.head
        
#         while ptr is not None:
#             print(ptr.data)
#             ptr = ptr.next
# #  -----------------------------------------------------------------------------------------------------------------

# # 이터레이터용 클래스 구현

# def __iter__(self) -> LinkednListIterator:
#     # 이터레이터를 반환
#     return LinkednListIterator(self.head)

# class LinkednListIterator:
#     # 클래스 LinkedList의 이터레이터용 클래스
    
#     def __init__(self, head:None):
#         self.current = head
    
#     def __iter__(self) -> LinkednListIterator:
#         return self
    
#     def __next__(self) -> Any:
#         if self.current is None:
#             raise StopIteration
#         else:
#             data = self.current.data
#             self.current = self.current.next
#             return data
# --------------------------------------------------------------------------------------------

# 포인터를 이용한 연결 리스트 클래스 LinkedList 사용하기

# from enum import Enum
# from linked_list import LinkedList

# Menu = Enum('Menu', ['머리노드에삽입', '꼬리노드에삽입', '머리노드삭제','꼬리노드삭제','주목노드출력','주목노드이동',
#                      '주목노드삭제','모든노드삭제','검색','멤버십판단','모든노드출력','스캔','종료'])

# def select_Menu() -> Menu:
#     # 메뉴선택
#     s = [f'({m.value}{m.name}' for m in Menu]
#     while True:
#         print(*s, sep=' ', end=' ')
#         n = int(input(': '))
#         if 1<= n <= len(Menu):
#             return Menu(n)
# lst = LinkedList() # 연결 리스트를 생성

# while True:
#     menu = select_Menu() # 메뉴 선택
    
#     if menu == Menu.머리노드에삽입:
#         lst.add_first(int(input('머리 노드에 넣을값을 입력하세요')))
    
#     elif menu == Menu.꼬리노드에삽입:
#         lst.add_last(int(input('꼬리 노드에 넣을값을 입력하세요')))
    
#     elif menu == Menu.머리노드삭제:
#         lst.remove_first()
    
#     elif menu == Menu.꼬리노드삭제:
#         lst.remove_last()
    
#     elif menu == Menu.주목노드출력:
#         lst.print_current_node()
    
#     elif menu == Menu.주목노드이동:
#         lst.next()
    
#     elif menu == Menu.주목노드삭제:
#         lst.remove_current_node()
    
#     elif menu == Menu.모든노드삭제:
#         lst.clear()
    
#     elif menu == Menu.검색:
#         pos = lst.search(int(input('검색할 값을 입력하세요 :')))
#         if pos>= 0:
#             print(f'그 값으 데이터는 {pos + 1 }번 째에 있습니다.')
#         else:
#             print('해당하는 데이터가 없습니다.')
            
#     elif menu == Menu.멤버십판단:
#         print('그 값의 데이터는 포함되어' + ('있습니다.' if int(input('판단할 값을 입력하세요')) in lst else '있지 않습니다'))
    
#     elif menu == Menu.모든노드출력:
#         lst.print1()
    
#     elif menu == Menu.스캔:
#         for e in lst:
#             print(e)
    
#     else:
#         break
# -----------------------------------------------------------------------------------------------------------------------------------------

# 커서로 연결 리스트 구현하기

# from __future__ import annotations
# from typing import Any, Type

# Null = -1

# class Node:
#     def __init__(self, data = Null, next = Null, dnext = Null):
#         self.data = data # 데이터
#         self.next = next # 리스트의 뒤쪽 포인터
#         self.dnext = dnext # 프리 리스트의 뒤쪽 포인터
    
#     def __init__(self, capacity: int):
#         self.head = Null # 머리노드
#         self.current = Null # 주목노드
#         self.max = Null # 사용중인 꼬리 레코드
#         self.deleted = Null # 프리 리스트의 머리 노드
#         self.capacity = capacity # 리스트의 크기
#         self.n = [Node()] * self.capacity # 리스트의 본체
#         self.no = 0
    
#     def __len__(self) -> int:
#         # 연결 리스트의 노드 수를 반환
#         return self.no
    
#     def get_insert_index(self):
#         # 다음에 삽입할 레코드의 인덱스를 구함
#         if self.deleted == Null: # 삭제 레코드는 존재하지 않음
#             if self.max + 1 < self.capacity:
#                 self.max += 1
#                 return self.max # 새 레코드 사용
#             else:
#                 return Null # 크기 초과
#         else:
#             rec = self.deleted
#             self.deleted = self.n[rec].dnext # 프리 리스트에서 맨 앞 rec를 꺼내기
#             return rec
    
#     def delete_index(self, idx: int) -> None:
#         # 레코드 idx를 프리 리스트에 등록
#         if self.deleted == Null:
#             self.deleted = idx
#             self.n[idx].dnext = Null
#         else:
#             rec = self.deleted
#             self.deleted = idx
#             self.n[idx].dnext = rec
    
#     def search(self, data: Any) -> int:
#         # data와 값이 같은 노드 검색
#         cnt = 0
#         ptr = self.head
#         while ptr != Null:
#             if self.n[ptr].data == data:
#                 self.current = ptr
#                 return cnt
#             cnt += 1
#             ptr = self.n[ptr].next
#         return Null
        
#     def __contains__(self, data: Any) -> bool:
#         # 연결 리스트에 data가  포함되어 있는지 확인
#         return self.search(data) >=0

#     def add_first(self, data: Any):
#         # 머리 노드에 삽입
#         ptr = self.head
#         rec = self.get_insert_index()
#         if rec != Null:
#             self.head = self.current = rec
#             self.n[self.head] = Node(data, ptr)
#             self.no += 1
    
#     def add_last(self, data: Any) -> None:
#         # 꼬리 노드에 삽입
#         if self.head == Null:
#             self.add_first(data)
#         else:
#             ptr = self.head
#             while self.n[ptr].next != Null:
#                 ptr = self.n[ptr].next
#             rec = self.get_insert_index()
            
#             if rec != Null:
#                 self.n[ptr].next = self.current = rec
#                 self.n[rec] = Node(data)
#                 self.no += 1
    
#     def remove_first(self) -> None:
#         # 머리 노드를 삭제
#         if self.head != Null: # 리스트가 비어 있으면
#             ptr = self.n[self.head].next
#             self.delete_index(self.head)
#             self.head = self.current = ptr
#             self.no -= 1
    
#     def remove_last(self) -> None:
#         # 꼬리 노드를 삭제
#         if self.head != Null:
#             if self.n[self.head].next == Null: 
#                 self.remove_first()
#             else:
#                 ptr = self.head # 스캔중인 도드
#                 pre = self.head # 스캔중인 노드의 앞쪽 노드
                
#                 while self.n[ptr].next != Null:
#                     pre = ptr
#                     ptr = self.n[ptr].next # pre는 삭제한 뒤의 꼬리노드
#                 self.n[pre].next = Null
#                 self.delete_index(ptr)     
#                 self.current = pre
#                 self.no -= 1
    
#     def remove(self, p: int) -> None:
#         # 레코드 p를 삭제
#         if self.head != Null:
#             if p == self.head:
#                 self.remove_first() # p가 머리 노드면 머리 노드를 삭제
#             else:
#                 ptr = self.head
            
#                 while self.n[ptr].next != p:
#                     ptr = self.n[ptr].next
#                     if ptr == Null:
#                         return
#                 self.n[ptr].next == Null
#                 self.delete_index(p)
#                 self.n[ptr].next = self.n[p].next
#                 self.current = ptr
#                 self.no -= 1
    
#     def remove_current_node(self) -> None:
#         # 주목 노드를 삭제
#         self.remove(self.current)
    
#     def clear(self) -> None:
#         # 모든 노드를 삭제
#         while self.head != Null:
#             self.remove_first()
#         self.current = Null
        
#     def next(self) -> bool:
#         # 주목 노드를 한칸 뒤로 이동
#         if self.current == Null or self.n[self.current].next == Null:
#             return False # 이동할 수 없음
#         self.current = self.n[self.current].next
#         return True
    
#     def print_current_node(self) -> None:
#         # 주목 노드를 출력
#         if self.current == Null:
#             print('주목 노드가 없습니다')
#         else:
#             print(self.n[self.current].data)
    
#     def print(self) -> None:
#         # 모든 노드를 출력
#         ptr = self.head
        
#         while ptr != Null:
#             print(self.n[ptr].data)
#             ptr = self.n[ptr].next
    
#     def dump(self) -> None:
#         # 배열을 덤프
#         for i in self.n:
#             print(f'[{i}] {i.data} {i.next} {i.dnext}')
    
#     def __iter__(self) -> ArrayLinkedListIterator:
#         return ArrayLinkedListIterator(self.n, self.head)

# class ArrayLinkedListIterator:
#     def __init__(self, n :int, head: int):
#         self.n = n
#         self.current = head
    
#     def __iter__(self) -> ArrayLinkedListIterator:
#         return self
    
#     def __next__(self) -> Any:
#         if self.current == Null:
#             raise stopIteration
#         else:
#             data = self.n[self.current].data
#             self.current = self.n[self.current].next
#             return data
#------------------------------------------------------------------------------------------------

# 커서를 이용한 연결 리스트 클래스 ArrayLinkedList 사용하기


# from enum import Enum
# from array_list import ArrayLinkedList

# Menu = Enum('Menu', ['머리에노드삽입', '꼬리에노드삽입', '머리노드삭제',
#                      '꼬리노드삭제', '주목노드출력', '주목노드이동',
#                      '주목노드삭제', '모든노드삭제', '검색', '멤버십판단',
#                      '모든노드출력', '스캔', '종료'])

# def select_Menu() -> Menu:
#     """메뉴 선택"""
#     s = [f'({m.value}){m.name}' for m in Menu]
#     while True:
#         print(*s, sep = '  ', end='')
#         n = int(input(' : '))
#         if 1 <= n <= len(Menu):
#             return Menu(n)

# lst = ArrayLinkedList(100)  # 선형 리스트를 생성

# while True:
#     menu = select_Menu()  # 메뉴 선택

#     if menu == Menu.머리에노드삽입:               # 맨 앞에 노드 삽입
#         lst.add_first(int(input('머리 노드에 넣을 값을 입력하세요.: ')))
                                    
#     elif menu == Menu.꼬리에노드삽입:             # 맨 끝에 노드 삽입
#         lst.add_last(int(input('꼬리 노드에 넣을 값을 입력하세요.: ')))

#     elif menu == Menu.머리노드삭제:             # 맨 앞 노드를 삭제
#         lst.remove_first()

#     elif menu == Menu.꼬리노드삭제:             # 맨 끝 노드를 삭제
#         lst.remove_last()

#     elif menu == Menu.주목노드출력:             # 주목 노드를 출력
#         lst.print_current_node()

#     elif menu == Menu.주목노드이동:             # 주목 노드를 한 칸 뒤로 이동
#         lst.next()

#     elif menu == Menu.주목노드삭제:             # 주목 노드를 삭제
#         lst.remove_current_node()

#     elif menu == Menu.모든노드삭제:             # 모두 삭제
#         lst.clear()

#     elif menu == Menu.검색:                     # 검색
#         pos = lst.search(int(input('검색할 값을 입력하세요.: ')))
#         if pos >= 0:
#             print(f'이 키를 갖는 데이터는 {pos + 1}번째에 있습니다.')
#         else:
#             print('해당 데이터가 없습니다.')

#     elif menu == Menu.멤버십판단:               # 멤버십을 판단
#         print('그 값의 데이터는 포함되어'
#               +('있습니다.' if int(input('판단할 값을 입력하세요.')) in lst else ' 있지 않습니다.'))

#     elif menu == Menu.모든노드출력:             # 모든 노드를 출력
#         lst.print()

#     elif menu == Menu.스캔:                     # 모든 노드 스캔
#         for e in lst:
#              print(e)

#     else:                                       # 종료
#         break
#------------------------------------------------------------------------------------------------

# 원형 이중 연결 리스트 구현하기

# from __future__ import annotations
# from typing import Any, Type

# class Node:
#     # 원형 이중 연결 리스트용 노드 클래스
#     def __init__(self, data: Any = None, prev: Node = None, next: Node = None) -> None:
#         # 초기화
#         self.data = data
#         self.prev = prev or self
#         self.next = next or self

# class DoubleLinkedList:
#     # 원형 이중 연결 리스트
    
#     def __init__(self) -> None:
#         # 초기화
#         self.head = self.current = Node() # 더미 노드를 생성
#         self.no = 0
        
#     def __len__(self) -> int:
#         # 연결 리스트의 노드 수를 반환
#         return self.no
    
#     def is_empty(self) -> bool:
#         # 리스트가 비어있는지 확인
#         return self.next is self.head
    
#     def search(self, data: Any) -> Any:
#         # data와 값이 같은 노드를 검색 
#         cnt = 0
#         ptr = self.head.next # 현재 스캔중인 노드
#         while ptr is not self.head:
#             if data == ptr.data:
#                 self.current = ptr
#                 return cnt
#             cnt += 1
#             ptr = ptr.next
#         return -1
    
#     def __contain__(self, data: Any) -> bool:
#         # 연결 리스트에 data가 포함되어 있는지 판단
#         return self.search(data) >= 0
    
#     def print_current_node(self) -> Node:
#         # 주목 노드를 출력
#         if self.is_empty():
#             print('주목 노드는 없습니다')
#         else:
#             print(self.current.data)
    
#     def print(self) -> None:
#         ptr = self.head.next # 더미 노드의 뒤족 노드
#         while ptr is not self.head:
#             print(ptr.data)
#             ptr = ptr.next
    
#     def print_reverse(self) -> None:
#         # 역순으로 출력
#         ptr = self.head.prev
#         while ptr is not self.head:
#             print(ptr.data)
#             ptr = ptr.prev
            
#     def next(self) -> bool:
#         if self.is_empty() or self.current.next is self.head:
#             return False # 이동할 수 없음
#         self.current = self.current.next
#         return True
    
#     def prev(self) -> bool:
#         # 주목 노드를 한칸 앞으로 이동
#         if self.is_empty() or self.current.prev is self.head:
#             return False
#         self.current = self.current.prev
#         return True
    
#     def add(self, data: Any) -> None:
#         # 주목 노드 바로 뒤에 노드를 삽입
#         node =  Node(data, self.current, self.current.next)
#         self.current.next.prev = node
#         self.current.next = node
#         self.current = node
#         self.no += 1
        
#     def add_first(self, data: Any) -> None:
#         # 맨 앞에 노드를 삽입
#         self.current = self.head # 더미 노드 head의 바로 뒤에 삽입
#         self.add(data)
        
#     def add_last(self, data: Any) -> None:
#         # 맨 뒤에 노드를 삽입
#         self.current = self.head.prev # 꼬리 노드 head.prev의 바로 뒤에 삽입
#         self.add(data)
        
#     def remove_current_node(self) -> None:
#         # 주목 노드 삭제
#         if not self.is_empty():
#             self.current.prev.next = self.current.next
#             self.current.next.prev = self.current.prev
#             self.current = self.current.prev
#             self.no -= 1
#             if self.current is self.head:
#                 self.current = self.head.next

#     def remove(self, p: Node) -> None:
#         # 노드 p를 삭제
#         ptr = self.head.next

#         while ptr is not self.head:
#             if ptr is p:  # p를 발견
#                 self.current = p
#                 self.remove_current_node()
#                 break
#             ptr = ptr.next

#     def remove_first(self) -> None:
#         # 머리 노드 삭제
#         self.current = self.head.next  # 머리 노드 head.next를 삭제
#         self.remove_current_node()

#     def remove_last(self) -> None:
#         # 꼬리 노드 삭제
#         self.current = self.head.prev  # 꼬리 노드 head.prev를 삭제
#         self.remove_current_node()

#     def clear(self) -> None:
#         # 모든 노드를 삭제
#         while not self.is_empty():  # 리스트 전체가 빌 때까지
#             self.remove_first()  # 머리 노드를 삭제
#         self.no = 0
    
#     def __iter__(self) -> DoubleLinkedListIterator:
#         return DoubleLinkedListIterator(self.head)
    
#     def __reversed__(self) -> DoubleLinkedListReverseIterator:
#         # 내림차순 반복자를 반환
#         return DoubleLinkedListReverseIterator(self.head)

# class DoubleLinkedListIterator:
#     # DoubleLinkedList의 반복자용 클래스

#     def __init__(self, head: Node):
#         self.head = head
#         self.current = head.next

#     def __iter__(self) -> DoubleLinkedListIterator:
#         return self

#     def __next__(self) -> Any:
#         if self.current is self.head:
#             raise StopIteration
#         else:
#             data = self.current.data
#             self.current = self.current.next
#             return data

# class DoubleLinkedListReverseIterator:
#     # DoubleLinkedList의 내림차순 반복자용 클래스

#     def __init__(self, head: Node):
#         self.head = head
#         self.current = head.prev

#     def __iter__(self) -> DoubleLinkedListReverseIterator:
#         return self

#     def __next__(self) -> Any:
#         if self.current is self.head:
#             raise StopIteration
#         else:
#             data = self.current.data
#             self.current = self.current.prev
#             return data
#------------------------------------------------------------------------------------------------


# from enum import Enum
# from double_list import DoubleLinkedList

# Menu = Enum('Menu', ['머리에노드삽입', '꼬리에노드삽입', '주목노드바로뒤삽입',
#                      '머리노드삭제', '꼬리노드삭제', '주목노드출력',
#                      '주목노드이동', '주목노드역순이동', '주목노드삭제',
#                      '모든노드삭제', '검색', '멤버십판단', '모든노드출력',
#                      '모든노드역순출력', '모든노드스캔', '모든노드역순스캔', '종료'])

# def select_Menu() -> Menu:
#     """메뉴 선택"""
#     s = [f'({m.value}){m.name}' for m in Menu]
#     while True:
#         print(*s, sep = '  ', end='')
#         n = int(input(': '))
#         if 1 <= n <= len(Menu):
#             return Menu(n)

# lst = DoubleLinkedList()  # 원형・이중 연결 리스트 생성

# while True:
#     menu = select_Menu()  # 메뉴 선택

#     if menu == Menu.머리에노드삽입:  # 맨 앞에 노드 삽입
#         lst.add_first(int(input('머리 노드에 넣을 값을 입력하세요.: ')))

#     elif menu == Menu.꼬리에노드삽입:  # 맨 끝에 노드 삽입
#         lst.add_last(int(input('꼬리 노드에 넣을 값을 입력하세요.: ')))

#     elif menu == Menu.주목노드바로뒤삽입:  # 주목 노드 바로 뒤에 삽입
#         lst.add(int(input('주목 노드 바로 뒤에 넣을 값을 입력하세요 : ')))

#     elif menu == Menu.머리노드삭제:  # 맨 앞 노드 삭제
#         lst.remove_first()

#     elif menu == Menu.꼬리노드삭제:  # 맨 끝 노드 삭제
#         lst.remove_last()

#     elif menu == Menu.주목노드출력:  # 주목 노드 출력
#         lst.print_current_node()

#     elif menu == Menu.주목노드이동:  # 주목 노드를 한 칸 뒤로 이동
#         lst.next()

#     elif menu == Menu.주목노드역순이동:  # 주목 노드를 한 칸 앞으로 이동
#         lst.prev()

#     elif menu == Menu.주목노드삭제:  # 주목 노드 삭제
#         lst.remove_current_node()

#     elif menu == Menu.모든노드삭제:  # 모두 삭제
#         lst.clear()

#     elif menu == Menu.검색:  # 검색
#         pos = lst.search(int(input('검색할 값을 입력하세요.: ')))
#         if pos >= 0:
#             print(f'그 값의 데이터는 {pos + 1}번째에 있습니다.')
#         else:
#             print('해당 데이터가 없습니다.')

#     elif menu == Menu.멤버십판단:  # 멤버십 판단
#         print('그 값의 데이터는 포함되어'
#               +(' 있습니다.' if int(input('판단할 값을 입력하세요.: ')) in lst else ' 있지 않습니다.'))

#     elif menu == Menu.모든노드출력:  # 모든 노드를 출력
#         lst.print()

#     elif menu == Menu.모든노드역순출력:  # 모든 노드 역순 출력
#         lst.print_reverse()

#     elif menu == Menu.모든노드스캔:  # 모든 노드 스캔
#         for e in lst:
#              print(e)

#     elif menu == Menu.모든노드역순스캔:  # 모든 노드 역순 스캔
#         for e in reversed(lst):
#              print(e)

#     else:  # 종료
#         break
#------------------------------------------------------------------------------------------------
    
    
    
    