"""
정렬 범위 중 하나의 피벗을 선택 후, 피벗 보다 작은 배열과 큰 배열로 나누고 이 배열들을 다시 재귀적으로 정렬한다.

1. 기준이 되는 데이터인 피벗을 하나 선택한다.(일반적으로 배열의 첫 요소)
2. 피벗을 기준으로 피벗보다 작은 데이터와 큰 데이터로 구분한다
3. 피벗을 피벗보다 작은 데이터와 피벗보다 큰 데이터 사이에 위치시키면 피벗의 위치가 결정된다
4. 왼쪽에서부터 피벗보다 큰 데이터를 선택하고, 오른쪽에서부터 피벗보다 작은 데이터를 선택하여 데이터의 위치를 교환한다
"""

TEST = [9, 4, 3, 7, 10, 22, 1,  6]


START = 0

END = len(TEST) -1

def quick_sort(arr, start, end):

    if start > end:
        return

    PIVOT = start # 피벗은 첫 번 째 원소

    LEFT = start + 1
    RIGHT  = end

    while(LEFT <= RIGHT):
        # 피벗보다 큰 데이터를 찾을 때 까지 반복
        while(LEFT <= end and TEST[LEFT] <= TEST[PIVOT]):
            LEFT += 1

        while(RIGHT > start and TEST[RIGHT] >= TEST[PIVOT]):
            RIGHT -= 1

        # 탐색하는 데이터 위치가 엇갈렸다면 ?
        if LEFT > RIGHT:
            TEST[RIGHT], TEST[PIVOT] = TEST[PIVOT], TEST[RIGHT]
        else:
            TEST[LEFT], TEST[RIGHT] = TEST[RIGHT], TEST[LEFT]

    quick_sort(arr, 0, RIGHT -1)
    quick_sort(arr, RIGHT + 1, end) 

quick_sort(TEST, 0, len(TEST)-1)
print(TEST)





























