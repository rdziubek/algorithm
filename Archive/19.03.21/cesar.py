def szyfruj(tekst, alfabet, klucz):
    wynik = ''
    dl_t, dl_a = len(tekst), len(alfabet)
    for i in range(dl_t):
        for j in range(dl_a):
            if tekst[i] == alfabet[j]:
                wynik += alfabet[(j + klucz) % dl_a]
    return wynik

print(szyfruj('testing', 'abcdefghijklmnopqrstuvxyz', 2))
