import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# --- Page Config ---
st.set_page_config(
    page_title="NETFLIX Strategy Report | 흑백요리사 IP",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Premium Professional CSS (Cloud Service Look) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Pretendard:wght@100;300;400;500;700;900&display=swap');
    
    * {
        font-family: 'Pretendard', sans-serif !important;
    }
    
    .stApp {
        background-color: #0b0b0b;
        color: #f5f5f7;
    }

    /* Remove Streamlit Header & Footer */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #121212 !important;
        border-right: 1px solid #1e1e1e;
        width: 320px !important;
    }
    
    section[data-testid="stSidebar"] .st-emotion-cache-16q9ru4 {
        padding-top: 2rem;
    }

    /* Content Cards */
    .section-card {
        background-color: #1a1a1c;
        padding: 40px;
        border-radius: 20px;
        border: 1px solid #2c2c2e;
        margin-bottom: 25px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.5);
    }
    
    .metric-container {
        display: flex;
        justify-content: space-between;
        gap: 20px;
        margin-bottom: 40px;
    }
    
    .metric-card {
        background: rgba(229, 9, 20, 0.05);
        border: 1px solid rgba(229, 9, 20, 0.2);
        border-radius: 16px;
        padding: 24px;
        flex: 1;
        text-align: center;
        transition: 0.3s;
    }
    
    .metric-card:hover {
        background: rgba(229, 9, 20, 0.1);
        border-color: #E50914;
        transform: translateY(-5px);
    }

    /* Typography */
    .hero-title {
        background: linear-gradient(135deg, #ffffff 0%, #a1a1a1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.8rem;
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 10px;
    }
    
    .red-accent {
        color: #E50914;
        font-weight: 700;
    }
    
    .section-header {
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 25px;
        border-left: 6px solid #E50914;
        padding-left: 20px;
    }

    /* Custom Navigation */
    .nav-item {
        padding: 12px 20px;
        border-radius: 10px;
        margin-bottom: 5px;
        cursor: pointer;
        transition: 0.2s;
        font-weight: 500;
        color: #8e8e93;
    }
    .nav-item:hover {
        background: rgba(255,255,255,0.05);
        color: #ffffff;
    }
    .nav-item.active {
        background: #E50914;
        color: #ffffff;
    }

    /* Bullets */
    .insight-list {
        list-style: none;
        padding-left: 0;
    }
    .insight-list li {
        margin-bottom: 15px;
        padding-left: 30px;
        position: relative;
        font-size: 1.1rem;
        color: #d1d1d6;
    }
    .insight-list li::before {
        content: "➜";
        position: absolute;
        left: 0;
        color: #E50914;
    }
</style>
""", unsafe_allow_html=True)

# --- Sidebar Content ---
with st.sidebar:
    st.image("https://images.ctfassets.net/4cdz5dd0rg3q/4Z9vDtGl98MlGu_1p_vByO/883f05a92a5d99616ae317929f9e5c54/Netflix_Logo_RGB.png", width=140)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 📑 STRATEGY REPORT")
    
    page = st.radio(
        "Navigation",
        ["🏠 Overview", "📈 01. Status", "💎 02. Asset Valuation", "🔥 03. Choi Kang-rok Case", "🚨 04. Risk & Churn", "🚀 05. Strategic Roadmap", "🏁 06. Vision"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("### 📂 DOCUMENTS")
    st.button("📥 Download Full PPTX", use_container_width=True)
    st.button("📊 Raw Data Export (CSV)", use_container_width=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.caption("© 2026 Netflix Internal Strategy Group")

# --- Page 0: Overview ---
if page == "🏠 Overview":
    st.markdown('<p class="hero-title">더 강력한 락인(Lock-in),<br>IP 자산의 실체</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:1.5rem; color:#8e8e93;">"흑백요리사" IP가 방어한 <span class="red-accent">2.1억 원</span>의 구독 가치 분석</p>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="metric-card"><small>가입자 유입</small><h2>21만+</h2><p style="color:#00ff00;">▲ 2.5% YoY</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><small>참여 밀도</small><h2>1.82x</h2><p style="color:#00ff00;">▲ S1 대비</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><small>IP 미디어 가치</small><h2>₩3.5B</h2><p style="color:#8e8e93;">환산 가치</p></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="metric-card"><small>연간 방어 수익</small><h2>₩211M</h2><p style="color:#E50914;">잠재적 손실 방어</p></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="section-card">
        <h3 class="section-header">Executive Summary: Key Insights</h3>
        <ul class="insight-list">
            <li><b>진짜 성과는 '참여'다:</b> 댓글 참여 밀도가 시즌 1 대비 1.82배 상향 평준화되었습니다. 단순 조회수(Volume)의 시대가 가고 관여(Engagement)의 시대가 왔음을 증명합니다.</li>
            <li><b>시장의 구원 투수:</b> 2024년 4분기 기준 점유율 35% 돌파, 무너졌던 시장 지배력을 '흑백요리사' IP 하나로 완벽히 재탈환했습니다.</li>
            <li><b>2.1억의 잠재적 리테이너:</b> 14일 이상 미활동 중인 위험군 4,356명을 '팬덤 IP'로 락인시켜 연간 약 2.1억 원의 구독료 누수를 차단했습니다.</li>
            <li><b>해지의 본질적 트리거:</b> 유저들은 조작 논란보다 '출연진 인성 검증 부실'에 더 민감하게 반응하며, 이는 즉각적인 해지 의도로 유발됩니다.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- Page 1: Status ---
elif page == "📈 01. Status":
    st.markdown('<p class="section-header">01. 현황 및 성과: 시장권을 탈환한 구원 투수</p>', unsafe_allow_html=True)
    st.subheader("넷플릭스 점유율 35% 돌파 및 V자 반등")
    
    col_chart, col_text = st.columns([2, 1])
    
    with col_chart:
        seasons = ["Season 1", "Season 2"]
        views = [277, 79] # Million
        density = [271, 494] # Comments per 1M Views
        
        fig = go.Figure()
        fig.add_trace(go.Bar(x=seasons, y=views, name="총 조회수 (Million)", marker_color='#2c2c2e', yaxis='y1'))
        fig.add_trace(go.Scatter(x=seasons, y=density, name="참여 밀도 (댓글/1M뷰)", mode='lines+markers+text', 
                                 text=density, textposition="top center", line=dict(color='#E50914', width=6), yaxis='y2'))
        fig.update_layout(template="plotly_dark", yaxis2=dict(overlaying='y', side='right'), height=550, margin=dict(t=50), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)
        
    with col_text:
        st.markdown("""
        <div class="section-card">
            <h4 class="red-accent">Performance Highlight</h4>
            <p>시즌 2는 '새로움'의 거품이 빠졌음에도 불구하고, 실질적인 활성 유저의 <b>상호작용 강도</b>는 더욱 단단해졌습니다.</p>
            <p><b>조회수의 함정 탈피:</b><br>시즌 1은 널리 퍼졌으나, 시즌 2는 깊게 박혔습니다. 이는 구독 유지(Retention)에 있어 훨씬 강력한 선행 지표입니다.</p>
        </div>
        """, unsafe_allow_html=True)

# --- Page 2: Asset Valuation ---
elif page == "💎 02. Asset Valuation":
    st.markdown('<p class="section-header">02. 핵심 진단: IP 경제적 파급 효과</p>', unsafe_allow_html=True)
    st.subheader("안성재 35억 vs 백종원 22억 가치 분석")
    
    chef_data = pd.DataFrame({
        "Chef": ["안성재", "백종원", "최강록", "임성근"],
        "Media Value (억)": [35, 22, 15, 8],
        "Viral Efficiency (점)": [1.4, 1.1, 1.95, 2.21],
        "Category": ["Main IP", "Main IP", "Fandom Engine", "Viral Engine"]
    })
    
    fig_scatter = px.scatter(
        chef_data, x="Media Value (억)", y="Viral Efficiency (점)",
        size="Media Value (억)", color="Category", text="Chef",
        hover_data=["Chef", "Category"],
        title="조회수(Volume) 대비 바이럴 효율(Efficiency) 4분면 분석",
        template="plotly_dark",
        color_discrete_map={"Main IP": "#E50914", "Fandom Engine": "#ffffff", "Viral Engine": "#8e8e93"}
    )
    fig_scatter.update_traces(textposition='top center')
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    st.markdown("""
    <div class="section-card">
        <h3>💡 효율의 표준, 임성근 & 최강록</h3>
        <p>메인 스트림인 안성재, 백종원 셰프가 전체 조회수를 견인한다면, **최강록 셰프**와 **임성근 셰프**는 투입 비용 대비 폭발적인 바이럴을 일으키는 '성능비 최강'의 자산입니다.</p>
        <p>특히 임성근 셰프는 <b>바이럴 강도 2.21점</b>으로 전체 1위를 기록하며, 대중적인 밈 확산의 기폭제가 되었습니다.</p>
    </div>
    """, unsafe_allow_html=True)

# --- Page 3: Choi Kang-rok ---
elif page == "🔥 03. Choi Kang-rok Case":
    st.markdown('<p class="section-header">CASE STUDY: 최강록 캐릭터 IP</p>', unsafe_allow_html=True)
    st.subheader("수치 너머의 '진짜 화력': 댓글 참여율 1위(0.057%)")
    
    col_radar, col_meme = st.columns([1, 1])
    
    with col_radar:
        categories = ['밈 전파력', '팬덤 충성도', '리텐션 기여', '브랜드 확장성', '서사 완성도']
        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(r=[5, 5, 5, 4, 5], theta=categories, fill='toself', name='최강록', line_color='#E50914'))
        fig_radar.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 5])), title="<b>최강록 캐릭터 IP 스코어카드</b>", template="plotly_dark", height=450)
        st.plotly_chart(fig_radar, use_container_width=True)
        
    with col_meme:
        st.markdown("""
        <div class="section-card">
            <h4>💬 Keyword: Fandom Engine</h4>
            <ol>
                <li><b>조리보이 (Meme Power):</b> 2024년 하반기 최고 유입 밈</li>
                <li><b>바질을 곁들인... (Identity):</b> 캐릭터 정체성 확립</li>
                <li><b>나야 들기름 (Interactive):</b> 유행어 기반 소통 강화</li>
                <li><b>만화책 (Origin Story):</b> 서사적 마케팅의 정점</li>
            </ol>
            <p><b>결론:</b> 마케팅 비용 없이도 유저를 스스로 찾아오게 만드는 <b>'자생적 검색 엔진'</b>으로 군림.</p>
        </div>
        """, unsafe_allow_html=True)

# --- Page 4: Risk & Churn ---
elif page == "🚨 04. Risk & Churn":
    st.markdown('<p class="section-header">04. 위기 진단: 2.1억 원의 구독 누수 위기</p>', unsafe_allow_html=True)
    st.subheader("이탈 위험군(At Risk) 4,356명 정밀 진단")
    
    col_pie, col_insight = st.columns([1, 1])
    
    with col_pie:
        risk_labels = ['인성 논란 (Moral)', '심사 공정성 (Fair)', '가격 저항 (Price)', '콘텐츠 퀄리티 (Quality)']
        risk_values = [51.5, 23.2, 15.3, 10.0]
        fig_pie = go.Figure(data=[go.Pie(labels=risk_labels, values=risk_values, hole=.6, marker_colors=['#8b0000', '#E50914', '#2c2c2e', '#444446'])])
        fig_pie.update_layout(template="plotly_dark", showlegend=True, margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(fig_pie, use_container_width=True)
        
    with col_insight:
        st.markdown("""
        <div class="section-card" style="border-left-color: #8b0000;">
            <h4 style="color:#8b0000;">Critical Risk: 인성 검증 부실</h4>
            <p>유저들은 <b>"내 돈 내고 범죄자나 인성 논란자를 봐야 하나"</b>라는 도덕적 정당성에 가장 민감하게 반응합니다.</p>
            <p><b>최강록 패러독스:</b><br>팬덤이 열광하는 인물의 분량이 줄어들면 유저들은 '볼 것이 없다'고 느끼며 앱을 종료합니다. (탐색 마비 지수 85점 기록 시)</p>
        </div>
        """, unsafe_allow_html=True)

# --- Page 5: Strategy ---
elif page == "🚀 05. Strategic Roadmap":
    st.markdown('<p class="section-header">05. 전략 제안: IP 가치 극대화 로드맵</p>', unsafe_allow_html=True)
    st.subheader("Defense - Quality - Expansion 3단계 전략")
    
    st.markdown("""
    <div class="metric-container">
        <div class="metric-card">
            <h3 style="color:#ffffff;">🛡️ Step 1. Defense</h3>
            <p class="red-accent">구독 가치 실체화</p>
            <hr style="border-color:#333;">
            <p style="font-size:0.9rem; color:#8e8e93;">출연 셰프 식당 '패스트트랙' 예약권 제공. 가격 저항 즉시 해소.</p>
            <h4 style="margin-top:10px;">방어율 35% 예상</h4>
        </div>
        <div class="metric-card">
            <h3 style="color:#ffffff;">⚖️ Step 2. Quality</h3>
            <p class="red-accent">시스템 신뢰 회복</p>
            <hr style="border-color:#333;">
            <p style="font-size:0.9rem; color:#8e8e93;">국민 심사단 100인 도입. 공정성 논란을 '이벤트'로 정면 돌파.</p>
            <h4 style="margin-top:10px;">신뢰도 +20점 상승</h4>
        </div>
        <div class="metric-card">
            <h3 style="color:#ffffff;">🚀 Step 3. Expansion</h3>
            <p class="red-accent">IP 유니버스 가동</p>
            <hr style="border-color:#333;">
            <p style="font-size:0.9rem; color:#8e8e93;">최강록 x 임성근 스핀오프 콘텐츠. 팬덤 기반의 독점 굿즈 출시.</p>
            <h4 style="margin-top:10px;">5.4억 추가 가치</h4>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🔥 [Action] Golden Time Care")
    st.info("💡 데이터 분석 결과, 유저 활동이 최고조에 달했다가 '볼 게 없다'고 느끼는 **매주 수요일 밤 10시**에 '최강록 미공개 컷' 푸시를 발포하여 이탈을 원천 차단합니다.")

# --- Page 6: Vision ---
elif page == "🏁 06. Vision":
    st.markdown('<p class="section-header">06. 결론: Paradigm Shift</p>', unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    v_col1, v_col2 = st.columns(2)
    
    with v_col1:
        st.markdown("""
        <div class="section-card">
            <h3 style="color:#8e8e93;">OLD Paradigm (Legacy)</h3>
            <ul class="insight-list">
                <li>Metric: 조회수 (View Count)</li>
                <li>User: 트래픽 (Traffic)</li>
                <li>Content: 일방향 송출 (Broadcast)</li>
                <li>Relation: 구독자 (Subscriber)</li>
            </ul>
            <p style="border-top:1px solid #333; padding-top:10px;">결과: 언제든 더 싼 곳으로 떠나는 <b>'철새 유저'</b></p>
        </div>
        """, unsafe_allow_html=True)
        
    with v_col2:
        st.markdown("""
        <div class="section-card" style="border-color:#E50914;">
            <h3>NEW Paradigm (Future)</h3>
            <ul class="insight-list">
                <li>Metric: <span class="red-accent">참여 & 반응 (Engagement)</span></li>
                <li>User: <span class="red-accent">팬덤 (Fandom)</span></li>
                <li>Content: <span class="red-accent">상호작용 (Interactive)</span></li>
                <li>Relation: <span class="red-accent">지지자 (Advocate)</span></li>
            </ul>
            <p style="border-top:1px solid #333; padding-top:10px;">결과: 플랫폼의 위기를 지켜주는 <b>'강력한 리테이너'</b></p>
        </div>
        """, unsafe_allow_html=True)

    st.success("""
    ### 💡 FINAL PROPOSAL
    **"콘텐츠가 플랫폼을 이깁니다."**
    
    넷플릭스는 단순 영상 전송망이 아닌, **'캐릭터와 팬덤이 가장 치열하게 노는 놀이터'**로 정의되어야 합니다. 
    지금 2.1억 원의 위기를 35억 원의 기회로 바꾸는 핵심 열쇠는 바로 **IP의 깊이**에 있습니다.
    """)
