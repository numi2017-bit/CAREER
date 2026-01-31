import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

base_path = r"c:\Users\pc\Desktop\mypyproject\black\흑백요리사\csv_파일"
output_path = r"c:\Users\pc\Desktop\mypyproject\black\흑백요리사"

def create_season2_negative_top5_bar():
    """시즌 2 실제 부정 키워드 TOP 5 막대 그래프 생성"""
    
    # 데이터 로드 (시즌 2 필터링)
    all_files = [f for f in os.listdir(base_path) if f.endswith(".csv")]
    season2_dfs = []
    
    for file in all_files:
        if "S2" in file or "_s2" in file or "시즌2" in file:
            try:
                file_path = os.path.join(base_path, file)
                try:
                    df = pd.read_csv(file_path, encoding='utf-8')
                except:
                    try:
                        df = pd.read_csv(file_path, encoding='cp949')
                    except:
                        continue
                if 'text' in df.columns:
                    season2_dfs.append(df)
            except:
                continue
    
    if not season2_dfs:
        print("시즌 2 데이터가 없습니다.")
        return

    full_text = pd.concat(season2_dfs, ignore_index=True)['text'].dropna().astype(str).tolist()
    
    # 핵심 부정 키워드 목록 (워드클라우드와 동일한 기준 적용)
    # 단, 의미가 겹치는 단어는 그룹핑 (예: 노잼/재미없 -> 재미)
    negative_keywords_map = {
        '실망': '실망/아쉬움', '아쉽': '실망/아쉬움', 
        '노잼': '재미없음', '재미없': '재미없음', '지루': '재미없음',
        '최악': '완성도 미흡', '미흡': '완성도 미흡', '별로': '완성도 미흡',
        '가격': '가격/비쌈', '비싸': '가격/비쌈', '창렬': '가격/비쌈', '돈아깝': '가격/비쌈',
        '대본': '공정성/조작', '조작': '공정성/조작', '주작': '공정성/조작', '짜고': '공정성/조작'
    }
    
    found_keywords = []
    
    for text in full_text:
        for key, category in negative_keywords_map.items():
            if key in text:
                found_keywords.append(category)
                # 한 댓글에서 같은 카테고리 중복 카운트 방지
                # (예: '노잼이고 재미없다' -> 1번만 카운트하려면 여기서 break하거나 set 사용해야 함. 여기선 빈도수 중요하므로 단순 append)
                
    keyword_counts = Counter(found_keywords)
    top5 = keyword_counts.most_common(5)
    
    # 데이터프레임 변환
    df_top5 = pd.DataFrame(top5, columns=['Keyword', 'Count'])
    
    # 시각화
    plt.figure(figsize=(10, 6))
    bars = sns.barplot(data=df_top5, x='Count', y='Keyword', palette='Reds_r', edgecolor='black')
    
    # 수치 표시
    for i, p in enumerate(bars.patches):
        width = p.get_width()
        plt.text(width + 5, p.get_y() + p.get_height()/2, 
                 f'{int(width)}건', 
                 va='center', fontweight='bold', fontsize=12)
        
    plt.title('시즌 2 핵심 이탈 원인 TOP 5 (부정 키워드)', fontsize=15, weight='bold', pad=20)
    plt.xlabel('언급 수 (건)')
    plt.ylabel('')
    plt.grid(axis='x', linestyle='--', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'season2_negative_top5_bar.png'), dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ Saved: season2_negative_top5_bar.png")

if __name__ == "__main__":
    create_season2_negative_top5_bar()
