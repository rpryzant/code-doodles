


class Stack:
    def __init__(self):
        self.data = []

    def push(self, c):
        self.data.append(c)

    def peek(self):
        if not self.data:
            return None
        else:
            return self.data[-1]

    def pop(self):
        if not self.data:
            return None
        else:
            self.data = self.data[:-1]
    
    def empty(self):
        return len(self.data) == 0


def is_valid(s):
    st = Stack()
    for ch in s:
        if ch not in ('(', ')'):
            continue
        if ch == '(':
            st.push(ch)
        else:
            if st.peek() == '(':
                st.pop()
            else:
                return False
    if st.empty():
        return True
    else:
        return False


test = '(a()((bs)))'
print is_valid(test)

test = '((()(())'
print is_valid(test)

test = '(()))()'
print is_valid(test)
