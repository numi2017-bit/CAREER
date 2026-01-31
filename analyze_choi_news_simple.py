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

    # 1. Yearly Trend Analysis
    year_counts = df['Year'].value_counts().sort_index()
    
    print("\n[Yearly Article Count]")
    print(year_counts)
    
    # Visualization: Yearly Trend
    plt.figure(figsize=(12, 6))
    bars = sns.barplot(x=year_counts.index, y=year_counts.values, palette='viridis')
    plt.title('Choi Kang-rok News Mencions by Year (2013-2025)')
    plt.xlabel('Year')
    plt.ylabel('Number of Articles')
    
    # Add numbers on top of bars
    for i, v in enumerate(year_counts.values):
        plt.text(i, v + 10, str(v), ha='center', va='bottom')
        
    plt.tight_layout()
    plt.savefig('choi_news_timeline.png')
    print("\nTimeline chart saved as 'choi_news_timeline.png'")

    # 2. Keyword Analysis (Simple)
    # Combine Title and Description
    all_text = " ".join(df['Title'].fillna("").astype(str) + " " + df['Description'].fillna("").astype(str))
    
    # Simple Korean filtering (keep Hangul only for keywords)
    hangul = re.compile('[^ \u3131-\u3163\uac00-\ud7a3]+')
    # This regex actually removes Hangul? No, I want to keep Hangul.
    # Let's extract Hangul words:
    words = re.findall(r'[가-힣]+', all_text)
    
    # Stopwords (Basic list)
    stopwords = ['최강록', '셰프', '요리', '출연', '등', '이', '가', '을', '를', '의', '에', '와', '과', '은', '는', '있다', '했다', '하는', '있는', '한', '으로', '로', '그리고', '다', '못', '안', '게', '거', '것', '수', '올리브', '방송', '프로그램', '시즌', '우승', '차지', '화제', '공개', '지난', '최근', '넷플릭스', '유튜브']
    
    filtered_words = [w for w in words if len(w) > 1 and w not in stopwords]
    
    print("\n[Top 20 Frequent Keywords]")
    common_words = Counter(filtered_words).most_common(20)
    for word, count in common_words:
        print(f"{word}: {count}")

    # 3. Year-by-Year Summary
    print("\n" + "="*50)
    print("[Year-by-Year Key Themes]")
    print("="*50)

    for year in sorted(df['Year'].unique()):
        year_df = df[df['Year'] == year]
        count = len(year_df)
        
        # Combine text for this year
        year_text = " ".join(year_df['Title'].fillna("").astype(str) + " " + year_df['Description'].fillna("").astype(str))
        year_words = re.findall(r'[가-힣]+', year_text)
        year_filtered = [w for w in year_words if len(w) > 1 and w not in stopwords]
        
        # Top 5 keywords for the year
        top_keywords = [w[0] for w in Counter(year_filtered).most_common(5)]
        
        print(f"\n>> {year}년 (Articles: {count})")
        print(f"   Keywords: {', '.join(top_keywords)}")
        
        # Show Top 3 representative titles (longest ones usually have more info, or just first few)
        # Using a simple heuristic: pick unique titles
        unique_titles = year_df['Title'].unique()
        print(f"   Key Headlines:")
        for title in unique_titles[:3]:
            # Clean HTML tags
            clean_title = title.replace("<b>", "").replace("</b>", "").replace("&quot;", "'")
            print(f"   - {clean_title}")

if __name__ == '__main__':
    filename = 'choi_news_2013_2025.csv'
    if os.path.exists(filename):
        target_file = filename
    elif os.path.exists(os.path.join('csv_����', filename)):
        target_file = os.path.join('csv_����', filename)
    else:
        print(f'File not found: {filename}')
        sys.exit()
        
    # Redirect stdout to a file for capture
    original_stdout = sys.stdout
    with open('choi_summary.txt', 'w', encoding='utf-8') as f:
        sys.stdout = f
        analyze_news(target_file)
        sys.stdout = original_stdout
    
    print(f'Analysis complete. Results saved to choi_summary.txt')
