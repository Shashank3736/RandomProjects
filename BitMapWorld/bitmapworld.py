import sys

bitmap = ''
with open('BitMapWorld/bitmapworld.txt') as f:
    bitmap = f.read()

print('BitMapWorld by Shreyash Raj.')
print('Enter the message to display with the bitmap.')
message = input('> ')
if message == '':
    sys.exit()

for line in bitmap.splitlines():
    for i, bit in enumerate(line):
        if bit == ' ':
            print(' ', end='')
        else:
            print(message[i%len(message)], end='')
    print()
