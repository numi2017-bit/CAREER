import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from collections import Counter
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# --- 1. Page Config ---
st.set_page_config(
    page_title="최강록 셰프 뉴스 분석 대시보드",
    page_icon="🍳",
    layout="wide"
)

# --- 2. Data Loading Function ---
@st.cache_data
def load_data():
    file_path = "choi_news_2013_2025.csv"
    try:
        # Try reading with different encodings just in case
        df = pd.read_csv(file_path, encoding='utf-8')
    except:
        df = pd.read_csv(file_path, encoding='utf-8-sig')
        
    # Parse Dates
    df['PubDate'] = pd.to_datetime(df['Date'], format='%a, %d %b %Y %H:%M:%S %z', errors='coerce')
    df = df.dropna(subset=['PubDate'])
    df['PubYear'] = df['PubDate'].dt.year
    df['PubMonth'] = df['PubDate'].dt.month
    df['YearMonth'] = df['PubDate'].dt.to_period('M').astype(str)
    
    return df

try:
    df = load_data()
except Exception as e:
    st.error(f"데이터 파일(choi_news_2013_2025.csv)을 찾을 수 없거나 읽는 중 오류가 발생했습니다: {e}")
    st.stop()

# --- 3. Sidebar Filtering ---
st.sidebar.header("🔍 필터 설정")

# Year Range Slider
min_year = int(df['PubYear'].min())
max_year = int(df['PubYear'].max())
selected_years = st.sidebar.slider(
    "기간 선택 (연도)",
    min_year, max_year, (min_year, max_year)
)

# Filter Data
filtered_df = df[
    (df['PubYear'] >= selected_years[0]) & 
    (df['PubYear'] <= selected_years[1])
]

# --- 4. Main Dashboard ---
st.title("🍳 최강록 셰프 미디어 화제성 분석")
st.markdown(f"**분석 기간:** {selected_years[0]}년 ~ {selected_years[1]}년 | **데이터 출처:** 네이버 뉴스")

# Top Metrics
col1, col2, col3, col4 = st.columns(4)
total_articles = len(filtered_df)
peak_year = filtered_df['PubYear'].value_counts().idxmax() if not filtered_df.empty else "-"
peak_count = filtered_df['PubYear'].value_counts().max() if not filtered_df.empty else 0

# Keyword Extraction for filtered data
all_text = " ".join(filtered_df['Title'].fillna("").astype(str) + " " + filtered_df['Description'].fillna("").astype(str))
words = re.findall(r'[가-힣]+', all_text)
stopwords = ['최강록', '셰프', '요리', '출연', '등', '이', '가', '을', '를', '의', '에', '와', '과', '은', '는', '있다', '했다', '하는', '있는', '한', '으로', '로', '그리고', '다', '못', '안', '게', '거', '것', '수', '올리브', '방송', '프로그램', '시즌', '우승', '차지', '화제', '공개', '지난', '최근', '넷플릭스', '유튜브']
filtered_words = [w for w in words if len(w) > 1 and w not in stopwords]
top_keyword = Counter(filtered_words).most_common(1)[0][0] if filtered_words else "-"

col1.metric("총 기사 수", f"{total_articles:,}건")
col2.metric("최대 화제 연도", f"{peak_year}년", f"{peak_count}건")
col3.metric("최다 등장 키워드", top_keyword)
col4.metric("분석 대상 기간", f"{selected_years[1] - selected_years[0] + 1}년")

st.divider()

# --- 5. Timeline Chart (Interactive) ---
st.subheader("📈 연도별 기사 발행 추이")

year_counts = filtered_df['PubYear'].value_counts().sort_index().reset_index()
year_counts.columns = ['Year', 'Count']

fig = px.bar(
    year_counts, 
    x='Year', 
    y='Count', 
    text='Count',
    color='Count',
    color_continuous_scale='Viridis',
    labels={'Year': '연도', 'Count': '기사 수'},
    title=f"연도별 언론 노출량 ({selected_years[0]}~{selected_years[1]})"
)
fig.update_traces(textposition='outside')
fig.update_layout(xaxis=dict(type='category')) # Ensure all years are shown
st.plotly_chart(fig, use_container_width=True)

# --- 6. Deep Dive Analysis Row ---
col_deep1, col_deep2 = st.columns([1, 1])

with col_deep1:
    st.subheader("☁️ 주요 키워드 워드클라우드")
    if filtered_words:
        # Font path for Windows (Malgun Gothic)
        font_path = "C:/Windows/Fonts/malgun.ttf"
        
        wc = WordCloud(
            font_path=font_path,
            width=800, 
            height=600, 
            background_color='white',
            colormap='viridis'
        ).generate_from_frequencies(Counter(filtered_words))
        
        fig_wc, ax = plt.subplots(figsize=(10, 6))
        ax.imshow(wc, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig_wc)
    else:
        st.warning("분석할 텍스트 데이터가 부족합니다.")

with col_deep2:
    st.subheader("📰 연도별 주요 이슈 탐색")
    
    # Year Selector for specific details
    available_years = sorted(filtered_df['PubYear'].unique(), reverse=True)
    if available_years:
        selected_target_year = st.selectbox("자세히 볼 연도를 선택하세요:", available_years)
        
        target_df = filtered_df[filtered_df['PubYear'] == selected_target_year]
        
        # Keywords for that year
        target_text = " ".join(target_df['Title'].fillna("").astype(str) + " " + target_df['Description'].fillna("").astype(str))
        target_words = re.findall(r'[가-힣]+', target_text)
        target_filtered = [w for w in target_words if len(w) > 1 and w not in stopwords]
        target_top_kw = [w[0] for w in Counter(target_filtered).most_common(7)]
        
        st.write(f"**[{selected_target_year}년 핵심 키워드]**")
        st.info(", ".join(target_top_kw) if target_top_kw else "키워드 없음")
        
        st.write(f"**[{selected_target_year}년 주요 뉴스 헤드라인 Top 5]**")
        unique_titles = target_df['Title'].unique()[:5]
        for idx, title in enumerate(unique_titles, 1):
            clean_title = title.replace("<b>", "").replace("</b>", "").replace("&quot;", "'")
            st.write(f"{idx}. {clean_title}")
    else:
        st.write("해당 기간에 데이터가 없습니다.")

# --- 7. Data Grid ---
st.divider()
st.subheader("📋 전체 데이터 조회")
with st.expander("원본 데이터 보기"):
    st.dataframe(
        filtered_df[['PubDate', 'Title', 'Link']].sort_values(by='PubDate', ascending=False),
        use_container_width=True,
        column_config={
            "PubDate": "발행일",
            "Title": "기사 제목",
            "Link": st.column_config.LinkColumn("링크")
        }
    )
