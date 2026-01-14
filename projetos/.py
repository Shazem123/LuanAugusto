
cidades = ['Recife', 'Fortaleza', 'Teresina', 'Salvador', 'Nova Iorque']

def listagem():
    for numero, nome in enumerate(cidades, start=1):
        print(f"Cidade nº{numero}: {nome}")

print('Bem vindo à lista de cidades!')

while True:
    escolha = input('Deseja ver a lista de cidades (1), adicionar cidades (2) ou remover cidades (3)? ').lower()
    print(f'Digite "q" para sair.')

    if escolha == '1':
        listagem()

    elif escolha == '2':
        cidade = input('Nome da cidade: ')
        cidades.append(cidade)
        print(f"Cidade {cidade} adicionada com sucesso! Veja a lista para verificar.")

    elif escolha == 'q':
        print("Fechando o programa.")
        break

    elif escolha == '3':
        listagem()
        n = int(input(f"Escolha o número da cidade: "))
        cidades.pop(n-1)
        print(f"Cidade nº {n} removida com sucesso! Veja a lista para verificar.")
        
    else:
        print("Opção inválida. Tente novamente.")

        

        
    
    