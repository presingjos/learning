## Find the missing two numbers

Given an array of n unique integers where each element in the array is
in range [1, n]. The array has all distinct elements and size of array
is (n-2). Hence Two numbers from the range are missing from this array.
Find the two missing numbers.

Necessary concepts:
* ```A ^ B = C``` also means ```A ^ C = B``` and ```B ^ C = A```
* ```A ^ A = 0```

We will denote:
* M -> as the array with two missing numbers
* T -> as the array from 1 - n
* A -> as the first missing number
* B -> as the second missing number

First we must understand the following relationship between A, M, T, and B
* M. is the XOR of all numbers in M
* T. is the XOR of all numbers in T

```M. ^ T. = A ^ B```

Now if we were looking for one missing number we would be done, but we're not!

### How do we get A and B from ```A ^ B```?
We must look more into what A ^ B means

Suppose A = b010 (2) and B = b100 (4) and A ^ B = b110 (6).

Notice that A ^ B will NEVER be 0 as long as A and B are different.

Also that a bit set in A ^ B represents either:
- flipped bit in A and a non-flipped bit in B 
- flipped bit in B and a non-flipped bit in A

A = b0**1**0 B = b1**0**0 and A ^ B = b1**1**0

### Now suppose we group all numbers in M and T with particular bit flipped into one group (G1) and group all numbers in M and T with a particular bit not flipped into another (G2)

Ex. 

M = [b001, b010, b011]

T = [b001, b010, b011, b100, b101]

A ^ B = b00**1** = b100 ^ b101 (the bit of interest is in bold)

G1 = [b00**1**, b00**1**, b01**1**, b01**1**, b10**1**] 

G2 = [b01**0**, b01**0**, b10**0**]

What would happen if you XORed all nums in G1 together? You would get b101

What would happen if you XORed all nums in G2 together? You would get b100

---

### Now as for determining a specific bit we can use twos complement to find 
the least significant bit:

LSB = (A ^ B) & (~(A ^ B) + 1)

### How do we create G1 and G2:

If the LSB is flipped:

LSB = b001

```b001 & b111 = b001 = LSB``` -> G1

```b001 & b110 = b000 != LSB``` -> G2




    











