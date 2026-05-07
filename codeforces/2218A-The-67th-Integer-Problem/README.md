# 2218A-The-67th-Integer-Problem

**Problem:** [2218A-The-67th-Integer-Problem](https://codeforces.com/contest/2218/problem/A)

**time limit per test:** 1 second

**memory limit per test:** 256 megabytes

---

Welcome to the New World, O Esteemed Earthly Visitor. You've been summoned by Macaque, a primate with four legs, a god complex and a terminal addiction to the word "trivial". You are Undertaking a Journey of Great Importance. Such Incredible Importance. No Journey Will EVER be as IMPORTANT as this one (and nothing this narrator says will sound so distinctly... orange again). You are implored to cooperate with Macaque, for his wrath (and joblessness) are unending. There is no room for error or incompetence. Lousiness shall be met with the full force of the law.

Macaque is given an integer x. Your task is to choose an integer y such that the value of \operatorname{min}(x, y)^{\text{∗}} is maximized.

If there are multiple valid y, you may output any of them.

^{\text{∗}}\operatorname{min}(x, y) is defined as the minimum of integers x and y.


**Input**

Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 6767). The description of the test cases follows.

The only line of each test case contains a single integer x (-67 ≤ x ≤ 67).


**Output**

For each test case, output one integer y (-67 ≤ y ≤ 67) such that \min(x, y) is maximized.


**Example**

**Input**

```
3
1
3
5
```

**Output**

```
2
4
6
```


**Note**

In the first case, 2 is a possible answer because \min(1, 2) = 1, which can be shown to be maximal.
