#!/usr/bin/python3
for letter in range(97, 123):
    if f"{letter:c}" != 'q' and f"{letter:c}" != 'e':
        print(f"{letter:c}", end="")
