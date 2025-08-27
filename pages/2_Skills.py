import streamlit as st
import matplotlib.pyplot as plt

# ================== Estilo ==================
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
st.title("🛠️ Skills & Competências")
st.write("Tecnologias, ferramentas e metodologias que domino ou tenho experiência prática.")


# ================== Linguagens de Programação ==================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<p class="subtitle">💻 Linguagens de Programação</p>', unsafe_allow_html=True)

langs = {"Python": 80, "Java": 65, "C++": 45, "JavaScript": 50, "SQL": 55}
fig, ax = plt.subplots()
ax.barh(list(langs.keys()), list(langs.values()))
ax.set_xlim(0, 100)
ax.set_xlabel("Nível de Proficiência (%)")
ax.set_title("Proficiência em Linguagens")
st.pyplot(fig)

st.markdown('</div>', unsafe_allow_html=True)


# ================== Desenvolvimento Web ==================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<p class="subtitle">🌐 Desenvolvimento Web</p>', unsafe_allow_html=True)

st.markdown("""
- 🟦 **HTML5 & CSS3** — Estruturação e estilização de páginas.  
- ⚡ **JavaScript** — Interatividade e lógica no front-end.  
""")

st.markdown('</div>', unsafe_allow_html=True)


# ================== Ferramentas & IDEs ==================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<p class="subtitle">🧰 Ferramentas & IDEs</p>', unsafe_allow_html=True)

tools = ["IntelliJ IDEA", "VS Code", "Eclipse", "Git", "GitHub", "SQL Developer", "Astah", "AutoCAD"]
st.markdown(''.join([f'<span class="chip">{t}</span>' for t in tools]), unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ================== Metodologias ==================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<p class="subtitle">📋 Metodologias</p>', unsafe_allow_html=True)

st.markdown("""
- 🔄 **Scrum** — Experiência em projetos ágeis, com sprints e cerimônias.  
- ✅ **Kanban** — Organização de tarefas e fluxos de trabalho.  
""")

st.markdown('</div>', unsafe_allow_html=True)


# ================== Competências Gerais ==================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<p class="subtitle">🚀 Outras Competências</p>', unsafe_allow_html=True)

skills = [
    "Comunicação", "Trabalho em equipe", "Resolução de problemas",
    "Aprendizado rápido", "Mentoria (Campus Expert)", "Networking"
]
st.markdown(''.join([f'<span class="chip">{s}</span>' for s in skills]), unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Acessos rápidos
st.subheader("Acessos rápidos")
st.page_link("Home.py", label="🏠Home")
st.page_link("pages/1_Formacao_e_Experiencia.py", label="🎓 Formação & Experiência")
st.page_link("pages/2_Skills.py", label="🛠️ Skills")
st.page_link("pages/3_Analise_de_Dados.py", label="📊 Análise de Dados (GitHub)")
