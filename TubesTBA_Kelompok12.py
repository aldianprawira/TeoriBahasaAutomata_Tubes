import sys


def VALID_IF(input_str):
    input_str += "@"
    word = list(input_str)

    state = "q1"

    rows = ["q1", "q2", "q3", "q4"]
    columns = ["i", "f", "selain", "EOS"]

    transition_table = [["" for _ in range(9)] for _ in range(9)]

    transition_table[0][0] = "q2"
    transition_table[0][1] = "q4"
    transition_table[0][2] = "q4"
    transition_table[0][3] = "error"

    transition_table[1][0] = "q4"
    transition_table[1][1] = "q3"
    transition_table[1][2] = "q4"
    transition_table[1][3] = "error"

    transition_table[2][0] = "q4"
    transition_table[2][1] = "q4"
    transition_table[2][2] = "q4"
    transition_table[2][3] = "accept"

    transition_table[3][0] = "q4"
    transition_table[3][1] = "q4"
    transition_table[3][2] = "q4"
    transition_table[3][3] = "error"

    i = 0
    b, k = 0, 0  # Baris dan kolom

    while state != "accept":
        symbol = word[i]
        if symbol == "i":
            input_symbol = "i"
        elif symbol == "f":
            input_symbol = "f"
        elif symbol == "@":
            input_symbol = "EOS"
        else:
            return False

        for j in range(len(rows)):
            if rows[j] == state:
                b = j

        for j in range(len(columns)):
            if columns[j] == input_symbol:
                k = j

        state = transition_table[b][k]
        if state == "error":
            return False

        i += 1

    return state == "accept"


def VALID_ELSE(input_str):
    input_str += "@"
    word = list(input_str)

    state = "q1"

    rows = ["q1", "q2", "q3", "q4", "q5", "q6"]
    columns = ["e", "l", "s", "selain", "EOS"]

    transition_table = [["" for _ in range(9)] for _ in range(9)]

    transition_table[0][0] = "q2"
    transition_table[0][1] = "q6"
    transition_table[0][2] = "q6"
    transition_table[0][3] = "q6"
    transition_table[0][4] = "q6"

    transition_table[1][0] = "q6"
    transition_table[1][1] = "q3"
    transition_table[1][2] = "q6"
    transition_table[1][3] = "q6"
    transition_table[1][4] = "q6"

    transition_table[2][0] = "q6"
    transition_table[2][1] = "q6"
    transition_table[2][2] = "q4"
    transition_table[2][3] = "q6"
    transition_table[2][4] = "q6"

    transition_table[3][0] = "accept"
    transition_table[3][1] = "q6"
    transition_table[3][2] = "q6"
    transition_table[3][3] = "q6"
    transition_table[3][4] = "q6"

    transition_table[4][0] = "q6"
    transition_table[4][1] = "q6"
    transition_table[4][2] = "q6"
    transition_table[4][3] = "q6"
    transition_table[4][4] = "q6"

    transition_table[5][0] = "q6"
    transition_table[5][1] = "q6"
    transition_table[5][2] = "q6"
    transition_table[5][3] = "q6"
    transition_table[5][4] = "q6"

    i = 0
    b, k = 0, 0  # Baris dan kolom

    symbol = word[i]
    while symbol != "@":
        if symbol == "e":
            input_symbol = "e"
        elif symbol == "l":
            input_symbol = "l"
        elif symbol == "s":
            input_symbol = "s"
        elif symbol == "@":
            input_symbol = "EOS"
        else:
            return False

        for j in range(len(rows)):
            if rows[j] == state:
                b = j

        for j in range(len(columns)):
            if columns[j] == input_symbol:
                k = j

        # print(b, k)
        state = transition_table[b][k]
        if state == "error":
            return False

        i += 1
        symbol = word[i]

    return state == "accept"


def VALID_aksi1(input_str):
    input_str += "@"
    word = list(input_str)

    state = "q1"

    rows = ["q1", "q2", "q3", "q4", "q5", "q6"]
    columns = ["x", "+", "=", "1", "selain", "EOS"]

    transition_table = [["" for _ in range(9)] for _ in range(9)]

    transition_table[0][0] = "q2"
    transition_table[0][1] = "q6"
    transition_table[0][2] = "q6"
    transition_table[0][3] = "q6"
    transition_table[0][4] = "q6"
    transition_table[0][5] = "error"

    transition_table[1][0] = "q6"
    transition_table[1][1] = "q3"
    transition_table[1][2] = "q6"
    transition_table[1][3] = "q6"
    transition_table[1][4] = "q6"
    transition_table[1][5] = "error"

    transition_table[2][0] = "q6"
    transition_table[2][1] = "q6"
    transition_table[2][2] = "q4"
    transition_table[2][3] = "q6"
    transition_table[2][4] = "q6"
    transition_table[2][5] = "error"

    transition_table[3][0] = "q6"
    transition_table[3][1] = "q3"
    transition_table[3][2] = "q6"
    transition_table[3][3] = "q5"
    transition_table[3][4] = "q6"
    transition_table[3][5] = "error"

    transition_table[4][0] = "q6"
    transition_table[4][1] = "q6"
    transition_table[4][2] = "q6"
    transition_table[4][3] = "q6"
    transition_table[4][4] = "q6"
    transition_table[4][5] = "accept"

    transition_table[5][0] = "q6"
    transition_table[5][1] = "q6"
    transition_table[5][2] = "q6"
    transition_table[5][3] = "q6"
    transition_table[5][4] = "q6"
    transition_table[5][5] = "error"

    i = 0
    b, k = 0, 0  # Baris dan kolom

    while state != "accept":
        symbol = word[i]
        if symbol == "x":
            input_symbol = "x"
        elif symbol == "+":
            input_symbol = "+"
        elif symbol == "=":
            input_symbol = "="
        elif symbol == "1":
            input_symbol = "1"
        elif symbol == "@":
            input_symbol = "EOS"
        else:
            return False

        for j in range(len(rows)):
            if rows[j] == state:
                b = j

        for j in range(len(columns)):
            if columns[j] == input_symbol:
                k = j

        state = transition_table[b][k]
        if state == "error":
            return False

        i += 1

    return state == "accept"


def VALID_aksi2(input_str):
    input_str += "@"
    word = list(input_str)

    state = "q1"

    rows = ["q1", "q2", "q3", "q4", "q5", "q6"]
    columns = ["y", "+", "=", "1", "selain", "EOS"]

    transition_table = [["" for _ in range(9)] for _ in range(9)]

    transition_table[0][0] = "q2"
    transition_table[0][1] = "q6"
    transition_table[0][2] = "q6"
    transition_table[0][3] = "q6"
    transition_table[0][4] = "q6"
    transition_table[0][5] = "error"

    transition_table[1][0] = "q6"
    transition_table[1][1] = "q3"
    transition_table[1][2] = "q6"
    transition_table[1][3] = "q6"
    transition_table[1][4] = "q6"
    transition_table[1][5] = "error"

    transition_table[2][0] = "q6"
    transition_table[2][1] = "q6"
    transition_table[2][2] = "q4"
    transition_table[2][3] = "q6"
    transition_table[2][4] = "q6"
    transition_table[2][5] = "error"

    transition_table[3][0] = "q6"
    transition_table[3][1] = "q3"
    transition_table[3][2] = "q6"
    transition_table[3][3] = "q5"
    transition_table[3][4] = "q6"
    transition_table[3][5] = "error"

    transition_table[4][0] = "q6"
    transition_table[4][1] = "q6"
    transition_table[4][2] = "q6"
    transition_table[4][3] = "q6"
    transition_table[4][4] = "q6"
    transition_table[4][5] = "accept"

    transition_table[5][0] = "q6"
    transition_table[5][1] = "q6"
    transition_table[5][2] = "q6"
    transition_table[5][3] = "q6"
    transition_table[5][4] = "q6"
    transition_table[5][5] = "error"

    i = 0
    b, k = 0, 0  # Baris dan kolom

    while state != "accept":
        symbol = word[i]
        if symbol == "y":
            input_symbol = "y"
        elif symbol == "+":
            input_symbol = "+"
        elif symbol == "=":
            input_symbol = "="
        elif symbol == "1":
            input_symbol = "1"
        elif symbol == "@":
            input_symbol = "EOS"
        else:
            return False

        for j in range(len(rows)):
            if rows[j] == state:
                b = j

        for j in range(len(columns)):
            if columns[j] == input_symbol:
                k = j

        state = transition_table[b][k]
        if state == "error":
            return False

        i += 1

    return state == "accept"


def VALID_kurawalAwal(input_str):
    input_str += "@"
    word = list(input_str)

    state = "q1"

    rows = ["q1", "q2", "q3"]
    columns = ["{", "selain", "EOS"]

    transition_table = [["" for _ in range(5)] for _ in range(5)]

    transition_table[0][0] = "q2"
    transition_table[0][1] = "q3"
    transition_table[0][2] = "error"

    transition_table[1][0] = "q3"
    transition_table[1][1] = "q3"
    transition_table[1][2] = "accept"

    transition_table[2][0] = "q3"
    transition_table[2][1] = "q3"
    transition_table[2][2] = "error"

    i = 0
    b, k = 0, 0  # Baris dan kolom

    while state != "accept":
        symbol = word[i]
        if symbol == "{":
            input_symbol = "{"
        elif symbol == "@":
            input_symbol = "EOS"
        else:
            return False

        for j in range(len(rows)):
            if rows[j] == state:
                b = j

        for j in range(len(columns)):
            if columns[j] == input_symbol:
                k = j

        state = transition_table[b][k]
        if state == "error":
            return False

        i += 1

    return state == "accept"


def VALID_kurawalAkhir(input_str):
    input_str += "@"
    word = list(input_str)

    state = "q1"

    rows = ["q1", "q2", "q3"]
    columns = ["}", "selain", "EOS"]

    transition_table = [["" for _ in range(5)] for _ in range(5)]

    transition_table[0][0] = "q2"
    transition_table[0][1] = "q3"
    transition_table[0][2] = "error"

    transition_table[1][0] = "q3"
    transition_table[1][1] = "q3"
    transition_table[1][2] = "accept"

    transition_table[2][0] = "q3"
    transition_table[2][1] = "q3"
    transition_table[2][2] = "error"

    i = 0
    b, k = 0, 0  # Baris dan kolom

    while state != "accept":
        symbol = word[i]
        if symbol == "}":
            input_symbol = "}"
        elif symbol == "@":
            input_symbol = "EOS"
        else:
            return False

        for j in range(len(rows)):
            if rows[j] == state:
                b = j

        for j in range(len(columns)):
            if columns[j] == input_symbol:
                k = j

        state = transition_table[b][k]
        if state == "error":
            return False

        i += 1

    return state == "accept"


def VALID_kurangDari(input_str):
    input_str += "@"
    word = list(input_str)

    state = "q1"

    rows = ["q1", "q2", "q3"]
    columns = ["<", "selain", "EOS"]

    transition_table = [["" for _ in range(5)] for _ in range(5)]

    transition_table[0][0] = "q2"
    transition_table[0][1] = "q3"
    transition_table[0][2] = "error"

    transition_table[1][0] = "q3"
    transition_table[1][1] = "q3"
    transition_table[1][2] = "accept"

    transition_table[2][0] = "q3"
    transition_table[2][1] = "q3"
    transition_table[2][2] = "error"

    i = 0
    b, k = 0, 0  # Baris dan kolom

    while state != "accept":
        symbol = word[i]
        if symbol == "<":
            input_symbol = "<"
        elif symbol == "@":
            input_symbol = "EOS"
        else:
            return False

        for j in range(len(rows)):
            if rows[j] == state:
                b = j

        for j in range(len(columns)):
            if columns[j] == input_symbol:
                k = j

        state = transition_table[b][k]
        if state == "error":
            return False

        i += 1

    return state == "accept"


def VALID_lebihDari(input_str):
    input_str += "@"
    word = list(input_str)

    state = "q1"

    rows = ["q1", "q2", "q3"]
    columns = [">", "selain", "EOS"]

    transition_table = [["" for _ in range(5)] for _ in range(5)]

    transition_table[0][0] = "q2"
    transition_table[0][1] = "q3"
    transition_table[0][2] = "error"

    transition_table[1][0] = "q3"
    transition_table[1][1] = "q3"
    transition_table[1][2] = "accept"

    transition_table[2][0] = "q3"
    transition_table[2][1] = "q3"
    transition_table[2][2] = "error"

    i = 0
    b, k = 0, 0  # Baris dan kolom

    while state != "accept":
        symbol = word[i]
        if symbol == ">":
            input_symbol = ">"
        elif symbol == "@":
            input_symbol = "EOS"
        else:
            return False

        for j in range(len(rows)):
            if rows[j] == state:
                b = j

        for j in range(len(columns)):
            if columns[j] == input_symbol:
                k = j

        state = transition_table[b][k]
        if state == "error":
            return False

        i += 1

    return state == "accept"


def VALID_kurangDariSamaDengan(input_str):
    input_str += "@"
    word = list(input_str)

    state = "q1"

    rows = ["q1", "q2", "q3", "q4"]
    columns = ["<", "=", "selain", "EOS"]

    transition_table = [["" for _ in range(9)] for _ in range(9)]

    transition_table[0][0] = "q2"
    transition_table[0][1] = "q4"
    transition_table[0][2] = "q4"
    transition_table[0][3] = "error"

    transition_table[1][0] = "q4"
    transition_table[1][1] = "q3"
    transition_table[1][2] = "q4"
    transition_table[1][3] = "error"

    transition_table[2][0] = "q4"
    transition_table[2][1] = "q4"
    transition_table[2][2] = "q4"
    transition_table[2][3] = "accept"

    transition_table[3][0] = "q4"
    transition_table[3][1] = "q4"
    transition_table[3][2] = "q4"
    transition_table[3][3] = "error"

    i = 0
    b, k = 0, 0  # Baris dan kolom

    while state != "accept":
        symbol = word[i]
        if symbol == "<":
            input_symbol = "<"
        elif symbol == "=":
            input_symbol = "="
        elif symbol == "@":
            input_symbol = "EOS"
        else:
            return False

        for j in range(len(rows)):
            if rows[j] == state:
                b = j

        for j in range(len(columns)):
            if columns[j] == input_symbol:
                k = j

        state = transition_table[b][k]
        if state == "error":
            return False

        i += 1

    return state == "accept"


def VALID_lebihDariSamaDengan(input_str):
    input_str += "@"
    word = list(input_str)

    state = "q1"

    rows = ["q1", "q2", "q3", "q4"]
    columns = [">", "=", "selain", "EOS"]

    transition_table = [["" for _ in range(9)] for _ in range(9)]

    transition_table[0][0] = "q2"
    transition_table[0][1] = "q4"
    transition_table[0][2] = "q4"
    transition_table[0][3] = "error"

    transition_table[1][0] = "q4"
    transition_table[1][1] = "q3"
    transition_table[1][2] = "q4"
    transition_table[1][3] = "error"

    transition_table[2][0] = "q4"
    transition_table[2][1] = "q4"
    transition_table[2][2] = "q4"
    transition_table[2][3] = "accept"

    transition_table[3][0] = "q4"
    transition_table[3][1] = "q4"
    transition_table[3][2] = "q4"
    transition_table[3][3] = "error"

    i = 0
    b, k = 0, 0  # Baris dan kolom

    while state != "accept":
        symbol = word[i]
        if symbol == ">":
            input_symbol = ">"
        elif symbol == "=":
            input_symbol = "="
        elif symbol == "@":
            input_symbol = "EOS"
        else:
            return False

        for j in range(len(rows)):
            if rows[j] == state:
                b = j

        for j in range(len(columns)):
            if columns[j] == input_symbol:
                k = j

        state = transition_table[b][k]
        if state == "error":
            return False

        i += 1

    return state == "accept"


def VALID_tidakSamaDengan(input_str):
    input_str += "@"
    word = list(input_str)

    state = "q1"

    rows = ["q1", "q2", "q3", "q4"]
    columns = ["!", "=", "selain", "EOS"]

    transition_table = [["" for _ in range(9)] for _ in range(9)]

    transition_table[0][0] = "q2"
    transition_table[0][1] = "q4"
    transition_table[0][2] = "q4"
    transition_table[0][3] = "error"

    transition_table[1][0] = "q4"
    transition_table[1][1] = "q3"
    transition_table[1][2] = "q4"
    transition_table[1][3] = "error"

    transition_table[2][0] = "q4"
    transition_table[2][1] = "q4"
    transition_table[2][2] = "q4"
    transition_table[2][3] = "accept"

    transition_table[3][0] = "q4"
    transition_table[3][1] = "q4"
    transition_table[3][2] = "q4"
    transition_table[3][3] = "error"

    i = 0
    b, k = 0, 0  # Baris dan kolom

    while state != "accept":
        symbol = word[i]
        if symbol == "!":
            input_symbol = "!"
        elif symbol == "=":
            input_symbol = "="
        elif symbol == "@":
            input_symbol = "EOS"
        else:
            return False

        for j in range(len(rows)):
            if rows[j] == state:
                b = j

        for j in range(len(columns)):
            if columns[j] == input_symbol:
                k = j

        state = transition_table[b][k]
        if state == "error":
            return False

        i += 1

    return state == "accept"


def VALID_a(input_str):
    input_str += "@"
    word = list(input_str)

    state = "q1"

    rows = ["q1", "q2", "q3"]
    columns = ["a", "selain", "EOS"]

    transition_table = [["" for _ in range(5)] for _ in range(5)]

    transition_table[0][0] = "q2"
    transition_table[0][1] = "q3"
    transition_table[0][2] = "error"

    transition_table[1][0] = "q3"
    transition_table[1][1] = "q3"
    transition_table[1][2] = "accept"

    transition_table[2][0] = "q3"
    transition_table[2][1] = "q3"
    transition_table[2][2] = "error"

    i = 0
    b, k = 0, 0  # Baris dan kolom

    while state != "accept":
        symbol = word[i]
        if symbol == "a":
            input_symbol = "a"
        elif symbol == "@":
            input_symbol = "EOS"
        else:
            return False

        for j in range(len(rows)):
            if rows[j] == state:
                b = j

        for j in range(len(columns)):
            if columns[j] == input_symbol:
                k = j

        state = transition_table[b][k]
        if state == "error":
            return False

        i += 1

    return state == "accept"


def VALID_b(input_str):
    input_str += "@"
    word = list(input_str)

    state = "q1"

    rows = ["q1", "q2", "q3"]
    columns = ["b", "selain", "EOS"]

    transition_table = [["" for _ in range(5)] for _ in range(5)]

    transition_table[0][0] = "q2"
    transition_table[0][1] = "q3"
    transition_table[0][2] = "error"

    transition_table[1][0] = "q3"
    transition_table[1][1] = "q3"
    transition_table[1][2] = "accept"

    transition_table[2][0] = "q3"
    transition_table[2][1] = "q3"
    transition_table[2][2] = "error"

    i = 0
    b, k = 0, 0  # Baris dan kolom

    while state != "accept":
        symbol = word[i]
        if symbol == "b":
            input_symbol = "b"
        elif symbol == "@":
            input_symbol = "EOS"
        else:
            return False

        for j in range(len(rows)):
            if rows[j] == state:
                b = j

        for j in range(len(columns)):
            if columns[j] == input_symbol:
                k = j

        state = transition_table[b][k]
        if state == "error":
            return False

        i += 1

    return state == "accept"


def VALID_c(input_str):
    input_str += "@"
    word = list(input_str)

    state = "q1"

    rows = ["q1", "q2", "q3"]
    columns = ["c", "selain", "EOS"]

    transition_table = [["" for _ in range(5)] for _ in range(5)]

    transition_table[0][0] = "q2"
    transition_table[0][1] = "q3"
    transition_table[0][2] = "error"

    transition_table[1][0] = "q3"
    transition_table[1][1] = "q3"
    transition_table[1][2] = "accept"

    transition_table[2][0] = "q3"
    transition_table[2][1] = "q3"
    transition_table[2][2] = "error"

    i = 0
    b, k = 0, 0  # Baris dan kolom

    while state != "accept":
        symbol = word[i]
        if symbol == "c":
            input_symbol = "c"
        elif symbol == "@":
            input_symbol = "EOS"
        else:
            return False

        for j in range(len(rows)):
            if rows[j] == state:
                b = j

        for j in range(len(columns)):
            if columns[j] == input_symbol:
                k = j

        state = transition_table[b][k]
        if state == "error":
            return False

        i += 1

    return state == "accept"


def VALID_x(input_str):
    input_str += "@"
    word = list(input_str)

    state = "q1"

    rows = ["q1", "q2", "q3"]
    columns = ["a", "b", "c", "selain", "EOS"]

    transition_table = [["" for _ in range(5)] for _ in range(5)]

    transition_table[0][0] = "q2"
    transition_table[0][1] = "q2"
    transition_table[0][2] = "q2"
    transition_table[0][3] = "q3"
    transition_table[0][4] = "error"

    transition_table[1][0] = "q3"
    transition_table[1][1] = "q3"
    transition_table[1][2] = "q3"
    transition_table[1][3] = "q3"
    transition_table[1][3] = "accept"

    transition_table[1][0] = "q3"
    transition_table[1][1] = "q3"
    transition_table[1][2] = "q3"
    transition_table[1][3] = "q3"
    transition_table[1][3] = "error"

    i = 0
    b, k = 0, 0  # Baris dan kolom

    while state != "accept":
        symbol = word[i]
        if symbol == "c":
            input_symbol = "c"
        elif symbol == "b":
            input_symbol = "b"
        elif symbol == "a":
            input_symbol = "a"
        elif symbol == "@":
            input_symbol = "EOS"
        else:
            return False

        for j in range(len(rows)):
            if rows[j] == state:
                b = j

        for j in range(len(columns)):
            if columns[j] == input_symbol:
                k = j

        state = transition_table[b][k]
        if state == "error":
            return False

        i += 1

    return state == "accept"


def get_lexic(word):
    if VALID_IF(word):
        return "1"
    elif VALID_ELSE(word):
        return "2"
    elif VALID_aksi1(word):
        return "3"
    elif VALID_aksi2(word):
        return "4"
    elif VALID_kurawalAwal(word):
        return "5"
    elif VALID_kurawalAkhir(word):
        return "6"
    elif VALID_kurangDari(word):
        return "7"
    elif VALID_lebihDari(word):
        return "8"
    elif VALID_tidakSamaDengan(word):
        return "9"
    elif VALID_a(word):
        return "10"
    elif VALID_b(word):
        return "11"
    elif VALID_c(word):
        return "12"
    else:
        return "error"


def dolA(sentence):
    lexes = []
    input_words = sentence.split()

    for word in input_words:
        lexes.append(get_lexic(word))

    lexes.append("@")
    return lexes


sentence = input("Enter a sentence: ")
lexes = dolA(sentence)

lexicalArray = []
for lex in lexes:
    lexicalArray.append(lex)
    if lex == "@":
        break
    print(lex, end=" ")

#########################################################################################
# PDA dari CFG
#########################################################################################

err = False
lexes = []
input_words = sentence.split()

for word in input_words:
    lex = get_lexic(word)
    if lex == "error":
        err = True


if err == False:
    # Membuat array kosong
    characters = []

    # Memasukkan setiap karakter ke dalam array tanpa spasi
    for character in sentence:
        if character != " ":
            characters.append(character)

    stack = []
    # Stack[-1] ->top of stack
    remaining = []
    # remaining[0] ->top of remaining

    remaining.extend(characters)  # Copy dari array character

    print("\n")
    print("remaining", remaining)

    state = "i"
    stack.append("#")
    state = "p"
    stack.append("S")
    state = "q"
    sentence = sentence.split()
    error = False

    structure = lexicalArray[::-1]
    structure.pop(0)

    print("structure", structure, "\n")

    while stack[-1] != "#" and error != True:
        top_of_stack = stack[-1]
        symbol = remaining[0]
        token = structure[-1]

        if top_of_stack == "S":
            if symbol == "i":
                stack.pop()
                stack.extend(
                    ["G", "D", "F", "E", "G", "C", "F", "B", "A"]
                )  # Push ABCEC
            else:
                print("Error")
                error = True
        print(stack)

        if top_of_stack == "A":
            if symbol == "i":
                stack.pop()
                structure.pop(-1)
                stack.extend(["f", "i"])  # Push(if)
            else:
                print("Error")
                error = True

        if top_of_stack == "B":
            if symbol == "a":
                stack.pop()
                structure.pop(-1)
                stack.extend(["Y", "Z", "X"])  # Push(x<y)
            elif symbol == "Z":
                stack.pop()
                structure.pop(-1)
                stack.extend(["Y", "Z", "X"])  # Push(x<y)
            elif symbol == "Y":
                stack.pop()
                structure.pop(-1)
                stack.extend(["Y", "Z", "X"])  # Push(x<y)
            else:
                print("Error")
                error = True

        if top_of_stack == "C":
            if symbol == "x":
                stack.pop()
                structure.pop(-1)
                stack.extend(["1", "=", "+", "x"])  # Push({D})
            else:
                print("Error")
                error = True

        if top_of_stack == "D":
            if symbol == "y":
                stack.pop()
                structure.pop(-1)
                stack.extend(["1", "=", "+", "y"])  # Push({D})
            else:
                print("Error")
                error = True

        if top_of_stack == "E":
            if symbol == "e":
                stack.pop()
                structure.pop(-1)
                stack.extend(["e", "s", "l", "e"])  # Push(else)
            else:
                print("Error")
                error = True

        if top_of_stack == "F":
            if symbol == "{":
                stack.pop()
                stack.extend(["{"])
            else:
                print("Error")
                error = True

        if top_of_stack == "G":
            if symbol == "}":
                stack.pop()
                stack.extend(["}"])
            else:
                print("Error")
                error = True

        if top_of_stack == "X":
            if symbol == "a":
                stack.pop()
                structure.pop(-1)
                stack.extend(["a"])  # Push(x<y)
            elif symbol == "b":
                stack.pop()
                structure.pop(-1)
                stack.extend(["b"])  # Push(x<y)
            elif symbol == "c":
                stack.pop()
                structure.pop(-1)
                stack.extend(["c"])  # Push(x<y)
            else:
                print("Error")
                error = True

        if top_of_stack == "Y":
            if symbol == "a":
                stack.pop()
                structure.pop(-1)
                stack.extend(["a"])  # Push(x<y)
            elif symbol == "b":
                stack.pop()
                structure.pop(-1)
                stack.extend(["b"])  # Push(x<y)
            elif symbol == "c":
                stack.pop()
                structure.pop(-1)
                stack.extend(["c"])  # Push(x<y)
            else:
                print("Error")
                error = True

        if top_of_stack == "Z":
            if symbol == "<":
                stack.pop()
                structure.pop(-1)
                stack.extend(["<"])  # Push(x<y)
            elif symbol == "b":
                stack.pop()
                structure.pop(-1)
                stack.extend([">"])  # Push(x<y)
            elif symbol == "c":
                stack.pop()
                structure.pop(-1)
                stack.extend(["!="])  # Push(x<y)
            else:
                print("Error")
                error = True

        if top_of_stack == "i":
            if symbol == "i":
                stack.pop()
                remaining.pop(0)
            else:
                print("Error")
                error = True

        if top_of_stack == "f":
            if symbol == "f":
                stack.pop()
                remaining.pop(0)
            else:
                print("Error")
                error = True

        if top_of_stack == "x":
            if symbol == "x":
                stack.pop()
                remaining.pop(0)
            else:
                print("Error")
                error = True

        if top_of_stack == "<":
            if symbol == "<":
                stack.pop()
                remaining.pop(0)
            else:
                print("Error")
                error = True

        if top_of_stack == ">":
            if symbol == ">":
                stack.pop()
                remaining.pop(0)
            else:
                print("Error")
                error = True

        if top_of_stack == "y":
            if symbol == "y":
                stack.pop()
                remaining.pop(0)
            else:
                print("Error")
                error = True

        if top_of_stack == "{":
            if symbol == "{":
                stack.pop()
                remaining.pop(0)
            else:
                print("Error")
                error = True

        if top_of_stack == "+":
            if symbol == "+":
                stack.pop()
                remaining.pop(0)
            else:
                print("Error")
                error = True

        if top_of_stack == "}":
            if symbol == "}":
                stack.pop()
                remaining.pop(0)
            else:
                print("Error")
                error = True

        if top_of_stack == "e":
            if symbol == "e":
                stack.pop()
                remaining.pop(0)
            else:
                print("Error")
                error = True

        if top_of_stack == "l":
            if symbol == "l":
                stack.pop()
                remaining.pop(0)
            else:
                print("Error")
                error = True

        if top_of_stack == "s":
            if symbol == "s":
                stack.pop()
                remaining.pop(0)
            else:
                print("Error")
                error = True

        if top_of_stack == "a":
            if symbol == "a":
                stack.pop()
                remaining.pop(0)
            else:
                print("Error")
                error = True

        if top_of_stack == "b":
            if symbol == "b":
                stack.pop()
                remaining.pop(0)
            else:
                print("Error")
                error = True

        if top_of_stack == "c":
            if symbol == "c":
                stack.pop()
                remaining.pop(0)
            else:
                print("Error")
                error = True

        if top_of_stack == "!=":
            if symbol == "!=":
                stack.pop()
                remaining.pop(0)
            else:
                print("Error")
                error = True
        if top_of_stack == "+":
            if symbol == "+":
                stack.pop()
                remaining.pop(0)
            else:
                print("Error")
                error = True

        if top_of_stack == "=":
            if symbol == "=":
                stack.pop()
                remaining.pop(0)
            else:
                print("Error")
                error = True

        if top_of_stack == "1":
            if symbol == "1":
                stack.pop()
                remaining.pop(0)
            else:
                print("Error")
                error = True

        print("stack", stack)
        print("remaining", remaining, "\n")

    if len(stack) == 1:
        state = "f"
    stack.pop()
    print(top_of_stack)
    print(state)
    if state == "f":
        print("Valid Input")
    else:
        print("Invalid Input")
