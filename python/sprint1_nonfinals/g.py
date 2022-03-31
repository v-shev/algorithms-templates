def to_binary(number: int) -> str:
    # Здесь реализация вашего решения
    binary = []
    while number >= 1:
        binary.append(str(number % 2))
        number = number // 2

    res = ("".join(reversed(binary)))
    return res

def read_input() -> int:
    return int(input().strip())

print(to_binary(read_input()))
