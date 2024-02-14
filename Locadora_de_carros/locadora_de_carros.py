import os

carros = [
    ("GOL Bolinha TURBAO", 150),
    ("PUNTO Venom TUNADO", 190)
]

carros_alugados = []

def mostrar_lista_de_carros(portifolio):
    for c, car in enumerate(portifolio):
        print(f"[{c}] {car[0]} - R$ {car[1]} /dia")

mostrar_lista_de_carros(carros)

while True:
    os.system("cls")
    print("0 para PORTIFÓLIO | 1 para ALUGAR | 2 para DEVOLVER")
    opcao = int(input())

    os.system("cls")
    if opcao == 0:
        mostrar_lista_de_carros(carros)

    elif opcao == 1:
        mostrar_lista_de_carros(carros)
        print("="*15)
        cod_car = int(input("Escolha o código do carro: "))
        dias = int(input("Por quantos dias? "))
        os.system("cls")

        print(f"Você escolheu {carros[cod_car][0]} por {dias} dias")
        print(f"O aluguel totaliza em R$ {dias*carros[cod_car][1]}. Deseja alugar?")

        print("0 - SIM | 1 - NÃO")
        conf = int(input())
        if conf == 0:
            print(f"Parabéns! Você alugou o {carros[cod_car][0]} por {dias} dias.")
            carros_alugados.append(carros.pop(cod_car))

    elif opcao == 2:
        if len(carros_alugados) == 0:
            print("Não há carros para devolver")
        else:
            print("segue a lista dos carros alugados. Qual você deseja devolver?")
            mostrar_lista_de_carros(carros_alugados)
            print("")
            print("Escolha o código do carro que deseja devolver: ")
            cod = int(input())
            if conf == 0:
                print(f"Obrigado por devolver o carro {carros_alugados[cod][0]}")
                carros.append(carros_alugados.pop(cod))

    print("")
    print("=====================================")
    print("Digite 0 para CONTINUAR | 1 para SAIR")
    if float(input()) == 1:
        print("Obrigado, Volte sempre!")
        break
        