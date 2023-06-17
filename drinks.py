n = int(input())
fractions = list(map(int, input().split()))

average_fraction = sum(fractions) / n
print(average_fraction)