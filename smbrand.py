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

find = [ ]
seed = random_init()
total = 0

#while True:
for i in range(0, 0x10000):
	sys.stdout.write('Frame: %d, Rule: %d - ' % (total, total / 21))
	print(''.join([ '%02X' % it for it in seed ]))
	seed = random_advance(seed)
		#if seed in find:
		#	print('[%d] Found block!' % (i))
		#	print('#' * 60)
	total += 1
