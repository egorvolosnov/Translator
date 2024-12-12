Token: INT
Token: MAIN
Token: LPAREN
Token: RPAREN
Token: LBRACE
Token: INT
Token: IDENTIFIER, value: a
Token: ASSIGN
Token: NUMBER, value: 10
Token: SEMICOLON
Token: INT
Token: IDENTIFIER, value: b
Token: ASSIGN
Token: NUMBER, value: 20
Token: SEMICOLON
Token: INT
Token: IDENTIFIER, value: c
Token: ASSIGN
Token: NUMBER, value: 0
Token: SEMICOLON
Token: INT
Token: IDENTIFIER, value: sum
Token: ASSIGN
Token: NUMBER, value: 0
Token: SEMICOLON
Token: WHILE
Token: LPAREN
Token: IDENTIFIER, value: a
Token: MIN
Token: NUMBER, value: 15
Token: RPAREN
Token: LBRACE
Token: IF
Token: LPAREN
Token: IDENTIFIER, value: a
Token: MOD
Token: NUMBER, value: 2
Token: EQUAL
Token: NUMBER, value: 0
Token: RPAREN
Token: LBRACE
Token: PRINTF
Token: LPAREN
Token: STRING, value: "Число a чётное: %d\n"
Token: ZAPITAYA
Token: IDENTIFIER, value: a
Token: RPAREN
Token: SEMICOLON
Token: RBRACE
Token: ELSE
Token: LBRACE
Token: PRINTF
Token: LPAREN
Token: STRING, value: "Число a нечётное: %d\n"
Token: ZAPITAYA
Token: IDENTIFIER, value: a
Token: RPAREN
Token: SEMICOLON
Token: RBRACE
Token: IDENTIFIER, value: a
Token: ASSIGN
Token: IDENTIFIER, value: a
Token: PLUS
Token: NUMBER, value: 1
Token: SEMICOLON
Token: RBRACE
Token: FOR
Token: LPAREN
Token: INT
Token: IDENTIFIER, value: i
Token: ASSIGN
Token: NUMBER, value: 0
Token: SEMICOLON
Token: IDENTIFIER, value: i
Token: MIN
Token: IDENTIFIER, value: b
Token: SEMICOLON
Token: IDENTIFIER, value: i
Token: ASSIGN
Token: IDENTIFIER, value: i
Token: PLUS
Token: NUMBER, value: 1
Token: RPAREN
Token: LBRACE
Token: IF
Token: LPAREN
Token: IDENTIFIER, value: i
Token: EQUAL
Token: NUMBER, value: 10
Token: RPAREN
Token: LBRACE
Token: PRINTF
Token: LPAREN
Token: STRING, value: "Значение i равно 10\n"
Token: RPAREN
Token: SEMICOLON
Token: RBRACE
Token: ELSE
Token: IF
Token: LPAREN
Token: IDENTIFIER, value: i
Token: EQUAL
Token: NUMBER, value: 5
Token: RPAREN
Token: LBRACE
Token: PRINTF
Token: LPAREN
Token: STRING, value: "Значение i равно 5\n"
Token: RPAREN
Token: SEMICOLON
Token: RBRACE
Token: ELSE
Token: LBRACE
Token: PRINTF
Token: LPAREN
Token: STRING, value: "Текущее значение i: %d\n"
Token: ZAPITAYA
Token: IDENTIFIER, value: i
Token: RPAREN
Token: SEMICOLON
Token: RBRACE
Token: RBRACE
Token: IF
Token: LPAREN
Token: IDENTIFIER, value: a
Token: MAX
Token: IDENTIFIER, value: b
Token: RPAREN
Token: LBRACE
Token: PRINTF
Token: LPAREN
Token: STRING, value: "Значение a больше b\n"
Token: RPAREN
Token: SEMICOLON
Token: RBRACE
Token: ELSE
Token: IF
Token: LPAREN
Token: IDENTIFIER, value: a
Token: EQUAL
Token: IDENTIFIER, value: b
Token: RPAREN
Token: LBRACE
Token: PRINTF
Token: LPAREN
Token: STRING, value: "Значения a и b равны\n"
Token: RPAREN
Token: SEMICOLON
Token: RBRACE
Token: ELSE
Token: LBRACE
Token: PRINTF
Token: LPAREN
Token: STRING, value: "Значение a меньше b\n"
Token: RPAREN
Token: SEMICOLON
Token: RBRACE
Token: INT
Token: IDENTIFIER, value: x
Token: ASSIGN
Token: NUMBER, value: 0
Token: SEMICOLON
Token: WHILE
Token: LPAREN
Token: IDENTIFIER, value: x
Token: MIN
Token: NUMBER, value: 3
Token: RPAREN
Token: LBRACE
Token: FOR
Token: LPAREN
Token: INT
Token: IDENTIFIER, value: y
Token: ASSIGN
Token: NUMBER, value: 0
Token: SEMICOLON
Token: IDENTIFIER, value: y
Token: MIN
Token: NUMBER, value: 3
Token: SEMICOLON
Token: IDENTIFIER, value: y
Token: ASSIGN
Token: IDENTIFIER, value: y
Token: PLUS
Token: NUMBER, value: 1
Token: RPAREN
Token: LBRACE
Token: PRINTF
Token: LPAREN
Token: STRING, value: "x: %d, y: %d, произведение: %d\n"
Token: ZAPITAYA
Token: IDENTIFIER, value: x
Token: ZAPITAYA
Token: IDENTIFIER, value: y
Token: ZAPITAYA
Token: IDENTIFIER, value: x
Token: MUL
Token: IDENTIFIER, value: y
Token: RPAREN
Token: SEMICOLON
Token: RBRACE
Token: IDENTIFIER, value: x
Token: ASSIGN
Token: IDENTIFIER, value: x
Token: PLUS
Token: NUMBER, value: 1
Token: SEMICOLON
Token: RBRACE
Token: FOR
Token: LPAREN
Token: INT
Token: IDENTIFIER, value: i
Token: ASSIGN
Token: NUMBER, value: 0
Token: SEMICOLON
Token: IDENTIFIER, value: i
Token: MIN
Token: NUMBER, value: 5
Token: SEMICOLON
Token: IDENTIFIER, value: i
Token: ASSIGN
Token: IDENTIFIER, value: i
Token: PLUS
Token: NUMBER, value: 1
Token: RPAREN
Token: LBRACE
Token: IF
Token: LPAREN
Token: IDENTIFIER, value: i
Token: MOD
Token: NUMBER, value: 2
Token: EQUAL
Token: NUMBER, value: 0
Token: RPAREN
Token: LBRACE
Token: PRINTF
Token: LPAREN
Token: STRING, value: "Чётное число во втором цикле: %d\n"
Token: ZAPITAYA
Token: IDENTIFIER, value: i
Token: RPAREN
Token: SEMICOLON
Token: RBRACE
Token: ELSE
Token: LBRACE
Token: PRINTF
Token: LPAREN
Token: STRING, value: "Нечётное число во втором цикле: %d\n"
Token: ZAPITAYA
Token: IDENTIFIER, value: i
Token: RPAREN
Token: SEMICOLON
Token: RBRACE
Token: RBRACE
Token: FOR
Token: LPAREN
Token: INT
Token: IDENTIFIER, value: i
Token: ASSIGN
Token: NUMBER, value: 1
Token: SEMICOLON
Token: IDENTIFIER, value: i
Token: LTE
Token: NUMBER, value: 10
Token: SEMICOLON
Token: IDENTIFIER, value: i
Token: ASSIGN
Token: IDENTIFIER, value: i
Token: PLUS
Token: NUMBER, value: 1
Token: RPAREN
Token: LBRACE
Token: IDENTIFIER, value: sum
Token: ASSIGN
Token: IDENTIFIER, value: sum
Token: PLUS
Token: IDENTIFIER, value: i
Token: SEMICOLON
Token: RBRACE
Token: PRINTF
Token: LPAREN
Token: STRING, value: "Сумма чисел от 1 до 10: %d\n"
Token: ZAPITAYA
Token: IDENTIFIER, value: sum
Token: RPAREN
Token: SEMICOLON
Token: INT
Token: IDENTIFIER, value: num
Token: ASSIGN
Token: NUMBER, value: 13
Token: SEMICOLON
Token: INT
Token: IDENTIFIER, value: is_prime
Token: ASSIGN
Token: NUMBER, value: 1
Token: SEMICOLON
Token: FOR
Token: LPAREN
Token: INT
Token: IDENTIFIER, value: i
Token: ASSIGN
Token: NUMBER, value: 2
Token: SEMICOLON
Token: IDENTIFIER, value: i
Token: LTE
Token: IDENTIFIER, value: num
Token: DIV
Token: NUMBER, value: 2
Token: SEMICOLON
Token: IDENTIFIER, value: i
Token: ASSIGN
Token: IDENTIFIER, value: i
Token: PLUS
Token: NUMBER, value: 1
Token: RPAREN
Token: LBRACE
Token: IF
Token: LPAREN
Token: IDENTIFIER, value: num
Token: MOD
Token: IDENTIFIER, value: i
Token: EQUAL
Token: NUMBER, value: 0
Token: RPAREN
Token: LBRACE
Token: IDENTIFIER, value: is_prime
Token: ASSIGN
Token: NUMBER, value: 0
Token: SEMICOLON
Token: IDENTIFIER, value: break
Token: SEMICOLON
Token: RBRACE
Token: RBRACE
Token: IF
Token: LPAREN
Token: IDENTIFIER, value: is_prime
Token: RPAREN
Token: LBRACE
Token: PRINTF
Token: LPAREN
Token: STRING, value: "Число %d простое\n"
Token: ZAPITAYA
Token: IDENTIFIER, value: num
Token: RPAREN
Token: SEMICOLON
Token: RBRACE
Token: ELSE
Token: LBRACE
Token: PRINTF
Token: LPAREN
Token: STRING, value: "Число %d не простое\n"
Token: ZAPITAYA
Token: IDENTIFIER, value: num
Token: RPAREN
Token: SEMICOLON
Token: RBRACE
Token: IF
Token: LPAREN
Token: IDENTIFIER, value: a
Token: MOD
Token: NUMBER, value: 2
Token: EQUAL
Token: NUMBER, value: 0
Token: RPAREN
Token: LBRACE
Token: PRINTF
Token: LPAREN
Token: STRING, value: "Число a чётное: %d\n"
Token: ZAPITAYA
Token: IDENTIFIER, value: a
Token: RPAREN
Token: SEMICOLON
Token: RBRACE
Token: ELSE
Token: LBRACE
Token: PRINTF
Token: LPAREN
Token: STRING, value: "Число a нечётное: %d\n"
Token: ZAPITAYA
Token: IDENTIFIER, value: a
Token: RPAREN
Token: SEMICOLON
Token: RBRACE
Token: RETURN
Token: NUMBER, value: 0
Token: SEMICOLON
Token: RBRACE
import sys

if __name__ == "__main__":
	a = 10
	b = 20
	c = 0
	sum = 0
	while (a < 15):
		if(a % 2 == 0):
			print("Число a чётное: %d\n" % (a))
		else:
			print("Число a нечётное: %d\n" % (a))

		a = a + 1

	for i in range(0,b,1):
		if(i == 10):
			print("Значение i равно 10\n")
		elif(i == 5):
			print("Значение i равно 5\n")
		else:
			print("Текущее значение i: %d\n" % (i))

	if(a > b):
		print("Значение a больше b\n")
	elif(a == b):
		print("Значения a и b равны\n")
	else:
		print("Значение a меньше b\n")

	x = 0
	while (x < 3):
		for y in range(0,3,1):
			print("x: %d, y: %d, произведение: %d\n" % (x, y, x * y))

		x = x + 1

	for i in range(0,5,1):
		if(i % 2 == 0):
			print("Чётное число во втором цикле: %d\n" % (i))
		else:
			print("Нечётное число во втором цикле: %d\n" % (i))

	for i in range(1,10,1):
		sum = sum + i

	print("Сумма чисел от 1 до 10: %d\n" % (sum))
	num = 13
	is_prime = 1
	for i in range(2,num // 2,1):
		if(num % i == 0):
			is_prime = 0
			break

	if(is_prime):
		print("Число %d простое\n" % (num))
	else:
		print("Число %d не простое\n" % (num))

	if(a % 2 == 0):
		print("Число a чётное: %d\n" % (a))
	else:
		print("Число a нечётное: %d\n" % (a))

	sys.exit(0)

