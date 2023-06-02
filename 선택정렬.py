"""
탐색 범위에서 최소값을 찾은 후, 그 값을 범위의 가장 앞으로 보내면서 정렬하는 정렬법

1. 현재 리스트에서 최소값을 찾는다.
2. 그 값을 첫 번째 인덱스 값과 교환한다
3. 첫 원소를 제외한 나머지 리스트를 기준으로 다시 1번으로 돌아가 정렬한다.
"""

TEST = [9, 4, 3, 7, 10, 22, 1,  6]

for i in range(len(TEST) - 1):
    min_idx = i
    
    for j in range(i+1, len(TEST)):
        if TEST[min_idx] > TEST[j]:
            min_idx = j
            print(min_idx)
    
    # 가장 작은 안덱스와 시작 인덱스를 변경한다        
    TEST[i], TEST[min_idx] = TEST[min_idx], TEST[i]
    
print(TEST)
































