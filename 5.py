# 이차원 리스트
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 요소 추가
matrix[1] = matrix[1] + [99]
print(matrix)  # [[1, 2, 3], [4, 5, 6, 99], [7, 8, 9]]

# 행 추가
matrix = matrix + [[10, 11, 12]]
print(matrix)  # [[1, 2, 3], [4, 5, 6, 99], [7, 8, 9], [10, 11, 12]]

# 요소 수정
matrix[0][1] = 100
matrix[1][1] = 5000
print(matrix)  # [[1, 100, 3], [4, 5000, 6, 99], [7, 8, 9], [10, 11, 12]]

# 행 삭제
del matrix[2]
print(matrix)  # [[1, 100, 3], [4, 5000, 6, 99], [10, 11, 12]]

# 행 개수 확인
rows = len(matrix)
rows2 = len(matrix[0])
rows3 = len(matrix[1])
rows4 = len(matrix[2])
print(rows)  # 3
print(rows2)  # 3
print(rows3)  # 4
print(rows4)  # 3

# 이차원 메서드
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 요소 추가
matrix[0].append(10)
print(matrix)  # [[1, 2, 3, 10], [4, 5, 6], [7, 8, 9]]

# 행 추가
matrix.append([10, 11, 12])
print(matrix)  # [[1, 2, 3, 10], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

# 요소 삽입
matrix[1].insert(1, 100)
print(matrix)  # [[1, 2, 3, 10], [4, 100, 5, 6], [7, 8, 9], [10, 11, 12]]

# 리스트 확정
matrix[0].extend([11, 12])
print(matrix)

# 문자열 조합
words = [
    [["마", "크"], ["구", "이"]],[["피", "아"], 
    ["림", "차"]], [["스", "사"], ["나", "가"]],
]
words = words[1][0][1] + words[0][1][1] + words[2][0][0] + words[0][0][1] + words[1][1][0]
print(words)