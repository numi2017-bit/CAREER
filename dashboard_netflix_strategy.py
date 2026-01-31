import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- Page Config & Custom CSS ---
st.set_page_config(
    page_title="Netflix Strategy Report: 흑백요리사",
    page_icon="🎬",
    layout="wide"
)

st.markdown("""
<style>
    .metric-card {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    .big-font {
        font-size: 24px !important;
        font-weight: bold;
    }
    h1, h2, h3 {
        font-family: 'Malgun Gothic', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.title("📑 Netflix Strategy Report")
st.sidebar.markdown("**OTT Market Analysis Project**")
page = st.sidebar.radio("Navigation", ["1. Status (현황/성과)", "2. Diagnosis (핵심 진단)", "3. Strategy (전략 제안)", "4. Vision (결론)"])

st.sidebar.markdown("---")
st.sidebar.success(
    "**Project Goal:**\n"
    "넷플릭스 락인(Lock-in) 실체 분석 및\n"
    "이탈 방어 전략 수립"
)
st.sidebar.info("Target IP: **흑백요리사 (Culinary Class Wars)**")


# --- 1. Status ---
if page == "1. Status (현황/성과)":
    st.title("1. Status: 시장권을 탈환한 구원 투수")
    st.markdown("### 📊 Market Impact & Performance Overview")
    
    # Top Metrics Row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="시장 점유율 (2025)", value="35%", delta="1위 수성 (▲2.5%)")
    with col2:
        st.metric(label="브랜드 화제성 순위", value="1위", delta="8위 → 1위 (▲7)")
    with col3:
        st.metric(label="시즌2 참여 밀도", value="494개/1M", delta="시즌1 대비 1.82배 ▲")
    with col4:
        st.metric(label="가입자 견인 효과", value="21만 명", delta="방영 직후 유입")
        
    st.divider()
    
    # Deep Dive: View vs Engagement
    st.subheader("💬 Performance Deep Dive: 뷰(View)보다 값진 '락인(Lock-in)'")
    st.markdown("> **\"조회수는 시즌 1이 높았지만, 실질적인 유저 관여(Engagement)는 시즌 2가 압도적입니다.\"**")
    
    col_chart, col_desc = st.columns([2, 1])
    
    with col_chart:
        # Combo Chart Data
        seasons = ["Season 1", "Season 2"]
        views = [277, 79] # Million
        density = [271, 494] # Comments per 1M Views
        
        fig = go.Figure()
        # Bar: Views
        fig.add_trace(go.Bar(
            x=seasons, y=views, name="총 조회수 (백만)",
            marker_color='lightgray', yaxis='y1'
        ))
        # Line: Engagement Density
        fig.add_trace(go.Scatter(
            x=seasons, y=density, name="참여 밀도 (댓글/100만뷰)",
            mode='lines+markers+text', text=density, textposition="top center",
            line=dict(color='#E50914', width=4), yaxis='y2'
        ))
        
        fig.update_layout(
            title="조회수(Volume) vs 참여 밀도(Quality) 비교",
            yaxis=dict(title="총 조회수 (Million Views)", side='left', showgrid=False),
            yaxis2=dict(title="참여 밀도 (댓글 수/1M View)", side='right', overlaying='y', showgrid=False),
            legend=dict(x=0.1, y=1.1, orientation='h'),
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)
        
    with col_desc:
        st.info(
            """
            **💡 Key Insight**
            
            **1. 조회수의 함정**
            - 시즌 1은 '새로움' 버프(Buff)로 조회수가 높았으나, 휘발성 시청이 많았습니다.
            
            **2. 락인(Lock-in)의 승리**
            - 시즌 2는 조회수 대비 댓글 생성 비율이 **1.82배** 높습니다.
            - 이는 유저들이 단순히 보는 것을 넘어, **토론하고 싸우고 응원하는 '코어 팬덤'**으로 진화했음을 의미합니다.
            
            **3. 비즈니스 임팩트**
            - "시끄러운 도서관보다 북적이는 시장통이 낫다."
            - 높은 참여도는 **이탈 방어율(Retention Rate)**과 직결되는 선행 지표입니다.
            """
        )

# --- 2. Diagnosis ---
elif page == "2. Diagnosis (핵심 진단)":
    st.title("2. Diagnosis: 데이터가 본 두 얼굴")
    st.subheader("💰 Asset Valuation vs 🚨 Churn Risk")
    
    tab1, tab2 = st.tabs(["💎 셰프 IP 자산 가치 평가", "🚨 이탈 리스크 정밀 진단"])
    
    with tab1:
        st.markdown("### 1. 셰프별 경제적 가치 매트릭스")
        st.markdown("조회수(Volume)와 효율(Efficiency)의 4분면 분석")
        
        # Scatter Plot for Value vs Efficiency
        chef_data = pd.DataFrame({
            "Chef": ["안성재", "백종원", "최강록", "임성근"],
            "Media Value (억)": [35, 22, 15, 8],
            "Viral Efficiency (점)": [1.4, 1.1, 1.95, 2.21],
            "Role": ["Main Stream", "Main Stream", "Fandom King", "Viral King"]
        })
        
        fig_scatter = px.scatter(
            chef_data, x="Media Value (억)", y="Viral Efficiency (점)",
            size="Media Value (억)", color="Role", text="Chef",
            hover_data=["Chef", "Role"],
            title="미디어 가치(X) vs 바이럴 효율(Y) 매트릭스",
            template="plotly_white"
        )
        fig_scatter.update_traces(textposition='top center', marker=dict(line=dict(width=2, color='DarkSlateGrey')))
        fig_scatter.add_vline(x=20, line_dash="dash", line_color="gray", annotation_text="Avg Value")
        fig_scatter.add_hline(y=1.5, line_dash="dash", line_color="gray", annotation_text="Avg Eff")
        st.plotly_chart(fig_scatter, use_container_width=True)
        
        st.divider()
        st.markdown("### 2. 최강록: 대체 불가능한 팬덤 IP")
        
        col_c1, col_c2 = st.columns([1, 1])
        with col_c1:
            # Radar Chart
            categories = ['밈 전파력', '팬덤 충성도', '리텐션 기여', '브랜드 확장성', '리스크 관리']
            r_choi = [5, 5, 5, 4, 5]
            
            fig_radar = go.Figure()
            fig_radar.add_trace(go.Scatterpolar(r=r_choi, theta=categories, fill='toself', name='최강록', line_color='#E50914'))
            fig_radar.update_layout(
                polar=dict(radialaxis=dict(visible=True, range=[0, 5])), 
                title="<b>최강록 캐릭터 IP 스코어카드</b>",
                height=400
            )
            st.plotly_chart(fig_radar, use_container_width=True)
            
        with col_c2:
            st.success("**🏆 Fandom Analysis Result**")
            st.markdown("""
            - **댓글 참여율**: **0.057% (전체 1위)** (2위 백종원 대비 1.5배)
            - **핵심 키워드 Top 3**:
                1. **'조리보이'** (밈 전파력: 최상)
                2. **'나야 들기름'** (유행어: 최상)
                3. **'만화책'** (서사: 최상)
            - **결론**: 마케팅 비용 없이도 유저를 끌어당기는 **자생적 바이럴 엔진**.
            """)

    with tab2:
        st.markdown("### 🚨 Critical Warning: 2.1억 원이 새고 있다")
        
        # Risk Metrics
        row1_1, row1_2, row1_3 = st.columns(3)
        row1_1.metric("이탈 위험군 (At Risk)", "4,356명", "14일 이상 미활동")
        row1_2.metric("예상 손실액 (Annual)", "₩211,701,600", "객단가 13.5K 기준")
        row1_3.metric("브랜드 타격 지수", "95 (Critical)", "트리플스타 논란 시점")
        
        st.divider()
        
        col_risk1, col_risk2 = st.columns([1, 1])
        
        with col_risk1:
            st.markdown("#### 📉 해지 유발 트리거 (Churn Drivers)")
            # Donut Chart
            labels = ['인성 논란 (Moral Risk)', '심사 공정성 (Fairness)', '가격 가성비 (Price)', '콘텐츠 퀄리티 (Quality)', '기타']
            values = [51.5, 23.2, 15.3, 5.0, 5.0]
            colors = ['#8b0000', '#b22222', '#cd5c5c', '#f08080', 'gray'] # Red scales
            
            fig_donut = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.5, marker_colors=colors)])
            fig_donut.update_layout(title="<b>해지 의사 발생 원인 비중</b>")
            st.plotly_chart(fig_donut, use_container_width=True)
            
        with col_risk2:
            st.markdown("#### 🔍 Insight: 왜 떠나는가?")
            st.error(
                """
                **1. 인성 논란 (51.5%) - 가장 큰 구멍**
                - "내 돈 내고 범죄자(?)를 봐야 하냐"는 도덕적 반감이 해지로 직결.
                - 트리플스타, 이영숙 등 시즌 1 출연자 논란이 시즌 2 진정성까지 훼손.
                
                **2. 최강록 패러독스 (23.2%)**
                - 가장 보고 싶은 인물(최강록)의 분량이 줄어들자, **'탐색 마비(Decision Paralysis)'** 현상 발생.
                - 유저들은 앱을 켜고 뭘 볼지 헤매다 결국 이탈함.
                
                **3. 가성비의 재정의**
                - 13,500원이 비싼 게 아니라, **"불쾌한 경험에 지불하기 아깝다"**는 심리적 가격 저항선 붕괴.
                """
            )

# --- 3. Strategy ---
elif page == "3. Strategy (전략 제안)":
    st.title("3. Strategy: 골든 타임 공략과 IP 유니버스")
    st.markdown("### ⚡ Action Plan: 2.1억 손실을 막는 3단계 로드맵")
    
    # 3-Step Roadmap Visual
    st.markdown("#### 🗺️ Strategic Roadmap")
    col_step1, col_step2, col_step3 = st.columns(3)
    
    with col_step1:
        st.container(border=True)
        st.markdown("### 🛡️ Step 1. Defense")
        st.markdown("**[구독 가치 재정립]**")
        st.info("식당 예약 패스트트랙")
        st.caption("가격 저항 89건 즉시 해소")
        st.metric("예상 방어율", "35%", "+5%p")
        
    with col_step2:
        st.container(border=True)
        st.markdown("### ⚖️ Step 2. Quality")
        st.markdown("**[시스템 신뢰 회복]**")
        st.warning("국민 심사단 100인")
        st.caption("공정성 논란 원천 차단")
        st.metric("신뢰 회복 지수", "85점", "+20점")
        
    with col_step3:
        st.container(border=True)
        st.markdown("### 🚀 Step 3. Expansion")
        st.markdown("**[IP 유니버스 가동]**")
        st.success("최강록 x 임성근 스핀오프")
        st.caption("팬덤(최강록) + 바이럴(임성근) 결합")
        st.metric("추가 매출", "5.4억", "연간 기대효과")
        
    st.divider()
    
    st.markdown("#### ⏰ Golden Time Targeting")
    st.markdown("데이터가 지목한 **'유저가 가장 배고픈 시간'**에 푸시를 보냅니다.")
    
    # Heatmap Data
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    hours = list(range(24))
    z_data = [[10 for _ in hours] for _ in range(7)]
    # Setup Peaks
    z_data[2][22] = 100 # Wed 22:00
    z_data[5][4] = 85   # Sat 04:00
    
    fig_heat = go.Figure(data=go.Heatmap(
        z=z_data, x=hours, y=days, colorscale='Magma', showscale=False
    ))
    fig_heat.add_annotation(x=22, y=2, text="🔥 Wed 22:00 (탐색 마비)", showarrow=True, arrowhead=1)
    fig_heat.add_annotation(x=4, y=5, text="🌙 Sat 04:00 (정주행)", showarrow=True, arrowhead=1)
    
    fig_heat.update_layout(title="유저 활동 히트맵 (Targeting Points)", height=350, margin=dict(l=0, r=0, t=30, b=0))
    st.plotly_chart(fig_heat, use_container_width=True)
    
    st.info("**👉 Action:** 수요일 밤 10시에 **'최강록 미공개 컷'** 푸시 발송 시, 클릭률(CTR) 4.5% 예상 (평균 대비 3배)")

# --- 4. Vision ---
elif page == "4. Vision (결론)":
    st.title("4. Vision: Paradigm Shift")
    st.subheader("🚀 보는 플랫폼에서 '노는(Play)' 플랫폼으로")
    
    st.markdown("---")
    
    col_v1, col_v2 = st.columns(2)
    
    with col_v1:
        st.markdown("### 🔚 OLD Paradigm (Legacy)")
        st.markdown(
            """
            - **Metric**: 조회수 (View Count)
            - **User**: 트래픽 (Traffic)
            - **Content**: 일방향 송출 (Broadcast)
            - **Relation**: 구독자 (Subscriber)
            """
        )
        st.caption("결과: 언제든 더 싼 곳으로 떠나는 '철새 유저'")
        
    with col_v2:
        st.markdown("### 🚩 NEW Paradigm (Future)")
        st.error(
            """
            - **Metric**: **참여 & 반응 (Engagement)**
            - **User**: **팬덤 (Fandom)**
            - **Content**: **상호작용 (Interactive)**
            - **Relation**: **지지자 (Advocate)**
            """
        )
        st.caption("결과: 플랫폼의 실수를 방어해 주는 '찐팬'")
        
    st.markdown("---")
    
    st.success("""
    ### 💡 FINAL PROPOSAL
    
    **"콘텐츠가 플랫폼을 이깁니다."**
    
    다만 그 콘텐츠는 더 이상 '영상 파일'이 아닙니다.
    1. **최강록**이라는 캐릭터
    2. **임성근**이라는 가성비
    3. **블라인드 심사**라는 공정성 경험
    
    이 세 가지 **IP 자산**을 연결하여, 넷플릭스를 **'팬덤의 놀이터'**로 전환하십시오.
    지금 4,356명을 잡지 못하면, 내년의 넷플릭스는 없습니다.
    """)

