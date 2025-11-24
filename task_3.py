class Stack:
  def __init__(self):
    self.stack = []

  # Додавання елемента до стеку
  def push(self, item):
    self.stack.append(item)

  # Видалення елемента зі стеку
  def pop(self):
    if len(self.stack) < 1:
      return None
    return self.stack.pop()

  # Перевірка, чи стек порожній
  def is_empty(self):
    return len(self.stack) == 0

  # Перегляд верхнього елемента стеку без його видалення
  def peek(self):
    if not self.is_empty():
      return self.stack[-1]


dict_symbols = {
        "(": ")",
        "{": "}",
        "[": "]"
    }


def check_symbols(expression):
    stack_symbols = Stack()

    for i in expression:
        if expression.index(i) == 0 and (i not in dict_symbols.keys()):
            return False
        if i in dict_symbols.keys():
            stack_symbols.push(i)
        if i in dict_symbols.values():
            if dict_symbols[stack_symbols.peek()] == i:
                stack_symbols.pop()

    if stack_symbols.is_empty():
       return True
    return False

print(check_symbols("( ){[ 1 ]( 1 + 3 )( ){ }}"))
print(check_symbols("( 23 ( 2 - 3);"))
print(check_symbols("( 11 }"))
print(check_symbols("( 11 )"))