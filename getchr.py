c = open('smb-title.nes', 'rb').read()[0x10+0x8000:]
c = c[0x1ec0:]

v = ''

for it in c:
	v += '0x%02X, ' % (it)

print(v)

