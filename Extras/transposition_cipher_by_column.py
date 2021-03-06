"""
    KRYPT
    OANAL   ;   2, 1, 4, 0, 3   ->  YNARAZTLKOIPA
    IZA

O(n) — matrix transposition (√n by √n)
"""


def cipher(key: list, text):
    cols = len(key)

    if len(text) % cols != 0:
        rows = len(text) // cols + 1
    else:
        rows = len(text) // cols

    matrix = [['' for _ in range(cols)] for _ in range(rows)]

    k = 0
    for row in range(rows):
        for col in range(cols):
            if k < len(text):
                matrix[row][col] = text[k]
                k += 1
            else:
                matrix[row][col] = ''

    result = []
    for col in range(cols):
        for row in range(rows):
            if matrix[row][key[col]] != '':
                result += matrix[row][key[col]]
    return result


"""EVALUATION"""
cipher(
    key=[2, 1, 4, 0, 3],
    text='KRYPTOANALIZA'
)
