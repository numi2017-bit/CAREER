import pandas as pd
import os
import matplotlib.pyplot as plt
from collections import Counter
import re
from wordcloud import WordCloud

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

base_path = r"c:\Users\pc\Desktop\mypyproject\black\흑백요리사"
output_path = base_path

# 긍정 표현 (감정을 나타내는 단어만)
POSITIVE_WORDS = {
    '좋다', '좋아', '좋네', '좋은', '좋았', '최고', '대단', '멋있', '멋지', '멋진', '훌륭', 
    '감동', '재밌', '재미있', '재밌다', '웃기', '웃겨', '웃긴', '웃겼', '귀엽', '귀여워', 
    '귀엽다', '이쁘', '이쁜', '예쁘', '예쁜', '사랑', '사랑스', '완벽', '굿', '존경', 
    '대박', '짱', '개웃', '졸귀', '킹', '갓', '감탄', '훌륭하', '이쁘다', '예쁘다',
    '좋아요', '최고다', '멋있다', '대단하', '좋구만', '좋겠', '좋소', '훌륭한', '멋지다',
    '재밌네', '웃기네', '귀엽네', '이쁘네', '예쁘네', '감동적', '최고네', '대박이',
    '개꿀', '꿀잼', '핵꿀', '핵인싸', '레전드', '갓벽', '개이득'
}

# 부정 표현 (감정을 나타내는 단어만)
NEGATIVE_WORDS = {
    '싫다', '싫어', '싫은', '별로', '최악', '나쁘', '나빠', '나쁜', '못하', '못해', 
    '실망', '짜증', '화나', '화난', '재수없', '밉상', '거만', '싸가지', '똥', '쓰레기', 
    '개같', '킹받', '빡치', '열받', '짜증나', '실망스', '최악이', '나쁘다', '못한다',
    '실망이', '화난다', '재수없다', '밉상이', '거만하', '싸가지없', '개별로', '노잼',
    '실망했', '화났', '짜증났', '킹받네', '빡쳤', '열받네', '최악이다', '별로네',
    '못하네', '실망스럽', '재수없네', '밉상이네', '거만하네', '개노답', '핵노잼'
}

def extract_sentiment_words(text):
    """텍스트에서 감성 표현 단어만 추출"""
    text_lower = text.lower()
    
    positive_found = []
    negative_found = []
    
    # 긍정 단어 찾기
    for word in POSITIVE_WORDS:
        if word in text_lower:
            positive_found.append(word)
    
    # 부정 단어 찾기
    for word in NEGATIVE_WORDS:
        if word in text_lower:
            negative_found.append(word)
    
    return positive_found, negative_found

def create_real_wordcloud(words_dict, title, filename, sentiment='positive'):
    """진짜 워드클라우드 생성"""
    if not words_dict:
        print(f"No words for {filename}")
        return
    
    # 색상 설정
    if sentiment == 'positive':
        colormap = 'Blues'
        bg_color = '#F0F8FF'
    elif sentiment == 'negative':
        colormap = 'Reds'
        bg_color = '#FFF0F0'
    else:
        colormap = 'Greens'
        bg_color = '#F0FFF0'
    
    # 워드클라우드 생성
    wc = WordCloud(
        font_path='C:/Windows/Fonts/malgun.ttf',
        width=1200,
        height=800,
        background_color=bg_color,
        colormap=colormap,
        max_words=100,
        relative_scaling=0.5,
        min_font_size=10
    ).generate_from_frequencies(words_dict)
    
    # 시각화
    plt.figure(figsize=(15, 10))
    plt.imshow(wc, interpolation='bilinear')
    plt.title(title, fontsize=20, pad=20, weight='bold')
    plt.axis('off')
    plt.tight_layout(pad=0)
    
    save_path = os.path.join(output_path, filename)
    plt.savefig(save_path, dpi=200, bbox_inches='tight', facecolor=bg_color)
    plt.close()
    print(f"✓ Saved: {filename}")

def analyze_all_comments():
    """모든 댓글 분석 및 워드클라우드 생성"""
    comment_files = [f for f in os.listdir(base_path) if f.endswith("_comments.csv")]
    
    all_positive_words = Counter()
    all_negative_words = Counter()
    all_words = Counter()
    
    print(f"\n분석 중인 파일: {len(comment_files)}개\n")

    for file in comment_files:
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
        
        # 키워드 추출
        for text in df['text'].astype(str):
            # 전체 단어 추출
            cleaned = re.sub(r'[^가-힣a-zA-Z0-9\s]', '', text)
            words = [w for w in cleaned.split() if len(w) > 1]
            all_words.update(words)
            
            # 감성 표현 단어만 추출
            pos_words, neg_words = extract_sentiment_words(text)
            all_positive_words.update(pos_words)
            all_negative_words.update(neg_words)
        
        print(f"  처리 완료: {file}")
    
    print(f"\n긍정 표현: {len(all_positive_words)}개 (총 {sum(all_positive_words.values())}회)")
    print(f"부정 표현: {len(all_negative_words)}개 (총 {sum(all_negative_words.values())}회)")
    print(f"전체 키워드: {len(all_words)}개\n")
    
    # 워드클라우드 생성
    print("워드클라우드 생성 중...\n")
    
    if all_positive_words:
        create_real_wordcloud(
            dict(all_positive_words), 
            '긍정 표현 워드클라우드', 
            'wordcloud_positive_real.png',
            'positive'
        )
    
    if all_negative_words:
        create_real_wordcloud(
            dict(all_negative_words), 
            '부정 표현 워드클라우드', 
            'wordcloud_negative_real.png',
            'negative'
        )
    
    if all_words:
        create_real_wordcloud(
            dict(all_words), 
            '전체 댓글 워드클라우드', 
            'wordcloud_all.png',
            'neutral'
        )
    
    # 순위표 생성
    print("\n키워드 순위표 생성 중...\n")
    create_ranking_tables(all_positive_words, all_negative_words, all_words)
    
    print("\n✅ 워드클라우드 생성 완료!")
    print(f"\n저장 위치: {output_path}")

def create_ranking_tables(positive_words, negative_words, all_words):
    """키워드 순위표 생성"""
    
    # 1. 긍정 표현 TOP 30
    if positive_words:
        top_positive = positive_words.most_common(30)
        
        fig, ax = plt.subplots(figsize=(10, 12))
        ax.axis('tight')
        ax.axis('off')
        
        table_data = [['순위', '긍정 표현', '빈도']]
        for i, (word, count) in enumerate(top_positive, 1):
            table_data.append([f'{i}위', word, f'{count:,}'])
        
        table = ax.table(cellText=table_data, cellLoc='center', loc='center',
                        colWidths=[0.2, 0.5, 0.3])
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1, 2)
        
        # 헤더 스타일
        for i in range(3):
            table[(0, i)].set_facecolor('#4ECDC4')
            table[(0, i)].set_text_props(weight='bold', color='white')
        
        # 행 색상 교차
        for i in range(1, len(table_data)):
            for j in range(3):
                if i % 2 == 0:
                    table[(i, j)].set_facecolor('#F0F8FF')
        
        plt.title('긍정 표현 TOP 30', fontsize=16, weight='bold', pad=20)
        plt.savefig(os.path.join(output_path, 'ranking_positive.png'), 
                   dpi=150, bbox_inches='tight')
        plt.close()
        print("✓ Saved: ranking_positive.png")
    
    # 2. 부정 표현 TOP 30
    if negative_words:
        top_negative = negative_words.most_common(30)
        
        fig, ax = plt.subplots(figsize=(10, 12))
        ax.axis('tight')
        ax.axis('off')
        
        table_data = [['순위', '부정 표현', '빈도']]
        for i, (word, count) in enumerate(top_negative, 1):
            table_data.append([f'{i}위', word, f'{count:,}'])
        
        table = ax.table(cellText=table_data, cellLoc='center', loc='center',
                        colWidths=[0.2, 0.5, 0.3])
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1, 2)
        
        # 헤더 스타일
        for i in range(3):
            table[(0, i)].set_facecolor('#FF6B6B')
            table[(0, i)].set_text_props(weight='bold', color='white')
        
        # 행 색상 교차
        for i in range(1, len(table_data)):
            for j in range(3):
                if i % 2 == 0:
                    table[(i, j)].set_facecolor('#FFF0F0')
        
        plt.title('부정 표현 TOP 30', fontsize=16, weight='bold', pad=20)
        plt.savefig(os.path.join(output_path, 'ranking_negative.png'), 
                   dpi=150, bbox_inches='tight')
        plt.close()
        print("✓ Saved: ranking_negative.png")
    
    # 3. 전체 키워드 TOP 50
    if all_words:
        top_all = all_words.most_common(50)
        
        fig, ax = plt.subplots(figsize=(12, 16))
        ax.axis('tight')
        ax.axis('off')
        
        table_data = [['순위', '키워드', '빈도']]
        for i, (word, count) in enumerate(top_all, 1):
            table_data.append([f'{i}위', word, f'{count:,}'])
        
        table = ax.table(cellText=table_data, cellLoc='center', loc='center',
                        colWidths=[0.2, 0.5, 0.3])
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1, 2)
        
        # 헤더 스타일
        for i in range(3):
            table[(0, i)].set_facecolor('#95E1D3')
            table[(0, i)].set_text_props(weight='bold', color='white')
        
        # 행 색상 교차
        for i in range(1, len(table_data)):
            for j in range(3):
                if i % 2 == 0:
                    table[(i, j)].set_facecolor('#F0FFF0')
        
        plt.title('전체 키워드 TOP 50', fontsize=16, weight='bold', pad=20)
        plt.savefig(os.path.join(output_path, 'ranking_all.png'), 
                   dpi=150, bbox_inches='tight')
        plt.close()
        print("✓ Saved: ranking_all.png")

if __name__ == "__main__":
    print("=" * 50)
    print("흑백요리사 워드클라우드 생성기 (최종 버전)")
    print("=" * 50)
    analyze_all_comments()
