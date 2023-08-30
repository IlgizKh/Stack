class Stack():
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return True

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        deleted = self.stack.pop()
        return deleted

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


def bad_balance(string):
    s = Stack()
    for el in string:
        if el in ["(", "{", "["]:
            s.push(el)
        else:
            if s.is_empty() == True:
                print("Not balanced")
                s.push(el)
                break
            else:
                if (el == ")" and s.peek() == "(") or (el == "]" and s.peek() == "[") or (
                        el == "}" and s.peek() == "{"):
                    s.pop()
                else:
                    print("Not balanced")
                    break
    if s.size() == 0:
        print("Balanced")


bad_balance("(((([{}]))))")
bad_balance("[([])((([[[]]])))]{()}")
bad_balance("{{[()]}}")
bad_balance("}{}")
bad_balance("{{[(])]}}")
bad_balance("[[{())}]")