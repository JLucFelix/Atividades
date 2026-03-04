# Resumo Aula 3/3/2026 Jean #

-- Topologias de Rede -- 
Topologia : Estrela  
Física - Estrela 
Lógica - Barramento através de Hub/Switch

Datagramas - Pulsos elétricos que carregam data

Hub - Recebe o datagrama e direciona pelo barramento para todos os dispositivos conectados, parecido com um Repetidor com mais capacidade de conexões e portas.
Switch - Recebe o datagrama e direciona com base no Origem/Destino a partir de uma lista/tabela chamada CAM, livrando o fluxo de muitas colisões, parecido com uma Ponte com maior capacidade de conexões e portas.
Cada Dispositivo é distinto e identificado pelo MAC (Endereço físico), e IP (Endereço Lógico)

Dominio de colisão - Em Hubs - Dispositivos que permitem colisão, logo um hub com 3 dispositivos faz parte de um único Domínio. - Em switchs - Os dominios de colisão se concentram nos proprios dispositivos, já que todos os datagramas são enviados de forma inteligente e evitando colisões.

Modelo Referência OSI - Garante selos de qualidade para a empresa, com uma series de protocolos para melhor gestão da segurança. 
-- Divide a rede em 7 camadas independentes (Layers): 
* Aplicação 7
* Apresentação 6
* Sessão 5
* Transporte 4 : Controle de fluxo(Rapidez de transmissão e integridade de dados).
* Rede 3
* Enlace 2 
* Física 1 

Começamos de cima para baixo, cada camada possui protocolos que permitem seu funcionamento.

[*LAYER 7*: Interação humano-computador, onde aplicações podem acessar a rede.]
[*LAYER 6*: Se certifica de que a informação está em um formato usável, também é onde a criptografia do dado ocorre. Aqui o Payload ocorre, criando uma tradução dos dados de entrada para que o outro dispositivo possa entender. Essa camada Traduz, Compacta e Criptografa os dados.]
[*LAYER 5*: Mantém conexões e é responsável por controlar portas e sessões, garantindo que haja tempo suficiente para transmissão dos dados e o encerramento para evitar disperdicio de recursos. Essa camada também sincroniza a transferência dos dados em pontos(checkpoints), para que caso haja alguma interrupção, quando reestabelecida a conexão, voltem do ultimo ponto.] 
[*LAYER 4*: Responsável pelo transporte de ponta a ponta entre os dispositivos, utiliza os dados da camada de sessão e divide-os em porções chamados de segmentos, então, a camada de transporte do dispositivo receptor remonta os segmentos em dados que a camada de sessão possa consumir, aqui utilizamos o TCP/IPC.]
[*LAYER 3*: Realiza o transporte dos dados para dispositivos conectados em redes diferentees, dividindo os dados em segmentos da camada de transporte em unidades menores chamados pacotes no dispositivo remetente e remonta os dados no dispositivo receptor. A camada de rede sempre encontra o melhor caminho fisico para que os dados chegem ao seu destino, chamamos isso de Roteamento.]
[*LAYER 2*: O enlace de dados é semelhante a camada de redes, porém lidamos com dispositivos na mesma rede, ela pega os pacotes da camada de rede e os divide em pedaços menores chamados frames/quadros, ela também é reponsável pelo controle de fluxo e erros na comunicação intrarede.]
[*LAYER 1*: A camada primordial que envolve transferência de dados como cabos e switchs, também lida com os dados e sua conversão em fluxos de bits, ambas camadas fisicas dos dispositivos em comunicação precisam reconhecer a linguagem binária através de convenções de sinais.]

Quando o dado chega no dispositivo de destino cada camada obtém o dado de seu respeito que vem do dispositivo que enviou.

- Segmentação: Todos os dispositivos enviam informações na rede através de repartições que facilitam o fluxo e diminuem as cargas. 
A cada camada são adicionados cabeçalhos que levam informações à camada de transporte, todo segmento tem um identificador que facilita na remontagem. Adicionando IP de Destino e IP de Origem,


//IP: Endereço Hierarquico
//Pacote: Ecapsulamento de um Segmento.
//Trafrego de Rajadas: Estabelecimento de comunicações - Handshake triplo.
//PDU's: Unidade de dados de protocolos de cada camada.
//Payload: Camadas 5,6,7 Tratamento de dados para que os dispositivos consigam se comunicar propriamente.
//Protocolos de aplicação HTTP (Hypertext Transfer Protocol), FTP (File Transfer Protocol), DNS(Domain Name System) e SMTP (Simple Mail Transfer Protocol).
//TCP/IP (Transmission Control Protocol e Internet Protocol) -> Exige confirmações de recebimento e controle de fluxo. Orientado à conexão.
//SNMP (Simple Network Management Protocol): Protocolo que permite monitoramento da rede.
//UDP (User Datagram Protocol): -> Não exige confirmações ou controle de fluxo. Não-orientado à conexão.
//Camada de Payload: Parte da informação no Datagrama, contém os conteúdos à serem transmitidos, protocolos que se comunicam com qualquer dispositivo independente de arquitetura ou diferença, linguagem padrão que permite traduções de datas através de diferentes dispositivos. 
//Pilha de Protocolos: Sequência de Protocolos que permitem que a informação seja transmitida.
//Comunicação Virtual: Comunicação entre camadas.
//ISO 27001 - Modelo de protocolos de segurança.
//Encapsulamento - Uma camada adiciona algo para a camada inferior.







