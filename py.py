import math

#must have even length
def hash(s, length):
    length = math.floor(length/2)
    strlen = len(s)
    slope = length / strlen
    h = [0 for i in range(length)]
    for i in range(strlen):
        hi = math.floor(slope * i)
        n = ord(s[i])
        h[hi] = h[hi] ^ n
    return h 

if __name__ == "__main__":
    hashes = []
    for i in range(97, 97 + 26):
        for j in range(97, 97 + 26):
            for k in range(97, 97+26):
                s = ascii(i) + ascii(j) + ascii(k)
                h = hash(s,4)
                hashstr = ""
                for l in h:
                    if l < 16:
                        hashstr += "0" + hex(l)[2:]
                    else:
                        hashstr += hex(l)[2:]
                hashes.append(hashstr)

    print("done")
    print(hashes)
