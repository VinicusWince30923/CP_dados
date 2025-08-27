import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# ================== Carregar dados ==================
df = pd.read_csv("data/Tabela_Homic.csv", sep=";")
df.columns = ["cod", "estado", "ano", "homicidios"]

# População fixa fornecida
populacao = {"SP": 44411238, "MG": 20539989, "RJ": 16055174}

# Calcular taxa por 100k hab.
df["taxa_100k"] = df.apply(lambda row: (row["homicidios"] / populacao[row["estado"]]) * 100000, axis=1)

# ================== Título ==================
st.title("📊 Análise de Dados - Homicídios por 100 mil habitantes")
st.write("Análise estatística e exploratória da taxa de homicídios (por 100 mil habitantes) nos estados de SP, RJ e MG.")

# ================== 1. Apresentação dos dados ==================
st.header("1. Apresentação dos Dados e Variáveis")

st.markdown("""
- **Conjunto de dados**: homicídios registrados por estado (SP, RJ, MG) e ano.  
- **Variáveis**:  
  - `estado` → categórica nominal  
  - `ano` → numérica discreta (temporal)  
  - `homicidios` → numérica discreta (contagem absoluta)  
  - `taxa_100k` → numérica contínua (normalizada por população)  
- **Pergunta central**: Como evoluiu a taxa de homicídios por 100 mil habitantes ao longo dos anos e como os estados se comparam?
""")

st.dataframe(df.head(10))

# ================== 2. Medidas Centrais e Dispersão ==================
st.header("2. Medidas Centrais e Análise Estatística")

st.subheader("📌 Estatísticas Descritivas por Estado")
desc = df.groupby("estado")["taxa_100k"].describe()[["mean", "50%", "std", "min", "max"]]
desc.rename(columns={"50%": "median", "std": "desvio padrão"}, inplace=True)
st.dataframe(desc)

st.markdown("""
- **Média**: valor médio da taxa no período analisado  
- **Mediana**: ponto central da distribuição  
- **Desvio padrão**: medida de dispersão (quanto varia)  
""")

# 📊 GRÁFICO 1: Boxplot interativo com Altair (substitui Matplotlib)
st.subheader("🎨 Distribuição da Taxa por Estado")
st.bar_chart(df.groupby("estado")["taxa_100k"].mean())

# Mostrar distribuição com expander interativo
with st.expander("📋 Ver dados de distribuição detalhados"):
    st.write("**Valores por estado:**")
    for estado in df["estado"].unique():
        estado_data = df[df["estado"] == estado]["taxa_100k"]
        st.write(f"{estado}: {len(estado_data)} registros, Média: {estado_data.mean():.2f}")

# 📊 GRÁFICO 2: Série temporal interativa
st.subheader("📈 Evolução Temporal")

# Seletor de estados
estados_selecionados = st.multiselect(
    "Selecione os estados para visualizar:",
    options=df["estado"].unique(),
    default=df["estado"].unique()
)

if estados_selecionados:
    # Filtrar dados
    df_filtrado = df[df["estado"].isin(estados_selecionados)]
    
    # Criar tabela pivot para o gráfico de linha
    pivot_df = df_filtrado.pivot_table(
        values='taxa_100k', 
        index='ano', 
        columns='estado', 
        aggfunc='mean'
    ).reset_index()
    
    # Gráfico de linha interativo
    st.line_chart(pivot_df.set_index('ano'))
    
    # Mostrar dados em tabela
    with st.expander("📊 Ver dados da série temporal"):
        st.dataframe(pivot_df)
else:
    st.warning("Selecione pelo menos um estado para visualizar.")

# ================== 3. Intervalos de Confiança e Testes ==================
st.header("3. Intervalos de Confiança e Testes de Hipótese")

st.subheader("📌 Intervalos de Confiança (95%)")
ic_table = {}
for estado in df["estado"].unique():
    data = df[df["estado"] == estado]["taxa_100k"]
    mean = np.mean(data)
    sem = stats.sem(data)
    ci = stats.t.interval(0.95, len(data)-1, loc=mean, scale=sem)
    ic_table[estado] = [mean, ci[0], ci[1]]

ic_df = pd.DataFrame(ic_table, index=["Média", "IC_Inf", "IC_Sup"]).T
st.dataframe(ic_df)

st.markdown("""
O intervalo de confiança indica a faixa em que a **verdadeira média populacional** da taxa de homicídios provavelmente se encontra (95% de confiança).
""")

# 📊 GRÁFICO 3: Intervalos de Confiança interativos
st.subheader("📊 Visualização Interativa dos Intervalos de Confiança")

# Criar DataFrame para o gráfico
ic_plot_df = pd.DataFrame({
    'Estado': ic_df.index,
    'Média': ic_df['Média'],
    'IC_Inferior': ic_df['IC_Inf'],
    'IC_Superior': ic_df['IC_Sup']
})

# Mostrar gráfico de barras com intervalos
st.bar_chart(ic_plot_df.set_index('Estado')['Média'])

# Mostrar detalhes dos intervalos
with st.expander("🔍 Detalhes dos Intervalos de Confiança"):
    for estado in ic_df.index:
        st.metric(
            label=f"{estado} - Taxa Média",
            value=f"{ic_df.loc[estado, 'Média']:.2f}",
            delta=f"IC: [{ic_df.loc[estado, 'IC_Inf']:.2f}, {ic_df.loc[estado, 'IC_Sup']:.2f}]"
        )

# Teste de hipótese interativo
st.subheader("⚖️ Teste de Hipótese")

# Selecionar estados para comparar
col1, col2 = st.columns(2)
with col1:
    estado1 = st.selectbox("Primeiro estado:", df["estado"].unique(), index=1)  # RJ
with col2:
    estado2 = st.selectbox("Segundo estado:", df["estado"].unique(), index=0)  # SP

if estado1 != estado2:
    dados_estado1 = df[df["estado"] == estado1]["taxa_100k"]
    dados_estado2 = df[df["estado"] == estado2]["taxa_100k"]
    
    t_stat, p_val = stats.ttest_ind(dados_estado1, dados_estado2, equal_var=False)
    
    # Mostrar resultados de forma interativa
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Estatística ", f"{t_stat:.3f}")
    with col2:
        st.metric("Valor-p", f"{p_val:.4f}")
    
    # Interpretação interativa
    if p_val < 0.05:
        st.success(f"✅ **Resultado:** Há diferença estatisticamente significativa entre {estado1} e {estado2} (p < 0.05).")
    else:
        st.warning(f"⚠️ **Resultado:** Não há evidência suficiente de diferença significativa entre {estado1} e {estado2} (p ≥ 0.05).")
    
    # Gráfico comparativo
    st.subheader(f"📈 Comparação: {estado1} vs {estado2}")
    comparacao_df = pd.DataFrame({
        estado1: dados_estado1.values,
        estado2: dados_estado2.values
    })
    st.bar_chart(comparacao_df.mean())

# ================== Conclusão ==================
st.header("📌 Conclusão")

# Resumo com métricas
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Maior taxa média", f"{ic_df['Média'].max():.2f}")
with col2:
    st.metric("Menor taxa média", f"{ic_df['Média'].min():.2f}")
with col3:
    st.metric("Amplitude total", f"{ic_df['Média'].max() - ic_df['Média'].min():.2f}")

st.markdown("""
- RJ apresenta taxas médias consistentemente mais altas que SP e MG.  
- A dispersão é maior em RJ → maior instabilidade nos valores.  
- SP mantém valores baixos, relativamente estáveis.  
- O teste de hipótese sugere que **RJ tem taxas significativamente maiores que SP** no período analisado.  
""")

# ================== Acessos rápidos ==================
st.subheader("🌐 Navegação Rápida")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.page_link("Home.py", label="🏠 Home")
with col2:
    st.page_link("pages/1_Formacao_e_Experiencia.py", label="🎓 Formação")
with col3:
    st.page_link("pages/2_Skills.py", label="🛠️ Skills")
with col4:
    st.page_link("pages/3_Analise_de_Dados.py", label="📊 GitHub")