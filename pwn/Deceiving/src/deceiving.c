#include <errno.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>

#define CALCULATE_QWORDS(bytes) (((bytes) + 7) / 8)
#define FLUSH()                                                                \
  char c;                                                                      \
  while ((c = getchar()) != '\n' && c != EOF) {                                \
  }

char *RED = NULL;
char *BLUE = NULL;
char *YELLOW = NULL;


void *list[20] = {NULL};

void setup() {
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);

  RED = strdup("\033[31m%s: %s\033[0m\n");
  BLUE = strdup("\033[33m%s: %s\033[0m\n");
  YELLOW = strdup("\033[93m%s: %s\033[0m\n");
}

uint get_int() {
  uint integer = 0;
  char input[10] = "";
  char *endptr = NULL;
  errno = 0;

  fgets(input, sizeof(input), stdin);
  input[strcspn(input, "\n")] = '\0';
  integer = strtoul(input, &endptr, 0);
  if (ERANGE == errno || *endptr != '\0') {
    perror("strtoul");
    exit(EXIT_FAILURE);
  }
  return integer;
}

void get_string(char *p, size_t sz) {
  char in;
  for (int i = 0; i < sz; i++) {
    in = fgetc(stdin);
    if (in == '\n') {
      p[i] = '\0';
      return;
    }
    p[i] = in;
  }
  FLUSH();
}

char *get_color() {
  puts("Choose a Color");
  puts("1- Red");
  puts("2- Blue");
  puts("3- Yellow");

  switch (get_int()) {
  case 1:
    return RED;
  case 2:
    return BLUE;
  case 3:
    return YELLOW;
  default:
    exit(EXIT_FAILURE);
  }
}

void menu() {
  puts("what will it be this time?");
  puts("1- create a note");
  puts("2- edit a note");
  puts("3- print a note");
  puts("4- delete a note");
  puts("5- exit");
}

void create_note() {
  size_t content_size = 0;
  void *new = NULL;
  char *note_name = NULL;
  int i = 0;

  puts("What's the size of your note in bytes?");
  content_size = CALCULATE_QWORDS(get_int()) * 8 + 8 * 3;
  new = malloc(content_size);
  *(size_t *)(new) = content_size;

  puts("What's the name of your note ? [MAX SIZE 20 bytes]");
  note_name = malloc(20);
  get_string(note_name, 20);
  *(char **)(new + content_size - 16) = note_name;

  puts("Write down your note:");
  get_string((char *)(new + 8), content_size - 24);
  *(char **)(new + content_size - 8) = get_color();

  puts("Choose an index:");
  i = get_int();

  if (i < 0 || i >= 20) {
    puts("Choose an index between 0 and 19");
    free(new);
    new = NULL;
    return;
  }
  list[i] = new;
}

void edit_note() {
  puts("Choose the index of the note that will be modified:");
  int i = get_int();
  if (i < 0 || i >= 20) {
    puts("Choose an index between 0 and 19");
    return;
  }
  if (list[i] == NULL) {
    printf("No Note at index %d\n", i);
    return;
  }
  void *note = list[i];
  size_t content_size = *(size_t *)note;
  char *note_text = (char *)(note + 8);
  puts("Write down your note:");
  get_string((char *)(note + 8), content_size - 8);
}

void print_note() {
  puts("Choose the index of the note that will be printed:");
  int i = get_int();
  if (i < 0 || i >= 20) {
    puts("Choose an index between 0 and 19");
    return;
  }
  if (list[i] == NULL) {
    printf("No Note at index %d\n", i);
    return;
  }
  void *note = list[i];
  size_t content_size = *(size_t *)note;
  char *color = *(char **)(note + content_size - 8);
  char *note_name = *(char **)(note + content_size - 16);
  char *note_text = (char *)(note + 8);

  printf(color, note_name, note_text);
}

void delete_note() {
  puts("Choose the index of the note that will be deleted:");
  int i = get_int();

  if (i < 0 || i >= 20) {
    puts("Choose an index between 0 and 19");
    return;
  }
  free(list[i]);
  list[i] = NULL;
  puts("Note deleted");
}

int main() {
  setup();
  puts("Your notes will be safe and colourful");
  while (true) {
    menu();
    switch (get_int()) {
    case 1:
      create_note();
      break;
    case 2:
      edit_note();
      break;
    case 3:
      print_note();
      break;
    case 4:
      delete_note();
      break;
    default:
      puts("Bye Bye");
      exit(EXIT_SUCCESS);
    }
  }
}
