import streamlit as st

# ================== Título ==================
st.markdown('<p style="font-size:32px; font-weight:bold; color:#facc15;">👋 Bem-vindo ao Dashboard de Vinicius Wince</p>', unsafe_allow_html=True)

# Cartão de perfil
st.markdown("""
<div style="background: linear-gradient(135deg, #0f172a, #1e293b); 
            border-radius: 16px; 
            padding: 20px; 
            margin-top: 20px; 
            box-shadow: 0 4px 12px rgba(0,0,0,0.4);">
    <p style="font-size:24px; font-weight:600; background: linear-gradient(90deg, #06b6d4, #22c55e);
              -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Vinicius dos Santos Wince</p>
    <p><b>Desenvolvedor Back-end</b></p>
    <p>Estudante de Engenharia de Software (FIAP) focado em back-end.</p>
</div>
""", unsafe_allow_html=True)

# ================== Contatos com botões nativos ==================
st.subheader("📬 Contatos")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.link_button("📧 E-mail", "mailto:viniciuswince8@gmail.com")
with col2:
    st.link_button("💬 WhatsApp", "https://wa.me/5511998451437")
with col3:
    st.link_button("🐙 GitHub", "https://github.com/VinicusWince30923")
with col4:
    st.link_button("💼 LinkedIn", "https://www.linkedin.com/in/viniciuswince")

# ================== Resumo ==================
st.subheader("Resumo")
st.markdown("""
<div style="background: linear-gradient(135deg, #0f172a, #1e293b); 
            border-radius: 16px; 
            padding: 20px; 
            margin-top: 20px; 
            box-shadow: 0 4px 12px rgba(0,0,0,0.4);">
Sou estudante de Engenharia de Software na FIAP (4º semestre), com experiência prática em projetos acadêmicos e pessoais utilizando Python, Java, HTML, CSS, JavaScript e SQL. Tenho vivência em metodologias ágeis (Scrum) e uso de ferramentas como Git, GitHub, IntelliJ IDEA, VS Code e Eclipse. Participei do programa DIO Campus Expert, atuando no desenvolvimento de soft skills, liderança e conexão entre comunidade acadêmica e o mercado de tecnologia. Desenvolvi projetos como um Conversor de Moedas em Python e participei do projeto Fórmula E em parceria com a Tech Mahindra, aplicando tecnologias como Python, C++ e desenvolvimento web. Busco minha primeira oportunidade na área de programação, com facilidade de aprendizado, boa comunicação e foco em evolução constante.
</div>
""", unsafe_allow_html=True)

# ================== Acessos rápidos ==================
st.subheader("🌐 Acessos rápidos")
st.page_link("Home.py", label="🏠 Home")
st.page_link("pages/1_Formacao_e_Experiencia.py", label="🎓 Formação & Experiência")
st.page_link("pages/2_Skills.py", label="🛠️ Skills")
st.page_link("pages/3_Analise_de_Dados.py", label="📊 Análise de Dados (GitHub)")
