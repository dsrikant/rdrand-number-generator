import sys

def dump():
    with open('verified.txt') as f:
  	l = f.readlines()
    for n in l:
#      print n
      for line in readFile(n):
        val = ["%02x" % ord(c) for c in line]
        top8bits =val[0:1]
#	print top8bits
	t = open('res.txt', 'a')
        if (int(''.join(top8bits),16)^0x00000001) == 0:
        	t.write(str(int(''.join(val), 16)) + '\n')

def readFile(fname):
#    print fname
    f = open(fname.rstrip('\n'), "rb")
    f.seek(start)
    #chunk = f.read(60-0)
    chunk = f.read()
    gap = 16 - (len(chunk) % 16)
    chunk += gap * '\000'
    while chunk:
        yield chunk[:16]
        chunk = chunk[16:]

if __name__ == '__main__':
    try:
        dump()
    except TypeError:
        dump()
