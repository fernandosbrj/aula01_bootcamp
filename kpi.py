nome = input("Digite o seu nome: ")
salario = float(input("Digite o seu salário: "))
percentual_bonus = float(input("Digite o percentual de bônus que recebeu: "))

valor_do_bonus = 1000 + salario * percentual_bonus

print(f"Olá {nome}, o seu bônus foi de {valor_do_bonus}")

