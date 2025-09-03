create database sistema_veiculos;
use sistema_veiculos;

create table marca(
	id int auto_increment primary key,
    nome_marca varchar(50) not null 
);

create table modelo(
	id int auto_increment primary key, 
    nome_modelo varcharacter(50) not null,
    marca_id int not null,
    foreign key(marca_id) references marca(id)
);

create table veiculo(
	veiculo_id int auto_increment primary key,
    placa_veiculo varchar(7),
    ano_fabricacao year not null,
    modelo_id int not null, 
    foreign key(modelo_id) references modelo(id)
);

create table motorista_(
	id int primary key auto_increment,
    nome varchar(30) not null,
    cpf varchar(11) not null,
    data_nascimento date not null,
    categoria_cnh varchar(2) not null,
    validade_cnh date not null 
);

drop table motorista;

create table motorista_veiculo(
id int primary key auto_increment,
motorista_id int not null,
veiculo_id int not null,
data_inicio date not null,
data_fim date, 
FOREIGN key (motorista_id) references motorista(id),
foreign key (veiculo_id) references veiculo(id)


);

create table manutencao(
id int primary key auto_increment,
veiculo_id int not null,

foreign key (veiculo_id) references veiculo(id)
);

ALTER TABLE manutencao
ADD valor_manutencao decimal(10,2),
ADD data_manutencao date;


insert INTO marca (nome_marca)
values("Toyota"),("BMW"),("Ford"),("VolksWagen");

insert INTO modelo (nome_nodelo, marca_id)
values("supra",3), ("Fusca",3), ("EcoSport",2),("320i",1),("Santana",3);

insert INTO veiculo(placa_veiculo, ano_fabricacao, modelo_id)
values("abc1753",2011,6), ("fav5764", 1970,7), ("bnm9523", 2010,8);

insert INTO motorista_(nome, cpf, data_nascimento, categoria_cnh, validade_cnh)
values("Darci", 11135467, 1980-10-05, "B","2025-10-12");


SELECT * FROM veiculo;
SELECT * FROM modelo;

SELECT * from veiculo WHERE ano_fabricacao > 1985;

SELECT * from veiculo where id = 6;

SELECT * FROM marca WHERE id = 2;

SELECT * FROM manutencao WHERE valor > 500;


UPDATE veiculo
SET ano_fabricacao = 1956
WHERE id = 4; 

UPDATE motorista_
set nome = "Boneca"
where id = 1;

DELETE from marca where id = 4;














