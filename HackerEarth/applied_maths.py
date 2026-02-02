'''

Make an array
51% Success
11561 Attempts
20 Points
1s Time Limit
256MB Memory
1024 KB Max Code
You are given an array A of length N. You take an array B of length N such that B[i] = 0 for each 1 <= i <= N. You can apply the following operation on B any number of times:

Choose (N - 1) distinct indices and add 1 to each of those indices.
Task

Find the number of operations required to convert array B into array A by applying the given operation. Print -1 if it is impossible to do so.

Function description

Complete the function solve() provided in the editor. This function takes the following two parameters and returns the required answer:

N: Represents the length of array A.
A: Represents the array A.
Input format

Note: This is the input format that you must use to provide custom input (available above the Compile and Test button).

The first line contains T, denoting the number of test cases. T also specifies the number of times you have to run the solve function on a different set of inputs.
For each test case:
The first line contains N, denoting the size of array A.
The second line contains N space-separated integers A[1], A[2], ....., A[N], denoting the elements of array A.
Output format
For each test case, print the number of operations required to convert array B into array A by applying the given operation or -1 if it is impossible to do so.

Constraints

Examples
Input

2
3
3 1 0
2
0 2
Output

-1
2
Explanation
The first line denotes T = 2.

For the first test case

Given

N = 3
A = [3, 1, 0]
​​Approach

It is impossible to convert B = [0, 0, 0] into A = [3, 1, 0] using the given operation. Thus, the answer is -1.
For the second test case

Given

N = 2
A = [0, 2]
​​Approach

Initially, B = [0, 0].
Applying the operation on index i = 2 makes B = [0, 1].
Applying the operation on index i = 2 makes B = [0, 2], which is equal to A. Thus, the answer is 2.

'''

# Approach 
'''
Key Insight — Think in Reverse (Invariant Method)

We do not build array B step by step.
Instead, we analyze what must have happened to reach array A.

🔄 Reverse Thinking

Each operation:

Adds +1 to N-1 indices

Skips exactly one index

Let:

k = total number of operations

skip[i] = how many times index i was skipped

Then for each index:

A[i] = k - skip[i]


Because:

Every operation contributes +1

Except when that index is skipped

So:

skip[i] = k - A[i]

🔐 Core Invariant (Most Important Part)

Each operation skips exactly ONE index
So total skips over all operations:

skip[1] + skip[2] + ... + skip[N] = k


Substitute skip[i] = k - A[i]:

N*k - sum(A) = k


Rearranging:

(N - 1) * k = sum(A)


👉 This equation must hold.

✅ Feasibility Conditions

From:

k = sum(A) / (N - 1)

'''

# algorithm

'''
For each test case:

Compute sumA = sum(A)

If sumA % (N-1) != 0 → print -1

Else:

k = sumA / (N-1)

If max(A) > k → print -1

Else → print k

'''

#CODE

def solve(N, A):
    Sum = sum(A)

    if Sum % (N - 1) != 0:
        return -1
    else:
        k = Sum // (N - 1)   # integer division
        if k < max(A):
            return -1
        else:
            return k

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))


# reason of not using __main__ function
'''
Top-level code in Python refers to all statements written directly in a file, outside of any function, class, or conditional block. Python executes this top-level code immediately and sequentially when the file is run or even when it is imported as a module. This behavior can cause unintended execution during imports. To control this, Python provides the if __name__ == "__main__": guard, which ensures that execution-related code runs only when the file is executed directly, and not when it is imported. Functions defined in the file never run automatically; they execute only when explicitly called. Using the __main__ guard is a best practice in real-world applications to keep modules reusable and prevent unwanted execution during imports.
'''

'''
Key rule to remember

Python executes all top-level code immediately when a file is run or imported.

That's why imports can accidentally execute code if we're not careful.

🔍 Why this matters for __main__
print("A")                     # top-level → always runs

if __name__ == "__main__":
    print("B")                 # guarded → runs only when executed directly

Action	Output
python file.py	A B
import file	A
'''