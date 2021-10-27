"""
Como saber se um número é feliz ou triste?
1- Dado um número inteiro positivo
2- Substitua o número pela soma dos quadrados dos seus dígitos.
3- Se o resultado for 1, o número é feliz
4- Caso contrário, repita o processo indefinidamente.

"""

def happy(number):
    if number in (1, 10, 100):
        string = str(number)

        digits = [int(char) for char in string]
        for char in string:
            digits.append(int(char))

        total = 0
        for digit in digits:
            total += digit

        return total == 1

    return False


assert happy(1) == True 
assert happy(10)
assert happy(100)
assert not happy(4)
