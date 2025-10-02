def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro! Divisão por zero."
    return a / b

def calcular():
    print("Operações disponíveis:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")

    escolha = input("Escolha a operação (1/2/3/4): ")

    if escolha in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Por favor, insira números válidos.")
            return

        if escolha == '1':
            print(f'{num1} + {num2} = {somar(num1, num2)}')
        elif escolha == '2':
            print(f'{num1} - {num2} = {subtrair(num1, num2)}')
        elif escolha == '3':
            print(f'{num1} * {num2} = {multiplicar(num1, num2)}')
        elif escolha == '4':
            print(f'{num1} / {num2} = {dividir(num1, num2)}')
    else:
        print("Escolha inválida.")

if __name__ == "__main__":
    calcular()
