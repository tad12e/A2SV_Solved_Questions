# Enter your code here. Read input from STDIN. Print output to STDOUT

# Read input values
a = int(input())
b = int(input())
m = int(input())

# Calculate a^b and a^b % m
result_power = pow(a, b)          # First line: a raised to the power of b
result_mod_power = pow(a, b, m)   # Second line: a raised to the power of b modulo m

# Print results
print(result_power)
print(result_mod_power)
