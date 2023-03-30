import pandas as pd
import numpy as np

sexo = [1, 0]
glicose = [50, 200]
pressao = [50, 200]
espessuraPele = [10, 120]
insulina = [0, 1000]
imc = [10, 100]
idade = [10, 100]
diabeteHereditario = [1, 0, 2]
gravidez = [1, 0]
resultado = [1, 0]

valores = []

print('Gerando dados...')

for i in range(1000):
    sexoSelecionado = np.random.choice(sexo, 1)
    gravidezSelecionada = [0] if sexoSelecionado == 1 else np.random.choice(
        gravidez, 1)
    glicoseSelecionada = np.random.randint(glicose[0], glicose[1])
    pressaoSelecionada = np.random.randint(pressao[0], pressao[1])
    espessuraPeleSelecionada = np.random.randint(
        espessuraPele[0], espessuraPele[1])
    insulinaSelecionada = np.random.randint(insulina[0], insulina[1])
    imcSelecionado = np.random.randint(imc[0], imc[1])
    idadeSelecionada = np.random.randint(idade[0], idade[1])
    diabeteHereditarioSelecionado = np.random.choice(diabeteHereditario, 1)
    resultadoSelecionado = np.random.choice(resultado, 1)

    valores.append([
        sexoSelecionado[0],
        gravidezSelecionada[0],
        glicoseSelecionada,
        pressaoSelecionada,
        espessuraPeleSelecionada,
        insulinaSelecionada,
        imcSelecionado,
        idadeSelecionada,
        diabeteHereditarioSelecionado[0],
        resultadoSelecionado[0]
    ])


colunas = [
    'sexo', 'gravidez', 'glicose', 'pressao', 'espessuraPele', 'insulina', 'imc', 'idade', 'diabeteHereditario', 'resultado'
]

df = pd.DataFrame(valores, columns=colunas)
df.to_csv('datasets/diabetes_gerado_valor.csv', index=False)
print('Dados gerados!')
# df = pd.read_csv('diabetes.csv')

# def_rep = pd.DataFrame(np.repeat(df.values, 10, axis=0))
# def_rep.columns = df.columns

# def_rep.to_csv('diabetes_2.csv', index=False)
