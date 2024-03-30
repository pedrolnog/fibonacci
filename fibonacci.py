def fib(qtd):
    num = [0, 1]
    for _ in range(int(qtd)):
        num.append(num[-1] + num[-2])
    return "\n".join(str(i) for i in num)

print(fib(input("Quantidade de números a serem gerados: ")))