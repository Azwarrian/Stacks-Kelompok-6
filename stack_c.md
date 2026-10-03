# Implementasi Stack dalam Bahasa C

Stack berbasis array dengan operasi push, pop, peek, getBottom, dan getSize.

## Kode Program

```c
#include <stdio.h>
//Menentukan Jumlah Stack//
#define MAX 5
typedef struct { int data[MAX]; int top; } Stack;

//Inisialisasi Setup Stack//
void init(Stack *s)    { s->top = -1; }
int isEmpty(Stack *s)  { return s->top == -1; }
int isFull(Stack *s)   { return s->top == MAX - 1; }

//1. Operasi Push//
void push(Stack *s, int x) {
    if (isFull(s)) { printf("Overflow\n"); return; }
    s->data[++s->top] = x;
}

//2. Operasi Pop//
int pop(Stack *s) {
    if (isEmpty(s)) { printf("Underflow\n"); return -1; }
    return s->data[s->top--];
}
int peek(Stack *s) { return isEmpty(s) ? -1 : s->data[s->top]; }

//3. Operasi Mengecek Dasar//
int getBottom(Stack *s) {
    if (isEmpty(s)) {
        printf("Stack kosong\n");
        return -1; 
    }
    return s->data[0];
}

//4. Operasi Mengecek Data Array//
int getSize(Stack *s) {
    return s->top + 1;
}

//5. Implementasi Stack//
int main() {
    Stack s; init(&s);
    push(&s, 10); push(&s, 20); push(&s, 30); push(&s, 40); push(&s, 50);
    printf("Top : %d\n", peek(&s));
    printf("Pop : %d\n", pop(&s));
    printf("Pop : %d\n", pop(&s));
    printf("Pop : %d\n", pop(&s));
    printf("Bottom : %d\n", getBottom(&s));
    printf("Size : %d\n", getSize(&s));
    return 0;
}
```

## Output

```
Top : 50
Pop : 50
Pop : 40
Pop : 30
Bottom : 10
Size : 2
```
