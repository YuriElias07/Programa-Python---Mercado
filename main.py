from random import choice
import re

listagem_produtos = []
vendas = []

def validar_entrada_string(entrada):
    return bool(re.search(r'[a-zA-Z]', entrada))

def menu():
    while True:
        try:
            pergunta = int(input("""Menu:
                                 
1. Cadastrar produto
2. Listar produtos disponíveis
3. Editar produto
4. Excluir produto
5. Vender produto
6. Relatórios
7. Sair

Digite aqui: """))

            if pergunta == 1:
                cadastrar_produto()
                
            elif pergunta == 2:
                listar_produtos()
                
            elif pergunta == 3:
                editar_produto()
                
            elif pergunta == 4:
                excluir_produto()
                
            elif pergunta == 5:
                vender_produto()
                
            elif pergunta == 6:
                relatorio_de_vendas()
                
            elif pergunta == 7:
                print("Saindo...")
                sorteio()
                break
                
            else:
                print("Opção inválida! Por favor, escolha as opções listadas no menu.")
                
        except:
            print("Para selecionar uma opção do menu, selecione um número inteiro.")

def cadastrar_produto():
    while True:
        try:
            produto = input("Digite o nome do produto: ").strip()
            if not validar_entrada_string(produto):
                print("O nome do produto deve conter ao menos uma letra.")
                continue
            estoque = int(input("Digite o estoque do produto: ").strip())
            preco = float(input("Digite o preço do produto: ").strip())
            if estoque < 0 or preco < 0:
                 print("Estoque e preço não podem ser negativos.")
            info_produto = (produto, estoque, preco)
            listagem_produtos.append(info_produto)
            print("Produto adicionado com sucesso!")
            break
        except:
            print("Digite algo válido.")

def listar_produtos():
    if listagem_produtos:
        for i, info_produto in enumerate(listagem_produtos):
            print(f"{i + 1}. Produto: {info_produto[0]}, Estoque: {info_produto[1]}, Preço: R${info_produto[2]:.2f}")
    else:
        print("Nenhum produto cadastrado.")

def editar_produto():
    if not listagem_produtos:
        print("Nenhum produto disponível na lista.")
        return

    listar_produtos()
    try:
        update = int(input("Digite o número do produto que deseja editar: ")) - 1
        if 0 <= update < len(listagem_produtos):
            while True:
                produto = input("Digite o novo nome do produto: ").strip()
                if not validar_entrada_string(produto):
                    print("O nome do produto deve conter ao menos uma letra.")
                    continue
                estoque = int(input("Digite o novo estoque do produto: ").strip())
                preco = float(input("Digite o novo preço do produto: ").strip())
                if estoque < 0 or preco < 0:
                    print("Estoque e preço não podem ser negativos.")
                info_produto = (produto, estoque, preco)
                listagem_produtos[update] = info_produto
                print("Produto editado com sucesso!")
                break
        else:
            print("Número do produto inválido!")
    except:
        print("Por favor, digite um número válido.")

def excluir_produto():
    if not listagem_produtos:
        print("Nenhum produto disponível para excluir.")
        return

    listar_produtos()
    try:
        excluir = int(input("Digite o número do produto que deseja excluir: ")) - 1
        if 0 <= excluir < len(listagem_produtos):
            del listagem_produtos[excluir]
            print("Produto excluído com sucesso!")
        else:
            print("Número do produto inválido!")
    except:
        print("Por favor, digite um número válido.")

def vender_produto():
    if not listagem_produtos:
        print("Nenhum produto disponível para venda.")
        return

    try:
        nome_cliente = input("Digite o nome do cliente: ").strip()
        if not validar_entrada_string(nome_cliente):
            print("O nome do cliente deve conter ao menos uma letra.")
            return
    except:
        print("Por favor, digite um nome válido.")
        return

    itens_comprados = []
    valor_total = 0
    
    while True:
        listar_produtos()
        try:
            item = int(input("Digite o número do produto que deseja comprar: ")) - 1
            quantidade = int(input("Digite a quantidade: "))
            if 0 <= item < len(listagem_produtos):
                produto, estoque, preco = listagem_produtos[item]
                if quantidade <= estoque:
                    valor_total += preco * quantidade
                    itens_comprados.append((produto, quantidade, preco))
                    listagem_produtos[item] = (produto, estoque - quantidade, preco)
                else:
                    print(f"Estoque insuficiente para o produto {produto}.")
            else:
                print("Número do produto inválido!")
        except:
            print("Por favor, digite um número válido.")
            continue

        try:
            continuar = int(input("""
                Deseja adicionar mais produtos?
                    1 - Sim 
                    2 - Não  """))
            if continuar == 2:
                break
            elif continuar != 1:
                print("Opção inválida. Digite 1 para Sim ou 2 para Não.")
        except:
            print("Por favor, digite um número válido.")

    vendas.append({"cliente": nome_cliente, "itens": itens_comprados, "valor_total": valor_total})
    print(f"Venda realizada com sucesso! Valor total: R${valor_total:.2f}")

def relatorio_de_vendas():
    if not vendas:
        print("Nenhuma venda registrada.")
        return

    total_vendas = sum(venda["valor_total"] for venda in vendas)
    compra_mais_cara = max(vendas, key=lambda v: v["valor_total"])
    compra_mais_barata = min(vendas, key=lambda v: v["valor_total"])

    print(f"Valor total de vendas no dia: R${total_vendas:.2f}")
    print(f"Compra mais cara: Cliente: {compra_mais_cara['cliente']}, Valor: R${compra_mais_cara['valor_total']:.2f}")
    print(f"Compra mais barata: Cliente: {compra_mais_barata['cliente']}, Valor: R${compra_mais_barata['valor_total']:.2f}")

def sorteio():
    if vendas:
        clientes = [venda["cliente"] for venda in vendas]
        ganhador = choice(clientes)
        print(f"O ganhador do sorteio de R$1000,00 é: {ganhador}")
    else:
        print("Nenhum cliente registrado para o sorteio.")

menu()
