import sys

print('Building INES image from output...')

prg = open('smb.bin', 'rb').read()

if len(prg) > 0x8000:
	print('Too big prg rom by %d bytes' % (len(prg) - 0x8000))
	sys.exit(-1)

ines = open('ines.bin', 'rb').read()
gfx = open('smb.chr', 'rb').read()

interrupts = prg[-6:]
prg = prg[:-6]
pad = bytearray([ 0xEA ] * (0x8000 - (len(prg) + len(interrupts))))

print('Adding %d bytes of padding before interrupts...' % (len(pad)))

open('smb-hack.nes', 'wb').write(ines + prg + pad + interrupts + gfx)



