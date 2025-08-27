import streamlit as st

# ================== Estilo CSS ==================
st.markdown("""
    <style>
        body {
            background-color: #111827;
            color: #f1f5f9;
            font-family: "Segoe UI", sans-serif;
        }
        .title {
            font-size: 32px;
            font-weight: bold;
            color: #facc15;
        }
        .subtitle {
            font-size: 24px;
            font-weight: 600;
            background: linear-gradient(90deg, #06b6d4, #22c55e);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .card {
            background: linear-gradient(135deg, #0f172a, #1e293b);
            border-radius: 16px;
            padding: 20px;
            margin-top: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.4);
        }
        .info-box {
            background-color: #374151;
            border-radius: 10px;
            padding: 12px;
            text-align: center;
            font-size: 14px;
            margin: 5px;
        }
        .chips {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }
        .chip {
            background-color: #4b5563;
            border-radius: 20px;
            padding: 6px 14px;
            font-size: 13px;
        }
    </style>
""", unsafe_allow_html=True)

# ================== Conteúdo ==================

st.markdown('<p class="title">👋 Olá! Bem-vindo(a) ao meu Dashboard Profissional</p>', unsafe_allow_html=True)

# Cartão de perfil
st.markdown("""
<div class="card">
    <p class="subtitle">Vinicius dos Santos Wince</p>
    <p><b>Desenvolvedor Back-end</b></p>
    <p>Estudante de Engenharia de Software (FIAP) focado em back-end..</p>
</div>
""", unsafe_allow_html=True)

# Contatos
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="info-box"><b>E-mail</b><br><a href="mailto:viniciuswince8@gmail.com">viniciuswince8@gmail.com</a></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="info-box"><b>WhatsApp</b><br><a href="https://wa.me/5511998451437">+55 (11) 998451437</a></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="info-box"><b>GitHub</b><br><a href="https://github.com/RicardoFernandes2004">github.com/RicardoFernandes2004</a></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="info-box"><b>LinkedIn</b><br><a href="https://linkedin.com/in/ricardo-fernandes-8017b5261">linkedin.com/in/ricardo-fernandes</a></div>', unsafe_allow_html=True)

# Resumo
st.subheader("Resumo")
st.markdown("""
<div class="card">
Sou estudante de Engenharia de Software na FIAP (4º semestre), com experiência prática em projetos acadêmicos e pessoais utilizando Python, Java, HTML, CSS, JavaScript e SQL. Tenho vivência em metodologias ágeis (Scrum) e uso de ferramentas como Git, GitHub, IntelliJ IDEA, VS Code e Eclipse. Participei do programa DIO Campus Expert, atuando no desenvolvimento de soft skills, liderança e conexão entre comunidade acadêmica e o mercado de tecnologia. Desenvolvi projetos como um Conversor de Moedas em Python e participei do projeto Fórmula E em parceria com a Tech Mahindra, aplicando tecnologias como Python, C++ e desenvolvimento web. Busco minha primeira oportunidade na área de programação, com facilidade de aprendizado, boa comunicação e foco em evolução constante.
</div>
""", unsafe_allow_html=True)


# Acessos rápidos
st.subheader("Acessos rápidos")
st.page_link("Home.py", label="🏠Home")
st.page_link("pages/1_Formacao_e_Experiencia.py", label="🎓 Formação & Experiência")
st.page_link("pages/2_Skills.py", label="🛠️ Skills")
st.page_link("pages/3_Analise_de_Dados.py", label="📊 Análise de Dados (GitHub)")