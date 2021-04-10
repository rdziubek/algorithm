def cipher(key: int, content: list):
    ciphered = []

    for ch in content:
        candidate: int = ord(ch) + key

        if candidate > ord('z'):
            candidate -= 26
        elif candidate < ord('a'):
            candidate += 26

        ciphered.append(chr(candidate))

    return ciphered


print(cipher(2, list('xyz')))