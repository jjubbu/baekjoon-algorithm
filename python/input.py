# 자꾸 까먹어서 쓰는 백준 파이썬 입력

import sys

# 한줄 문자열 받을때
A = sys.stdin.readline()

# 정수 한개 받을때
A = int(sys.stdin.readline())

# 한줄에 있는 정수 여러개 받을때
A, B = map(int,sys.stdin.readline().split())

# 여러줄의 문자열 리스트 형식으로 받을때
C = int(sys.stdin.readline())
A = [sys.stdin.readline().strip() for i in range(C)]
