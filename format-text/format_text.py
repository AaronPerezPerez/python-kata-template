def execute(text: str) -> str:
    result = ''
    n = 0
    while n < len(text):
        c = text[n]
        if c == "<":
            while n < len(text) and text[n] != "/" and text[n] != ">":
                n += 1
            if n < len(text) and text[n] == "/":
                n += 4
            else:
                n += 1
        if n < len(text):
            result += text[n]
        n += 1

    return result
