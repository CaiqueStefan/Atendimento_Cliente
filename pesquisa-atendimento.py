excelente = 0
bom = 0
ruim = 0

for i in range(1, 51):
    print(f"\n--- Entrevistado {i} ---")

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    print("\nOpiniões sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opinião: "))

    if opiniao == 1:
        excelente += 1
    elif opiniao == 2:
        bom += 1
    elif opiniao == 3:
        ruim += 1
    else:
        print("Opção inválida!")

print("\n===== Resultado da pesquisa de satisfação TudoWeb =====")
print(f"Quantidade de respostas EXCELENTE: {excelente}")
print(f"Quantidade de respostas BOM: {bom}")
print(f"Quantidade de respostas RUIM: {ruim}")