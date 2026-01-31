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

def create_season2_negative_top5_bar_v4():
    """시즌 2 실제 부정 키워드 TOP 5 막대 그래프 생성 V4 (보고서 용어 대신 '진짜 키워드' 사용)"""
    
    # 데이터 로드
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
    
    # 키워드 매핑: 추상적 카테고리(X) -> 대표 단어(O)
    # 여러 변형을 가장 많이 쓰인 대표 단어로 통일
    negative_keywords_map = {
        '실망': '실망', '아쉽': '실망', 
        '노잼': '노잼', '재미없': '노잼', '지루': '노잼',
        '최악': '최악', '미흡': '최악', '별로': '최악', 
        '가격': '가격', '비싸': '가격', '창렬': '가격', '돈아깝': '가격',
        '대본': '주작/대본', '조작': '주작/대본', '주작': '주작/대본', '짜고': '주작/대본',
        # 인성 관련
        '인성': '인성', '싸가지': '인성', '거만': '인성', 
        '태도': '인성', '무례': '인성', '예의': '인성',
        '화나': '화남', '짜증': '화남', '불편': '화남'
    }
    
    found_keywords = []
    
    for text in full_text:
        for key, category in negative_keywords_map.items():
            if key in text:
                found_keywords.append(category)
                
    keyword_counts = Counter(found_keywords)
    top5 = keyword_counts.most_common(5)
    
    # 데이터프레임
    df_top5 = pd.DataFrame(top5, columns=['Keyword', 'Count'])
    
    # 시각화
    plt.figure(figsize=(10, 6))
    bars = sns.barplot(data=df_top5, x='Count', y='Keyword', palette='Reds_r', edgecolor='black')
    
    for i, p in enumerate(bars.patches):
        width = p.get_width()
        plt.text(width + 5, p.get_y() + p.get_height()/2, 
                 f'{int(width)}건', 
                 va='center', fontweight='bold', fontsize=12)
        
    plt.title('시즌 2 핵심 이탈 원인 TOP 5 (실제 키워드)', fontsize=15, weight='bold', pad=20)
    plt.xlabel('언급 수 (건)')
    plt.ylabel('')
    plt.grid(axis='x', linestyle='--', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'season2_negative_top5_bar_v4.png'), dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ Saved: season2_negative_top5_bar_v4.png")

if __name__ == "__main__":
    create_season2_negative_top5_bar_v4()
