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


print(cipher(2, 'xyz'))
