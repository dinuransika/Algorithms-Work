"""Functions that might be useful for the project Euler"""
def Insertion_Sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while i>=0 and A[i]>key:
            A[i+1] = A[i]
            i-=1
        A[i+1]=key
    return A
def prime(x):
    """If number is a prime this function outputs True"""
    if x < 2:
        return False
    elif x == 2 or x == 3:
        return True
    else:
        i = 1
        while i < int(x**0.5+1):
            i += 1
            if x % i == 0:
                return False
            else:
                continue
        else:
            return True


def palindromic(integer):
    """If the number is equal to the reversed number outputs True"""
    if str(integer) == str(integer)[::-1]:
        return True
    else:
        return False


def rev_num(num):
    """Outputs a reverse of an integer as an integer"""
    return int(str(num)[::-1])


def prime_factors(num):
    """Returns prime factors as a list"""
    sum_a = []
    if prime(num):
        sum_a.append(num)
    else:
        for i in range(2, num):
            if num % i == 0:
                sum_a.append(i)
                num /= i
    return sum_a


def totient_func(num):
    """Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number
       of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all
       less than nine and relatively prime to nine, φ(9)=6."""
    tot = 1
    for j in prime_factors(num):
        tot *= (1-1/j)
    return tot*num


def factors(num):
    """Returns factors as a list"""
    sum_a = []
    if prime(num):
        sum_a.append(num)
    else:
        for i in range(1, num):
            if num % i == 0:
                sum_a.append(i)
    return sum_a


def fibonacci(n):
    """This function returns the nTh fibonacci number."""
    phi = (1 + 5**0.5) / 2
    fn = (phi**n - (-1 * phi**(-1*n))) / 5**0.5
    return int(fn)

def bfs(n, m, edges, s):
    from collections import deque

    # Build graph
    graph = {}
    for num in range(1, n+1):
        graph[num] = set()
    for l, r in edges:
        graph[l].add(r)
        graph[r].add(l)
    
    reached = {}
    # Explore graph once
    frontier = deque([(s, 0)])
    seen = {s}

    while frontier:
        curr_node, curr_cost = frontier.popleft()
        for nbour in graph[curr_node]:
            if nbour not in seen:
                seen.add(nbour)
                reached[nbour] = curr_cost+6
                frontier.append((nbour, curr_cost+6))

    result = []
    for node in range(1, n+1):
        if s != node:
            result.append(reached.get(node, -1))
    
    return result


def max_area_histogram(histogram):
    stack = list()

    max_area = 0

    index = 0
    while index < len(histogram):

        if (not stack) or (histogram[stack[-1]] <= histogram[index]):
            stack.append(index)
            index += 1

        else:

            top_of_stack = stack.pop()

            area = (histogram[top_of_stack] *
                    ((index - stack[-1] - 1)
                     if stack else index))
            max_area = max(max_area, area)
    while stack:
        top_of_stack = stack.pop()
        area = (histogram[top_of_stack] *
                ((index - stack[-1] - 1)
                 if stack else index))
        max_area = max(max_area, area)
    return max_area
