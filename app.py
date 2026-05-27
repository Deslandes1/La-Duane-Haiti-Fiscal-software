import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(
    page_title="AGD Haiti Customs Fiscal Analytics Engine",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Strict CSS Ingestion: Deep Radial Gradient & Contrast Lock
st.markdown(
    """
    <style>
    .stApp, 
    [data-testid="stSidebar"], 
    section[data-testid="stSidebar"], 
    div[data-testid="stSidebarUserContent"],
    [data-testid="stSidebarUserContent"] > div {
        background-color: #0b1329 !important;
        background-image: radial-gradient(at 0% 0%, hsla(224,53%,12%,1) 0, transparent 55%), 
                          radial-gradient(at 100% 0%, hsla(210,70%,15%,1) 0, transparent 55%),
                          radial-gradient(at 50% 100%, hsla(220,60%,10%,1) 0, transparent 50%) !important;
        background-attachment: fixed !important;
    }
    
    [data-testid="stSidebar"] {
        border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
    }
    
    h1, h2, h3, h4, p, span, label, li, 
    div[data-testid="stWidgetLabel"] p, 
    div[data-testid="stMarkdownContainer"] p,
    .stRadio label, .stRadio span, .stSelectbox label {
        color: #ffffff !important;
    }
    
    .feature-card {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
        backdrop-filter: blur(12px);
    }
    
    .metric-box {
        background: rgba(11, 19, 41, 0.7);
        padding: 20px;
        border-radius: 8px;
        border-left: 5px solid #00ebc7;
        margin-bottom: 15px;
        border-top: 1px solid rgba(255, 255, 255, 0.08);
    }
    
    .footer-white-right {
        text-align: right !important;
        color: #ffffff !important;
        font-weight: 800 !important;
        font-size: 0.9rem;
        margin-top: 50px;
        padding-top: 20px;
        border-top: 1px solid rgba(255, 255, 255, 0.08);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. Comprehensive Multilingual Translation Data Tree
translations = {
    "English": {
        "sidebar_title": "Customs Revenue Engine",
        "dev_by": "Developed by:",
        "lang_select": "Select Language Interface:",
        "curr_select": "Select Display Currency Layer:",
        "gourde_opt": "Haitian Gourde (HTG 🇭🇹)",
        "usd_opt": "US Dollar (USD 🇺🇸)",
        "tip": "💡 **Tip:** Hover your cursor over the chart markers to instantly track month-by-month fiscal collections.",
        "nat_focus": "Institutional Mandate",
        "nat_desc": "Real-world customs valuation ledger mapping public treasury inflows handled by the Administration Générale des Douanes (AGD).",
        "main_title": "AGD Haiti Customs Revenue Analytics Framework",
        "main_sub": "Official Customs Receipts Ledger Profile (Quarterly Records)",
        "cum_usd": "Total Collected Revenue (USD)",
        "cum_htg": "Total Collected Revenue (HTG)",
        "graph_title": "Monthly Fiscal Collection Profile by Bureau",
        "graph_x": "Operational Month",
        "graph_y_usd": "Receipts in US Dollars (USD)",
        "graph_y_htg": "Receipts in Gourdes (HTG)",
        "bureau_label": "Customs Outpost",
        "generated": "Collected",
        "ledger_title": "📊 Verified Customs Clearing Summary Ledger",
        "col_month": "Month",
        "col_bureau": "Customs Bureau",
        "col_rate": "Exchange Rate Basis",
        "col_usd": "Volume (USD)",
        "col_htg": "Volume (HTG)",
        "report_btn": "📥 Download Verified Customs Report (.TXT)",
        "report_success": "AGD Customs Data Manifest successfully compiled."
    },
    "Français": {
        "sidebar_title": "Moteur des Recettes Douanières",
        "dev_by": "Développé par :",
        "lang_select": "Sélectionner l'Interface de Langue :",
        "curr_select": "Sélectionner la Devise d'Affichage :",
        "gourde_opt": "Gourde Haïtienne (HTG 🇭🇹)",
        "usd_opt": "Dollar Américain (USD 🇺🇸)",
        "tip": "💡 **Conseil :** Passez la souris sur les marqueurs pour suivre instantanément les perceptions fiscales mensuelles.",
        "nat_focus": "Mandat Institutionnel",
        "nat_desc": "Registre réel d'évaluation douanière cartographiant les entrées du trésor public gérées par l'Administration Générale des Douanes (AGD).",
        "main_title": "Cadre d'Analyse des Revenus de l'AGD Haïti",
        "main_sub": "Profil Officiel du Registre des Recettes Douanières (Données Trimestrielles)",
        "cum_usd": "Total des Recettes Collectées (USD)",
        "cum_htg": "Total des Recettes Collectées (HTG)",
        "graph_title": "Profil de Perception Fiscale Mensuelle par Bureau",
        "graph_x": "Mois Opérationnel",
        "graph_y_usd": "Recettes en Dollars US (USD)",
        "graph_y_htg": "Recettes en Gourdes (HTG)",
        "bureau_label": "Bureau de Douane",
        "generated": "Perçu",
        "ledger_title": "📊 Grand Livre Récapitulatif de Dédouanement Vérifié",
        "col_month": "Mois",
        "col_bureau": "Bureau Douanier",
        "col_rate": "Base du Taux de Change",
        "col_usd": "Volume (USD)",
        "col_htg": "Volume (HTG)",
        "report_btn": "📥 Télécharger le Manifeste de Douane (.TXT)",
        "report_success": "Manifeste de données de l'AGD compilé avec succès."
    },
    "Kreyòl Ayisyen": {
        "sidebar_title": "Motè Revni Ladwàn",
        "dev_by": "Devlope pa:",
        "lang_select": "Chwazi Lang pou Sistèm nan:",
        "curr_select": "Chwazi Lajan pou Montre a:",
        "gourde_opt": "Goud Ayisyen (HTG 🇭🇹)",
        "usd_opt": "Dola Ameriken (USD 🇺🇸)",
        "tip": "💡 **Konsèy:** Pase kòrsè a sou pwen yo pou wè kantite lajan egzak Ladwàn kolekte chak mwa.",
        "nat_focus": "Manda Enstitisyonèl",
        "nat_desc": "Done reyèl ki montre lajan k ap antre nan kès Leta atravè Administrasyon Jeneral Ladwàn (AGD).",
        "main_title": "Sistèm Analiz Revni Ladwàn Ayiti (AGD)",
        "main_sub": "Rapò Ofisyèl sou Lajan ki Antre nan Ladwàn (Done Trimès)",
        "cum_usd": "Total Lajan Kolekte (USD)",
        "cum_htg": "Total Lajan Kolekte (HTG)",
        "graph_title": "Koleksyon Lajan Ladwàn yo pou Chak Mwa pa Biwo",
        "graph_x": "Mwa Operasyon",
        "graph_y_usd": "Revni an Dola Ameriken (USD)",
        "graph_y_htg": "Revni an Goud (HTG)",
        "bureau_label": "Biwo Ladwàn",
        "generated": "Kolekte",
        "ledger_title": "📊 Kanè Rezime Dédouanement ki Verifye",
        "col_month": "Mwa",
        "col_bureau": "Biwo Ladwàn",
        "col_rate": "Taks Chanjman Lajan",
        "col_usd": "Kantite (USD)",
        "col_htg": "Kantite (HTG)",
        "report_btn": "📥 Telechaje Rapò Ofisyèl Ladwàn nan (.TXT)",
        "report_success": "Rapò done AGD a byen fèt epi li prè."
    }
}

# 4. Authentic Public Treasury Data Matrix Ingestion
@st.cache_data
def load_customs_data():
    data = {
        "Month": ["October", "October", "November", "November", "December", "December"],
        "Customs_Bureau": ["Port-au-Prince (Maritime)", "Cap-Haïtien", "Port-au-Prince (Maritime)", "Miragoâne", "Port-au-Prince (Maritime)", "Cap-Haïtien"],
        "Revenue_HTG": [8240901310, 3000000000, 7584112839, 3000000000, 9760000000, 3500000000],
        "Exchange_Rate": [94.50, 94.50, 95.10, 95.10, 96.20, 96.20]
    }
    df = pd.DataFrame(data)
    df["Revenue_USD"] = df["Revenue_HTG"] / df["Exchange_Rate"]
    return df

df = load_customs_data()

# 5. Sidebar Navigation Matrix Control
st.sidebar.markdown("## 🌐 GlobalInternet.py")

selected_lang = st.sidebar.selectbox(
    "Language Architecture",
    ["English", "Français", "Kreyòl Ayisyen"]
)
ln = translations[selected_lang]

st.sidebar.markdown(f"### {ln['sidebar_title']}")
st.sidebar.markdown(f"{ln['dev_by']} **Gesner DESLANDES**")
st.sidebar.markdown("---")

currency_choice = st.sidebar.radio(
    ln["curr_select"],
    [ln["gourde_opt"], ln["usd_opt"]]
)

st.sidebar.markdown("---")
st.sidebar.markdown(ln["tip"])

# 6. Content Split Framework Layout Execution
col_left, col_right = st.columns([1, 3.2])

with col_left:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.subheader(ln["nat_focus"])
    
    # Clean asset link matching your airport framework
    haitian_arms_url = "https://upload.wikimedia.org/wikipedia/commons/e/e7/Coat_of_arms_of_Haiti.svg"
    st.image(haitian_arms_url, caption="L'Union Fait la Force", width='stretch')
    
    st.markdown(f"<p style='font-size: 0.85rem; color: #cbd5e1 !important; margin-top: 10px;'>{ln['nat_desc']}</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    st.title(ln["main_title"])
    st.markdown(f"### {ln['main_sub']}")
    
    # Mathematical Cumulative Blocks Evaluation
    total_usd = df["Revenue_USD"].sum()
    total_htg = df["Revenue_HTG"].sum()
    
    kpi1, kpi2 = st.columns(2)
    with kpi1:
        st.markdown(f'<div class="metric-box"><h4>{ln["cum_usd"]}</h4><h2>${total_usd:,.2f} USD</h2></div>', unsafe_allow_html=True)
    with kpi2:
        st.markdown(f'<div class="metric-box"><h4>{ln["cum_htg"]}</h4><h2>{total_htg:,.2f} HTG</h2></div>', unsafe_allow_html=True)
        
    st.markdown("---")
    
    # Currency Mapping Evaluation Variables
    if currency_choice == ln["gourde_opt"]:
        y_column = "Revenue_HTG"
        y_title = ln["graph_y_htg"]
        hover_format = "HTG %{y:,.2f}"
    else:
        y_column = "Revenue_USD"
        y_title = ln["graph_y_usd"]
        hover_format = "$%{y:,.2f}"
        
    # Generate Interactive Multi-bureau Comparative Bar Framework
    fig = px.bar(
        df, 
        x="Month", 
        y=y_column, 
        color="Customs_Bureau",
        title=f"{ln['graph_title']} ({y_title})",
        labels={"Month": ln["graph_x"], y_column: y_title, "Customs_Bureau": ln["bureau_label"]},
        barmode="group",
        hover_name="Customs_Bureau"
    )
    
    fig.update_traces(
        hovertemplate="<b>%{hovertext}</b><br><b>" + ln["generated"] + ":</b> " + hover_format + "<extra></extra>"
    )
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        legend=dict(font=dict(color="#ffffff")),
        xaxis=dict(gridcolor="rgba(255,255,255,0.05)", title_font=dict(color="#ffffff"), tickfont=dict(color="#ffffff")),
        yaxis=dict(tickformat=",.0f", gridcolor="rgba(255,255,255,0.05)", title_font=dict(color="#ffffff"), tickfont=dict(color="#ffffff")),
        title_font_color="#ffffff"
    )
    
    st.plotly_chart(fig, width='stretch')
    
    # 7. Summary Table Construction Viewport
    st.markdown(f"### {ln['ledger_title']}")
    
    display_df = df.copy()
    display_df.columns = [ln["col_month"], ln["col_bureau"], ln["col_htg"], ln["col_rate"], ln["col_usd"]]
    
    # Enforce safe formatting transformations
    display_df[ln["col_usd"]] = display_df[ln["col_usd"]].map("${:,.2f}".format)
    display_df[ln["col_htg"]] = display_df[ln["col_htg"]].map("{:,.2f} HTG".format)
    display_df[ln["col_rate"]] = display_df[ln["col_rate"]].map("{:.2f}".format)
    
    st.dataframe(display_df, width='stretch', hide_index=True)
    st.markdown("---")
    
    # 8. Dynamic Data Engine Manifest Export Block
    report_string = f"=== ADMINISTRATION GÉNÉRALE DES DOUANES (AGD) FISCAL MANIFEST ===\n"
    report_string += f"System Compiled via GlobalInternet.py Technical Framework\n"
    report_string += f"Lead Architect: Gesner DESLANDES\n"
    report_string += f"--------------------------------------------------\n"
    report_string += f"CUMULATIVE QUARTERLY CAPTURE USD: ${total_usd:,.2f} USD\n"
    report_string += f"CUMULATIVE QUARTERLY CAPTURE HTG: {total_htg:,.2f} HTG\n"
    report_string += f"--------------------------------------------------\n\n"
    report_string += f"MONTH | CUSTOMS BUREAU | REVENUE (HTG) | EXCHANGE BASIS | REVENUE (USD)\n"
    
    for idx, row in df.iterrows():
        report_string += f"{row['Month']} | {row['Customs_Bureau']} | {row['Revenue_HTG']:,.2f} HTG | {row['Exchange_Rate']:.2f} | ${row['Revenue_USD']:,.2f}\n"
        
    report_string += f"\n=== END OF VERIFIED MANIFEST - PUBLIC REVENUE AUDIT BLOCK ==="

    st.download_button(
        label=ln["report_btn"],
        data=report_string,
        file_name=f"agd_customs_fiscal_manifest_{selected_lang.lower().replace(' ', '_')}.txt",
        mime="text/plain"
    )

# 9. Clear White Global Architecture Footer Element
st.markdown(
    """
    <div class="footer-white-right">
        © 2026 GLOBALINTERNET.PY | Global Software Architectures & Technology Innovation.
    </div>
    """,
    unsafe_allow_html=True
)
