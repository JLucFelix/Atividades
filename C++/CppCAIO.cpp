#include <stdio.h>
#include <stdlib.h>


typedef struct no {
	int conteudo;
	struct no* esq;
	struct no* dir;
} no;

no* criarNo(int qtd) {
	no* novo_no;
	if (qtd == 0)
		novo_no = NULL;
	else
	{
		novo_no = (no*)calloc(1, sizeof(no));
		printf("Digite o valor: ");
		scanf_s("%d", &novo_no->conteudo);
		novo_no->esq = criarNo(qtd / 2);
		novo_no->dir = criarNo(qtd - qtd / 2 - 1);
	}
	return novo_no;
}
void apresentar(no* raiz)
{
	if (raiz != NULL)
	{
		printf("%d ", raiz->conteudo);
		apresentar(raiz->dir);
		apresentar(raiz->esq);
		
	}
}
void achar_folha(no* raiz)
{
	if (raiz == NULL)
		return;
	if (raiz->esq == NULL && raiz->dir == NULL)
	{
		printf("%d ", raiz->conteudo);
	}
	achar_folha(raiz->esq);
	achar_folha(raiz->dir);
}
void achar_no_naofolha(no* raiz)
{
	if (raiz == NULL)
		return;
	if (raiz->esq != NULL || raiz->dir != NULL)
	{
		printf("%d ", raiz->conteudo);
	}
	achar_no_naofolha(raiz->esq);
	achar_no_naofolha(raiz->dir);
}

int main()
{
	no* Raiz;
	Raiz = criarNo(10);
	printf("\n mostrar a ordem da arvore: ");
	apresentar(Raiz);
	printf("\n Achar folhas da arvore: ");
	achar_folha(Raiz);
	printf("\n Achar não folhas na arvore:");
	achar_no_naofolha(Raiz);

	return 0;
}

---------------------------------------------------------------------------------

código 2:

#include <stdio.h>
#include <stdlib.h>


typedef struct no {
	float conteudo;
	struct no* esq;
	struct no* dir;
} no;

int contador = 1;
no* criarNo(int qtd) {
	no* novo_no;
	int vezes = 0;
	if (qtd == 0)
		novo_no = NULL;
	
	else
	{
		novo_no = (no*)calloc(1, sizeof(no));
		novo_no->conteudo = contador++;
		novo_no->esq = criarNo(qtd / 2);
		novo_no->dir = criarNo(qtd - qtd / 2 - 1);
	}
	return novo_no;
}
void apresentar(no* raiz)
{
	if (raiz != NULL)
	{
		printf("%.2lf ", raiz->conteudo);
		apresentar(raiz->dir);
		apresentar(raiz->esq);
		
	}
}
int max(int a, int b) {
	return (a > b) ? a : b;
}
int calcular_altura(no* raiz)
{
	if (raiz == NULL)
	{
		return -1;
	}
	else{
		float altura_esquerda = calcular_altura(raiz->esq);
		float altura_direita = calcular_altura(raiz->dir);
		
		return(1 + max(altura_direita, altura_esquerda));
	}
}
int main()
{
	no* Raiz;
	Raiz = criarNo(10);
	printf("\n mostrar a ordem da arvore: ");
	apresentar(Raiz);
	printf("\n calcular altura: ");
	float h = calcular_altura(Raiz);
	printf("%.2lf", h);
}
