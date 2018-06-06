# Importando o classificador Multi Layer Perceptron Classifier
from sklearn.neural_network import MLPClassifier as MLPC
# Importando classes necessarias para as metricas (matriz de confusao e erro medio quadratico)
from sklearn.metrics import confusion_matrix, mean_squared_error
# Importando classe para dividir o dataset em treino e em teste
from sklearn.model_selection import train_test_split
# Importando para transformar os atributos do training set para uma escala padrao(tecnica recomendada para RNAs)
from sklearn.preprocessing import StandardScaler
# Importando dataset da biblioteca
from sklearn.datasets import load_breast_cancer

# Biblioteca para trabalhar com dataframes
import pandas as pd
# Bibliotecas para plotar com gráficos
import seaborn as sns
import matplotlib.pyplot as plt

# Carrega o dataset
data = load_breast_cancer()

# Divide os atributos do treino e os atributos alvo(atributo a ser classificado)
X = data['data']
y = data['target']

# Dividindo um porcentagem de 20% do data set para test e 80% para treino
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)

scaler = StandardScaler()

# Convertendo para uma escala padrao de acordo com  os atributos de treino
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# Criando a RNA com 3 layers de 100 neuronios cada uma, e com 1000 epocas
clf = MLPC(hidden_layer_sizes=(100, 100, 100), max_iter=1000)

# Criando o modelo atraves do treinamento
clf.fit(X_train, y_train)

# Classificando os atributos do teste
predictions = clf.predict(X_test)

# Calculando o erro medio quadratico
mean = mean_squared_error(y_test, predictions)

print(mean)
# Criando uma matriz de confusao
confusion_m = pd.DataFrame(confusion_matrix(y_test,predictions), columns=['Benigno', 'Maligno'], index=['Benigno','Maligno'])

# Exibindo a matriz de forma gráfica
plt.show(sns.heatmap(confusion_m, annot=True, fmt='g')) 

