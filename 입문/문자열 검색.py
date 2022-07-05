# 브루트 포스법: 선형 검색을 단순하게 확장한 알고리즘
# Kmp법 : 텍스트와 패턴안에서 겹치는 문자열을 찾아내 검사를 다시 사작할 위치를 구하여 패턴의 이동을 되도록이면 크게 하는 알고리즘 (몇 번째 문자열부터 검사를 다시 시작할지 패턴을 이동할 때마다 계산한다면 비효율적)
# 따라서 값을 표로 만들어 문제를 해결한다.
# 보이어 무어법: 패턴의 끝 문자에서 시작하여 앞쪽을 향해 검사를 수행합니다. 이 과정에서 일치하지 않는 문자를 발견하면 미리 준비한 표를 바탕으로 패턴이 이동하는 값을 결정
# ------------------------------------------------------------------------------------

# def bf_match(txt: str, pat: str) -> int:
#     pt = 0 # txt를 따라가는 커서
#     pp = 0 # pat를 따라가는 커서

#     while pt !=len(txt) and pp != len(pat):
#         if txt[pt] == pat[pp]:
#             pt += 1
#             pp += 1
#         else:
#             pt = pt - pp +1
#             pp = 0
    
#     return pt - pp  if pp == len(pat) else -1

# if __name__ == '__main__':
#     s1 = input('텍스트를 입력하세요.:')
#     s2 = input('패턴을 입력하세요.:')
    
#     idx = bf_match(s1,s2)
    
#     if idx == -1:
#         print('텍스트 안에 패턴이 존재하지 않습니다.')
#     else:
#         print(f'{(idx+1)} 번째 문자가 일치합니다.')
# ------------------------------------------------------------------------------------

# 멤버쉽 연산자와 표준 라이브러리를 사용한 문자열 검색
# 멤버쉽 연산자인 in과 not in을 사용하면 어떤 문자열이 다른 문자열 안에 포함되어 있는지 검색할 수 있다.
# 예를 들어 txt안에 문자열 ptn이 포함되어 있는지 판단할 때는 다음과 같이 수행한다
# ptn in txt (ptn은 txt안에 포함되어 있습니까?)
# ptn not in txt(ptn은 txt에 포함되어 있지 않습니까?)
# 이 방법은 어떤 문자열이 다른 문자열 안에 포함되어 있는지 판단할 수는 있지만 그 위치는 알지 못한다.

# str.find(sub[, start[, end]]) # 문자열 str의 [start:end]에 sub가 포함되면 그 가운데 가장 작은 인덱스를 반환하고, 그렇지 않으면 -1을 반환

# str.rfind(sub[, start [,end]]) # 문자열 str의 [start:end]에 sub가 포함되면 가장 큰 인덱스를 반환

# str.index(sub[, start[, end]]) # find 함수와 같은 기능 수행

# str.rindex(sub[, start[, end]]) # rfind 함수와 같은 기능 수행

# str.startswith(prefix[, start [, end]]) # 문자열이 prefix로 시작하면 True, 그렇지 않으면 false를 반환

# str.endswith(prefix[, start [, end]]) # 문자열이 prefix로 끝나면 True, 그렇지 않으면 false를 반환
# ------------------------------------------------------------------------------------

# KMP법으로 문자열 검색하기

# def kmp_match(txt :str, pat:str) -> int:
#     # kmp법으로 문자열 검색
    
#     pt =1 # txt를 따라가는 커서
#     pp =0 # pat를 따라가는 커서
#     skip = [0] * (len(pat) +1) # 건너뛰기 표

#     # 건너뛰기 표 만들기
#     skip[pt] = 0
#     while pt != len(pat):
#         if pat[pt] == pat[pp]:
#             pt += 1
#             pp += 1
#             skip[pt] = pp
#         elif pp == 0:
#             pt += 1
#             skip[pt] = pp
#         else:
#             pp = skip[pp]
    
#     # 문자열 검색하기
#     pt = pp = 0
#     while pt != len(txt) and pp != len(pat):
#         if txt[pt] == pat[pp]:
#             pt +=1
#             pp +=1
#         elif pp == 0:
#             pt +=1
#         else:
#             pp = skip[pp]    
            
#     return pt - pp if pp == len(pat) else -1

# if __name__ == '__main__':
#     s1 = input('텍스트를 입력하세요')
#     s2 = input('패턴을 입력하세요')
    
#     idx = kmp_match(s1,s2)
    
#     if idx == -1:
#         print('텍스트 안에 패턴이 존재하지 않습니다')
        
#     else:
#         print(f'{(idx +1)}번째 문자가 일치합니다.')
# ------------------------------------------------------------------------------------

# 보이어 무어법으로 문자열 검색하기 (문자열 길이는 0 ~ 255개)

# from unittest import skip


# def bm_match(txt : str, pat: str) -> int:
#     skip = [None] * 256
    
#     # 건너뛰기 표 만들기
#     for pt in range(256):
#         skip[pt] = len(pat)
#     for pt in range(len(pat)):
#         skip[ord(pat[pt])] = len(pat) - pt - 1
        
#     # 검색하기
#     while pt < len(txt):
#         pp = len(pat) -1
#         while txt[pt] == pat[pp]:
#             if pp == 0:
#                 return pt
#             pt -= 1
#             pp -= 1
#         pt += skip[ord(txt[pt])] if skip[ord(txt[pt])] > len(pat) - pp \
#             else len(pat) - pp
    
#     return -1

# if __name__ == '__main__':
#     s1 = input('텍스트를 입력하세요')
#     s2 = input('패턴을 입력하세요')
    
#     idx = bm_match(s1,s2)
    
#     if idx == -1:
#         print('텍스트 안에 패턴이 존재하지 않습니다')
        
#     else:
#         print(f'{(idx+1)} 번째 문자가 일치합니다. ')
    


    


