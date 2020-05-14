import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")
f.close()

with open('names_1.txt', 'r') as f:
    names = BinarySearchTree(f.readline())
    for line in f.readlines():
        names.insert(line.strip())

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure
# Replace the nested for loops below with your improvements
for name in names_2:
    if names.contains(name):
        duplicates.append(name)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# the fastest thing I could find on the web
start_time2 = time.time()
duplicates = set(names_1) & set(names_2)  # I got this line from google

end_time2 = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(list(duplicates))}\n\n")
print(f"runtime: {end_time2 - start_time2} seconds")

# stretch goal: use only lists

start_time3 = time.time()
duplicates = [i for i in names_1 if i in names_2]

end_time3 = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(list(duplicates))}\n\n")
print(f"runtime: {end_time3 - start_time3} seconds")


# Original Runtime: O(n^2)
# BST Runtime: O(n log n)? Possibly O(log n)?
