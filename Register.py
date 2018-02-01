print("Bem Vindo")
print("Menu:\n1 = Cadastro Médico\n2 = Cadastro Escolar\n3 = Criador da Aplicação")
opcao = input("\nDigite a opção desejada: ")
if opcao == '1':
    print("Bem vindo ao Cadastro Médico")
    print("Opções:\n1 = Cadastrar Idoso\n2 = Cadastrar Crianças")
    escolha = input('\nEscolha a opção de cadastro: ')
    if escolha == '1':
        print('\nBem vindo ao Cadastro do Idoso!')
        nome = str(input('\nDigite o nome do Idoso: '))
        idade = int(input('Digite a idade do Idoso: '))
        altura = float(input('Digite a altura do Idoso: '))
        peso = float(input('Digite o peso do Idoso: '))
        cpf = str(input('Digite o cpf do Idoso: '))
        rg = str(input('Digite o Rg do Idoso: '))
        print('\nNome do idoso é', nome, 'Sua idade', idade, 'Sua altura', altura, 'Seu peso é', peso, 'Seu cpf é', cpf, 'seu rg é', rg,'?')
        correto = input('\nEstá correto? S/N: ')
        if correto == 'S':
            print('\nSim está correto!')
        else:
            print('\nNão está correto!')
    if escolha == '2':
        print('\nBem vindo ao Cadastro da Criança!')
        nome2 = str(input('\nDigite o nome da Criança: '))
        idade2 = int(input('Digite a idade do Criança: '))
        altura2 = float(input('Digite a altura do Criança: '))
        peso2 = float(input('Digite o peso do Criança: '))
        rg2 = str(input('Digite o Rg do Criança: '))
        print('\nNome da Criança é', nome2, 'Sua idade', idade2, 'Sua altura', altura2, 'Seu peso é', peso2, 'Seu rg é', rg2,'?')
        correto2 = input('\nEstá correto? S/N: ')
        if correto2 == 'S':
            print('\nCadastrado!')
        else:
            print('\nNão Cadastrado!')
elif opcao == '2':
    print('Bem vindo ao Cadastro Escolar')
    print('Opções:\n1 = Cadastrar Crianças\n2 = Cadastrar Adolescente')
    escolha2 = input('\nEscolha a opção de Cadastro: ')
    if escolha2 == '1':
        print('\nBem vindo ao Cadastro da Criança')
        nome3 = str(input('\nDigite o nome da Criança: '))
        idade3 = int(input('Digite a idade do Criança: '))
        altura3 = float(input('Digite a altura do Criança: '))
        peso3 = float(input('Digite o peso do Criança: '))
        rg3 = str(input('Digite o Rg do Criança: '))
        print('\nNome da Criança é', nome3, 'Sua idade', idade3, 'Sua altura', altura3, 'Seu peso é', peso3, 'Seu rg é',rg3,'?')
        correto3 = input('\nEstá correto? S/N: ')
        if correto3 == 'S':
            print('\nCadastrado!')
        else:
            print('\nNão Cadastrado!')
    if escolha2 == '2':
        print('\nBem vindo ao Cadastro do Adolescente')
        nome4 = str(input('\nDigite o nome da Criança: '))
        idade4 = int(input('Digite a idade do Criança: '))
        altura4 = float(input('Digite a altura do Criança: '))
        peso4 = float(input('Digite o peso do Criança: '))
        rg4 = str(input('Digite o Rg do Criança: '))
        print('\nNome da Criança é', nome4, 'Sua idade', idade4, 'Sua altura', altura4, 'Seu peso é', peso4, 'Seu rg é',rg4,'?')
        correto4 = input('\nEstá correto? S/N: ')
        if correto4 == 'S':
            print('\nCadastrado!')
        else:
            print('\nNão Cadastrado!')
elif opcao == '3':
    print('\nCRIADOR DA APLICAÇÃO:\n\nJOAS ANTONIO DOS SANTOS')
    print('\nEQUIPE 29SECURITY\n')
    lista_nomes = ['']
    lista_nomes.append('JOAS')
    print(lista_nomes[1])
    lista_nomes.append('ALEX')
    print(lista_nomes[2])
    lista_nomes.append('CARLOS')
    print(lista_nomes[3])