import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re
import numpy as np

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

base_path = r"c:\Users\pc\Desktop\mypyproject\black\흑백요리사"
output_path = base_path

# 긍정/부정 키워드 사전 (간단한 버전)
POSITIVE_WORDS = ['좋다', '최고', '대단', '멋있', '훌륭', '감동', '재밌', '웃기', '귀엽', '이쁘', '예쁘', '사랑', '완벽', '최고', '굿', '좋아', '존경', '대박', '짱']
NEGATIVE_WORDS = ['싫다', '별로', '최악', '나쁘', '못하', '실망', '짜증', '화나', '싫어', '재수없', '밉상', '거만', '싸가지', '똥', '쓰레기']

def load_video_info():
    """비디오 메타데이터 로드"""
    search_result_path = os.path.join(base_path, "흑백요리사_검색결과.csv")
    if os.path.exists(search_result_path):
        try:
            df = pd.read_csv(search_result_path, encoding='utf-8')
            return df
        except:
            try:
                df = pd.read_csv(search_result_path, encoding='cp949')
                return df
            except Exception as e:
                print(f"Error loading metadata: {e}")
    return None

def analyze_sentiment(text):
    """간단한 감성 분석"""
    text_lower = text.lower()
    pos_count = sum(1 for word in POSITIVE_WORDS if word in text_lower)
    neg_count = sum(1 for word in NEGATIVE_WORDS if word in text_lower)
    
    if pos_count > neg_count:
        return 'positive'
    elif neg_count > pos_count:
        return 'negative'
    else:
        return 'neutral'

def create_wordcloud(words_dict, title, filename, color='positive'):
    """키워드 막대 그래프 생성 (워드클라우드 대체)"""
    if not words_dict:
        return
    
    # 상위 30개 키워드
    top_words = sorted(words_dict.items(), key=lambda x: x[1], reverse=True)[:30]
    if not top_words:
        return
    
    words, counts = zip(*top_words)
    
    # 색상 설정
    if color == 'positive':
        bar_color = '#4ECDC4'
    elif color == 'negative':
        bar_color = '#FF6B6B'
    else:
        bar_color = '#95E1D3'
    
    plt.figure(figsize=(12, 10))
    plt.barh(range(len(words)), counts, color=bar_color, alpha=0.8)
    plt.yticks(range(len(words)), words, fontsize=10)
    plt.xlabel('빈도', fontsize=12)
    plt.title(title, fontsize=14, pad=15)
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, filename), dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {filename}")

def analyze_comments_enhanced(video_map=None):
    """댓글 분석 - 감성분석 및 워드클라우드 포함"""
    comment_files = [f for f in os.listdir(base_path) if f.endswith("_comments.csv")]
    
    # 각 비디오별 색상 팔레트
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
    
    fig, axes = plt.subplots(len(comment_files), 1, figsize=(12, 4 * len(comment_files)))
    if len(comment_files) == 1:
        axes = [axes]
    
    plt.subplots_adjust(hspace=0.5)
    
    all_positive_words = Counter()
    all_negative_words = Counter()

    for idx, file in enumerate(comment_files):
        video_id = file.split("_")[0]
        video_title = video_id
        
        if video_map is not None and 'videoId' in video_map.columns:
            match = video_map[video_map['videoId'] == video_id]
            if not match.empty:
                video_title = match.iloc[0]['title']
                if len(video_title) > 35:
                    video_title = video_title[:33] + "..."

        file_path = os.path.join(base_path, file)
        try:
            df = pd.read_csv(file_path, encoding='utf-8')
        except:
            try:
                df = pd.read_csv(file_path, encoding='cp949')
            except:
                continue

        if 'text' not in df.columns:
            continue
        
        # 감성 분석
        df['sentiment'] = df['text'].astype(str).apply(analyze_sentiment)
        
        # 키워드 추출
        text_data = df['text'].astype(str).tolist()
        words = []
        positive_words = []
        negative_words = []
        
        for i, text in enumerate(text_data):
            cleaned = re.sub(r'[^가-힣a-zA-Z0-9\s]', '', text)
            text_words = [w for w in cleaned.split() if len(w) > 1]
            words.extend(text_words)
            
            sentiment = df.iloc[i]['sentiment']
            if sentiment == 'positive':
                positive_words.extend(text_words)
            elif sentiment == 'negative':
                negative_words.extend(text_words)
        
        # 전체 키워드 카운트
        word_counts = Counter(words)
        top_words = word_counts.most_common(10)
        
        if top_words:
            keywords, counts = zip(*top_words)
            
            # 각 비디오마다 다른 색상 사용
            axes[idx].barh(keywords, counts, color=colors[idx % len(colors)])
            axes[idx].set_title(f"{video_title}\n(긍정: {sum(df['sentiment']=='positive')} | 부정: {sum(df['sentiment']=='negative')})", 
                               fontsize=11, pad=10)
            axes[idx].invert_yaxis()
            axes[idx].set_xlabel('빈도', fontsize=9)
        
        # 긍정/부정 워드 누적
        all_positive_words.update(positive_words)
        all_negative_words.update(negative_words)
    
    plt.tight_layout()
    chart_path = os.path.join(output_path, "comment_analysis_colorful.png")
    plt.savefig(chart_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: comment_analysis_colorful.png")
    
    # 워드클라우드 생성
    if all_positive_words:
        create_wordcloud(dict(all_positive_words.most_common(50)), 
                        '긍정 댓글 워드클라우드', 
                        'wordcloud_positive.png', 
                        'positive')
    
    if all_negative_words:
        create_wordcloud(dict(all_negative_words.most_common(50)), 
                        '부정 댓글 워드클라우드', 
                        'wordcloud_negative.png', 
                        'negative')

def analyze_youtube_rankings_enhanced():
    """유튜브 조회수 순위 - 개선된 시각화"""
    ranking_path = os.path.join(base_path, "흑백요리사_검색결과_시청순위.csv")
    if os.path.exists(ranking_path):
        try:
            try:
                df = pd.read_csv(ranking_path, encoding='cp949')
            except:
                df = pd.read_csv(ranking_path, encoding='utf-8')
                
            if 'viewCount' in df.columns and 'title' in df.columns:
                df['viewCount'] = pd.to_numeric(df['viewCount'], errors='coerce')
                df = df.dropna(subset=['viewCount'])
                top_10 = df.sort_values('viewCount', ascending=False).head(10)
                
                # 그라디언트 색상
                colors_gradient = plt.cm.viridis(np.linspace(0, 1, len(top_10)))
                
                plt.figure(figsize=(14, 8))
                bars = plt.barh(range(len(top_10)), top_10['viewCount'], color=colors_gradient)
                
                # 제목 설정 (짧게)
                labels = [t[:40] + '...' if len(t) > 40 else t for t in top_10['title']]
                plt.yticks(range(len(top_10)), labels)
                
                plt.xlabel('조회수', fontsize=12)
                plt.title('유튜브 조회수 TOP 10', fontsize=14, pad=15)
                plt.gca().invert_yaxis()
                
                # 값 표시
                for i, (bar, val) in enumerate(zip(bars, top_10['viewCount'])):
                    plt.text(val, i, f' {val:,.0f}', va='center', fontsize=9)
                
                plt.tight_layout()
                yt_chart_path = os.path.join(output_path, "youtube_top_views_colorful.png")
                plt.savefig(yt_chart_path, dpi=150, bbox_inches='tight')
                plt.close()
                print(f"Saved: youtube_top_views_colorful.png")
                
        except Exception as e:
            print(f"Error visualizing YouTube rankings: {e}")

def analyze_netflix_simple():
    """넷플릭스 데이터 간단 분석 - 시즌별 비교"""
    excel_path = os.path.join(base_path, "2025-12-21_global_weekly.xlsx")
    if os.path.exists(excel_path):
        try:
            # 청크로 읽기 (메모리 절약)
            df_ex = pd.read_excel(excel_path, nrows=10000)  # 처음 10000행만
            
            # 흑백요리사 필터링
            mask = df_ex['show_title'].str.contains('Culinary Class Wars|흑백요리사', case=False, na=False)
            df_show = df_ex[mask]
            
            if not df_show.empty and 'season_title' in df_show.columns:
                seasons = df_show['season_title'].unique()
                print(f"Found seasons: {seasons}")
                
                # 시즌별 국가 수 비교
                season_country_count = df_show.groupby('season_title')['country_name'].nunique()
                
                plt.figure(figsize=(10, 6))
                colors_bar = ['#FF6B6B', '#4ECDC4']
                season_country_count.plot(kind='bar', color=colors_bar[:len(season_country_count)])
                plt.title('시즌별 진출 국가 수 비교', fontsize=14)
                plt.xlabel('시즌', fontsize=12)
                plt.ylabel('국가 수', fontsize=12)
                plt.xticks(rotation=45)
                plt.tight_layout()
                
                netflix_path = os.path.join(output_path, "netflix_season_comparison.png")
                plt.savefig(netflix_path, dpi=150, bbox_inches='tight')
                plt.close()
                print(f"Saved: netflix_season_comparison.png")
                
        except Exception as e:
            print(f"Netflix analysis error: {e}")

if __name__ == "__main__":
    print("=== 흑백요리사 데이터 분석 시작 ===\n")
    
    vmap = load_video_info()
    
    print("[1/3] 댓글 분석 (감성분석 + 워드클라우드)...")
    analyze_comments_enhanced(vmap)
    
    print("\n[2/3] 유튜브 조회수 분석...")
    analyze_youtube_rankings_enhanced()
    
    print("\n[3/3] 넷플릭스 시즌 비교...")
    analyze_netflix_simple()
    
    print("\n=== 분석 완료! ===")
