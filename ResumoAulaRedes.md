# Resumo de Aula: Redes de Computadores 
**Data:** 03 de março de 2026  


---

## 1. Topologias e Dispositivos de Rede
### Endereços:
* **Lógico:** IP.
* **Físico:** MAC.
### Topologia Estrela
* **Física:** Configuração em estrela (ponto central).
* **Lógica:** Comportamento de barramento quando operando através de Hubs ou Switches.

### Componentes e Conceitos Fundamentais
* **Datagramas:** Pulsos elétricos que transportam dados através do meio físico.
* **Hub:** Dispositivo que replica o datagrama para todas as portas (broadcast), funcionando de forma análoga a um repetidor multiportas.
* **Switch:** Direciona datagramas com base no endereço de origem e destino utilizando a tabela **CAM** (*Content Addressable Memory*). Reduz colisões e atua de forma semelhante a uma *Bridge* de alta performance.
* **Identificação:** Cada dispositivo possui um **MAC Address** (Endereço Físico) e um **IP** (Endereço Lógico).

### Domínios de Colisão
* **Em Hubs:** Todos os dispositivos conectados compartilham um único domínio de colisão.
* **Em Switches:** Cada porta individual representa um domínio de colisão isolado, otimizando o fluxo de dados e evitando congestionamentos.

---

## 2. Modelo de Referência OSI
O modelo OSI (*Open Systems Interconnection*) padroniza a comunicação de rede em 7 camadas independentes para garantir a interoperabilidade entre diferentes sistemas.


### Detalhamento das Camadas (Top-Down) // Explicar mais detalhadamnente as camadas COM MAIS TEXTO

| Nível | Camada | Função Principal | Unidade de Dados (PDU) |
| :--- | :--- | :--- | :--- |
| 7 | **Aplicação** | Interface para interação humano-computador e serviços de rede. | Dados / Payload |
| 6 | **Apresentação** | Tradução, compactação e criptografia de dados. | Dados / Payload |
| 5 | **Sessão** | Gerenciamento de diálogo, controle de portas e sincronização (checkpoints). | Dados / Payload |
| 4 | **Transporte** | Controle de fluxo, integridade e segmentação (TCP/UDP). | PDU = Segmento |
| 3 | **Rede** | Roteamento de pacotes entre diferentes redes (Melhor caminho). | PDU = Pacote |
| 2 | **Enlace** | Comunicação intra-rede, controle de erros e endereçamento MAC. | PDU = Quadro (Frame) |
| 1 | **Física** | Transmissão de bits brutos através de meios físicos (cabos e sinais). |PDU = Bits |

---

## 3. Processos de Comunicação e Protocolos

### Segmentação e Encapsulamento
* **PDU's:** Protocol Data Unit
* **Segmentação:** Divisão da informação em partes menores para facilitar o fluxo e reduzir a carga na rede.
* **Encapsulamento:** Processo onde cada camada adiciona cabeçalhos específicos (*Headers*) à PDU da camada superior, incluindo informações como IP de origem e destino.
* **Comunicação Virtual:** Conceito de que uma camada em um dispositivo comunica-se logicamente com a camada equivalente no dispositivo receptor.

### Glossário Técnico e Protocolos //Colocar os nomes de cada protocolos junto da abreviação 
* **Payload:** Conteúdo útil dos dados tratados nas camadas superiores (5, 6 e 7).
* **Three-way Handshake:** Processo de estabelecimento de conexão para garantir a sincronia entre dispositivos.
* **Protocolos de Aplicação:** * **HTTP:** Protocolo de transferência de hipertexto.
    * **FTP:** Protocolo de transferência de arquivos.
    * **DNS:** Sistema de resolução de nomes de domínio.
    * **SMTP:** Protocolo para envio de e-mails.
* **Protocolos de Transporte:**
    * **TCP/IP:** Orientado à conexão; exige confirmação de recebimento e controle de fluxo.
    * **UDP:** Não orientado à conexão; prioriza velocidade sem confirmações.
    *  **Controle de fluxo:** Confirmações de recebimento de envios de frames, utiliza o TCP, controla a velocidade de envios //Explicar melhor
* **Monitoramento e Segurança:**
    * **SNMP:** Protocolo para monitoramento e gerenciamento de rede.
    * **ISO 27001:** Modelo de padrões para gestão de segurança da informação.

//Explicar todo o caminho para envio, como cada camada interfere nos dados até chegar no outro dispositivo, incluindo os cabeçalhos explicados 
---

**Data:** 10/03/2026

## 1. 
explicar FRAME RELAY e comos os quadros vão sendo alterados

IP: Endereçamento e Roteamento, entrega de pacotes. Roteadores possuem tabelas de rotiamento que mostram para onde os pacotes devem chegar, endereçando os pacotes.

## Endereçamento
* **Hierarquia IP:** Hierarquia de endereços que vão do mais abrangente ao mais específico. Formado por 32 bits em 4 blocos de 8 bits
* **Bits:**










