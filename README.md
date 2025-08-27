# 📊 Análise de Homicídios no Brasil (SP, RJ e MG)

Este projeto consiste em uma aplicação interativa desenvolvida com **Streamlit** para explorar dados de homicídios em três estados brasileiros: **São Paulo (SP), Rio de Janeiro (RJ) e Minas Gerais (MG)**.  

A análise considera a **evolução temporal**, **estatísticas descritivas**, **intervalos de confiança** e **testes de hipótese**, além de permitir comparações entre os estados.  

---

## 📂 Estrutura do Projeto
- `Home.py` → Página inicial com resumo e navegação.  
- `pages/1_Formacao_e_Experiencia.py` → Formação e experiências do autor.  
- `pages/2_Skills.py` → Habilidades técnicas.  
- `pages/3_Analise_de_Dados.py` → Página da análise de dados (homicídios).  
- `data/Tabela_Homic.csv` → Base de dados utilizada.  

---

## 📊 Fonte dos Dados

Os dados de homicídios foram obtidos no **IpeaData** (Instituto de Pesquisa Econômica Aplicada), especificamente da série histórica de **taxas de homicídios por estados brasileiros**.

- Fonte: [IpeaData - Taxas de Homicídio](http://www.ipeadata.gov.br/)  
- Estados considerados: **SP, RJ e MG**  
- Variáveis originais:
  - `estado` → Sigla da unidade federativa  
  - `ano` → Ano da observação  
  - `homicidios` → Número absoluto de homicídios  

---

## 🧮 Cálculos Realizados

### 1. Conversão para **taxa por 100 mil habitantes**
O número de homicídios foi convertido em **taxa por 100 mil habitantes**, utilizando a população atual de cada estado como base de referência. Isso garante comparabilidade entre estados com tamanhos populacionais diferentes.  

---

### 2. Estatísticas descritivas
Para cada estado, foram calculados indicadores como:  
- **Média**  
- **Mediana**  
- **Desvio padrão**  
- **Valores mínimo e máximo**  

---

### 3. Intervalos de confiança (95%)
Com base nas estatísticas amostrais, foram estimados **intervalos de confiança de 95%** para as taxas médias de homicídio de cada estado. Isso permite avaliar a incerteza associada às estimativas.  

---

### 4. Testes de hipótese
Foram realizados **testes estatísticos** para verificar se as diferenças entre as taxas médias de homicídio dos estados eram significativas.  
- Hipótese nula: não existe diferença entre os estados.  
- Hipótese alternativa: existe diferença entre os estados.  
- Critério: valores de p inferiores a 0,05 indicam diferença estatisticamente significativa.  

---

## 📈 Principais Resultados

- **Rio de Janeiro (RJ)** apresenta consistentemente as **maiores taxas médias de homicídios** no período analisado.  
- **São Paulo (SP)** possui os **menores valores**, além de maior estabilidade ao longo do tempo.  
- Os **testes de hipótese confirmam** que as taxas de homicídio do RJ são significativamente maiores que as de SP.  
- **Minas Gerais (MG)** aparece em posição intermediária, variando entre os dois extremos.  

