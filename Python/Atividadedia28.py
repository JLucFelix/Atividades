LISTA 2 

from abc import ABC, abstractmethod
from datetime import datetime, timedelta
#EXERCICIO 1 
class Reserva_Hotel:
    def __init__(self, Hospede: 'Hospede', nmrQ: int, valor_diaria: float, dias:int):
        self.Hospede = Hospede
        self.nmrQ = nmrQ
        self.valor_diaria = valor_diaria
        self.dias = dias
    def Calcular_custo_total(self):
        return (f"O valor total da diaria do quarto nmrº {self.nmrQ} do hospede {self.Hospede.nome} de cpf {self.Hospede.cpf}, é R$ {self.valor_diaria * self.dias}, referente aos {self.dias} decorridos.")

class Hospede:
    def __init__(self, nome: str, cpf: str, data_nascimento: str, idade: int):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.idade = idade 
    def RetornaIdade(self):
        return (f"A idade é {self.idade} anos")

hospede1 = Hospede("Jean Lucas", "553.780.458-19", "7/2/2006", 18)
reserva1 = Reserva_Hotel(hospede1, 14, float(600), 2)
print(hospede1.RetornaIdade())
print(reserva1.Calcular_custo_total())

#EXERCICIO 2 
class Cliente:
    def __init__(self, nome: str, endereco: str, lista_favoritos: list):
        self.nome = nome
        self.endereco = endereco
        self.lista_favoritos = lista_favoritos

    def criar_lista_favoritos(self, restaurante):
        self.lista_favoritos.append(restaurante.nome_estabelecimento)
        return f"Os favoritos são: {self.lista_favoritos}"

    def retornar_info(self):
        return f"Cliente {self.nome}, endereço {self.endereco}"


class Pedido:
    def __init__(self, cliente: Cliente, lista_itens: list[dict]):
        self.lista_itens = lista_itens
        self.cliente = cliente

    def adicionar_itens(self, item_nome: str, item_valor: float):
        self.lista_itens.append({"Nome": item_nome, "Valor": item_valor})

    def valor_total(self):
        soma = 0
        for item in self.lista_itens:
            soma += item.get("Valor")
        return soma


class Restaurante:
    def __init__(self, nome_estabelecimento: str, lista_pedido: list[Pedido]):
        self.nome_estabelecimento = nome_estabelecimento
        self.lista_pedido = lista_pedido

    def criar_pedido(self, pedido: Pedido):
        self.lista_pedido.append(pedido)



cliente1 = Cliente("Jean Lucas", "Rua Tapajos", [])
pedido1 = Pedido(cliente1, [{"Nome": 'Pão', 'Valor': 4}, {"Nome": 'Refri', 'Valor': 4}])
restaurante1 = Restaurante("Bocada", [pedido1])
pedido1.adicionar_itens("Banana", 5)
print(f"Valor total do pedido: {pedido1.valor_total()}")
print(cliente1.retornar_info())

#EXERCICIO 3
from datetime import datetime

class Projeto:
    def __init__(self, nome_projeto: str, data_inicio: datetime, lista_membros: list):
        self.nome_projeto = nome_projeto
        self.data_inicio = data_inicio
        self.lista_membros = lista_membros

    def exibir_detalhes(self):
        return f"Projeto de nome {self.nome_projeto}, data de início {self.data_inicio}, membros {self.lista_membros}"

    def add_membros(self, membro: 'Membros'):
        self.lista_membros.append({'Nome': membro.nome_membro, 'Email': membro.email})

    def duracao(self, data_termino: datetime):
        return data_termino - self.data_inicio


class Membros:
    def __init__(self, nome_membro: str, email: str):
        self.nome_membro = nome_membro
        self.email = email

membro1 = Membros("Jean Lucas", "jeanlucas.email")
projeto1 = Projeto("Alpha", datetime(2024, 10, 1), [])
projeto1.add_membros(membro1)
print(projeto1.exibir_detalhes())
data_fim = datetime(2024, 12, 1)
print(f"Duração do projeto: {projeto1.duracao(data_fim).days} dias")

#EXERCICIO 4

class Tarefa:
    def __init__(self, descricao: str, data_criacao: datetime, status: bool):
        self.descricao = descricao
        self.data_criacao = data_criacao
        self.status = status
        self.data_termino = None  

    def concluir(self, data_termino: datetime):
        self.data_termino = data_termino
        self.status = True  
        return "Atividade concluída"

    def exibir_detalhes(self):
        if self.status:
            if self.data_termino and self.data_termino > self.data_criacao + timedelta(days=30):
                status = "Concluída"
            else:
                status = "Atrasada"
        else:
            status = "Não concluída"
        
        return f"Atividade '{self.descricao}', criada no dia {self.data_criacao}, status: {status}"


tarefa1 = Tarefa("Atividade de programação", datetime(2024, 10, 1), False)
print(tarefa1.exibir_detalhes())
tarefa1.concluir(datetime(2024, 1, 30))
print(tarefa1.exibir_detalhes())

#EXERCICIO 5
class MetodoPagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor: float):
        pass
    def Realizar_Pagamento(self, valor:float):
        return self.processar_pagamento(valor)
class Pix(MetodoPagamento):
    def processar_pagamento(self, valor):
        return f"Pagamento de R${valor:.2f} por Pix"
class Cartao_debito(MetodoPagamento):
    def processar_pagamento(self, valor):
        return f"Pagamento de R${valor:.2f} por Cartão de Debito"
class Cartao_credito(MetodoPagamento):
    def processar_pagamento(self, valor):
        return f"Pagamento de R${valor:.2f} por Cartão de Credito"

valorcompra = 100.0
pix_pagamento = Pix()
print(pix_pagamento.Realizar_Pagamento(valorcompra))
debito = Cartao_debito()
print(debito.Realizar_Pagamento(valorcompra))
cartão = Cartao_credito()
print(cartão.Realizar_Pagamento(valorcompra))

#EXERCICIO 6

from datetime import datetime

class Estacionamento:
    def __init__(self, taxa: float, placa: str, marca: str, modelo: str, hora_chegada: datetime):
        self.taxa = taxa
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.hora_chegada = hora_chegada

class Carro(Estacionamento):
    def __init__(self, taxa: float, placa: str, marca: str, modelo: str, hora_chegada: datetime, hora_saida: datetime):
        super().__init__(taxa, placa, marca, modelo, hora_chegada)
        self.hora_saida = hora_saida
    def Calcular_taxa(self):
        diferenca = self.hora_saida - self.hora_chegada
        horas_totais = diferenca.total_seconds() / 3600
        return (f"Total da taxa por hora no estacionamento é de R${horas_totais * self.taxa:.2f}, "
                f"equivalente a {horas_totais:.2f} horas")

class Moto(Estacionamento):
    def __init__(self, taxa: float, placa: str, marca: str, modelo: str, hora_chegada: datetime, hora_saida: datetime):
        super().__init__(taxa, placa, marca, modelo, hora_chegada)
        self.hora_saida = hora_saida
    def Calcular_taxa(self):
        diferenca = self.hora_saida - self.hora_chegada
        horas_totais = diferenca.total_seconds() / 3600
        return (f"Total da taxa por hora no estacionamento é de R${horas_totais * self.taxa:.2f}, "
                f"equivalente a {horas_totais:.2f} horas")

class VUC(Estacionamento):
    def __init__(self, taxa: float, placa: str, marca: str, modelo: str, hora_chegada: datetime, hora_saida: datetime):
        super().__init__(taxa, placa, marca, modelo, hora_chegada)
        self.hora_saida = hora_saida
    def Calcular_taxa(self):
        diferenca = self.hora_saida - self.hora_chegada
        horas_totais = diferenca.total_seconds() / 3600
        return (f"Total da taxa por hora no estacionamento é de R${horas_totais * self.taxa:.2f}, "
                f"equivalente a {horas_totais:.2f} horas")

carro1 = Carro(5.0, "ABC1234", "Fusca", "Fusca", datetime(2024,10,1,10,0), datetime(2024,10,1,15,0))
print(carro1.Calcular_taxa())
moto1 = Moto(2.5, "XYZ5678", "Honda", "CB500", datetime(2024,10,1,10,0), datetime(2024,10,1,15,0))
print(moto1.Calcular_taxa())
vuc1 = VUC(12.0, "VUC1010", "Mercedes", "Sprinter", datetime(2024,10,1,10,0), datetime(2024,10,1,15,0))
print(vuc1.Calcular_taxa())

-----------------------------------------------------------------------------------------------------------------------
from abc import ABC, abstractmethod

#Exercicio 1

class Pagamento(ABC):
    @abstractmethod
    def processar_pagamento(self):
        pass
class PagamentoCartao(Pagamento):
    def __init__(self, valor: float):
        self.valor = valor
    def processar_pagamento(self):
        return f"Compra aprovada no cartão de crédito. No valor de R${self.valor}"
class PagamentoBoleto(Pagamento):
    def __init__(self, valor: float):
        self.valor = valor
    def processar_pagamento(self):
        return f"Compra aprovada via Boleto. No valor de R${self.valor}"

pagamento_cartao = PagamentoCartao(450.0)
print(pagamento_cartao.processar_pagamento())
pagamento_boleto = PagamentoBoleto(450.0)
print(pagamento_boleto.processar_pagamento())

#Exercicio 2

class Veiculo(ABC):
    def __init__(self, modelo: str, ano:int):
        self.modelo = modelo
        self.ano = ano
    @abstractmethod
    def acelerar(self):
        pass 
    @abstractmethod
    def freiar(self):
        pass
class Carro(Veiculo):
    def __init__(self, modelo, ano):
        super().__init__(modelo, ano)
    def acelerar(self):
        return "O carro acelerou"
    def freiar(self):
        return "O carro freiou"

class Moto(Veiculo):
    def __init__(self, modelo, ano):
        super().__init__(modelo, ano)
    def acelerar(self):
        return "A moto acelerou"
    def freiar(self):
        return "A moto freiou"

class Caminhao(Veiculo):
    def __init__(self, modelo, ano):
        super().__init__(modelo, ano)
    def acelerar(self):
        return "O caminhão acelerou"
    def freiar(self):
        return "O caminhão freiou"
    
carro1 = Carro("Tiguan", 2012)
print(carro1.freiar())
print(carro1.acelerar())
moto1 = Moto("Tornado", 2005)
print(moto1.acelerar())
print(moto1.freiar())
caminhao1 = Caminhao("Scania 111",2004)
print(caminhao1.acelerar())
print(caminhao1.freiar())

#Exercicio 3

class Acomodacao(ABC):
    def __init__(self, preco_dia: float, nome_acomodacao: str, nmrDias: int):
        self.preco_dia = preco_dia
        self.nome_acomodacao = nome_acomodacao
        self.nmrDias = nmrDias
        self.valor_servico = 0  
        self.taxa = 0  

    def Servicos(self, servico: str, valor_servico: float, taxa: float):
        self.servico = servico
        self.valor_servico = valor_servico
        self.taxa = taxa
        return f"Serviço {self.servico} utilizado, no valor de R${self.valor_servico:.2f}"

    @abstractmethod
    def CalcularValorTotal(self):
        pass

    @abstractmethod
    def Exibir_detalhes(self):
        pass


class Hotel(Acomodacao):
    def __init__(self, preco_dia, nome_acomodacao, nmrDias):
        super().__init__(preco_dia, nome_acomodacao, nmrDias)

    def Servicos(self, servico, valor_servico, taxa):
        return super().Servicos(servico, valor_servico, taxa)

    def CalcularValorTotal(self):
        return (self.preco_dia * self.nmrDias) + (self.valor_servico + (self.valor_servico * self.taxa))

    def Exibir_detalhes(self):
        return (f"Acomodação {self.nome_acomodacao}, por {self.nmrDias} dias, "
                f"no valor diário de R${self.preco_dia:.2f}, totalizando R${self.CalcularValorTotal():.2f}"
                f"\nOBS: Oferecemos café da manhã. Não Permitimos animais.")

class Apartamento(Acomodacao):
    def __init__(self, preco_dia, nome_acomodacao, nmrDias):
        super().__init__(preco_dia, nome_acomodacao, nmrDias)
        self.taxa_fixa = 150.00  

    def Servicos(self, servico, valor_servico=None, taxa=None):
        self.valor_servico = self.taxa_fixa  
        return f"Serviço {servico} utilizado, valor de R${self.valor_servico:.2f}"

    def CalcularValorTotal(self):
        
        return (self.preco_dia * self.nmrDias) + self.valor_servico

    def Exibir_detalhes(self):
        return (f"Acomodação {self.nome_acomodacao}, por {self.nmrDias} dias, "
                f"no valor diário de R${self.preco_dia:.2f}, totalizando R${self.CalcularValorTotal():.2f}"
                f"\nOBS: Não oferecemos café da manhã. Permitimos animais.")

class Pousada(Acomodacao):
    def __init__(self, preco_dia, nome_acomodacao, nmrDias):
        super().__init__(preco_dia, nome_acomodacao, nmrDias)

    def Servicos(self, servico, valor_servico, taxa):
        return super().Servicos(servico, valor_servico, taxa)

    def CalcularValorTotal(self):
        return (self.preco_dia * self.nmrDias) + (self.valor_servico + (self.valor_servico * self.taxa))

    def Exibir_detalhes(self):
        return (f"Acomodação {self.nome_acomodacao}, por {self.nmrDias} dias, "
                f"no valor diário de R${self.preco_dia:.2f}, totalizando R${self.CalcularValorTotal():.2f}"
                f"\nOBS: Oferecemos café da manhã. Permitimos animais.")


hotel1 = Hotel(500.0, "Hotel Mozes", 4)
hotel1.Servicos("Internet", 50.0, 0.15)  
print(hotel1.Exibir_detalhes())

apartamento1 = Apartamento(500.0, "Ap Camila", 4)
apartamento1.Servicos("Internet 5G")  
print(apartamento1.Exibir_detalhes())

pousada1 = Pousada(500.0, "Pousada Santa Maria", 4)
pousada1.Servicos("Internet", 50.0, 0.08)
print(pousada1.Exibir_detalhes())

#Exercicio 4

class Transporte(ABC):
    def __init__(self, distancia: float, peso: float, prioridade: bool = False):
        self.distancia = distancia  
        self.peso = peso  
        self.prioridade = prioridade  

    @abstractmethod
    def CalcularCustoTotal(self):
        pass

    @abstractmethod
    def CalcularTempo(self):
        pass

    def Exibir_detalhes(self):
        return (f"Transporte usado pela distância de {self.distancia:.2f} km, "
                f"carregando o peso de {self.peso:.2f} kg, "
                f"custo total de R${self.CalcularCustoTotal():.2f}.")


class Rodoviario(Transporte):
    def __init__(self, distancia: float, peso: float, prioridade: bool = False):
        super().__init__(distancia, peso, prioridade)

    def CalcularCustoTotal(self):
        tarifa_km = self.distancia * 5  
        tarifa_kg = self.peso * 0.10  
        pedagio = (self.distancia // 100) * 10  
        seguro = self.peso * 0.10
        custo_total = tarifa_km + tarifa_kg + pedagio + seguro
        if self.prioridade:
            custo_total *= 1.25  
        return custo_total

    def CalcularTempo(self):
        velocidade_media = 60.0
        if self.prioridade:
            velocidade_media += 30.0
        tempo_horas = self.distancia / velocidade_media
        return tempo_horas

class Aereo(Transporte):
    def __init__(self, distancia: float, peso: float, prioridade: bool = False):
        super().__init__(distancia, peso, prioridade)

    def CalcularCustoTotal(self):
        tarifa_km = self.distancia * 10 
        tarifa_kg = self.peso * 0.25
        pedagio = (self.distancia // 100) * 10  
        seguro = self.peso * 0.10
        custo_total = tarifa_km + tarifa_kg + pedagio + seguro
        if self.prioridade:
            custo_total *= 1.50 
        return custo_total

    def CalcularTempo(self):
        velocidade_media = 800.0
        if self.prioridade:
            velocidade_media += 20.0
        tempo_horas = self.distancia / velocidade_media
        return tempo_horas


class Maritmo(Transporte):
    def __init__(self, distancia: float, peso: float, prioridade: bool = False):
        super().__init__(distancia, peso, prioridade)

    def CalcularCustoTotal(self):
        tarifa_km = self.distancia * 2
        tarifa_kg = self.peso * 0.05
        pedagio = (self.distancia // 100) * 10  
        seguro = self.peso * 0.10
        custo_total = tarifa_km + tarifa_kg + pedagio + seguro
        if self.prioridade:
            custo_total *= 1.75  
        return custo_total

    def CalcularTempo(self):
        velocidade_media = 30.0
        if self.prioridade:
            velocidade_media += 50.0
        tempo_horas = self.distancia / velocidade_media
        return tempo_horas

transporte_rodoviario = Rodoviario(350.0, 500.0, prioridade=False)  
print(transporte_rodoviario.Exibir_detalhes())
transporte_aereo = Aereo(1000.0, 400.0, prioridade=False)
print(transporte_aereo.Exibir_detalhes())
transporte_maritmo = Maritmo(350.0, 250.0, prioridade=True)
print(transporte_maritmo.Exibir_detalhes())
