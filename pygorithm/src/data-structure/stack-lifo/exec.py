from stack import Stack
print("hello stack")

# push: add factor
# pop: delete factor
# peak: check first factor
# bounded stack
# unbounded stack

list = ["a", "b", "c"]
test = Stack()
test.push(list)
test.push("abc")
print(test.size())
print(test.pop())
print(test.size())

print(test.peek())
print(test.pop())
print(test.size())
print(test.is_empty())
