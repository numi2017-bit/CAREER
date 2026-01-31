import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# --- Page Config ---
st.set_page_config(
    page_title="Executive Strategy | Netflix x Culinary Class Wars",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Ultra-Premium Cinematic CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100;300;400;700;900&family=Inter:wght@300;400;700&display=swap');
    
    :root {
        --netflix-red: #E50914;
        --deep-black: #080808;
        --card-bg: #141414;
        --text-gray: #a3a3a3;
    }

    * {
        font-family: 'Outfit', 'Inter', sans-serif !important;
    }
    
    .stApp {
        background: radial-gradient(circle at 50% -20%, #220506 0%, #080808 60%);
        color: #f5f5f7;
    }

    /* Hide Streamlit elements */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stHeader"] {background: rgba(0,0,0,0);}

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: rgba(10, 10, 10, 0.95) !important;
        border-right: 1px solid #1f1f1f;
    }
    
    .st-emotion-cache-16q9ru4 {
        padding-top: 3rem;
    }

    /* Glassmorphism Cards */
    .glass-card {
        background: rgba(30, 30, 30, 0.4);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 40px;
        margin-bottom: 25px;
        transition: 0.4s ease;
    }
    
    .glass-card:hover {
        border: 1px solid rgba(229, 9, 20, 0.5);
        box-shadow: 0 12px 40px rgba(0,0,0,0.6);
        transform: translateY(-8px);
    }

    /* Metrics */
    .metric-box {
        text-align: center;
        padding: 30px 20px;
        background: linear-gradient(135deg, #1a1a1a 0%, #0d0d0d 100%);
        border-radius: 20px;
        border: 1px solid #222;
        transition: 0.3s;
    }
    .metric-box:hover {
        border-color: var(--netflix-red);
    }
    .metric-box h2 {
        font-size: 2.8rem;
        font-weight: 800;
        margin: 10px 0;
        color: white !important;
    }
    .metric-box p {
        color: var(--netflix-red);
        font-weight: 600;
        font-size: 1rem;
        margin: 0;
    }
    .metric-box small {
        color: var(--text-gray);
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }

    /* Titles */
    .hero-title {
        font-size: 4.5rem;
        font-weight: 900;
        letter-spacing: -3px;
        line-height: 1;
        margin-bottom: 20px;
        background: linear-gradient(180deg, #fff 0%, #777 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .accent-red {
        color: var(--netflix-red) !important;
        -webkit-text-fill-color: var(--netflix-red) !important;
    }

    .section-header {
        font-size: 1.8rem;
        font-weight: 700;
        color: white;
        margin-bottom: 30px;
        display: flex;
        align-items: center;
        gap: 15px;
    }
    .section-header::before {
        content: "";
        width: 5px;
        height: 30px;
        background: var(--netflix-red);
        display: inline-block;
    }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 30px;
        padding: 10px 0;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 1.1rem;
        color: #555;
        border-bottom: 2px solid transparent;
        transition: 0.3s;
    }
    .stTabs [aria-selected="true"] {
        color: white !important;
        border-bottom: 2px solid var(--netflix-red) !important;
    }

    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #080808;
    }
    ::-webkit-scrollbar-thumb {
        background: #333;
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: var(--netflix-red);
    }
</style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.markdown("""
        <div style="text-align: center; padding-bottom: 40px;">
            <img src="https://images.ctfassets.net/4cdz5dd0rg3q/4Z9vDtGl98MlGu_1p_vByO/883f05a92a5d99616ae317929f9e5c54/Netflix_Logo_RGB.png" width="160">
        </div>
    """, unsafe_allow_html=True)
    st.markdown('<p style="font-weight: 700; color: #555; font-size: 0.8rem; letter-spacing: 2px; text-align: center;">STRATEGY REPORT v2.0</p>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    page = st.radio(
        "Reporting Flow",
        ["🏠 Dashboard Home", "� 01. Market Impact", "💎 02. Asset Valuation", "🔥 03. Fandom Engine", "🚨 04. Risk Analysis", "🚀 05. Roadmap", "🏁 06. Future Vision"],
        label_visibility="collapsed"
    )
    
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("---")
    st.button("⚙️ Professional Settings", use_container_width=True)
    st.caption("© 2026 Netflix Internal. Strictly Confidential.")

# --- Content Logic ---

# --- Page 0: Home ---
if page == "🏠 Dashboard Home":
    st.markdown('<p class="hero-title">BEYOND THE <span class="accent-red">SCREENS.</span></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 1.6rem; color: #888; margin-top: -20px;">흑백요리사 IP가 방어한 <span style="color:white; font-weight:700;">2.1억 원</span>의 경제적 실체 분석</p>', unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # 4 Metric Cards
    c1, c2, c3, c4 = st.columns(4)
    metrics = [
        {"lab": "New Members", "val": "210,000+", "delta": "▲ 2.5%", "sub": "Post-Release"},
        {"lab": "Engagement", "val": "1.82x", "delta": "▲ S1 vs S2", "sub": "Lock-in Index"},
        {"lab": "Media Value", "val": "₩3.5B", "delta": "Viral Power", "sub": "Earned Media"},
        {"lab": "Retention Save", "val": "₩211M", "delta": "Churn Prevented", "sub": "Annual Saving"}
    ]
    for i, col in enumerate([c1, c2, c3, c4]):
        with col:
            st.markdown(f"""
                <div class="metric-box">
                    <small>{metrics[i]['lab']}</small>
                    <h2>{metrics[i]['val']}</h2>
                    <p>{metrics[i]['delta']}</p>
                    <span style="font-size: 0.8rem; color: #555;">{metrics[i]['sub']}</span>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="glass-card">
            <h3 class="section-header">Executive Summary</h3>
            <p style="font-size: 1.2rem; line-height: 1.8; color: #bbb;">
                본 전략 보고서는 넷플릭스 오리지널 <b>'흑백요리사'</b>가 단순한 콘텐츠 화제성을 넘어, 플랫폼 비즈니스의 핵심인 <span class="accent-red">리텐션(Retention)</span>과 
                <span class="accent-red">팬덤 경제(Fandom Economy)</span>에 끼친 실질적인 가치를 데이터로 증명합니다. 
                <br><br>
                조회수는 분산되었으나 참여는 응축되었습니다. 우리는 이 현상을 <b>'진성 락인(True Lock-in)'</b>이라 정의하며, 
                연간 약 2.1억 원의 구독료 누수를 막아낸 IP 자산의 힘을 분석합니다.
            </p>
        </div>
    """, unsafe_allow_html=True)

# --- Page 1: Market Impact ---
elif page == "� 01. Market Impact":
    st.markdown('<p class="section-header">MARKET IMPACT ANALYSIS</p>', unsafe_allow_html=True)
    st.subheader("Volume(양)에서 Quality(질)로의 패러다임 변화")
    
    st.markdown("""<div style="background: rgba(229,9,20,0.1); padding: 20px; border-radius: 15px; margin-bottom: 30px;">
        <span class="accent-red">"시끄러운 도서관보다 북적이는 시장통이 낫다."</span> - 데이터가 증명하는 시즌 2의 락인 효과
    </div>""", unsafe_allow_html=True)
    
    col_chart, col_info = st.columns([2, 1])
    with col_chart:
        data = {'Season': ['Season 1', 'Season 2'], 'Views (M)': [277, 79], 'Intensity': [271, 494]}
        fig = go.Figure()
        fig.add_trace(go.Bar(x=data['Season'], y=data['Views (M)'], name='Total Views', marker_color='#2c2c2e', yaxis='y1'))
        fig.add_trace(go.Scatter(x=data['Season'], y=data['Intensity'], name='Engagement Intensity', mode='lines+markers+text', 
                                 text=data['Intensity'], textposition='top center', line=dict(color='#E50914', width=6), yaxis='y2'))
        fig.update_layout(template="plotly_dark", yaxis2=dict(overlaying='y', side='right'), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=500)
        st.plotly_chart(fig, use_container_width=True)
        
    with col_info:
        st.markdown("""<div class="glass-card">
            <h4 class="accent-red">Key Insights</h4>
            <ul style="color: #bbb; line-height: 1.8;">
                <li><b>시장 점유율:</b> 35% 돌파 (국내 OTT 1위 수성)</li>
                <li><b>참여 밀도 1.82배:</b> 조회수 대비 댓글 생성 비율이 폭발적으로 상승했습니다.</li>
                <li><b>락인 기여:</b> 방영 기간 중 '휴면 유저'의 복귀율이 15%p 증가했습니다.</li>
            </ul>
        </div>""", unsafe_allow_html=True)

# --- Page 2: Asset Valuation ---
elif page == "💎 02. Asset Valuation":
    st.markdown('<p class="section-header">ASSET VALUATION MATRIX</p>', unsafe_allow_html=True)
    st.subheader("안성재 35억 vs 백종원 22억 가치 분석")
    
    chef_df = pd.DataFrame({
        "Chef": ["안성재", "백종원", "최강록", "임성근"],
        "Media Value (Bn)": [3.5, 2.2, 1.5, 0.8],
        "Viral Efficiency (Index)": [1.4, 1.1, 1.95, 2.21],
        "Category": ["Gold IP", "Gold IP", "Fandom King", "Viral King"]
    })
    
    fig_scat = px.scatter(chef_df, x="Media Value (Bn)", y="Viral Efficiency (Index)", size="Media Value (Bn)", color="Category",
                         text="Chef", template="plotly_dark", color_discrete_map={"Gold IP": "#E50914", "Fandom King": "#fff", "Viral King": "#888"})
    fig_scat.update_traces(textposition='top center')
    st.plotly_chart(fig_scat, use_container_width=True)
    
    st.markdown("""<div class="glass-card">
        <h3>💡 캐스팅의 미학: 가성비와 화력의 조화</h3>
        <p style="color: #bbb;">메인 스트림 IP가 플랫폼의 신뢰를 만든다면, <b>임성근 & 최강록</b> 같은 바이럴 IP는 유저의 실질적인 유입과 재확산을 유도합니다. 
        특히 임성근 셰프는 바이럴 강도 2.21로 <b>가장 효율적인 IP</b>로 선정되었습니다.</p>
    </div>""", unsafe_allow_html=True)

# --- Page 3: Fandom Engine ---
elif page == "🔥 03. Fandom Engine":
    st.markdown('<p class="section-header">CASE STUDY: CHOI KANG-ROK</p>', unsafe_allow_html=True)
    st.subheader("수치 너머의 '진짜 화력': 댓글 참여율 1위(0.057%)")
    
    c1, c2 = st.columns(2)
    with c1:
        # Radar Chart
        cat = ['밈 전파력', '팬덤 충성도', '리텐션 기여', '브랜드 확장성', '서사 완성도']
        fig_r = go.Figure(data=go.Scatterpolar(r=[5, 5, 5, 4, 5], theta=cat, fill='toself', line_color='#E50914'))
        fig_r.update_layout(polar=dict(radialaxis=dict(visible=False, range=[0, 5])), template="plotly_dark")
        st.plotly_chart(fig_r, use_container_width=True)
        
    with c2:
        st.markdown("""<div class="glass-card" style="height: 400px;">
            <h4 class="accent-red">Meme Power Engine</h4>
            <p style="color: #aaa;">최강록 캐릭터가 생성한 자생적 밈 리스트:</p>
            <ul style="color: white; font-weight: 500;">
                <li>1. <b>'조리보이'</b> - 2024 최고의 바이럴 밈</li>
                <li>2. <b>'나야 들기름'</b> - 유행어 기반 관계 형성</li>
                <li>3. <b>'바질을 곁들인...'</b> - 캐릭터 아이덴티티</li>
                <li>4. <b>'만화책으로 배운 요리'</b> - 강력한 서사 구조</li>
            </ul>
            <p style="border-top: 1px solid #333; padding-top: 15px; color: #888;">
                <b>결론:</b> 마케팅 비용 투입 없이 유저를 스스로 찾아오게 만드는 <b>'자생적 검색 엔진'</b>
            </p>
        </div>""", unsafe_allow_html=True)

# --- Page 4: Risk Analysis ---
elif page == "🚨 04. Risk Analysis":
    st.markdown('<p class="section-header">RISK & CHURN ANALYSIS</p>', unsafe_allow_html=True)
    st.subheader("🚨 2.1억 원의 구독 누수 위기 보고")
    
    col_p, col_i = st.columns([1, 1])
    with col_p:
        labels = ['인성 논란 (51.5%)', '심사 공정성 (23.2%)', '가격 가성비 (15.3%)', '기타 (10%)']
        values = [51.5, 23.2, 15.3, 10.0]
        fig_p = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.6, marker_colors=['#8b0000', '#E50914', '#2c2c2e', '#444'])])
        fig_p.update_layout(template="plotly_dark", showlegend=False)
        st.plotly_chart(fig_p, use_container_width=True)
        
    with col_i:
        st.markdown("""<div class="glass-card" style="border-left: 5px solid #8b0000;">
            <h4 style="color:#8b0000;">Critical Alert</h4>
            <p style="color: #bbb;">유저들은 콘텐츠의 퀄리티보다 <b>출연진의 도덕성(인성)</b>에 가장 민감하게 반응하며, 이는 즉각적인 해지 고려로 연결됩니다.</p>
            <p style="color: #bbb;">특히 최강록 셰프와 같은 핵심 팬덤 IP의 분량이 실종될 경우, 유저들은 <b>'탐색 마비(Decision Paralysis)'</b> 시점으로 진입하며 종료 후 이탈합니다.</p>
        </div>""", unsafe_allow_html=True)

# --- Page 5: Roadmap ---
elif page == "🚀 05. Roadmap":
    st.markdown('<p class="section-header">STRATEGIC ROADMAP 2026</p>', unsafe_allow_html=True)
    
    col_a, col_b, col_c = st.columns(3)
    steps = [
        {"t": "🛡️ DEFENSE", "s": "구독 가치 재정립", "d": "출연 셰프 식당 예약 패스트트랙 제공. 가격 저항 89건 즉시 해소."},
        {"t": "⚖️ QUALITY", "s": "시스템 신뢰 회복", "d": "국민 심사단 100인 도입. 공정성 논란을 '이벤트'로 정면 돌파."},
        {"t": "🚀 EXPANSION", "s": "IP 유니버스 가동", "d": "최강록 x 임성근 스핀오프 콘텐츠. 팬덤 기반 독점 굿즈 출시."}
    ]
    for i, col in enumerate([col_a, col_b, col_c]):
        with col:
            st.markdown(f"""<div class="glass-card" style="height: 300px; text-align: center;">
                <h3 style="color: white;">{steps[i]['t']}</h3>
                <p class="accent-red">{steps[i]['s']}</p>
                <hr style="border-color: #333;">
                <p style="font-size: 0.95rem; color: #888;">{steps[i]['d']}</p>
            </div>""", unsafe_allow_html=True)
    
    st.info("� **Golden Time Push:** 유저 이탈이 최고조에 달하는 매주 수요일 밤 10시, '셰프 비하인드 컷' 푸시를 통해 리텐션을 4.5% 추가 확보합니다.")

# --- Page 6: Vision ---
elif page == "🏁 06. Future Vision":
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
    st.markdown('<p class="hero-title" style="font-size: 5rem;">FANDOM IS <span class="accent-red">ASSET.</span></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 1.8rem; color: #555;">조회수를 넘어 관계(Relationship)를 소유하십시오.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.success("""
    ### 🏁 FINAL TAKEAWAY
    "콘텐츠가 플랫폼을 이깁니다." 하지만 그 콘텐츠는 더 이상 영상 파일이 아닙니다. 
    최강록이라는 **캐릭터**, 블라인드라는 **공정성**, 식당 예약이라는 **실체적 유대감**. 
    이 세 가지 IP 가치를 연결함으로써 넷플릭스는 2.1억 원의 위기를 35억 원의 팬덤 기회로 전환할 수 있습니다.
    """)
