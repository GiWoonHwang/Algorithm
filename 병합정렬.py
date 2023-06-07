"""
전체 원소를 하나 단위로 분활 후, 원소를 각각 비교하여 병합하는 과정에서 정렬한다.

1. 배열을 반으로 계속 나누어 1개의 원소를 가질 때 까지 반복한다
2. 하나로 나누어진 배열을 다시 합치며 작은 원소값이 앞으로 오도록 정렬한다.
3. 합쳐진 배열들끼리 다시 비교하여 재정렬한다.
"""

TEST = [9, 4, 3, 7, 10, 22, 1,  6]

def merge_sort(arr):
    if len(arr) < 2: 
        return arr 

    # 중간 인덱스를 구한다
    mid = len(arr) / 2
    
    # 배열을 좌우로 나눠 그 배열을 또 나눈다.
    left = merge_sort(arr[mid:])
    right = merge_sort(arr[:mid])
    
    # 좌우를 결합한다
    return merge(left, right)


def merge(left, right):
    
    # 좌, 우가 정렬된 데이터를 저장하는 임시 배열
    merged = []
    
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            merged.append(left.pop[0]) # 맨 앞의 데이터를 빼서 넣는다.
        else:
            merged.append(right.pop(0))
        
        # 정렬하고 남은거 뒤에 붙여줌
        if left:
            merged += left
        else:
            merged += right
        
        return merged

print(TEST)
