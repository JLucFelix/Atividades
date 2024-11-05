#Atividade 1
from abc import abstractmethod, ABC

class Contribuinte:
    def __init__(self, nome: str, renda_bruta: float):
        self.nome = nome
        self.renda_bruta = renda_bruta 
    def calcularImposto(self):
        pass

class Pessoa_fisica(Contribuinte):
    def __init__(self, nome: str, renda_bruta: float):
        super().__init__(nome, renda_bruta)
        
    def calcularImposto(self):
        if self.renda_bruta < 1400:
            aliquota = 0
            parcela = 0
        elif self.renda_bruta <= 2100.0:
            aliquota = 0.10
            parcela = 100.00
        elif self.renda_bruta <= 2800.01:
            aliquota = 0.15
            parcela = 270.00
        elif self.renda_bruta <= 3600.0:
            aliquota = 0.25
            parcela = 500.00
        elif self.renda_bruta > 3600.01:
            aliquota = 0.30
            parcela = 700.00
        imposto = (self.renda_bruta * aliquota) - parcela
        return f"O imposto da pessoa fisica {self.nome} é de R${imposto:.2f} acrescido os respectivos impostos \n "

class Pessoa_juridica(Contribuinte):
    def __init__(self, nome: str, renda_bruta: float):
        super().__init__(nome, renda_bruta)
    def calcularImposto(self):
        return f"\nO imposto da pessoa juridica {self.nome} é de R${self.renda_bruta*0.10} acrescido os 10% "
        
    
Pessoa_juridica1 = Pessoa_juridica("Jean Lucas", 4000.0)
print(Pessoa_juridica1.calcularImposto())
Pessoa_fisica1 = Pessoa_fisica("Jean Lucas", 4000.0)
print(Pessoa_fisica1.calcularImposto())

#Atividade 2
class Remedio:
    def __init__(self, nome: str, valor: float):
        self.nome = nome
        self.valor = valor

    def obter_valor(self):
        return self.valor

class RemedioGenerico(Remedio):
    def obter_valor(self):
        return self.valor * 0.8

class RemedioMarca(Remedio):
    def __init__(self, nome, valor, marca: str):
        super().__init__(nome, valor)
        self.marca = marca

class Farmacia:
    def __init__(self):
        self.remedios_genericos = []
        self.remedios_marca = []

    def adicionar_remedio_generico(self, remedio):
        self.remedios_genericos.append(remedio)

    def adicionar_remedio_marca(self, remedio):
        self.remedios_marca.append(remedio)

    def calcular_valor_generico(self):
        return sum(remedio.obter_valor() for remedio in self.remedios_genericos)

    def calcular_valor_marca(self):
        return sum(remedio.obter_valor() for remedio in self.remedios_marca)

    def calcular_valor_total(self):
        return self.calcular_valor_generico() + self.calcular_valor_marca()

farmacia1 = Farmacia()

farmacia1.adicionar_remedio_generico(RemedioGenerico("Dipirona", 12.0))
farmacia1.adicionar_remedio_generico(RemedioGenerico("Dramin", 20.0))
farmacia1.adicionar_remedio_generico(RemedioGenerico("Mind", 34.0))

farmacia1.adicionar_remedio_marca(RemedioMarca("Novalgina", 13.0, "Marca1"))
farmacia1.adicionar_remedio_marca(RemedioMarca("Binotal", 21.0, "Marca2"))

print(f"Valor total dos remédios genéricos R${farmacia1.calcular_valor_generico():.2f}")
print(f"Valor total dos remédios de marca R${farmacia1.calcular_valor_marca():.2f}")
print(f"Valor total de todos os remédios R${farmacia1.calcular_valor_total():.2f}")

#Atividade 3


    
class Produto:
    def __init__(self, Nome: str, Preco: float):
        self.Nome = Nome
        self.Preco = Preco
    def calcular_preco(self):
        pass

class Livro(Produto):
    def __init__(self, Nome, Preco):
        super().__init__(Nome, Preco)
    def calcular_preco(self):
        return self.Preco * 0.10
class Eletronico(Produto):
    def __init__(self, Nome, Preco):
        super().__init__(Nome, Preco)
    def calcular_preco(self):
        return self.Preco * 1.15
class Roupas(Produto):
    def __init__(self, Nome, Preco, Importada: bool, Estacao: bool):
        super().__init__(Nome, Preco)
        self.Importada = Importada
        self.Estacao = Estacao
    def calcular_preco(self):
        preco_final = self.Preco
        if self.Importada == True:
            preco_final *= 1.05
        if self.Estacao == True:
            preco_final *= 0.80
        return preco_final
class Carrinho:
    def __init__(self):
        self.carrinho = []
    def adicionar_produtos(self, Produto):
        self.carrinho.append(Produto)
    def calcular_valor_total(self):
        return sum(Produto.calcular_preco() for Produto in self.carrinho)
    
Carrinho1 = Carrinho()

Carrinho1.adicionar_produtos(Livro("Cronicas de Narnia", 45.0))
Carrinho1.adicionar_produtos(Eletronico("Smartphone", 1300.0))
Carrinho1.adicionar_produtos(Roupas("Blusa Colegial", 200.0, True, True))

print(f"Valor total do carrinho é R$ {Carrinho1.calcular_valor_total():.2f}")

#Atividade 4

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    def calcular_pontuacao(self):
        pass
    def calcular_bonus(self):
        return self.salario * 0.05  

class FuncionarioVendas(Funcionario):
    def __init__(self, nome, salario, vendas, meta):
        super().__init__(nome, salario)
        self.vendas = vendas
        self.meta = meta
    def calcular_pontuacao(self):
        if self.vendas >= self.meta:
            return 100
        else:
            return int((self.vendas / self.meta) * 100)
    def calcular_bonus(self):
        bonus = super().calcular_bonus()
        if self.calcular_pontuacao() > 50:
            bonus += self.salario * 0.10 
        return bonus

class FuncionarioTecnologia(Funcionario):
    def __init__(self, nome, salario, avaliacao, prazo: bool):
        super().__init__(nome, salario)
        self.avaliacao = avaliacao
        self.prazo = prazo
    def calcular_pontuacao(self):
        return self.avaliacao
    def calcular_bonus(self):
        bonus = super().calcular_bonus()
        if self.prazo:
            bonus += self.salario * 0.09  
        return bonus

class FuncionarioAdm(Funcionario):
    def __init__(self, nome, salario, avaliacao_anual, metas: bool):
        super().__init__(nome, salario)
        self.avaliacao_anual = avaliacao_anual
        self.metas = metas

    def calcular_pontuacao(self):
        return self.avaliacao_anual

    def calcular_bonus(self):
        bonus = super().calcular_bonus()
        if self.metas:
            bonus += self.salario * 0.08  
        return bonus

class Empresa:
    def __init__(self):
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def avaliar_funcionarios(self):
        resultados = []
        for funcionario in self.funcionarios:
            pontuacao = funcionario.calcular_pontuacao()
            bonus = funcionario.calcular_bonus()
            resultados.append({
                'Nome': funcionario.nome,
                'Pontuacao': pontuacao,
                'Bonus': bonus
            })
        return resultados

empresa1 = Empresa()
empresa1.adicionar_funcionario(FuncionarioVendas("Jean Lucas", 1500.0, vendas=50, meta=50))
empresa1.adicionar_funcionario(FuncionarioTecnologia("Jean Lucas", 2000.0, avaliacao=80, prazo=True))
empresa1.adicionar_funcionario(FuncionarioAdm("Jean Lucas", 1800.0, avaliacao_anual=85, metas=True))
avaliar = empresa1.avaliar_funcionarios()

for resultado in avaliar:
    print(f"Nome do funcionário: {resultado['Nome']}, Pontuação: {resultado['Pontuacao']}, Bônus: R${resultado['Bonus']:.2f}")


#Atividade 5

class Recurso:
    def __init__(self):
        pass
    def calcular_custo_alocacao(self, dias: int):
        pass

class Humano(Recurso):
    def __init__(self, taxadiaria: float):
        super().__init__()  
        self.taxadiaria = taxadiaria
    def calcular_custo_alocacao(self, dias):
        return dias * self.taxadiaria

class Equipamento(Recurso):
    def __init__(self, taxadiaria: float, instalacao: float):
        super().__init__()  
        self.taxadiaria = taxadiaria
        self.instalacao = instalacao
    def calcular_custo_alocacao(self, dias):
        return (dias * self.taxadiaria) + self.instalacao 

class Licenca(Recurso):
    def __init__(self, taxamensal: float):
        super().__init__()  
        self.taxamensal = taxamensal
    def calcular_custo_alocacao(self, dias):
        taxa_diaria = self.taxamensal / 30  
        return dias * taxa_diaria

class Projeto:
    def __init__(self, recursos: list[Recurso]):
        self.recursos = recursos
    def calcular_custo_total(self, dias):
        custo_total = 0
        for recurso in self.recursos:  
            custo_total += recurso.calcular_custo_alocacao(dias)
        return custo_total

humano1 = Humano(300.0)
equipamento1 = Equipamento(300.0, 150.0)
licenca1 = Licenca(300.0)
recursos = [humano1, equipamento1, licenca1]
projeto1 = Projeto(recursos)

custo_total = projeto1.calcular_custo_total(10)
print("Custo total do projeto para 10 dias: R$", custo_total)
