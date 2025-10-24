/*Explicação PK composta Matricula:
A FK de id_turma e id_aluno em matricula garantem integridade referencial,
um sistema que só aceita os id's caso existam nas respectivas tabelas.
As FK's também garantem integridade de entidade, não permitindo duplicatas 
do relacionamento entre aluno e uma turma.
*/ 


CREATE DATABASE Exercicio3;
USE Exercicio3;

CREATE TABLE aluno(
id_aluno INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(50) NOT NULL,
email VARCHAR(50) NOT NULL UNIQUE
);
CREATE TABLE curso(
id_curso INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(50) NOT NULL UNIQUE,
carga_horaria DECIMAL(5,2) NOT NULL,
ativo TINYINT(1) DEFAULT 1
);
CREATE TABLE turma(
id_turma INT AUTO_INCREMENT PRIMARY KEY,
id_curso INT NOT NULL,
sala INT NOT NULL UNIQUE,
periodo VARCHAR(20) NOT NULL CHECK (periodo IN('Integral', 'Manhã', 'Noite')),
CONSTRAINT fk_turma_curso
	FOREIGN KEY (id_curso) REFERENCES curso(id_curso)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);
CREATE TABLE matricula(
id_aluno INT NOT NULL,
id_turma INT NOT NULL,
data_matricula DATE NOT NULL,
status_matricula VARCHAR(20) NOT NULL CHECK (status_matricula IN('Cursando', 'Trancado', 'Concluido')),
PRIMARY KEY(id_aluno, id_turma),
CONSTRAINT fk_matricula_aluno
	FOREIGN KEY (id_aluno) REFERENCES aluno(id_aluno)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
CONSTRAINT fk_matricula_turma 
	FOREIGN KEY (id_turma) REFERENCES turma(id_turma)
    ON UPDATE CASCADE 
    ON DELETE RESTRICT

);

INSERT INTO aluno (nome,email) VALUES ('Jean', 'emailgenerico@gmail.com');
INSERT INTO curso (nome, carga_horaria) VALUES ('BCC',40.00);
INSERT INTO turma (sala,id_curso, periodo) VALUES (1,1,'Noite');
INSERT INTO matricula(id_turma,id_aluno, data_matricula, status_matricula) 
VALUES (1,1,'2024-02-07', 'Cursando');

SELECT * FROM aluno;
SELECT nome, carga_horaria FROM curso WHERE id_curso = 1;
UPDATE aluno SET email = 'novoemailjean@gmail.com' WHERE id_aluno = 1;
DELETE FROM aluno WHERE id_aluno = 1; #ERRO DE RESTRICT
DELETE FROM turma WHERE id_turma = 1; #ERRO CASCADE
DELETE FROM matricula WHERE id_aluno AND id_turma = 1;
DELETE FROM aluno WHERE id_aluno = 1; #SEM ERRO POIS APAGAMOS OS ELEMENTOS FILHOS PRIMEIROS
DELETE FROM turma WHERE id_turma = 1;
