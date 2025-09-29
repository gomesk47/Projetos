# Passo 1: Importar Bibliotecas e Carregar Dados
import tensorflow as tf
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Carregar o conjunto de dados Iris
iris = load_iris()
X = iris.data           # Características (comprimento/largura sépala e pétala)
y = iris.target         # Classes (0, 1 ou 2)

# Passo 2: Pré-processamento dos Dados
# Dividir os dados em treino (80%) e teste (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar os dados para melhorar o desempenho do modelo
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Passo 3: Construir o Modelo
model = tf.keras.Sequential([
    tf.keras.layers.Dense(8, activation='relu', input_shape=(4,)),  # Camada oculta com 8 neurônios
    tf.keras.layers.Dense(3, activation='softmax')                  # Camada de saída para 3 classes
])

# Compilar o modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',  # porque os rótulos são inteiros
              metrics=['accuracy'])

# Passo 4: Treinar o Modelo
model.fit(X_train, y_train, epochs=30, verbose=1)

# Passo 5: Avaliar o Modelo
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"\n✅ Acurácia no conjunto de teste: {accuracy*100:.2f}%")

# Passo 6: Fazer Previsões
# Pegar uma amostra do conjunto de teste
amostra = X_test[0].reshape(1, -1)
previsao = model.predict(amostra)
classe_prevista = previsao.argmax(axis=1)
print(f"🌼 Classe prevista: {classe_prevista[0]}")