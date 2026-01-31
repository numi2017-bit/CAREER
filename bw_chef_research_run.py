
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
output_path = base_path # Artifacts save location

def load_video_info():
    """Video ID와 Title 매핑"""
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
                print(f"Error loading search results: {e}")
    return None

def analyze_comments(video_map=None):
    """댓글 키워드 분석 및 시각화"""
    if not os.path.exists(base_path):
        return

    comment_files = [f for f in os.listdir(base_path) if f.endswith("_comments.csv")]
    
    # 5개 파일 각각에 대해 상위 10개 키워드 시각화
    fig, axes = plt.subplots(len(comment_files), 1, figsize=(10, 4 * len(comment_files)))
    if len(comment_files) == 1: axes = [axes]
    
    plt.subplots_adjust(hspace=0.5)

    for i, file in enumerate(comment_files):
        video_id = file.split("_")[0]
        video_title = video_id
        
        if video_map is not None and 'videoId' in video_map.columns:
             match = video_map[video_map['videoId'] == video_id]
             if not match.empty:
                 video_title = match.iloc[0]['title']
                 # 제목이 너무 길면 자르기
                 if len(video_title) > 30:
                     video_title = video_title[:28] + "..."

        file_path = os.path.join(base_path, file)
        try:
            df = pd.read_csv(file_path, encoding='utf-8') # 기본 utf-8 시도
        except:
            try:
                df = pd.read_csv(file_path, encoding='cp949')
            except:
                continue

        if 'text' not in df.columns:
            continue
        
        text_data = df['text'].astype(str).tolist()
        words = []
        for text in text_data:
            cleaned = re.sub(r'[^가-힣a-zA-Z0-9\s]', '', text)
            for w in cleaned.split():
                if len(w) > 1:
                    words.append(w)
        
        word_counts = Counter(words)
        top_words = word_counts.most_common(10)
        
        if not top_words:
            continue
            
        keywords, counts = zip(*top_words)
        
        axes[i].barh(keywords, counts, color='skyblue')
        axes[i].set_title(f"Video: {video_title}", fontsize=12)
        axes[i].invert_yaxis() # 상위 키워드가 위로 오게

    plt.tight_layout()
    chart_path = os.path.join(output_path, "comment_analysis_chart.png")
    plt.savefig(chart_path)
    print(f"Saved comment chart to {chart_path}")


def analyze_rankings():
    """시청 순위 분석 및 시각화"""
    # 1. 흑백요리사_검색결과_시청순위.csv (Encoding issue fix)
    ranking_path = os.path.join(base_path, "흑백요리사_검색결과_시청순위.csv")
    if os.path.exists(ranking_path):
        try:
            df = pd.read_csv(ranking_path, encoding='cp949')
            # Assuming columns: 'date' and 'rank' (Need to guess or print columns)
            # If inspection showed it's Naver Trends or similar, adapt.
            # For now, print columns to be sure for next step if this fails logic.
            print("Ranking CSV Columns:", df.columns.tolist())
            
            # TODO: Implement visualization based on actual columns
            # For now, let's look at the excel mainly as it had 'weekly_rank'
        except Exception as e:
            print(f"Error reading header of ranking csv: {e}")

    # 2. Excel Analysis (South Korea specific)
    excel_path = os.path.join(base_path, "2025-12-21_global_weekly.xlsx")
    if os.path.exists(excel_path):
        try:
            df_ex = pd.read_excel(excel_path)
            target = "Culinary Class Wars"
            target_kr = "흑백요리사"
            
            # Filter for the show
            mask = df_ex.astype(str).apply(lambda x: x.str.contains(target, case=False) | x.str.contains(target_kr, case=False)).any(axis=1)
            df_show = df_ex[mask]
            
            if not df_show.empty:
                # Filter for South Korea if possible, or Global
                # Check 'country_name' column
                if 'country_name' in df_show.columns:
                    df_kr = df_show[df_show['country_name'] == 'South Korea']
                    region_label = "South Korea"
                    
                    if df_kr.empty: # If not by country, maybe it's global data list
                        df_kr = df_show # Use whatever we match
                        region_label = "Global/Available Regions"
                    
                    # Sort by week
                    if 'week' in df_kr.columns and 'weekly_rank' in df_kr.columns:
                        df_kr = df_kr.sort_values('week')
                        
                        plt.figure(figsize=(10, 6))
                        sns.lineplot(data=df_kr, x='week', y='weekly_rank', marker='o')
                        plt.gca().invert_yaxis() # 1위가 위로
                        plt.title(f"Weekly Ranking Trend ({region_label})")
                        plt.ylabel("Rank")
                        plt.xlabel("Week")
                        plt.grid(True)
                        
                        rank_chart_path = os.path.join(output_path, "viewership_ranking_trend.png")
                        plt.savefig(rank_chart_path)
                        print(f"Saved ranking chart to {rank_chart_path}")
                
        except Exception as e:
            print(f"Error processing excel: {e}")

def analyze_youtube_rankings():
    """유튜브 조회수 순위 시각화"""
    ranking_path = os.path.join(base_path, "흑백요리사_검색결과_시청순위.csv")
    if os.path.exists(ranking_path):
        try:
            # Try CP949 first for Korean CSVs usually created by Excel/Pandas on Windows
            try:
                df = pd.read_csv(ranking_path, encoding='cp949')
            except:
                df = pd.read_csv(ranking_path, encoding='utf-8')
                
            if 'viewCount' in df.columns and 'title' in df.columns:
                # Top 10 by View Count
                df['viewCount'] = pd.to_numeric(df['viewCount'], errors='coerce')
                df = df.dropna(subset=['viewCount'])
                top_10 = df.sort_values('viewCount', ascending=False).head(10)
                
                plt.figure(figsize=(12, 8))
                sns.barplot(data=top_10, y='title', x='viewCount', palette='viridis')
                plt.title("Top 10 Most Viewed YouTube Videos")
                plt.xlabel("View Count")
                plt.ylabel("Video Title")
                
                # Truncate long titles for y-axis labels
                current_labels = [label.get_text() for label in plt.gca().get_yticklabels()]
                new_labels = [l[:30] + '...' if len(l) > 30 else l for l in current_labels]
                plt.gca().set_yticklabels(new_labels)
                
                plt.tight_layout()
                yt_chart_path = os.path.join(output_path, "youtube_top_views.png")
                plt.savefig(yt_chart_path)
                print(f"Saved YouTube views chart to {yt_chart_path}")
                
        except Exception as e:
            print(f"Error visualizing YouTube rankings: {e}")

if __name__ == "__main__":
    vmap = load_video_info()
    analyze_comments(vmap)
    analyze_rankings()
    analyze_youtube_rankings()
