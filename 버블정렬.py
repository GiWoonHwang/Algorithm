"""
현재 요소와 다음 요소를 비교하여 큰 값을 뒤로 옮긴다.

1. 현재 인덱스와 다음 인덱스를 비교하여 현재 인덱스가 더 크다면 스왑한다
2. 현재 인덱스 값이 len(arr) -1 까지 반복한다. (마지막 인덱스는 비교가 불가능하다)
3. 매 정렬마다 비교한 마지막 부분이 가장 큰 값이기 때문에, 다음 정렬에서는 마지막 부분을 제외한다.  
"""

TEST = [9, 4, 3, 7, 10, 22, 1,  6]
n_swap = 0 # 교환 횟수 기록

# 맨 뒤는 교환 할 요소가 없기 때문에 -1
for i in range(len(TEST) -1): 
    for j in range(len(TEST) -1 -i): # 가장 큰 값은 맨 뒤로 가기 때문에 비교요소를 하나씩 줄여줌
        print(j)
        if(TEST[j] > TEST[j+1]):
            TEST[j+1] , TEST[j] = TEST[j] , TEST[j+1]

print(TEST)

        
