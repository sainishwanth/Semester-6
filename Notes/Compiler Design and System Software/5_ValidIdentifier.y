/*
    5. Write a YACC Program to recognize a valid variable which starts with a letter, followed by any number of letters or digits
*/

%{
    #include <stdio.h>
    int valid = 1;
%}

%token digit letter

%%
start: letter s
s: letter s | digit s | ;
%%

int yyerror() {
    printf("\nIt is not a valid identifier\n");
    valid = 0;
    return 0;
}

int main() {
    printf("\nEnter a sequence of characters to be checked as a valid identifier: ");
    yyparse();
    if(valid) {
        printf("\nIt is a valid identifier\n");
    }
}
