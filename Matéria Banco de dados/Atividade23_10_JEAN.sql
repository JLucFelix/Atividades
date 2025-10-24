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
carga_horaria DECIMAL NOT NULL,
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
data_matricula DATE NOT NULL,
status_matricula VARCHAR(20) NOT NULL CHECK (status_matricula IN('Cursando', 'Trancado', 'Concluido')),
CONSTRAINT fk_matricula_aluno
	FOREIGN KEY (id_aluno) REFERENCES aluno(id_aluno)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

INSERT INTO aluno (nome,email) VALUES ('Jean', 'emailgenerico@gmail.com');
INSERT INTO curso (nome, carga_horaria) VALUES ('BCC',40.000);
INSERT INTO turma (id_curso, periodo) VALUES (1,'Noite', 1);
INSERT INTO matricula 
