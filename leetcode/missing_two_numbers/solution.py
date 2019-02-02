"""Missing two numbers

Problem statement
-----------------
Given an array of n unique integers where each element in the array is
in range [1, n]. The array has all distinct elements and size of array
is (n-2). Hence Two numbers from the range are missing from this array.
Find the two missing numbers.

"""

def simple_approach(nums, N):
    """In this approach we will iterate through the list
    nums and hash every single number.

    Next, we will iterate through numbers 1 - N and check
    if that number is in the hash table. If the number
    is not in the hash table then we have found a missing
    number.

    T: O(N)
    S: O(N) - for the hash table

    """
    store = {}
    for i in nums:
        store[i] = None
    result = []
    for j in range(1, N + 1):
        if j not in store:
            result.append(j)
    return result

def XOR_approach(nums, N):
    """With this approach we will try to improve the simple_approach
    by not using any extra space.

    1. XOR all numbers in nums with each other -> X
    2. XOR all numbers from 1 - N -> Y
    3. X XOR Y = A XOR B
    4. Determine least significant bit (using least sig. bit not necessary)
       in A XOR B
    5. XOR all numbers in nums and 1 - N that have the least sig. bit flipped -> A
    6. XOR all numbers in nums and 1 - N that have the least sig. bit not flipped -> B
    7. Return [A, B]

    T: O(n)
    S: O(1) -> constant

    """
    # XOR all numbers in nums with each other -> X
    X = nums[0]
    for i in range(1, len(nums)):
        X = X ^ nums[i]

    # XOR all numbers from 1 - N -> Y
    Y = 1
    for j in range(2, N + 1):
        Y = Y ^ j

    # Determine least sig. bit
    AB = X ^ Y
    # AKA twos complement of AB
    least_sig_bit = AB & (~AB + 1)
    # We know
    # least_sig_bit & num with least sig bit flipped = least sig bit

    # Start grouping
    A = None
    B = None
    # Group by flipped and not flipped least sig. bit
    for num in range(1, N + 1):
        if num & least_sig_bit == least_sig_bit:
            if A is None:
                A = num
            else:
                A = A ^ num
        else:
            if B is None:
                B = num
            else:
                B = B ^ num
    for num in nums:
        if num & least_sig_bit == least_sig_bit:
            A = A ^ num
        else:
            B = B ^ num
    return [A, B]

if __name__ == "__main__":
    print(simple_approach([1, 2, 3], 5))
    print(XOR_approach([4, 5, 1], 5))
