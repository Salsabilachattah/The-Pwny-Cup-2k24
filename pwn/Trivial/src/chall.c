#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>


char* chunks[10];
int sizes[10];

void setup(){
    setvbuf(stderr, 0LL, 2, 0LL);
    setvbuf(stdin, 0LL, 2, 0LL);
    setvbuf(stdout, 0LL, 2, 0LL);
}

int menu(){
    int choice;
    puts("1. Create");
    puts("2. Delete");
    puts("3. Show");
    puts("4. Edit");
    puts("5. Exit");
    printf("choice: ");
    scanf("%d",&choice);
    return choice ;
}

void welcome(){
    puts("Welcome To My Pwn Challenge");
    puts("Let's see what can you do without hooks");
}

void create(){
    int idx;
    int size;

    printf("index: ");
    scanf("%d",&idx);

    if (idx<0 || idx >=10){
        puts("Index out of range.");
        exit(-1);
    }

    printf("size: ");
    scanf("%d",&size);

    if (size<0 || size>=0x1000){
        puts("Size out of range.");
        exit(-1);
    }

    char* chk = malloc(size);
    if (chk==NULL){
        printf("Memory Error, exiting ...");
        exit(-1);
    }

    chunks[idx] = chk ;
    sizes[idx] = size ;

}

void delete(){

    int idx;

    printf("index: ");
    scanf("%d",&idx);

    if (idx<0 || idx >=10){
        puts("Index out of range.");
        exit(-1);
    }

    free(chunks[idx]);
}

void show(){
    int idx;

    printf("index: ");
    scanf("%d",&idx);

    if (idx<0 || idx >=10){
        puts("Index out of range.");
        exit(-1);
    }

    printf("Content: ");
    write(1,chunks[idx],sizes[idx]);
    printf("\n");
}

void edit(){

    int idx;

    printf("index: ");
    scanf("%d",&idx);

    if (idx<0 || idx >=10){
        puts("Index out of range.");
        exit(-1);
    }

    printf("Content: ");
    if (chunks[idx]){
        read(0,chunks[idx],sizes[idx]);
    } else {
        puts("Invalid Index");
    }

}

int main(){
    setup();
    
    welcome();

    while (1){

        switch(menu()){

            case 1:
                create();
                break ;
            case 2:
                delete();
                break ;
            case 3:
                show();
                break;
            case 4:
                edit();
                break;
            
            default:
                return 0 ;
        }

    }
    return 0 ;
}