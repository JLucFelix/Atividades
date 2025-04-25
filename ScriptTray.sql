CREATE DATABASE feedback_tray;

USE feedback_tray;

create table if not exists usuario (
  id int auto_increment primary key,
  nome varchar(255) not null,
  email varchar(255) not null
);

create table if not exists lojista (
	id int auto_increment primary key,
	nome varchar(255) not null,
    email varchar(255) not null
);

create table if not exists loja (
  id int auto_increment primary key,
  nome varchar(255) not null,
  cnpj varchar(14) not null,
  endereco varchar(255) null
);

create table if not exists produto (
	id int auto_increment primary key,
	nome varchar(255) not null,
    descricao text not null,
    valor decimal(8,2)
); 

create table if not exists compra (
  id int auto_increment primary key,
  data_compra date,
  data_finalização date
  /*id_comprador
  foreign key id_comprador references comprador(id)
  id_produto
  foreign key id_produto references produto(id)*/
);

create table if not exists pergunta (
  id int auto_increment primary key,
  pergunta varchar(255) not null,
  /*tipo de pergunta */
  tipo_resposta varchar(20) not null check(tipo_resposta = 'estrela' OR tipo_resposta = 'sim_nao'),
  valor_inteiro INT check(tipo_resposta = 'estrela' and valor_inteiro BETWEEN 1 AND 5),
  valor_booleano BOOLEAN check(tipo_resposta = 'sim_nao')
);

create table if not exists formulario_feedback_produto (
  id int auto_increment primary key,
  /*id_compra
  foreign key id_compra references compra(id)*/
  finalizado boolean,
  data_envio date
);

create table if not exists pergunta_formulario_feedback_produto (
 id int auto_increment primary key
 /*id_formulario
 foreign key id_formulario references formulario_feedback_produto(id)
 id_pergunta
 foreign key id_pergunta references pergunta(id)*/
);

create table if not exists resposta_formulario_feedback_produto (
 id int auto_increment primary key,
 /*id_pergunta_formulario_feedback_produto
 foreign key id_pergunta_formulario_feedback_produto(id)*/
 avaliacao_estrelas INT null check (pergunta_formulario_feedback_produto.pergunta.tipo_resposta = 'estrela' and avaliacao_estrela BETWEEN 1 and 5 ),
 avaliacao_binaria bool null check ( pergunta_formulario_feedback_produto.pergunta.tipo_resposta = 'sim_nao' and avaliacao_binaria = true or false)
);