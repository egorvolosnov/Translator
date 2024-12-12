%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "bison.tab.h"  // Подключаем заголовочный файл с объявлениями токенов

void yyerror(const char *s); 
%}

%%

"#include <stdio.h>" { 
    // Игнорируем #include <stdio.h>
}
"int"        { 
    printf("Token: INT\n"); 
    return INT; 
} 
"main"       { 
    printf("Token: MAIN\n"); 
    return MAIN; 
} 
"return"     { 
    printf("Token: RETURN\n"); 
    return RETURN; 
} 
"printf"     { 
    printf("Token: PRINTF\n"); 
    return PRINTF; 
}
"while"      { 
    printf("Token: WHILE\n"); 
    return WHILE; 
} 
"for"        { 
    printf("Token: FOR\n"); 
    return FOR; 
}
"%"          { 
    printf("Token: MOD\n"); 
    return MOD; 
}
"if"         { 
    printf("Token: IF\n"); 
    return IF; 
}
"else"       { 
    printf("Token: ELSE\n"); 
    return ELSE; 
}
"{"          { 
    printf("Token: LBRACE\n"); 
    return LBRACE; 
} 
"}"          { 
    printf("Token: RBRACE\n"); 
    return RBRACE; 
} 
"("          { 
    printf("Token: LPAREN\n"); 
    return LPAREN; 
} 
")"          { 
    printf("Token: RPAREN\n"); 
    return RPAREN; 
} 
";"          { 
    printf("Token: SEMICOLON\n"); 
    return SEMICOLON; 
}
","          { 
    printf("Token: ZAPITAYA\n"); 
    return ZAPITAYA; 
}
"="          { 
    printf("Token: ASSIGN\n"); 
    return ASSIGN; 
}
"+"          { 
    printf("Token: PLUS\n"); 
    return PLUS; 
}
">"          { 
    printf("Token: MAX\n"); 
    return MAX; 
}
"<"          { 
    printf("Token: MIN\n"); 
    return MIN; 
}
"=="         { 
    printf("Token: EQUAL\n"); 
    return EQUAL; 
}
"!="         { 
    printf("Token: NOTEQUAL\n"); 
    return NOTEQUAL; 
}
"-"          { 
    printf("Token: MINUS\n"); 
    return MINUS; 
}
"*"          { 
    printf("Token: MUL\n"); 
    return MUL; 
}
"/"          { 
    printf("Token: DIV\n"); 
    return DIV; 
}
">="         { 
    printf("Token: GTE\n"); 
    return GTE; 
}
"<="         { 
    printf("Token: LTE\n"); 
    return LTE; 
}

[0-9]+            { 
    yylval.number = atoi(yytext);  
    printf("Token: NUMBER, value: %d\n", yylval.number); 
    return NUMBER; 
}

[a-zA-Z_][a-zA-Z0-9_]* { 
    strncpy(yylval.token, yytext, sizeof(yylval.token) - 1); 
    printf("Token: IDENTIFIER, value: %s\n", yylval.token); 
    return IDENTIFIER; 
}

\"[^"]*\"    { 
    strncpy(yylval.token, yytext, sizeof(yylval.token) - 1); 
    printf("Token: STRING, value: %s\n", yylval.token); 
    return STRING; 
}

[ \t\n]            { 
    // Игнорируем пробелы и переводы строк
}

.                 { 
    printf("Неизвестный символ: %s\n", yytext); 
    exit(1); 
}

%%

int yywrap() {
    return 1;
}
