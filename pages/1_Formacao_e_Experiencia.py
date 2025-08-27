import streamlit as st

# ================== Estilo CSS ==================
st.markdown("""
    <style>
        .card {
            background-color: #1e293b;
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
            color: #f1f5f9;
        }
        .subtitle {
            font-size: 20px;
            font-weight: bold;
            color: #38bdf8;
            margin-bottom: 10px;
        }
        .chip {
            display: inline-block;
            background-color: #334155;
            color: #e2e8f0;
            padding: 6px 14px;
            margin: 4px;
            border-radius: 20px;
            font-size: 13px;
        }
    </style>
""", unsafe_allow_html=True)


# ================== Título ==================
st.title("🎓 Formação & Experiência")
st.write("Aqui você encontra um resumo acadêmico, certificações e experiências profissionais baseadas no meu currículo.")


# ================== Formação ==================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<p class="subtitle">📚 Formação Acadêmica</p>', unsafe_allow_html=True)

st.markdown("""
- 🎓 **FIAP** — Engenharia de Software (4º semestre) *(Cursando)*  
- 🎓 **USJT** — Engenharia da Computação *(trancado)*  
- 🏫 **Ensino Médio** — Colégio Moraes (2021)  
- 🏅 **Técnico em TI & Comunicação** — SENAI Celso Charuri (2022)  
""")

st.markdown('</div>', unsafe_allow_html=True)


# ================== Certificações ==================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<p class="subtitle">📜 Certificações</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.metric("Bootcamp Bradesco - Java Cloud Native", "Conclui Jun/2025")
    st.progress(100)
with col2:
    st.metric("Python 3 - Curso em Vídeo", "Fev/2025 - 40h")
    st.progress(100)

st.markdown("""
- 🚀 **DIO Campus Expert** (2025)  
   - Atuação como embaixador universitário  
   - Desenvolvimento de soft skills e liderança  
   - Promoção de eventos, mentorias e networking
""")

st.markdown('</div>', unsafe_allow_html=True)


# ================== Experiências ==================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<p class="subtitle">💼 Experiência Profissional</p>', unsafe_allow_html=True)

st.markdown("""
- 🏢 **Auxiliar de Logística – TEX Courier S.A.** *(1 mês)*  
   - Atuação no suporte às operações logísticas.  

- ☎️ **Jovem Aprendiz – Teleperformance** *(8 meses)*  
   - Experiência em atendimento, comunicação, trabalho em equipe e resolução de problemas.  
""")

st.markdown('</div>', unsafe_allow_html=True)


# ================== Projetos e Atividades ==================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<p class="subtitle">⚡ Projetos e Atividades Extracurriculares</p>', unsafe_allow_html=True)

with st.expander("🔗 Conversor de Moedas em Python"):
    st.write("Projeto pessoal que permite converter valores entre Real, Dólar e Euro, com cálculos automáticos.")
    st.markdown("[Acessar no GitHub](https://github.com/VinicusWince30923/Conversor_moedas)")

with st.expander("🏎️ Projeto Fórmula E – FIAP + Tech Mahindra"):
    st.write("""
    - Desenvolvimento de plataforma interativa para corridas da Fórmula E.  
    - Tecnologias: Python, HTML, CSS, C++.  
    - Incluiu transmissão interativa, sistema de palpites e engajamento de usuários com prêmios.  
    """)

st.markdown('</div>', unsafe_allow_html=True)


# ================== Competências ==================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<p class="subtitle">🛠️ Competências Técnicas</p>', unsafe_allow_html=True)

skills = [
    "Python", "Java", "C++", "SQL", "HTML5/CSS3", "JavaScript",
    "Scrum", "Astah", "AutoCAD", "Oracle SQL Developer",
    "IntelliJ IDEA", "VS Code", "Eclipse", "Git/GitHub"
]
st.markdown(''.join([f'<span class="chip">{s}</span>' for s in skills]), unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ================== Idiomas ==================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<p class="subtitle">🌎 Idiomas</p>', unsafe_allow_html=True)

st.metric("Português", "Nativo/Fluente")
st.metric("Inglês", "Intermediário")

st.markdown('</div>', unsafe_allow_html=True)

# Acessos rápidos
st.subheader("Acessos rápidos")
st.page_link("Home.py", label="🏠Home")
st.page_link("pages/1_Formacao_e_Experiencia.py", label="🎓 Formação & Experiência")
st.page_link("pages/2_Skills.py", label="🛠️ Skills")
st.page_link("pages/3_Analise_de_Dados.py", label="📊 Análise de Dados (GitHub)")
