def sorting_for_decrypt_steep1(tokenText, n):
    decrypted_text = [x[:] for x in tokenText]
    for i in range(len(decrypted_text)):
        for j in range(len(decrypted_text[i]) - n):
            temp = decrypted_text[i][j]
            decrypted_text[i][j] = decrypted_text[i][j + n]
            decrypted_text[i][j + n] = temp
    return decrypted_text


def sorting_for_decrypt_steep2(tokenText: list[list[int]], n: int) -> list[list[int]]:
    decrypted_result = []
    for i in range(0, len(tokenText), 2):
        decrypted_result.append(tokenText[i])
    return sorting_for_decrypt_steep1([decrypted_result], n)


def custom_decrypt(tokenText: list[list[int]], n: int) -> list[list[int]]:
    for i in range(len(tokenText)):
        for j in range(len(tokenText[i])):
            tokenText[i][j] -= n
    return tokenText


def level2_decrypt(tokenText: list[list[int]]) -> list[list[int]]:
    for i in range(len(tokenText)):
        tokenText[i].reverse()
    return tokenText


def level3_decrypt(tokenText: list[list[int]]) -> list[list[int]]:
    for i in range(len(tokenText)):
        tokenText[i] = [x // 2 for x in tokenText[i]]
    return tokenText
