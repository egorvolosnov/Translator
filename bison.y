%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void yyerror(const char *s);
char* add_indentation(const char* input);
int is_prev_newline = 0;
int yylex();
%}

%union {
    char type[4096]; 
    char token[2048];  
    int number;        
}

%token <number> NUMBER 
%token <token> IDENTIFIER STRING INT MAIN RETURN PRINTF WHILE FOR MOD IF 
%token <token> ELSE LBRACE RBRACE LPAREN RPAREN SEMICOLON ASSIGN PLUS
%token <token> MAX MIN EQUAL NOTEQUAL MINUS MUL DIV GTE LTE ZAPITAYA

%type <type> start main expressions progs cycles conditions signes elements print idents

%start start 

%%

start:
    INT MAIN LPAREN RPAREN LBRACE main RBRACE
    {
        printf("import sys\n\nif __name__ == \"__main__\":\n%s\n", add_indentation($6));
    }
    ;

main:
    { strcpy($$, ""); }
    | progs main
    {
        snprintf($$, sizeof($$), "%s\n%s", $1, $2);
    }
    ;

progs:
    INT expressions SEMICOLON
    {
        snprintf($$, sizeof($$), "%s", $2);
    }
    | expressions SEMICOLON
    {
        snprintf($$, sizeof($$), "%s", $1);
    }
    | conditions
    {
        snprintf($$, sizeof($$), "%s", $1);
    }
    | cycles
    {
        snprintf($$, sizeof($$), "%s", $1);
    }
    | print SEMICOLON
    {
        snprintf($$, sizeof($$), "%s", $1);
    }
    | RETURN elements SEMICOLON
    {
        snprintf($$, sizeof($$), "sys.exit(0)");
    }
    ;

expressions:
    elements signes elements
    {
        snprintf($$, sizeof($$), "%s %s %s", $1, $2, $3);
    }
    | elements signes elements signes elements
    {
        snprintf($$, sizeof($$), "%s %s %s %s %s", $1, $2, $3, $4, $5);
    }
    | elements
    {
        snprintf($$, sizeof($$), "%s", $1);
    }
    ;
elements:
    IDENTIFIER
    {
        snprintf($$, sizeof($$), "%s", $1);
    }
    | NUMBER
    {
        snprintf($$, sizeof($$), "%d", $1);
    }
    ;
signes:
    PLUS
    {
        snprintf($$, sizeof($$), "+");
    }
    | MINUS
    {
        snprintf($$, sizeof($$), "-");
    }
    | MAX
    {
        snprintf($$, sizeof($$), ">");
    }
    | MIN
    {
        snprintf($$, sizeof($$), "<");
    }
    | EQUAL
    {
        snprintf($$, sizeof($$), "==");
    }
    | NOTEQUAL
    {
        snprintf($$, sizeof($$), "!=");
    }
    | MUL
    {
        snprintf($$, sizeof($$), "*");
    }
    | DIV
    {
        snprintf($$, sizeof($$), "//");
    }
    | GTE
    {
        snprintf($$, sizeof($$), ">=");
    }
    | LTE
    {
        snprintf($$, sizeof($$), "<=");
    }
    | ASSIGN
    {
        snprintf($$, sizeof($$), "=");
    }
    | MOD
    {
        snprintf($$, sizeof($$), "%%");
    }
    ;

conditions:
    IF LPAREN expressions RPAREN LBRACE main RBRACE ELSE LBRACE main RBRACE
    {
        char* indented_true_block = add_indentation($6);
        char* indented_false_block = add_indentation($10);
        snprintf($$, sizeof($$), "if(%s):\n%selse:\n%s", $3, indented_true_block, indented_false_block);
        free(indented_true_block);
        free(indented_false_block);
    }
    | IF LPAREN expressions RPAREN LBRACE main RBRACE 
    {
        char* indented_true_block = add_indentation($6);
        snprintf($$, sizeof($$), "if(%s):\n%s", $3, indented_true_block);
        free(indented_true_block);
    }
    | IF LPAREN expressions RPAREN LBRACE main RBRACE ELSE IF LPAREN expressions RPAREN LBRACE main RBRACE ELSE LBRACE main RBRACE
    {
        char* indented_true1_block = add_indentation($6);
        char* indented_true2_block = add_indentation($14);
        char* indented_false_block = add_indentation($18);
        snprintf($$, sizeof($$), "if(%s):\n%selif(%s):\n%selse:\n%s", $3, indented_true1_block, $11, indented_true2_block, indented_false_block);
        free(indented_true1_block);
        free(indented_true2_block);
        free(indented_false_block);
    }
    ;

cycles:
    WHILE LPAREN expressions RPAREN LBRACE main RBRACE
    {
        char* indented_while_block = add_indentation($6);

        snprintf($$, sizeof($$), "while (%s):\n%s", $3, indented_while_block);

        free(indented_while_block);
    }
    | FOR LPAREN INT elements signes elements SEMICOLON elements signes expressions SEMICOLON elements signes elements signes elements RPAREN LBRACE main RBRACE
    {
        char* indented_while_block = add_indentation($19);
        snprintf($$, sizeof($$), "for %s in range(%s,%s,%s):\n%s", $4, $6, $10, $16, indented_while_block);
        free(indented_while_block);
    }
    ;
print:
    PRINTF LPAREN STRING RPAREN 
    {
        snprintf($$, sizeof($$), "print(%s)", $3);
    } 
    | PRINTF LPAREN STRING idents RPAREN 
    {
        snprintf($$, sizeof($$), "print(%s %% (%s))", $3, $4);  // Proper string formatting
    }
    ;

idents:
    ZAPITAYA expressions
    {
        snprintf($$, sizeof($$), "%s", $2);  // Format the expression correctly
    }
    | idents ZAPITAYA expressions
    {
        snprintf($$, sizeof($$), "%s, %s", $1, $3);  // Correctly add a comma between expressions
    } 
    ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

char* add_indentation(const char* input) {
    const char* indent = "\t";
    size_t indent_len = strlen(indent);

    // Вычисляем размер необходимого буфера
    size_t input_len = strlen(input);
    size_t max_result_len = input_len + (input_len * indent_len); // Максимально возможный размер (все строки с отступами)

    // Выделяем память
    char* result = (char*)malloc(max_result_len + 1); // +1 для завершающего нуля
    if (!result) {
        fprintf(stderr, "Memory allocation failed\n");
        return NULL;
    }

    const char* ptr = input;
    char* dest = result;

    

    while (*ptr) {
        // Пропускаем последовательность из двух или более \n
        if (*ptr == '\n' && *(ptr + 1) == '\n') {
            ptr++; // Пропускаем один из \n
            continue; // Пропускаем текущий символ \n
        }

        // Если текущий символ - это \n, проверяем, была ли предыдущая строка пустой
        if (*ptr == '\n') {
            if (is_prev_newline) {
                ptr++; // Пропускаем лишний перенос строки
                continue; // Пропускаем текущий символ \n
            }
            is_prev_newline = 1; // Отметим, что текущий символ это новый перенос
        } else {
            is_prev_newline = 0; // Если это не \n, сбрасываем флаг
        }

        // Добавляем отступ, если не пустая строка
        if (*ptr != '\n') { 
            strncpy(dest, indent, indent_len);
            dest += indent_len;
        }

        // Копируем строку до конца или новой строки
        while (*ptr && *ptr != '\n') {
            *dest++ = *ptr++;
        }

        // Если новая строка
        if (*ptr == '\n') {
            *dest++ = *ptr++; // Записываем сам символ новой строки
        }
    }

    *dest = '\0'; // Завершающий символ

    return result;
}





int main(void) {
    return yyparse();
}
