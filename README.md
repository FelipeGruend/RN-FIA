# Relatório de Redes Neurais
Alunos
- Felipe Gruendemann
- Isabelle de Araújo Azevedo
- Juan Burtet
- Thales Cézar Castro

## Introdução
Este projeto desenvolveu-se com a linguagem Python e algumas de suas
bibliotecas, como Sklearn, Pandas, Seaborn e Matplotlib.

## Erro médio quadrático
O erro médio quadrático neste trabalho foi calculado por meio das métricas
utilizadas pela biblioteca “Sklearn.metrics”.

## Número de épocas usadas
No dado trabalho, o número de épocas foi definido como 1000.

## Porcentagem da dataset usada para aprendizado e para o teste
Trabalhou-se com 80 por cento dos dados voltados para o treinamento e 20 por
cento para o teste.

## Topologia e arquitetura da RNA
A topologia da rede neural artificial utilizada compreende o uso de redes diretas, as quais possuem o seu grafo sem ciclos e 
são comumente representadas em mais de duas camadas. Esta configuração é denominada de Feed Forward de Camadas Múltiplas. A 
arquitetura da rede com essa configuração usada no 	trabalho consiste de uma camada para entrada, três camadas intermediárias 
com 100 “neurônios” (perceptrons) cada e uma camada para saída. Tais aspectos constituem o modelo de Multilayer Perceptron 
(MLP).

## Análise do comportamento da rede
A rede Multilayer Pecerptron é um algoritmo de aprendizado supervisionado que aprende uma função por meio de um treinamento a 
partir de um banco de dados como entrada. Tal função é não- linear, aproximada e tem o ofício de classificação no projeto. 
Cada neurônio desta rede está ligado com todos os outros das camadas vizinhas, mas os neurônios de uma mesma camada não se 
comunicam. Obtém-se, assim,	uma comunicação unidirecional, definindo um comportamento estático para esta 	rede. Sua estrutura é 
composta de uma camada de entrada, camadas intermediárias e uma camada de saída. Na camada de entrada dispõe-se das amostras e 
das respectivas saídas desejadas para que, assim, nas camadas intermediárias os	pesos e limiares sejam ajustados continuamente 
pelo algoritmo de aprendizagem, conforme o treinamento supervisionado. Na camada de saída recebe-se os estímulos da camada 
intermediária e constrói-se o padrão que será a resposta.  
