import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("ggplot")

fig, (ax1, ax2) = plt.subplots(1,2, figsize=(17, 15))

planilha = pd.read_excel("Graficos.xlsx")

es = planilha['Estado']
po = planilha['Porcentagem']

ax1.set(title="Comparação da ocupação dos leitos de UTI em Rondônia e São Paulo:")

ax1.pie(po, labels=es, autopct='%1.2f%%')

est = planilha['Estados']
cs = planilha['nº casos confirmados']

ax2.set(title="Comparação dos casos confirmados de Covid-19 em Rondônia e São Paulo:")

ax2.bar(est, cs, color='blue', width=0.5)

plt.show()