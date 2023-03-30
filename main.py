
# Importando as bibliotecas necessárias
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Carregando o conjunto de dados
data = pd.read_csv('diabetes.csv')

# Separando os dados em variáveis de entrada e saída
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Dividindo os dados em conjunto de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)

# Criando um modelo de Árvore de Decisão
model = DecisionTreeClassifier()

# Treinando o modelo com o conjunto de treinamento
model.fit(X_train, y_train)

# Fazendo previsões com o conjunto de teste
y_pred = model.predict(X_test)

# Avaliando a precisão do modelo
print('Acurácia do modelo: {:.2f}%'.format(accuracy_score(y_test, y_pred)*100))

# Criando a matriz de confusão
cm = confusion_matrix(y_test, y_pred)
print('Matriz de Confusão:')
print(cm)

# Imprimindo o relatório de classificação
print('Relatório de Classificação:')
print(classification_report(y_test, y_pred))
