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
A normalização dos homicídios foi feita com base em uma **população fixa de referência** (IBGE), garantindo comparabilidade entre estados:

```python
populacao = {"SP": 44411238, "MG": 20539989, "RJ": 16055174}
```

A taxa foi calculada como:

\[
\text{taxa\_100k} = \frac{\text{homicidios}}{\text{populacao}} \times 100000
\]

---

### 2. Estatísticas descritivas
Foram calculadas para cada estado:
- **Média**  
- **Mediana**  
- **Desvio padrão**  
- **Mínimo e máximo**  

---

### 3. Intervalos de confiança (95%)
Utilizou-se a estatística **t de Student**:

```python
stats.t.interval(0.95, n-1, loc=media, scale=erro_padrao)
```

Permitindo estimar o intervalo em que a **verdadeira taxa média** de homicídios se encontra com 95% de confiança.

---

### 4. Testes de hipótese
Foram aplicados **testes t de Student** (independentes, variâncias diferentes) para verificar diferenças estatisticamente significativas entre estados:

\[
H_0: \mu_{estado1} = \mu_{estado2}
\]

\[
H_1: \mu_{estado1} \neq \mu_{estado2}
\]

Critério: **p < 0.05** → rejeita-se a hipótese nula.

---

## 📈 Principais Resultados

- **RJ** apresenta consistentemente **maiores taxas médias de homicídios** no período.  
- **SP** possui os **menores valores** e maior estabilidade.  
- O **teste de hipótese confirma** que as taxas de homicídio do RJ são **estatisticamente maiores que as de SP**.  
- MG ocupa posição intermediária entre os dois estados.  

---

## 🚀 Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repo.git
   cd seu-repo
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Rode a aplicação Streamlit:
   ```bash
   streamlit run Home.py
   ```

---

## 🛠️ Tecnologias Utilizadas
- **Python 3.9+**  
- **Streamlit** → criação da aplicação interativa  
- **Pandas / NumPy** → manipulação e análise de dados  
- **Matplotlib / Altair** → visualizações gráficas  
- **SciPy** → cálculos estatísticos  

---

## 📌 Conclusão

Este dashboard fornece uma visão clara e interativa sobre a **violência letal** nos estados analisados.  
A análise confirma desigualdades regionais e evidencia a importância de políticas públicas voltadas para a redução de homicídios, especialmente no Rio de Janeiro.  
