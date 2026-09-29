

import time

# Finding Fibonacci number using recursion
operations = 0
series = []

def fibonacci(number):
    global operations
    operations += 1
    if number == 0 or number == 1:
        return number
    return fibonacci(number-1) + fibonacci(number-2)

n = 10
start_time = time.perf_counter()
print('\n\nFibonacci number using Simple Recursion')
print('Fibonacci of ', n, ' = ', fibonacci(n))
print('Number of operations performed to calculate above => ', operations)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time:.6f} seconds")



# Finding fibonacci number using memoization
operations = 0
array = [None] * 100
def fibonacci_memoization(num, memory):
    global operations
    operations += 1
    if memory[num] is not None:
        return memory[num]

    if num == 0 or num == 1:
        return num

    memory[num] = fibonacci_memoization(num-1, memory) + fibonacci_memoization(num-2, memory)
    return memory[num]

n = 50
start_time = time.perf_counter()
print('\n\nFibonacci number using Memoization')
print('Fibonacci of ', n, ' = ', fibonacci_memoization(n, array))
print('Number of operations performed to calculate above => ', operations)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time:.6f} seconds")


# Finding fibonacci number using tabulation
array = [None] * 100
def fibonacci_tabulation(num, memory):
    global operations
    operations += 1
    memory[0] = 0
    memory[1] = 1
    for i in range(2, num+1):
        memory[i] = memory[i-1] + memory[i-2]

    return memory[num]

n = 50
start_time = time.perf_counter()
print('Fibonacci number using Tabulation')
print('\n\nFibonacci of ', n, ' = ', fibonacci_tabulation(n, array))
print('Number of operations performed to calculate above => ', operations)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time:.6f} seconds")


# Finding fibonacci number using tabulation with space optimization
def fibonacci_tabulation_space_optimization(num):
    prev = 1
    prev2 = 0
    current = prev + prev2
    for i in range(2, num+1):
        current = prev + prev2
        prev2 = prev
        prev = current
    return current


n = 50
start_time = time.perf_counter()
print('\n\nFibonacci number using tabulation with space optimization')
print('Fibonacci of ', n, ' = ', fibonacci_tabulation_space_optimization(n))
print('Number of operations performed to calculate above => ', operations)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time:.6f} seconds")




