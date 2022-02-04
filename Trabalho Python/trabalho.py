import os
from random import lognormvariate
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF 

plt.style.use("ggplot")

fig, (ax1, ax2) = plt.subplots(1,2, figsize=(18, 5))

planilha = pd.read_excel("Graficos.xlsx")

es = planilha['Estado']
po = planilha['Porcentagem']

ax1.set(title="Comparação da ocupação dos leitos de UTI em Rondônia e São Paulo:")

ax1.pie(po, labels=es, autopct='%1.2f%%')

est = planilha['Estados']
cs = planilha['nº casos confirmados']

ax2.set(title="Comparação dos casos confirmados de Covid-19 em Rondônia e São Paulo:")

ax2.bar(est, cs, color='blue', width=0.5)

plt.savefig("graficos.png")

pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()
pdf.set_font('Times', '', 16)
texto = "Desigualdades regionais na disponibilidade de leitos de UTI para a população\n\nPor: Brenda Custódio de Souza\n\nConforme apontado por Junior e Cabral(2020), a Região Norte possui a menor porcentagem de proporção da distribuição de leitos de UTI totais(SUS e não SUS), mesmo abrangendo cerca de 18,43 milhões de pessoas, 90,72% dependentes do SUS, a estimativa é que há aproximadamente um leito SUS a cada 9.325 pessoas. A região Sudeste por sua vez concentra 51,9% dos leitos, juntas, as regiões Norte e Centro Oeste não alcançam 10% dos leitos totais. Para ilustrar essa análise, foram desenvolvidos os gráficos abaixo com dados de um estado da região Norte e outro da região Sudeste do país. No primeiro gráfico vemos a comparação da ocupação dos leitos de UTI de Rondônia e São Paulo, sendo a da primeira claramente superior a segunda, o estado de Rondônia atingiu 90% da ocupação de leitos de UTI Covid na última semana e optou por utilizar leitos do Centro de Reabilitação de Rondônia (Cero) para reduzir a taxa de ocupação. Em relação ao segundo gráfico, embora os casos positivados de Covid sejam maiores em São Paulo, a população de Rondônia passou a ser diagnosticada, junto ao Covid, com dengue e h1n1/h3n2, o que os torna mais vulneráveis e sujeitos a maiores complicações da Covid, extremamente perigosa principalmente as pessoas com comorbidades. Atualmente o cenário de pandemia tem trazido a tona muitos aspectos da desigualdade social, o que analisamos expõe uma realidade já existente nos momentos pré-pandemia, o que abre espaço para reflexão, como são avaliados a necessidade de recursos hospitalares para as diferentes regiões do país? "
pdf.multi_cell(w=0, h=7, txt= texto)

pdf.image(name="graficos.png", x=0, y=180, w=200)
pdf.output("relatorio.pdf")

os.system("pause")