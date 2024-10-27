#include <stdio.h>
#include <stdlib.h>

void setup() {
  setbuf(stdin, 0LL);
  setbuf(stdout, 0LL);
  setbuf(stderr, 0LL);
}

void yap() {
  char story[20];
  fgets(story, 1000, stdin);
}

int main() {
  setup();
  puts("I love stories!!");
  puts("I love listening to people talking about their day or what they are "
       "passionate about");
  puts("Therefore i made this simple program so that you can tell me all about "
       "yourself");
  puts("You can tell me everything don't worry if it's too long, i'll read it "
       "all");
  printf("I'll go first, my favorite function is system @ %p i love using it "
         "when pwning\n",
         &system);
  puts("Someday i'll tell you all my secrets that are located in this file: "
       "flag.txt ");

  yap();
}
