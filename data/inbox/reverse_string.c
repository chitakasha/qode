#include <stdio.h>
#include <string.h>

// A function that swaps two characters
void swap(char *a, char *b) {
  char temp = *a;
  *a = *b;
  *b = temp;
}

// A function that reverses a string in place
void reverse(char *str) {
  // Get the length of the string
  int len = strlen(str);
  // Loop from both ends of the string and swap characters
  for (int i = 0; i < len / 2; i++) {
    swap(&str[i], &str[len - i - 1]);
  }
}
