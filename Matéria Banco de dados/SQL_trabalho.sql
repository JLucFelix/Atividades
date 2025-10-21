CREATE DATABASE oficina;
USE oficina;

#CRIAÇÃO TABELAS 

CREATE TABLE clientes(
id_cliente INT UNIQUE AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(50) NOT NULL,
telefone VARCHAR(15) UNIQUE
);

CREATE TABLE veiculos(
id_veiculo INT UNIQUE AUTO_INCREMENT PRIMARY KEY,
id_cliente_ref INT,
placa VARCHAR(7) NOT NULL UNIQUE,
marca VARCHAR(50),
modelo VARCHAR(50)
);

CREATE TABLE servicos(
id_servico INT UNIQUE AUTO_INCREMENT,
nome_servico VARCHAR(50) NOT NULL UNIQUE,
descricao VARCHAR(250),
preco_fixo DECIMAL(10,2) NOT NULL CHECK (preco_fixo > 0)
);

CREATE TABLE agendamento(
id_agendamento INT UNIQUE AUTO_INCREMENT,
data_recebimento_veiculo DATETIME NOT NULL,
data_devolucao_veiculo_estimada DATETIME CHECK (data_devolucao_veiculo_estimada >= data_recebimento_veiculo),
status_servico VARCHAR(20) NOT NULL CHECK (status_servico IN ('Agendado', 'Andamento', 'Concluido', 'Cancelado')),
id_cliente_ref INT,
id_veiculo_ref INT
);

#MANIPULAÇÃO

INSERT INTO clientes (nome, telefone) VALUES ("Pedro Jonas", "(14)99453-4443");
INSERT INTO veiculos (placa, marca, modelo, id_cliente_ref) VALUES ("BRA2E19", "Grand Siena", "FIAT", 1);
INSERT INTO servicos (nome_servico, descricao, preco_fixo) VALUES ("Troca de óleo", "Serviço de troca de óleo, carro apresentava indicador no painel e foi confirmado com a vareta de medição", 150);
INSERT INTO agendamento (data_recebimento_veiculo, data_devolucao_veiculo_estimada, status_servico, id_cliente_ref,id_veiculo_ref) VALUES ("2025-10-17 10:23:00", "2025-10-20 13:15:00", "Concluído",1,1);

SELECT * FROM clientes;
SELECT * FROM servicos WHERE id_servico = 1;
SELECT data_recebimento_veiculo, status_servico FROM agendamento; 

UPDATE clientes SET telefone = "(14)99758-5454" WHERE id_cliente = 1;
UPDATE servicos SET preco_fixo = 125 WHERE id_servico = 1;
UPDATE veiculos SET modelo = "UNO" WHERE id_veiculo = 1;









