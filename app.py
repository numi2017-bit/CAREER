import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# --- Page Config ---
st.set_page_config(
    page_title="NETFLIX STRATEGY | 흑백요리사 IP 분석",
    page_icon="🎬",
    layout="wide"
)

# --- Clean & Premium CSS (Netflix Theme) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;700;900&display=swap');
    
    html, body, [class*="css"], .stMarkdown {
        font-family: 'Noto Sans KR', sans-serif !important;
    }
    
    .stApp {
        background-color: #050505;
        color: #e0e0e0;
    }

    /* Sidebar Navigation */
    section[data-testid="stSidebar"] {
        background-color: #111111 !important;
        border-right: 1px solid #333;
    }

    /* Title & Headers */
    .main-header {
        color: #E50914;
        font-size: 3rem;
        font-weight: 900;
        margin-bottom: 5px;
        letter-spacing: -2px;
    }
    
    .sub-header {
        color: #888;
        font-size: 1.1rem;
        margin-bottom: 40px;
    }

    /* Content Cards */
    .report-card {
        background-color: #181818;
        padding: 30px;
        border-radius: 15px;
        border-left: 5px solid #E50914;
        margin-bottom: 25px;
    }

    /* Metrics */
    div[data-testid="stMetric"] {
        background-color: #1f1f1f;
        border-radius: 12px;
        padding: 20px !important;
        border: 1px solid #333;
    }
    
    div[data-testid="stMetricValue"] {
        color: #E50914 !important;
    }

    /* Tabs Customization */
    .stTabs [aria-selected="true"] {
        color: #E50914 !important;
        border-bottom: 3px solid #E50914 !important;
    }
</style>
""", unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.title("🎬 분석 리포트")
page = st.sidebar.radio(
    "메뉴를 선택하세요",
    ["1. 전략 통합 요약", "2. 상세 데이터 진단", "3. 실행 로드맵"]
)

st.sidebar.markdown("---")
st.sidebar.caption("Target IP: 흑백요리사 S2")

# --- 1. 전략 통합 요약 (Notion 핵심 내용) ---
if page == "1. 전략 통합 요약":
    st.markdown('<p class="main-header">NETFLIX STRATEGY HUB</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">"흑백요리사" IP가 방어한 2.1억 원의 구독 가치 실체 분석</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("가입자 견인", "21만 명", "+2.5% YoY")
    col2.metric("IP 자산 가치", "₩35억", "미디어 환산 가치")
    col3.metric("연간 해지 방어액", "₩2.1억", "Retention Reward")
    
    st.markdown("""
    <div class="report-card">
        <h3>💡 Executive Summary</h3>
        <p>본 고는 <b>'흑백요리사'</b>라는 강력한 IP가 어떻게 넷플릭스의 시장 지배력을 공고히 했는지를 다룹니다.</p>
        <ul>
            <li><b>참여 밀도 1.82배 상승:</b> 조회수 감소에도 불구하고 커뮤니티 활성도는 폭발적으로 증가했습니다.</li>
            <li><b>락인(Lock-in)의 주역:</b> 최강록 등 핵심 출연진의 캐릭터 IP가 유저의 이탈을 효과적으로 방어했습니다.</li>
            <li><b>패러다임 전환:</b> 단순 시청 플랫폼에서 '팬덤의 소통 창구'로의 진화 가능성을 확인했습니다.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- 2. 상세 데이터 진단 ---
elif page == "2. 상세 데이터 진단":
    st.markdown('<p class="main-header">DATA DIAGNOSIS</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">데이터로 증명하는 셰프 IP의 경제적 가치</p>', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["💎 IP 자산 가치 평가", "🚨 이탈 리스크 정밀 진단"])
    
    with tab1:
        col_l, col_r = st.columns([1, 1])
        with col_l:
            st.markdown("#### 핵심 IP 스코어카드 (최강록)")
            fig = go.Figure(data=go.Scatterpolar(
                r=[5, 5, 5, 4, 5],
                theta=['밈 전파력','팬덤 충성도','리텐션 기여','브랜드 확장','정서적 유대'],
                fill='toself',
                line_color='#E50914'
            ))
            fig.update_layout(template="plotly_dark", polar=dict(radialaxis=dict(visible=False, range=[0, 5])))
            st.plotly_chart(fig, use_container_width=True)
        with col_r:
            st.markdown("""<div style="margin-top: 50px;">
                <p><b>분석 결과:</b> 최강록 IP는 단순 출연자가 아닌 <b>'자생적 바이럴 엔진'</b>입니다.</p>
                <p>미디어 가치 환산 결과 <b>35억 원</b> 이상의 홍보 효과를 거둔 것으로 분석되며, 
                특히 2030 세대의 '밈(Meme)' 문화 형성에 결정적 역할을 수행했습니다.</p>
            </div>""", unsafe_allow_html=True)

    with tab2:
        st.markdown("#### 해지 유발 트리거 분석")
        risk_df = pd.DataFrame({'사유': ['인성 논란', '심사 공정성', '가격 저항', '기타'], '비중': [51.5, 23.2, 15.3, 10]})
        fig_p = px.pie(risk_df, values='비중', names='사유', hole=0.6, 
                      color_discrete_sequence=['#8b0000', '#E50914', '#333', '#555'])
        fig_p.update_layout(template="plotly_dark", showlegend=True)
        st.plotly_chart(fig_p, use_container_width=True)
        st.error("주의: 핵심 출연진을 둘러싼 논란이 발생할 경우, 결제 해지 의사도가 즉각적으로 2배 이상 폭등함.")

# --- 3. 실행 로드맵 ---
else:
    st.markdown('<p class="main-header">STRATEGIC ROADMAP</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">2.1억 원의 손실을 방어하기 위한 3단계 전략</p>', unsafe_allow_html=True)
    
    roadmap_col = st.columns(3)
    titles = ["1. DEFENSE", "2. QUALITY", "3. EXPANSION"]
    descs = [
        "출연 셰프 식당 '넷플릭스 전용 패스트트랙' 예약권 제공",
        "국민 심사단 및 블라인드 시스템 강화로 공정성 논란 차단",
        "최강록 x 임성근 스핀오프 콘텐츠 및 독점 굿즈 IP화"
    ]
    
    for i, col in enumerate(roadmap_col):
        with col:
            st.markdown(f"""
            <div class="report-card">
                <h2 style="color:#E50914;">{titles[i]}</h2>
                <p>{descs[i]}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.info("💡 위 로드맵 실행 시, 연간 약 4,356명의 해지 위험군을 방어하여 2.1억 원 이상의 리텐션 수익을 보전할 수 있습니다.")
