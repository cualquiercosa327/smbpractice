import sys

def _ror(val, carry):
	next_carry	= bool(val & 1)
	val			= (val >> 1)
	if carry:
		val |= 0x80
	return val, next_carry

def random_init():
	return [ 0xA5 ] + ([ 0 ] * 6)

def random_advance(seed):
	carry = bool((seed[0] & 0x02) ^ (seed[1] & 0x02))

	for i in range(0, len(seed)):
		seed[i], carry = _ror(seed[i], carry)

	return seed

find = [ [ 0x6A, 0x18, 0xCC, 0xFD, 0x64, 0x9E, 0x57 ] ]
seed = random_init()
total = 0

while True:
	print('Frame rule: %d' % (total))
	for i in range(0, 21):
		seed = random_advance(seed)
		print(' '.join([ '%02X' % it for it in seed ]))
		if seed in find:
			print('[%d] Found block!' % (i))
			print('#' * 60)
			sys.exit(0)
	total += 1
