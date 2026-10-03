public class StackArray {
    // Menentukan Jumlah Stack
    private static final int MAX = 5;
    private int[] data = new int[MAX];
    private int top = -1; // Inisialisasi Setup Stack

    boolean isEmpty() { return top == -1; }
    boolean isFull()  { return top == MAX - 1; }

    // 1. Operasi Push
    void push(int x) {
        if (isFull()) { System.out.println("Overflow"); return; }
        data[++top] = x;
    }

    // 2. Operasi Pop
    int pop() {
        if (isEmpty()) { System.out.println("Underflow"); return -1; }
        return data[top--];
    }

    int peek() { return isEmpty() ? -1 : data[top]; }

    // 3. Operasi Mengecek Dasar
    int getBottom() {
        if (isEmpty()) {
            System.out.println("Stack kosong");
            return -1;
        }
        return data[0];
    }

    // 4. Operasi Mengecek Data Array
    int getSize() { return top + 1; }

    // 5. Implementasi Stack
    public static void main(String[] args) {
        StackArray s = new StackArray();
        s.push(10); s.push(20); s.push(30); s.push(40); s.push(50);
        System.out.println("Top : " + s.peek());
        System.out.println("Pop : " + s.pop());
        System.out.println("Pop : " + s.pop());
        System.out.println("Pop : " + s.pop());
        System.out.println("Bottom : " + s.getBottom());
        System.out.println("Size : " + s.getSize());
    }
}
