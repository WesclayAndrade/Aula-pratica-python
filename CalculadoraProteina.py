dieta_dia = []
total_proteina = 0
proteina_da_porcao = 0
cadastro = []

print("Seja bem vindo ao calculadora de proteina")
usuario = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))

cadastro.append({
    "nome": usuario,
    "idade": idade
})

print(f"Seja bem vindo {usuario}. Agora escolha uma das opções a seguir: ")

while True:
    print("1 - Adicionar Alimento")
    print("2 - Ver resumo da dieta")
    print("3 - Finalizar o dia")
    opcao = input("Qual a opção desejada: ")

    if opcao == '1':
       nome = input("Qual o nome do alimento: ")
       peso = float(input("Qual a quantide consumida: "))
       proteina = float(input(f"Quantas gramas de proteina {nome} tem a cada 100 gramas: "))
       proteina_da_porcao = (peso/100)* proteina
       total_proteina += proteina_da_porcao
     
       dieta_dia.append({
           "nome_ali": nome,
           'peso': peso,
           "proteina_100":proteina,
           "proteina_porcao": proteina_da_porcao,
            })
       print(f"Alimento cadastrado com sucesso.")

    elif opcao == '2':
        if len(dieta_dia) == 0:
            print("A sua lista esta vazia")
        else:
            print("\n"+ "="*20 + "RESUMO DA DIETA" + "="*20)
            for imprimir in dieta_dia:
                print("-" * 40)
                print(f"Alimento: {imprimir['nome_ali']} - Peso: {imprimir['peso']} gramas")
                print(f"Você cadastrou o alimento {imprimir['nome_ali']}, sua ingestão foi de {imprimir['peso']} gramas deste alimento que contém {imprimir['proteina_100']} proteina por porção.")
                print(f"O total de proteina desta porção é de: {imprimir['proteina_porcao']:.1f}")
                print("-" * 40)
            print(f"Total de proteina do dia: {total_proteina:.1f} g")
            print("-" * 40)
    elif opcao == '3':
        print("Obrigado por sua visita.")
        break
    else:
        print("Opção inválida.")




    
