def fibonacci_up_to_value(n):
    a, b = 0, 1
    series = []
    while a <= n:
        series.append(a)
        a, b = b, a + b
    return series

n = int(input("Enter the maximum value: "))
result = fibonacci_up_to_value(n)
print(f"Fibonacci series up to value {n}:")
print(*result, sep=", ")