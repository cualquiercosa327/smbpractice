import sys

if len(sys.argv) < 2:
	sys.exit(-1)

for it in sys.argv[1].lower():
	sys.stdout.write('$%02x, ' % (0x0a + ord(it) - ord('a')))
