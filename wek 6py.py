
numbers = [3, 7, 2, 9, 4, 1, 8]
numbers.append(5)
numbers.remove(9)
numbers.sort()
numbers.reverse()
numbers.insert(2, 6)
print(numbers.index(4))

my_tuple = (15, "Python", 3.14, True, 42, False)
print(my_tuple.index("Python"))
print(my_tuple.count(True))
print(my_tuple[1:5])


marks = {"Alice": 75, "Bob": 82, "Charlie": 68, "David": 90, "Eve": 77}
marks["Frank"] = 60
for student, mark in marks.items():
    print(student, mark)


mutable_example = [1, 2, 3]
mutable_example.append(4)
print(mutable_example)

immutable_example = (1, 2, 3)
print(immutable_example)


global_var = "I am global"

def example_function():
    local_var = "I am local"
    print(local_var)
    print(global_var)

example_function()
