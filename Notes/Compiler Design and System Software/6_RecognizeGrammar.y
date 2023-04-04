/*
    6. Write a YACC Program to recognize the strings of the form (a^nb^n), where n>=0.
*/


%{
    #include <stdio.h>
    #include <stdlib.h>
%}
  
%token A B NL

%%
string: S NL  { 
    printf("The given string is valid.\n");
    exit(0); 
}
;
S: A S B |
;
%%
  
int yyerror(char *msg) {
    printf("The given string is invalid.\n");
    exit(0);
}
  
int main() {
    printf("Enter any string: ");
    yyparse();
}