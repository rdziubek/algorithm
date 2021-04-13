def cipher_custom(key: int, alphabet, content):
    result = []

    for i in range(len(content)):
        for j in range(len(alphabet)):
            if content[i] == alphabet[j]:
                result += [alphabet[(j + key) % len(alphabet)]]

    return result


print(cipher_custom(2, 'abcdefghijklmnopqrstuvwxyz', 'xyz'))
