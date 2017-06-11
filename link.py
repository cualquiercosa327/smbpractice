import sys
'''
PatchTitle:
        ldx #4
NextPatch:
        lda WorldText, x
        sta $3f8, x
        lda LevelText, x
        sta $408, x
        dex
        bpl NextPatch
        ldx #5
MorePatch:
        lda #$24
        sta $3fd, x
        sta $40d, x
        dex
        bpl MorePatch
        rts
'''
def patch_at(c, off, v):
	for i in range(0, len(v)):
		c[off+i] = v[i]

def patch_chr(c):
	c = bytearray(c)
	world = bytearray([ 0x20, 0x18, 0x1b, 0x15, 0x0d ] + ([ 0x24 ] * 6))
	level = bytearray([ 0x15, 0x0e, 0x1f, 0x0e, 0x15 ] + ([ 0x24 ] * 6))
	rule = bytearray([ 0x1b, 0x1e, 0x15, 0x0e, 0x24 ])

	patch_at(c, 0x1fb8, world)
	patch_at(c, 0x1fc8, level)
	patch_at(c, 0x1fd6, rule)

	return c

print('Building INES image from output...')

prg = open('smb.bin', 'rb').read()

if len(prg) > 0x8000:
	print('Too big prg rom by %d bytes' % (len(prg) - 0x8000))
	sys.exit(-1)

ines = open('ines.bin', 'rb').read()
gfx = patch_chr(open('smb-org.nes', 'rb').read()[len(ines)+0x8000:])

interrupts = prg[-6:]
prg = prg[:-6]
pad = bytearray([ 0xEA ] * (0x8000 - (len(prg) + len(interrupts))))

print('Adding %d bytes of padding before interrupts...' % (len(pad)))

open('smb-hack.nes', 'wb').write(ines + prg + pad + interrupts + gfx)



