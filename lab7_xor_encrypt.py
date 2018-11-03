def xor_encrypt(text, key):
    ciphertext = []
    j = 0
    for i in range(0, len(text)):
        if j >= len(key):
            j = j % len(key)
        ciphertext.append(chr(ord(text[i]) ^ ord(key[j])))
        # ciphertext.append(ord(text[i]) ^ ord(key[j]))
        j += 1
    return ''.join(ciphertext)
    #return ciphertext


def xor_decryt(ciphertext, key):
    text = []
    j = 0
    for i in range(0, len(ciphertext)):
        if j >= len(key):
            j = j % len(key)
        text.append(chr(ord(ciphertext[i]) ^ ord(key[j])))
        # text.append(ord(ciphertext[i] ^ ord(key[j])))
        j += 1
    return ''.join(text)


key = 'asvg'
text = '1235'
ciphertext = xor_encrypt(text, key)
print(ciphertext)
text = xor_decryt(ciphertext, key)
print(text)