def szyfruj(key: int, content: list):
    ciphered = []

    for ch in content:
        candidate = chr(ord(ch) + key)

        if ord(candidate) > ord('z'):
            candidate = chr(ord(candidate) - 26)
        elif ord(candidate) < ord('a'):
            candidate = chr(ord(candidate) + 26)

        ciphered.append(candidate)

    return ciphered


print(szyfruj(2, 'xyz'))

