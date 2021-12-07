A, B, V = map(int, input().split())

result = 0
count = 0
while result < V :
    result = result + A
    if result < V :
        result = result - B
    count = count + 1
print(result)