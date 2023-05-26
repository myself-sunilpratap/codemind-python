def sum_up_to_k(nums, k):
    return sum(nums[:k])

# Read input
N = int(input())
nums = list(map(int, input().split()))
K = int(input())

# Calculate the sum up to Kth number
result = sum_up_to_k(nums, K)

# Print the result
print(result)
