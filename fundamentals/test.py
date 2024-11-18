from collections import deque


queue = deque([1,2,4,5,6])
print(queue.popleft())
print(queue.pop())

print("remaining queue", queue)
arr = [1,3,4,5]

sqaure = lambda i:i*2
print(sqaure(40))

res = list(map(sqaure, arr))
print(res)

# map(function, iterables)


#set
xset = {'Orange', 'Apple', 'Banana'}
print(xset)

emptySet = set()
print(emptySet)

val1 = set("Shailendra")
print(val1)

val2 = set('Singh')
print(f"val1-val2 is: {val1-val2}")

# val1 = set("Shailendra", "Singh", "Yadav") compliation error, set() only expect single arguments
val1 = set(["Shailendra", "Singh", "Yadav"])
print(val1)

val2 = set(["Singh"])
print(f"New val1-val2 is: {val1-val2}")


print(val1 & val2) #common letter in both val1 and val2
print(val1 ^ val2) # letters in a or b but not in both


dic = {'Shailendra':100, 300: "Singh"}
print(dic[300])

count = int(10.76)
a_count = int(10.01)
print(count, a_count)



nums = [1,2,3,4,5]
for i, val in enumerate(nums,2):
	if val != 0:
		print(f"value is val: {val} and index is: {i}")
	
for i in range(1, len(nums)):
	print(f"index: {i} and value: {nums[i]}")

right = []
right.insert(-1, 1)
#right.insert(-2, 100)
print(f"right: {right}")

k = -2
for i in reversed(nums):
	print(f"Reversed index: {i} and value: {nums[i-1]}")
	right.insert(k, nums[i-1] * right[k+1])
	k = k-1



nums = [-1,1,0,-3,3]
print(f"new nums: {nums}")
k = -2
res = []
res.insert(-1,1)
for j in range(len(nums), 0, -1):
    print(f"j: {j}")

print(f"right now: {res}")

nums = [1,2,3,4,5]
for i in range(len(nums)):
	print(f"i: {i} and value is: {nums[~i]}")
