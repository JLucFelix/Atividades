#Exercício 1 Prova A
class Fatura:
    def __init__(self, nmr_item: int, descricao: str, quantidade: int, preco: float):
        self.nrm_item = nmr_item
        self.descricao = descricao
        self.quantidade = quantidade
        self.preco = preco
        if self.quantidade < 1:
            self.quantidade == (float(0)) 
        else:
            pass
        if self.preco < 1:
            self.preco == float(0)
    def calcular_valor_total(self):
        calculo = self.quantidade * self.preco
        return (f"O valor da fatura é {calculo:.2f}")
    

fatura1 = Fatura(432, "Lanchonete", 0, 5.90)
print(fatura1.calcular_valor_total())


#Exercício 2 Prova A
class Empregado:
    def __init__(self, p_nome: str, s_nome:str, salario_mensal: float):
        self.p_nome = p_nome
        self.s_nome = s_nome
        self.salario_mensal = salario_mensal
        if self.salario_mensal < 1:
            self.quantidade == float(0)
        else:
            pass
    def Exibir_salario_mensal(self):
        return (f"Empregado: {self.p_nome} {self.s_nome}, salario {self.salario_mensal:.3f}")
    
    def Exibir_salario_anual(self):
        return (f"O salario anual é {self.salario_mensal * 12:.3f}")
    
    
    def Aumento(self):
        aumento = (self.salario_mensal * 0.20)
        self.salario_mensal += aumento
        return (f"O aumento foi de {aumento:.3f}")
        

empregado3 = Empregado("Jesus", "Alan", 2.000)
print(empregado3.Exibir_salario_anual())
print(empregado3.Aumento())
print(empregado3.Exibir_salario_mensal())

#Exercício 2 Prova B

class Produto:
    def __init__(self, nome: str, preco: float, quantidade_estoque: int):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

        if self.quantidade_estoque < 1:
            raise ValueError("Quantidade insuficiente do produto")
        if self.preco < 1:
            self.preco = float(0)

class Pedido:
    def __init__(self):
        self.itens = []
        self.pagamento = None

    def add_itens(self, produto: Produto, quantidade: int):
        if quantidade > produto.quantidade_estoque:
            raise ValueError(f"Quantidade solicitada para {produto.nome} excede o estoque.")
        else:
            self.itens.append((produto, quantidade))

    def calcular_total(self):
        total = 0
        for produto, quantidade in self.itens:
            total += produto.preco * quantidade
        return total

    def definir_pagamento(self):
        pagamento = input("Defina o método de pagamento. 1 = Dinheiro, 2 = Cheque, 3 = Cartão: ")
        if pagamento == '1':
            self.pagamento = "Dinheiro"
        elif pagamento == '2':
            self.pagamento = "Cheque"
        elif pagamento == '3':
            self.pagamento = "Cartão"
        else:
            raise ValueError("Método de pagamento inválido!")

    def exibir_pedido(self):
        itens_detalhes = ', '.join([f"{quantidade}x {produto.nome}" for produto, quantidade in self.itens])
        total = self.calcular_total()
        return f"O pedido dos itens ({itens_detalhes}) foi realizado com sucesso. Forma de pagamento: {self.pagamento}. Total: R$ {total:.2f}"


produto1 = Produto("Banana", 3.0, 5)
produto2 = Produto("Maçã", 2.5, 10)

# Criando o pedido
pedido1 = Pedido() 
pedido1.add_itens(produto1, 3)  
pedido1.add_itens(produto2, 5)  


pedido1.definir_pagamento()  
print(pedido1.exibir_pedido())

#Exercício 3 prova B

class Pessoa:
    def __init__(self, nome, idade, pai: 'Pessoa' = None, mae: 'Pessoa'=None):
        self.nome = nome
        self.pai = pai
        self.idade = idade
        self.mae = mae
    def __str__(self):
        return self.nome


avo_flora = Pessoa("Flora", 80)
pai_Fernando = Pessoa("Fernando",64)
mae_Rose = Pessoa("Rose", 56, mae=avo_flora)
Eu = Pessoa("Jean Lucas", 18, pai_Fernando, mae_Rose)
print(f"Eu {Eu} sou filho do meu pai {Eu.pai} e da minha mãe {Eu.mae}, que por sua vez é filha da minha avó {Eu.mae.mae} ")

#Exercício 2 Prova C
class Produto:
    def _init_(self, nome: str, preco_u: float, quantidade: int):
        self.nome = nome
        self.preco_u = preco_u
        self.quantidade = quantidade

    def calcular_total(self):
        return self.preco_u * self.quantidade

    def aplicar_desconto(self):
        preco_total = self.calcular_total()
        if 11 <= self.quantidade < 20:
            desconto = 0.10  
        elif 21 <= self.quantidade < 50:
            desconto = 0.15 
        elif self.quantidade >= 50:
            desconto = 0.20
        else:
            desconto = 0
        return preco_total * (1 - desconto)

def adicionar_produto(lista, produto):
    lista.append(produto)


lista_produtos = []
adicionar_produto(lista_produtos, Produto("Arroz", 5.50, 10))
adicionar_produto(lista_produtos, Produto("Feijão", 7.00, 15))
adicionar_produto(lista_produtos, Produto("Macarrão", 3.00, 30))
adicionar_produto(lista_produtos, Produto("Óleo", 8.50, 5))
adicionar_produto(lista_produtos, Produto("Açúcar", 4.20, 60))

for produto in lista_produtos:
    preco_total_sem_desconto = produto.calcular_total()
    preco_total_com_desconto = produto.aplicar_desconto()
    print(f"Produto: {produto.nome}, Preço Unitário: R${produto.preco_u:.2f}, "
          f"Quantidade: {produto.quantidade}, Total: R${preco_total_sem_desconto:.2f}, "
          f"Total com desconto: R${preco_total_com_desconto:.2f}")

#Exercício 3 Prova C

class Divisao_conta:
    def _init_(self, quantidade_pessoas: int, valor_sem_garcon: float, dez_do_garcon: bool):
        self.quantidade_pessoas = quantidade_pessoas
        self.valor_sem_garcon = valor_sem_garcon
        self.dez_do_garcon = dez_do_garcon

    def calcular_garcon(self):
        return self.valor_sem_garcon * 0.10

    def exibir(self):
        if self.dez_do_garcon:
            valor_total = self.valor_sem_garcon + self.calcular_garcon()
        else:
            valor_total = self.valor_sem_garcon
        valor_por_pessoa = valor_total / self.quantidade_pessoas
        return (f"\nO total a ser pago é de R${valor_total:.2f}, dividido entre {self.quantidade_pessoas} pessoas. "
                f"Cada pessoa paga R${valor_por_pessoa:.2f}.")

conta1 = Divisao_conta(2, 400, True)
print(conta1.exibir()) 

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#EXERCICIO 1 LISTA 3
class Ingresso:
    def __init__(self, valor: float):
        self.valor = valor

    def Retornar_valor(self):
        return self.valor

class VIP(Ingresso):
    def valor_VIP(self):
        valor_vip = self.valor + (self.valor * 0.075) 
        return f"Valor VIP: R$ {valor_vip:.2f}"

class Normal(Ingresso):
    def valor_normal(self):
        return f"Valor Normal: R$ {self.valor:.2f}"

class Camarote_inferior(VIP):
    def __init__(self, valor, local: str):
        super().__init__(valor)  
        self.local = local

    def Exibir_local(self):
        return f"Local: {self.local}, {self.valor_VIP()}"

class Camarote_superior(VIP):
    def __init__(self, valor, local: str):
        super().__init__(valor)  
        self.local = local

    def valor_VIP_SUP(self):
        valor_vip_sup = self.valor + (self.valor * 0.075) + (self.valor * 0.025)  
        return f"Valor VIP Superior: R$ {valor_vip_sup:.2f}, Local: {self.local}"


ticket_vip = VIP(100.00)
print(ticket_vip.valor_VIP())  

ticket_normal = Normal(100.00)
print(ticket_normal.valor_normal())  

camarote_inferior = Camarote_inferior(200.00, "Setor A")
print(camarote_inferior.Exibir_local())  

camarote_superior = Camarote_superior(200.00, "Setor B")
print(camarote_superior.valor_VIP_SUP())

#EXERCICIO 2 LISTA 3

class Imovel:
    def __init__(self, endereco: str, preco_base: float):
        self.endereco = endereco
        self.preco_base = preco_base
    def Exibir_preco(self, preco_final: float):
        self.preco_final = preco_final
        return self.preco_base, self.preco_final
class Novo(Imovel):
    def __init__(self, endereco, preco_base):
        super().__init__(endereco, preco_base)
        self.preco_final = self.preco_base + (self.preco_base* 0.20)
    def Exibir_preco(self):
        return f"Endereço: {self.endereco}, preço final(novo): R${self.preco_final:.3f}"
class Usado(Imovel):
    def __init__(self, endereco, preco_base):
        super().__init__(endereco, preco_base)
        self.preco_final = self.preco_base - (self.preco_base* 0.50)
    def Exibir_preco(self):
        return f"Endereço: {self.endereco}, preço final(usado): R${self.preco_final:.3f}"

imovel_novo = Novo("Rua Doutor Montanha, 123", 250.000)
print(imovel_novo.Exibir_preco())

imovel_usado = Usado("Rua uahdiuhaud, 234", 250.000)
print(imovel_usado.Exibir_preco())

#EXERCICIO 3 LISTA 3

class Pessoa:
    def __init__(self, nome: str, endereco: str, telefone: str):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

class Fornecedor(Pessoa):
    def __init__(self, nome, endereco, telefone, valor_credito: float, valor_divida: float):
        super().__init__(nome, endereco, telefone)
        self.valor_divida = valor_divida
        self.valor_credito = valor_credito

    def Exibir_saldo(self):
        return f"Valor do saldo é: R${self.valor_credito - self.valor_divida:.2f}"

class Empregado(Pessoa):
    def __init__(self, nome, endereco, telefone, codigo_setor: int, salario_base: float, imposto: float):
        super().__init__(nome, endereco, telefone)
        self.salario_base = salario_base
        self.codigo_setor = codigo_setor
        self.imposto = imposto

    def Calcular_salario_liquido(self):
        return self.salario_base - self.imposto

class Administrador(Empregado):
    def __init__(self, nome, endereco, telefone, codigo_setor, salario_base, imposto, ajuda_de_custo: float):
        super().__init__(nome, endereco, telefone, codigo_setor, salario_base, imposto)
        self.ajuda_de_custo = ajuda_de_custo

    def Calcular_salario_liquido(self):
        salario_liquido = super().Calcular_salario_liquido() + self.ajuda_de_custo
        return salario_liquido

class Vendedor(Empregado):
    def __init__(self, nome, endereco, telefone, codigo_setor, salario_base, imposto, valor_vendas: float, comissao: float):
        super().__init__(nome, endereco, telefone, codigo_setor, salario_base, imposto)
        self.valor_vendas = valor_vendas
        self.comissao = comissao

    def Calcular_salario_liquido(self):
        salario_liquido = super().Calcular_salario_liquido() + self.valor_vendas * (1 + (self.comissao / 100))
        return salario_liquido


fornecedor1 = Fornecedor("Jean", "Rua Doutor Montanha, 61", "14997877054", 10000.00, 3000.00)
print(fornecedor1.Exibir_saldo())  

empregado1 = Empregado("Alana", "Rua Botocudos, 8534", "14885893954", 1, 5000.00, 500.00)
print(f"Salário líquido: R$ {empregado1.Calcular_salario_liquido():.2f}")  

administrador1 = Administrador("Fernando", "Rua Coronados, 666", "149960485", 2, 6000.00, 600.00, 800.00)
print(f"Salário líquido: R$ {administrador1.Calcular_salario_liquido():.2f}")  

vendedor1 = Vendedor("Cibele", "Rua Tapajós, 354", "159974843", 3, 4000.00, 400.00, 10000.00, 5.00)
print(f"Salário líquido: R$ {vendedor1.Calcular_salario_liquido():.2f}") 


