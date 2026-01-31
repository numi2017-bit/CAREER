import pandas as pd
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import re

# 한글 폰트 설정 (시스템에 설치된 폰트 경로 지정 필요, 여기선 Malgun Gothic 가정)
font_path = 'C:/Windows/Fonts/malgun.ttf'

base_path = r"c:\Users\pc\Desktop\mypyproject\black\흑백요리사\csv_파일"
output_path = r"c:\Users\pc\Desktop\mypyproject\black\흑백요리사"

def generate_season2_negative_wordcloud():
    """시즌 2 부정 댓글 워드클라우드 생성"""
    
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
    print(f"시즌 2 댓글 수: {len(full_text)}개")

    # 부정 키워드 사전 (간이) - 실제 감성 분석 모델 대신 핵심 부정 키워드 필터링 사용
    # 논리적 일관성을 위해 앞서 분석한 '가격', '미흡', '실망', '조작' 등의 키워드 위주로 추출
    negative_keywords = ['실망', '노잼', '최악', '미흡', '아쉽', '별로', '재미없', '지루', 
                         '가격', '비싸', '창렬', '돈아깝', '구독료', 
                         '조작', '대본', '짜고', '주작', '편파', '공정',
                         '화나', '짜증', '불편', '싸가지', '인성', '거만']
    
    filtered_words = []
    
    for text in full_text:
        # 간단한 전처리
        text = re.sub(r'[^가-힣\s]', '', text) # 한글만 남김
        words = text.split()
        
        for word in words:
            # 부정 키워드가 포함된 단어만 수집 (어절 단위)
            for nk in negative_keywords:
                if nk in word:
                    filtered_words.append(word)
                    break
    
    if not filtered_words:
        print("추출된 부정 키워드가 없습니다.")
        return
        
    word_counts = Counter(filtered_words)
    
    # 워드클라우드 생성
    wc = WordCloud(
        font_path=font_path,
        background_color='black', # 검은 배경 (경고 느낌)
        width=1600,
        height=1000,
        colormap='Reds', # 빨간색 계열 (위험)
        max_words=100,
        prefer_horizontal=0.8
    ).generate_from_frequencies(word_counts)
    
    plt.figure(figsize=(16, 10))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis('off')
    # 한글 폰트 깨짐 방지를 위해 영문 타이틀 사용
    plt.title('Season 2 Negative Keywords (Warning)', fontsize=30, color='white', pad=20, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'wordcloud_season2_negative.png'), dpi=150, bbox_inches='tight', facecolor='black')
    plt.close()
    print("✓ Saved: wordcloud_season2_negative.png")

if __name__ == "__main__":
    generate_season2_negative_wordcloud()
