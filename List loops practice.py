"""
Python Practice File
--------------------
Demonstrates:
  1. Lists (creation, access)
  2. All common list functions/methods
  3. For loop (multiple styles)
  4. While loop
  
Run this file standalone: python list_loops_practice.py
"""

print("=" * 60)
print(" PYTHON LIST + LOOPS PRACTICE")
print("=" * 60)


# ==========================================================
# 1. LIST BASICS
# ==========================================================
print("\n--- 1. LIST BASICS ---")

fruits = ["apple", "banana", "mango", "orange", "grape"]
print(f"List: {fruits}")
print(f"Length: {len(fruits)}")
print(f"First item: {fruits[0]}")
print(f"Last item: {fruits[-1]}")
print(f"Slicing [1:4]: {fruits[1:4]}")


# ==========================================================
# 2. LIST FUNCTIONS / METHODS (all common ones)
# ==========================================================
print("\n--- 2. LIST FUNCTIONS ---")

numbers = [10, 20, 30]
print(f"Original: {numbers}")

# append - add single item at end
numbers.append(40)
print(f"After append(40): {numbers}")

# insert - add at specific index
numbers.insert(1, 15)
print(f"After insert(1, 15): {numbers}")

# extend - add multiple items
numbers.extend([50, 60])
print(f"After extend([50, 60]): {numbers}")

# remove - remove by value
numbers.remove(15)
print(f"After remove(15): {numbers}")

# pop - remove by index (default last)
popped = numbers.pop()
print(f"After pop() - removed {popped}: {numbers}")

# index - find position of value
pos = numbers.index(30)
print(f"Index of 30: {pos}")

# count - count occurrences
nums2 = [1, 2, 2, 3, 2, 4]
print(f"Count of 2 in {nums2}: {nums2.count(2)}")

# sort - sort in place
unsorted = [5, 2, 8, 1, 9, 3]
unsorted.sort()
print(f"Sorted ascending: {unsorted}")

unsorted.sort(reverse=True)
print(f"Sorted descending: {unsorted}")

# reverse - reverse the list
unsorted.reverse()
print(f"After reverse: {unsorted}")

# copy - copy a list
copied = unsorted.copy()
print(f"Copy: {copied}")

# clear - empty the list
copied.clear()
print(f"After clear: {copied}")

# Built-in functions on lists
nums3 = [12, 45, 7, 89, 23, 5]
print(f"\nList: {nums3}")
print(f"min(): {min(nums3)}")
print(f"max(): {max(nums3)}")
print(f"sum(): {sum(nums3)}")
print(f"sorted(): {sorted(nums3)}")
print(f"len(): {len(nums3)}")


# ==========================================================
# 3. FOR LOOP - DIFFERENT STYLES
# ==========================================================
print("\n--- 3. FOR LOOP ---")

# Style 1: Simple iteration
print("\n[For loop - simple]")
for fruit in fruits:
    print(f"  Fruit: {fruit}")

# Style 2: With index using enumerate
print("\n[For loop - with index]")
for i, fruit in enumerate(fruits):
    print(f"  {i} -> {fruit}")

# Style 3: Using range
print("\n[For loop - range 1 to 5]")
for i in range(1, 6):
    print(f"  Number: {i}")

# Style 4: range with step
print("\n[For loop - even numbers 0 to 10]")
for i in range(0, 11, 2):
    print(f"  Even: {i}")

# Style 5: Loop with condition (filter)
print("\n[For loop - filter big numbers]")
big_nums = []
for n in nums3:
    if n > 20:
        big_nums.append(n)
print(f"  Numbers > 20: {big_nums}")

# Style 6: List comprehension (one-liner)
print("\n[List comprehension - squares]")
squares = [x * x for x in range(1, 6)]
print(f"  Squares: {squares}")


# ==========================================================
# 4. WHILE LOOP - DIFFERENT STYLES
# ==========================================================
print("\n--- 4. WHILE LOOP ---")

# Style 1: Counter
print("\n[While loop - counter 1 to 5]")
i = 1
while i <= 5:
    print(f"  Count: {i}")
    i += 1

# Style 2: Reverse counter
print("\n[While loop - countdown from 5]")
n = 5
while n > 0:
    print(f"  Countdown: {n}")
    n -= 1
print("  Liftoff!")

# Style 3: Sum until target
print("\n[While loop - sum until > 50]")
total = 0
i = 1
while total <= 50:
    total += i
    i += 1
print(f"  Final total: {total} (took {i-1} iterations)")

# Style 4: Loop through list with while
print("\n[While loop - iterate list]")
idx = 0
while idx < len(fruits):
    print(f"  fruits[{idx}] = {fruits[idx]}")
    idx += 1

# Style 5: Break and continue
print("\n[While loop - break and continue]")
i = 0
while i < 10:
    i += 1
    if i == 3:
        continue   # skip 3
    if i == 7:
        break      # stop at 7
    print(f"  i = {i}")


# ==========================================================
# 5. COMBINED EXAMPLE - real use case
# ==========================================================
print("\n--- 5. COMBINED EXAMPLE ---")

salaries = [45000, 75000, 60000, 90000, 55000, 80000, 70000]
print(f"Salaries: {salaries}")

# Use for loop to filter high earners
high_earners = []
for s in salaries:
    if s > 70000:
        high_earners.append(s)
print(f"High earners (>70k): {high_earners}")

# Use list functions
print(f"Total: {sum(salaries)}")
print(f"Average: {sum(salaries) / len(salaries)}")
print(f"Highest: {max(salaries)}")
print(f"Lowest: {min(salaries)}")

# Use while loop to find first salary > 80000
print("\nFinding first salary above 80000:")
idx = 0
while idx < len(salaries):
    if salaries[idx] > 80000:
        print(f"  Found at index {idx}: {salaries[idx]}")
        break
    idx += 1


print("\n" + "=" * 60)
print(" END OF PRACTICE FILE")
print("=" * 60)