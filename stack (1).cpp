#include <iostream>
using namespace std;

// Menentukan Jumlah Stack
const int MAX = 5;

class Stack {
private:
    int data[MAX];
    int top;

public:
    // Inisialisasi Setup Stack
    Stack() : top(-1) {}
    bool isEmpty() { return top == -1; }
    bool isFull()  { return top == MAX - 1; }

    // 1. Operasi Push
    void push(int x) {
        if (isFull()) { cout << "Overflow" << endl; return; }
        data[++top] = x;
    }

    // 2. Operasi Pop
    int pop() {
        if (isEmpty()) { cout << "Underflow" << endl; return -1; }
        return data[top--];
    }

    int peek() { return isEmpty() ? -1 : data[top]; }

    // 3. Operasi Mengecek Dasar
    int getBottom() {
        if (isEmpty()) {
            cout << "Stack kosong" << endl;
            return -1;
        }
        return data[0];
    }

    // 4. Operasi Mengecek Data Array
    int getSize() { return top + 1; }
};

// 5. Implementasi Stack
int main() {
    Stack s;
    s.push(10); s.push(20); s.push(30); s.push(40); s.push(50);
    cout << "Top : " << s.peek() << endl;
    cout << "Pop : " << s.pop() << endl;
    cout << "Pop : " << s.pop() << endl;
    cout << "Pop : " << s.pop() << endl;
    cout << "Bottom : " << s.getBottom() << endl;
    cout << "Size : " << s.getSize() << endl;
    return 0;
}
