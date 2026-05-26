carteira = [ ]

print("Seja bem vindo ao seu Gerenciador de Ativos.")
print("Escolha uma das opções abaixo para iniciar.")

while True:
    print("1 - Comprar atiivo (FII/Ação)")
    print("2 - Ver patrimônio total")
    print("3 - Buscar ativo específico")
    print("4 - Sair do Home Broker")
    opcao = input("Qual a opção desejada?")
    
    if opcao == '1':
        ticker= input("Escreva qual o ticker: ").upper()
        quantidade= int(input("Qual a quantidade adquirida: "))
        preco = float(input("Qual o valor pago por Ticker: "))
        total_investido = quantidade * preco
        carteira.append({
            'ticker': ticker,
            'quantidade': quantidade,
            'total_investido': total_investido
        })
        print("Cadastro efetuado com sucesso.")

    elif opcao == '2':
        if len(carteira) == 0:
            print("Nenhum ativo cadastrado ainda.")
        else: 
            soma_patrimonio = 0
            for ativo in carteira:
                print(f"O seu ativo é {ativo['ticker']} e você tem {ativo['quantidade']} dele com um total de investimento de {ativo['total_investido']} ")
                soma_patrimonio += ativo['total_investido']
            print(f"Total acumulado na carteira {soma_patrimonio:.2f} ")

    elif opcao == '3':
        buscar = input("Qual ticker você deseja buscar: ").upper()
        encontrado = False

        for procurar in carteira:
            if buscar == procurar['ticker']:
                encontrado = True
                print("Ativo encontrado.")
                print(f"Ticker: {procurar['ticker']} | Quantidade: {procurar['quantidade']} | Total: {procurar['total_investido']:.2f} ")
                break

        if encontrado == False: 
            print("Ativo não encontrado.")

    elif opcao == '4':
        print("Muito obrigado por sua visita. Até a próxima.")
        break
    else: 
        print("Opção inválida.")
    
