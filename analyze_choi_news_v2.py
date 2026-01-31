import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re
import os
import sys

# Set font for Korean display (Malgun Gothic for Windows)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

def analyze_news(file_path):
    print(f"Analyzing file: {file_path}", flush=True)
    
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    # --- FIX: Parse Publication Date ---
    # Naver API Date Format: "Fri, 30 Jan 2026 10:30:00 +0900"
    df['PubDate'] = pd.to_datetime(df['Date'], format='%a, %d %b %Y %H:%M:%S %z', errors='coerce')
    
    # Drop rows where date parsing failed
    df = df.dropna(subset=['PubDate'])
    
    # Extract Year from Publication Date
    df['PubYear'] = df['PubDate'].dt.year
    
    # 1. Yearly Trend Analysis (Based on Publication Year)
    year_counts = df['PubYear'].value_counts().sort_index()
    
    print("\n[연도별 기사 발행 건수 (발행일 기준)]")
    print(year_counts)
    
    # Visualization: Yearly Trend
    plt.figure(figsize=(12, 6))
    bars = sns.barplot(x=year_counts.index, y=year_counts.values, palette='viridis')
    plt.title('최강록 셰프 연도별 언론 노출 추이 (발행일 기준)')
    plt.xlabel('발행 연도')
    plt.ylabel('기사 발행 건수')
    
    # Add numbers on top of bars
    for i, v in enumerate(year_counts.values):
        plt.text(i, v + 5, str(v), ha='center', va='bottom')
        
    plt.tight_layout()
    plt.savefig('choi_news_timeline_corrected.png')
    print("\n수정된 타임라인 차트가 'choi_news_timeline_corrected.png'로 저장되었습니다.")

    # 2. Keyword Analysis (Simple)
    # Combine Title and Description
    all_text = " ".join(df['Title'].fillna("").astype(str) + " " + df['Description'].fillna("").astype(str))
    
    # Simple Korean filtering
    words = re.findall(r'[가-힣]+', all_text)
    
    # Stopwords
    stopwords = ['최강록', '셰프', '요리', '출연', '등', '이', '가', '을', '를', '의', '에', '와', '과', '은', '는', '있다', '했다', '하는', '있는', '한', '으로', '로', '그리고', '다', '못', '안', '게', '거', '것', '수', '올리브', '방송', '프로그램', '시즌', '우승', '차지', '화제', '공개', '지난', '최근', '넷플릭스', '유튜브']
    
    filtered_words = [w for w in words if len(w) > 1 and w not in stopwords]
    
    print("\n[상위 20개 키워드 (전체 기간)]")
    common_words = Counter(filtered_words).most_common(20)
    for word, count in common_words:
        print(f"{word}: {count}")

    # 3. Year-by-Year Summary (Based on PubYear)
    print("\n" + "="*50)
    print("[연도별 주요 테마 (발행일 기준)]")
    print("="*50)

    for year in sorted(df['PubYear'].unique()):
        year_df = df[df['PubYear'] == year]
        count = len(year_df)
        
        if count < 5: continue # Skip years with very few articles to reduce noise
        
        # Combine text for this year
        year_text = " ".join(year_df['Title'].fillna("").astype(str) + " " + year_df['Description'].fillna("").astype(str))
        year_words = re.findall(r'[가-힣]+', year_text)
        year_filtered = [w for w in year_words if len(w) > 1 and w not in stopwords]
        
        # Top 5 keywords
        if not year_filtered:
            top_keywords = []
        else:
            top_keywords = [w[0] for w in Counter(year_filtered).most_common(5)]
        
        print(f"\n>> {year}년 (Articles: {count})")
        print(f"   Keywords: {', '.join(top_keywords)}")
        
        unique_titles = year_df['Title'].unique()
        print(f"   Key Headlines:")
        for title in unique_titles[:3]:
            
            clean_title = title.replace("<b>", "").replace("</b>", "").replace("&quot;", "'")
            print(f"   - {clean_title}")

if __name__ == "__main__":
    filename = "choi_news_2013_2025.csv"
    if os.path.exists(filename):
        target_file = filename
    elif os.path.exists(os.path.join("csv_파일", filename)):
        target_file = os.path.join("csv_파일", filename)
    else:
        print(f"File not found: {filename}")
        sys.exit()
        
    # Redirect stdout to a file for capture
    original_stdout = sys.stdout
    with open("choi_summary.txt", "w", encoding="utf-8") as f:
        sys.stdout = f
        analyze_news(target_file)
        sys.stdout = original_stdout
    
    print(f"Analysis complete. Results saved to choi_summary.txt")
