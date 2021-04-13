def cipher(key: int, content):
    result = []

    for i in range(len(content)):
        candidate: int = ord(content[i]) + key

        if candidate > ord('z'):
            candidate -= 26
        elif candidate < ord('a'):
            candidate += 26

        result.append(chr(candidate))

    return result


def cipher_custom(key: int, alphabet, content):
    result = []

    for i in range(len(content)):
        for j in range(len(alphabet)):
            if content[i] == alphabet[j]:
                result += [alphabet[(j + key) % len(alphabet)]]

    return result


print(cipher(2, 'xyz'))
print(cipher_custom(2, 'abcdefghijklmnopqrstuvwxyz', 'xyz'))
