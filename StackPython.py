# Menentukan Jumlah Stack
MAX = 5


class Stack:
    # Inisialisasi Setup Stack
    def __init__(self):
        self.data = [None] * MAX
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == MAX - 1

    # 1. Operasi Push
    def push(self, x):
        if self.is_full():
            print("Overflow")
            return
        self.top += 1
        self.data[self.top] = x

    # 2. Operasi Pop
    def pop(self):
        if self.is_empty():
            print("Underflow")
            return -1
        x = self.data[self.top]
        self.top -= 1
        return x

    def peek(self):
        return -1 if self.is_empty() else self.data[self.top]

    # 3. Operasi Mengecek Dasar
    def get_bottom(self):
        if self.is_empty():
            print("Stack kosong")
            return -1
        return self.data[0]

    # 4. Operasi Mengecek Data Array
    def get_size(self):
        return self.top + 1


# 5. Implementasi Stack
if __name__ == "__main__":
    s = Stack()
    for nilai in (10, 20, 30, 40, 50):
        s.push(nilai)
    print("Top :", s.peek())
    print("Pop :", s.pop())
    print("Pop :", s.pop())
    print("Pop :", s.pop())
    print("Bottom :", s.get_bottom())
    print("Size :", s.get_size())
