class Integer:
  def __init__(self, value):
    self.value = value

class Tuple:
  def __init__(self, one, two):
    self.one = one
    self.two = two

a = Integer(1)
b = 1

def add_one(first:Integer, second:int):
  first.value += 1
  second += 1

add_one(a, b)

print(a.value)
print(b)

