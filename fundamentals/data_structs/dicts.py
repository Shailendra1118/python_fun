import math

map = {}
key = 10
val = bin(key)
map[key] = val
print(f"key: {key} and value: {map.get(key)}")

map[-132] = 6
res = -132/6
print(f"division res: {res}")

res1 = 6/132
print(f"division res1 with ceiling: {math.ceil(res1)}")
print(f"division res1: {res1}")


# Python dictionaries maintain insertion order
my_map = {}
my_map["Shailendra"] = 100
my_map["Soorya"] = 150
my_map["Aman"] = 500
my_map["Vinayak"] = 300

sorted_map = dict(sorted(my_map.items()))
print(f"sorted_map is {sorted_map}")

# Sort by values
sorted_by_values = dict(sorted(my_map.items(), key=lambda item: -item[1]))
print(f"sorted_map by value is {sorted_by_values}")

# Sort by descending values, then by keys alphabetically
sorted_custom = dict(sorted(my_map.items(), key=lambda item: (-item[1], item[0])))
print("custom sorted", sorted_custom)  