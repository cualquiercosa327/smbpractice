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

back = [ 0x8C, 0xC3, 0xDA, 0x5D, 0xE9, 0x52, 0x80 ]
seed = random_init()
total = 0

for i in range(0, 21):
	print(' '.join([ '%02X' % it for it in seed ]))
	seed = random_advance(seed)

for i in range(0, 21):
	print(' '.join([ '%02X' % it for it in seed ]))
	seed = random_advance(seed)

seed[0] = 0xA5
print('------------------------------')

for i in range(0, 21):
	print(' '.join([ '%02X' % it for it in seed ]))
	seed = random_advance(seed)

for i in range(0, 21):
	print(' '.join([ '%02X' % it for it in seed ]))
	seed = random_advance(seed)

