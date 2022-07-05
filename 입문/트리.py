# 알고리즘 순서
# 1. 루트에 주목한다 예를들어 p라고 가정
# 2. p가 none이면 검색을 실패하고 종료한다
# 3. 검색하는 key와 주목 노드 p의 키를 비교한다.
# key = p: 검색을 성공하고 종료
# key < p: 주목 노드를 왼쪽 자식 노드로 옮김
# key > p: 주목 노드를 오른쪽 자식 노드로 이동
# 4. 2번과정으로 돌아감

# 삽입 알고리즘 순서
# 1. 루트에 주목한다. 여기서 주목하는 노드를 node라고 가정
# 2. 삽입하는 key와 주목 노드 node의 키를 비교
# key = node인 경우: 삽입을 실패하고 종료
# key < node인 경우:
# 왼쪽 자식 노드가 없으면 그 자리에 노드를 삽입하고 종료
# 왼쪽 자식 노드가 있으면 주목 노드를 왼쪽 자식노드로 옮긴다
# key > node:
# 오른쪽 자식 노드가 없으면 그 자리에 노드를 삽입하고 종료
# 오른쪾 자식 노드가 있으면 주목 노드를 오른쪽 자식 노드로 옮긴다.

# 삭제 알고리즘 순서
# 삭제할 노드가 부모 노드의 왼쪽 자식이면, 부모의 왼쪽 포인터를 None으로 (오른쪽도 마찬가지)
# 삭제할 노드가 자식노드 한개일 때 노드의 왼쪽 자식인 경우 보무의 왼쪽 포인터가 삭제할 노드의 자식을 가리키도록 업데이트(오른쪽도 마찬가지)
# 삭제할 노드가 자식노드 두개일 때
# 1. 삭제할 노드의 왼쪽 서브트리에서 키값이 갖아 큰 노드를 검색
# 2. 검색한 노드를 삭제 위치로 옮깁니다. 즉 검색한 노드의 데이털르 삭제할 노드 위치에 복사
# 3. 옮긴 노드를 삭제한다. 이때 자식 노드의 개수에 따라 다음을 수행
# 옮긴 노드에 자식이 없으면 : 자식노드가 없는 노드 삭제에 따라 노드 삭제
# 옮긴 노드에 자식이 1개만 있으면 : 자식 노드가 1개인 노드의 삭제에 따라 노드 삭제
# --------------------------------------------------------------------------------------------------------------

# 이진 검색 트리 구현하기

from __future__ import annotations
from typing import Any, Type

class Node:
    # 이진 검색 트리의 노드
    def __inti__(self, key:Any, value:Any, left: Node = None, right: Node = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    # 이진 검색 트리 루트에 대한 참조를 유지한다
    # root에 none을 대입하여 노드가 하나도 없는 빈상태의 이진 검색 트리를 만듬
    def __init__(self):
        # 초기화
        self.root = None
# --------------------------------------------------------------------------------------------------------------

# 키가 key인 노드를 검색

def search(self, key: Any) -> Any:
    p = self.root # 루트에 주목
    while True:
        if p is None:
            return None
        if key == p.key:
            return p.value
        elif key < p.key:
            return p.left
        else:
            p = p.right
# --------------------------------------------------------------------------------------------------------------

# 키가 key이고 값이 value인 노드를 삽입

def add(self, key: Any, value: Any) -> bool:

    def add_node(node: None, key: Any, value: Any) -> None:
        # node를 루트로 하는 서브트리에 키가 key이고 값이 value인 노드를 삽입
        if key == node.key:
            return False
        elif key < node.key:
            if node.left is None:
                node.left = Node(key, value, None, None)
            else:
                add_node(node.left, key, value)
        else:
            if node.right is None:
                node.right = Node(key,value,None,None)
            else:
                add_node(node.right, key, value)
        return True

    if self.root is None:
            self.root = Node(key, value, None, None)
            return True
    else:
        return add_node(self.root, key, value)
# --------------------------------------------------------------------------------------------------------------

def remove(self, key: Any) -> bool:
    """키가 key인 노드를 삭제"""
    p = self.root           # 스캔 중인 노드
    parent = None           # 스캔 중인 노드의 부모 노드
    is_left_child = True    # p는 parent의 왼쪽 자식 노드인지 확인
    while True:
        if p is None:       # 더 이상 진행할 수 없으면
            return False    # 그 키는 존재하지 않음
        if key == p.key:    # key와 노드 p의 키가 같으면
            break           # 검색 성공
        else:
            parent = p                  # 가지를 내려가기 전에 부모를 설정
            if key < p.key:             # key 쪽이 작으면
                is_left_child = True    # 여기서 내려가는 것은 왼쪽 자식
                p = p.left              # 왼쪽 서브 트리에서 검색
            else:                       # key 쪽이 크면
                is_left_child = False   # 여기서 내려가는 것은 오른쪽 자식
                p = p.right             # 오른쪽 서브 트리에서 검색
    if p.left is None:                  # p에 왼쪽 자식이 없으면
        if p is self.root:
            self.root = p.right
        elif is_left_child:
            parent.left = p.right       # 부모의 왼쪽 포인터가 오른쪽 자식을 가리킴
        else:
            parent.right = p.right      # 부모의 오른쪽 포인터가 오른쪽 자식을 가리킴
    elif p.right is None:               # p에 오른쪽 자식이 없으면
        if p is self.root:
            self.root = p.left
        elif is_left_child:
            parent.left = p.left        # 부모의 왼쪽 포인터가 왼쪽 자식을 가리킴
        else:
            parent.right = p.left       # 부모의 오른쪽 포인터가 왼쪽 자식을 가리킴
    else:
        parent = p
        left = p.left                   # 서브 트리 안에서 가장 큰 노드
        is_left_child = True
        while left.right is not None:   # 가장 큰 노드 left를 검색
            parent = left
            left = left.right
            is_left_child = False
        p.key = left.key                # left의 키를 p로 이동
        p.value = left.value            # left의 데이터를 p로 이동
        if is_left_child:
            parent.left = left.left     # left를 삭제
        else:
            parent.right = left.left    # left를 삭제
    return True
def dump(self) -> None:
    """덤프(모든 노드를 키의 오름차순으로 출력)"""
    def print_subtree(node: Node):
        """node를 루트로 하는 서브 트리의 노드를 키의 오름차순으로 출력"""
        if node is not None:
            print_subtree(node.left)            # 왼쪽 서브 트리를 오름차순으로 출력
            print(f'{node.key}  {node.value}')  # node를 출력
            print_subtree(node.right)           # 오른쪽 서브 트리를 오름차순으로 출력
    print_subtree(self.root)
def min_key(self) -> Any:
    """가장 작은 키"""
    if self.root is None:
        return None
    p = self.root
    while p.left is not None:
        p = p.left
    return p.key
def max_key(self) -> Any:
    """가장 큰 키"""
    if self.root is None:
        return None
    p = self.root
    while p.right is not None:
        p = p.right
    return p.key
# -------------------------------------------------------------------------------------------------------------------
from enum import Enum
# from bst2 import BinarySearchTree #교제와 다르게 바로 위에 코딩했기 때문에 import 할 필요 없음

Menu = Enum('Menu', ['삽입', '삭제', '검색', '오름차순덤프', '내림차순덤프', '키의범위', '종료'])

def select_Menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '  ', end='')
        n = int(input(' : '))
        if 1 <= n <= len(Menu):
            return Menu(n)

tree = BinarySearchTree()  # 이진 검색 트리를 생성

while True:
    menu = select_Menu()  # 메뉴 선택

    if menu == Menu.삽입:  # 삽입
        key = int(input('삽입할 키를 입력하세요.: '))
        val = input('삽입할 값을 입력하세요.: ')
        if not tree.add(key, val):
            print('삽입에 실패했습니다!')

    elif menu == Menu.삭제:  # 삭제
        key = int(input('삭제할 키를 입력하세요.: '))
        tree.remove(key)

    elif menu == Menu.검색:  # 검색
        key = int(input('검색할 키를 입력하세요.: '))
        t = tree.search(key)
        if t is not None:
            print(f'이 키를 갖는 값은 {t}입니다.')
        else:
            print('해당 데이터가 없습니다.')

    elif menu == Menu.오름차순덤프:  # 오름차순 덤프
        tree.dump()


    elif menu == Menu.내림차순덤프:  # 내림차순 덤프
        tree.dump(reverse = True)

    elif menu == Menu.키의범위 :  # 키의 범위(최솟값과 최댓값)
        print(f'키의 최솟값은 {tree.min_key()}입니다.')
        print(f'키의 최댓값은 {tree.max_key()}입니다.')
        
    else:# 종료
        break