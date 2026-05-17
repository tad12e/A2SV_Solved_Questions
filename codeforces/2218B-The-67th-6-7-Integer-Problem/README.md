# 2218B-The-67th-6-7-Integer-Problem

**Problem:** [2218B-The-67th-6-7-Integer-Problem](https://codeforces.com/contest/2218/problem/B)

**time limit per test:** 1 second

**memory limit per test:** 256 megabytes

---

So, Macaque has passed his first challenge (and is not acknowledging your help whatsoever). After all, it was only given to him so he could engage in his greatest pleasure — crunching on desiccated freezedried hamburgers and yelling 'trivial' at the screen. However, he has another, much more important task ahead of him, and he has once again enlisted you to help him.

You are given 7 integers a_1, a_2, …, a_7.

You must negate 6 out of the 7 integers (that is, multiply them by -1). Over all possible ways to negate 6 out of the 7 integers, find the maximum possible sum of a.


**Input**

Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 6767). The description of the test cases follows.

The first and only line of each test case contains 7 space-separated integers a_1, a_2, …, a_7 (-67 ≤ a_i ≤ 67).


**Output**

For each test case, output the maximum sum of a after negating 6 out of the 7 integers, on a new line.


**Example**

**Input**

```
4
41 41 41 41 41 41 41
6 9 4 20 6 7 67
1 2 3 4 5 6 7
6 7 6 7 6 7 6
```

**Output**

```
-205
15
-14
-31
```


**Note**

In the first test case, no matter which 6 integers we pick to negate, the maximum sum is -41-41-41-41-41-41+41=-205.

In the second test case, we can negate all integers except a_7 to obtain a sum of -6-9-4-20-6-7+67=15.
