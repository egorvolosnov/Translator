#include <stdio.h>

int main() {
    int a = 10;
    int b = 20;
    int c = 0;
    int sum = 0;

    while (a < 15) {
        if (a % 2 == 0) {
            printf("Число a чётное: %d\n", a);
        } else {
            printf("Число a нечётное: %d\n", a);
        }
        a = a + 1; 
    }

    for (int i = 0; i < b; i = i + 1) {
        if (i == 10) {
            printf("Значение i равно 10\n");
        } else if (i == 5) {
            printf("Значение i равно 5\n");
        } else {
            printf("Текущее значение i: %d\n", i);
        }
    }

    if (a > b) {
        printf("Значение a больше b\n");
    } else if (a == b) {
        printf("Значения a и b равны\n");
    } else {
        printf("Значение a меньше b\n");
    }

    int x = 0;
    while (x < 3) {
        for (int y = 0; y < 3; y = y + 1) {
            printf("x: %d, y: %d, произведение: %d\n", x, y, x * y);
        }
        x = x + 1;
    }

    for (int i = 0; i < 5; i = i + 1) {
        if (i % 2 == 0) {
            printf("Чётное число во втором цикле: %d\n", i);
        } else {
            printf("Нечётное число во втором цикле: %d\n", i);
        }
    }

    for (int i = 1; i <= 10; i = i + 1) {
        sum = sum + i;
    }
    printf("Сумма чисел от 1 до 10: %d\n", sum);
    int num = 13;
    int is_prime = 1;
    for (int i = 2; i <= num / 2; i = i + 1) {
        if (num % i == 0) {
            is_prime = 0;  
            break;
        }
    }
    if (is_prime) {
        printf("Число %d простое\n", num);
    } else {
        printf("Число %d не простое\n", num);
    }
    if (a % 2 == 0) {
        printf("Число a чётное: %d\n", a);
    } else {
        printf("Число a нечётное: %d\n", a);
    }
    return 0;
}
