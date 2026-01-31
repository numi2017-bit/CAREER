import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# --- Page Config ---
st.set_page_config(
    page_title="PORTFOLIO & STRATEGY HUB",
    page_icon="🚀",
    layout="wide"
)

# --- Clean & Premium CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;700;900&display=swap');
    
    html, body, [class*="css"], .stMarkdown {
        font-family: 'Noto Sans KR', sans-serif !important;
    }
    
    .stApp {
        background-color: #0c0c0c;
        color: #e0e0e0;
    }

    /* Sidebar Navigation */
    section[data-testid="stSidebar"] {
        background-color: #151515 !important;
        border-right: 1px solid #333;
    }

    /* Title & Headers */
    .main-header {
        background: linear-gradient(90deg, #E50914 0%, #ff4b2b 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.2rem;
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
        background-color: #1a1a1a;
        padding: 30px;
        border-radius: 15px;
        border: 1px solid #333;
        margin-bottom: 25px;
        transition: transform 0.2s ease-in-out;
    }
    
    .report-card:hover {
        border-color: #E50914;
        transform: translateY(-5px);
    }

    /* Metrics */
    div[data-testid="stMetric"] {
        background-color: #222;
        border-radius: 12px;
        padding: 20px !important;
    }

    /* Tabs Customization */
    .stTabs [data-baseweb="tab-list"] {
        gap: 15px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 45px;
        background-color: transparent;
        color: #777;
        font-weight: 600;
        border: none;
    }
    .stTabs [aria-selected="true"] {
        color: #E50914 !important;
        border-bottom: 3px solid #E50914 !important;
    }
</style>
""", unsafe_allow_html=True)

# --- Sidebar Logic ---
st.sidebar.title("🗂️ PROJECT SELECT")
project_category = st.sidebar.selectbox(
    "카테고리를 선택하세요",
    ["1. 넷플릭스 전략 리포트", "2. 마케터 자산 & 연봉 분석", "3. 흑백요리사 데이터 센터"]
)

st.sidebar.markdown("---")

# --- 1. 넷플릭스 전략 리포트 (통합 버전) ---
if project_category == "1. 넷플릭스 전략 리포트":
    st.markdown('<p class="main-header">NETFLIX LOCK-IN STRATEGY</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">"흑백요리사" IP 가치 평가 및 해지 방어 로드맵</p>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["📊 STATUS", "🔍 DIAGNOSIS", "🚀 STRATEGY", "🚩 VISION"])
    
    with tab1:
        col1, col2, col3 = st.columns(3)
        col1.metric("가입자 견인", "21만 명", "+2.5% YoY")
        col2.metric("IP 가치", "₩35억", "Media Value")
        col3.metric("방어 수익", "₩2.1억", "Retention Benefit")
        
        st.markdown("""<div class="report-card">
            <h3>📈 시장 장악력 분석</h3>
            <p>시즌 1 대비 조회수는 자연 감소했으나, <b>참여 밀도(Engagement Density)는 1.82배 상승</b>했습니다. 
            이는 단순 시청에서 충성도 높은 '팬덤'으로의 전환을 의미하며, 넷플릭스 락인(Lock-in)의 핵심 지표로 작동합니다.</p>
        </div>""", unsafe_allow_html=True)

    with tab2:
        col_l, col_r = st.columns(2)
        with col_l:
            st.markdown("#### 최강록 캐릭터 IP 스캔")
            fig = go.Figure(data=go.Scatterpolar(r=[5, 5, 5, 4, 5], theta=['밈 전파력','팬덤 충성','리텐션','확장성','리스크'], fill='toself', line_color='#E50914'))
            fig.update_layout(template="plotly_dark", polar=dict(radialaxis=dict(visible=False, range=[0, 5])))
            st.plotly_chart(fig, use_container_width=True)
        with col_r:
            st.markdown("#### 해지 유발 트리거 비중")
            risk_data = pd.DataFrame({'사유': ['인성 논란', '공정성', '가격', '기타'], '비중': [51, 23, 15, 11]})
            fig_p = px.pie(risk_data, values='비중', names='사유', hole=0.6, color_discrete_sequence=['#8b0000', '#E50914', '#333', '#555'])
            fig_p.update_layout(template="plotly_dark", showlegend=False)
            st.plotly_chart(fig_p, use_container_width=True)

    with tab3:
        st.markdown("""
        <div class="report-card">
            <h3>🚀 3-Step Action Plan</h3>
            <p><b>1. Defense:</b> 출연진 식당 패스트트랙 예약권 제공 (구독 가치 체감)</p>
            <p><b>2. Quality:</b> 국민 심사단 100인 도입 (시스템 신뢰 회복)</p>
            <p><b>3. Expansion:</b> 팬덤 맞춤형 스핀오프 '최강록 프로젝트' 가동</p>
        </div>
        """, unsafe_allow_html=True)

    with tab4:
        st.markdown('<div style="text-align:center; padding:50px;"><h2>"보는 플랫폼에서 관계의 플랫폼으로"</h2><p style="color:#888;">지속 가능한 OTT 비즈니스의 핵심은 조회수가 아닌 지지자(Advocate)의 수입니다.</p></div>', unsafe_allow_html=True)

# --- 2. 마케터 자산 & 연봉 분석 (기존 visualize_salary.py 통합) ---
elif project_category == "2. 마케터 자산 & 연봉 분석":
    st.markdown('<p class="main-header">MARKETER ASSET ANALYSIS</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">커리어 가치 평가 및 시장 연봉 데이터 벤치마크</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📊 시장 연봉 벤치마크 (3년차 기준)")
        # 샘플 데이터 생성 (CSV 로드 실패 시 대비)
        bench_data = pd.DataFrame({
            '플랫폼': ['잡코리아', '사람인', '원티드', '블라인드'],
            '평균연봉': [3400, 3600, 4200, 4500]
        })
        fig_b = px.bar(bench_data, x='평균연봉', y='플랫폼', orientation='h', text='평균연봉',
                      color_discrete_sequence=['#1E90FF'])
        fig_b.update_layout(template="plotly_dark", xaxis_title="연봉 (만원)")
        st.plotly_chart(fig_b, use_container_width=True)
        
    with col2:
        st.markdown("""<div class="report-card">
            <h3>🚩 Career Insight</h3>
            <p>현재 내 연봉 대비 시장 평균은 <b>약 700만원(+20%)</b>의 상향 여력이 존재합니다. 
            특히 원티드/블라인드 기반의 데이터는 전문 역량이 강조될수록 가치가 급등하는 경향을 보입니다.</p>
        </div>""", unsafe_allow_html=True)

# --- 3. 흑백요리사 데이터 센터 (시즌2 수집 데이터) ---
else:
    st.markdown('<p class="main-header">DATA CENTER: S2 ANALYSIS</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">유튜브/뉴스 크롤링 기반 날것의 데이터 분석</p>', unsafe_allow_html=True)
    
    wc_path = r"c:\Users\pc\Desktop\mypyproject\black\흑백요리사\wordcloud_season2_negative.png"
    if os.path.exists(wc_path):
        st.image(wc_path, caption="시즌 2 소셜 부정 반응 워드클라우드", use_container_width=True)
    else:
        st.info("💡 데이터 수집 및 분석 리포트 생성 중입니다. (YouTube API 연동 완료)")
    
    st.markdown("""
    <div class="report-card">
        <h3>🔍 실시간 수집 현황</h3>
        <ul>
            <li><b>수집 소스:</b> YouTube Comments API, Naver News</li>
            <li><b>핵심 키워드:</b> 최강록, 밈, 공정성, 편집 이슈</li>
            <li><b>분석 상태:</b> 감성 분석 모델을 통한 긍/부정 트렌드 모니터링 중</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
