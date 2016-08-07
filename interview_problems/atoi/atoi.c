#include <string.h>
#include <stdio.h>

int digit_to_int(char c) {
    return c - '0';
}

int is_digit(char c) {
    if (c >= '0' && c <= '9') {
	return 1;
    } else {
	return 0;
    }
}

int atoi(char *buf) {
    int out = 0;
    for (char *ptr = buf; *ptr != '\n'; ptr++) {
	if (!is_digit(*ptr))
	    return 0;
	out += digit_to_int(*ptr);
	out *= 10;
    }
    return out / 10;
}

int main() {
    char *buf[100];
    int converted;
    while (1) {
	puts("gimme a num to atoi:\n");
	fgets(buf, sizeof(buf), stdin);
	converted = atoi(buf);
	printf("value: %d\n", converted);
    }
    return 1;
}
