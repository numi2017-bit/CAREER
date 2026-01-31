import pandas as pd
import os
import matplotlib.pyplot as plt
from collections import Counter
import re
from wordcloud import WordCloud
import numpy as np

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

base_path = r"c:\Users\pc\Desktop\mypyproject\black\흑백요리사"
output_path = base_path

# 긍정/부정 표현
POSITIVE_WORDS = {
    '좋다', '좋아', '좋네', '최고', '대단', '멋있', '멋지', '훌륭', '감동', '재밌', '재미있',
    '웃기', '웃겨', '귀엽', '귀여워', '이쁘', '예쁘', '사랑', '완벽', '굿', '존경', '대박', 
    '짱', '개웃', '졸귀', '킹', '갓', '레전드', '꿀잼', '핵꿀'
}

NEGATIVE_WORDS = {
    '싫다', '싫어', '별로', '최악', '나쁘', '나빠', '못하', '못해', '실망', '짜증', '화나',
    '재수없', '밉상', '거만', '싸가지', '똥', '쓰레기', '킹받', '빡치', '열받', '노잼', '핵노잼'
}

def extract_sentiment_words(text):
    """감성 표현 단어 추출"""
    text_lower = text.lower()
    positive_found = [w for w in POSITIVE_WORDS if w in text_lower]
    negative_found = [w for w in NEGATIVE_WORDS if w in text_lower]
    return positive_found, negative_found

def analyze_season_comments(season_label, file_suffix):
    """시즌별 댓글 분석"""
    comment_files = [f for f in os.listdir(base_path) if f.endswith(f"_comments{file_suffix}.csv")]
    
    all_positive_words = Counter()
    all_negative_words = Counter()
    all_words = Counter()
    total_comments = 0
    
    print(f"\n{season_label} 분석 중... (파일: {len(comment_files)}개)")

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
        
        total_comments += len(df)
        
        for text in df['text'].astype(str):
            cleaned = re.sub(r'[^가-힣a-zA-Z0-9\s]', '', text)
            words = [w for w in cleaned.split() if len(w) > 1]
            all_words.update(words)
            
            pos_words, neg_words = extract_sentiment_words(text)
            all_positive_words.update(pos_words)
            all_negative_words.update(neg_words)
    
    print(f"  총 댓글: {total_comments:,}개")
    print(f"  긍정 표현: {sum(all_positive_words.values()):,}회")
    print(f"  부정 표현: {sum(all_negative_words.values()):,}회")
    
    return {
        'positive': all_positive_words,
        'negative': all_negative_words,
        'all': all_words,
        'total_comments': total_comments
    }

def create_comparison_charts(s1_data, s2_data):
    """시즌 1 vs 시즌 2 비교 차트 생성"""
    
    # 1. 댓글 수 비교
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    
    # 1-1. 총 댓글 수
    seasons = ['시즌 1', '시즌 2']
    comment_counts = [s1_data['total_comments'], s2_data['total_comments']]
    
    axes[0, 0].bar(seasons, comment_counts, color=['#FF6B6B', '#4ECDC4'])
    axes[0, 0].set_title('총 댓글 수 비교', fontsize=14, weight='bold')
    axes[0, 0].set_ylabel('댓글 수')
    for i, v in enumerate(comment_counts):
        axes[0, 0].text(i, v, f'{v:,}', ha='center', va='bottom', fontsize=12)
    
    # 1-2. 긍정/부정 비율
    s1_pos = sum(s1_data['positive'].values())
    s1_neg = sum(s1_data['negative'].values())
    s2_pos = sum(s2_data['positive'].values())
    s2_neg = sum(s2_data['negative'].values())
    
    x = np.arange(2)
    width = 0.35
    
    axes[0, 1].bar(x - width/2, [s1_pos, s2_pos], width, label='긍정', color='#4ECDC4')
    axes[0, 1].bar(x + width/2, [s1_neg, s2_neg], width, label='부정', color='#FF6B6B')
    axes[0, 1].set_title('긍정/부정 표현 비교', fontsize=14, weight='bold')
    axes[0, 1].set_xticks(x)
    axes[0, 1].set_xticklabels(seasons)
    axes[0, 1].set_ylabel('빈도')
    axes[0, 1].legend()
    
    # 1-3. 시즌 1 TOP 10 키워드
    s1_top = s1_data['all'].most_common(10)
    if s1_top:
        words, counts = zip(*s1_top)
        axes[1, 0].barh(range(len(words)), counts, color='#FF6B6B', alpha=0.7)
        axes[1, 0].set_yticks(range(len(words)))
        axes[1, 0].set_yticklabels(words)
        axes[1, 0].set_title('시즌 1 TOP 10 키워드', fontsize=14, weight='bold')
        axes[1, 0].invert_yaxis()
    
    # 1-4. 시즌 2 TOP 10 키워드
    s2_top = s2_data['all'].most_common(10)
    if s2_top:
        words, counts = zip(*s2_top)
        axes[1, 1].barh(range(len(words)), counts, color='#4ECDC4', alpha=0.7)
        axes[1, 1].set_yticks(range(len(words)))
        axes[1, 1].set_yticklabels(words)
        axes[1, 1].set_title('시즌 2 TOP 10 키워드', fontsize=14, weight='bold')
        axes[1, 1].invert_yaxis()
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'season_comparison.png'), dpi=200, bbox_inches='tight')
    plt.close()
    print("\n✓ Saved: season_comparison.png")

def create_wordclouds(s1_data, s2_data):
    """시즌별 워드클라우드 생성"""
    
    # 시즌 1 워드클라우드
    if s1_data['all']:
        wc = WordCloud(
            font_path='C:/Windows/Fonts/malgun.ttf',
            width=1200, height=800,
            background_color='#FFF0F0',
            colormap='Reds',
            max_words=100
        ).generate_from_frequencies(dict(s1_data['all']))
        
        plt.figure(figsize=(15, 10))
        plt.imshow(wc, interpolation='bilinear')
        plt.title('시즌 1 워드클라우드', fontsize=20, weight='bold', pad=20)
        plt.axis('off')
        plt.tight_layout(pad=0)
        plt.savefig(os.path.join(output_path, 'wordcloud_season1.png'), dpi=200, bbox_inches='tight')
        plt.close()
        print("✓ Saved: wordcloud_season1.png")
    
    # 시즌 2 워드클라우드
    if s2_data['all']:
        wc = WordCloud(
            font_path='C:/Windows/Fonts/malgun.ttf',
            width=1200, height=800,
            background_color='#F0F8FF',
            colormap='Blues',
            max_words=100
        ).generate_from_frequencies(dict(s2_data['all']))
        
        plt.figure(figsize=(15, 10))
        plt.imshow(wc, interpolation='bilinear')
        plt.title('시즌 2 워드클라우드', fontsize=20, weight='bold', pad=20)
        plt.axis('off')
        plt.tight_layout(pad=0)
        plt.savefig(os.path.join(output_path, 'wordcloud_season2.png'), dpi=200, bbox_inches='tight')
        plt.close()
        print("✓ Saved: wordcloud_season2.png")

def main():
    print("=" * 60)
    print("흑백요리사 시즌 1 vs 시즌 2 비교 분석")
    print("=" * 60)
    
    # 시즌 1 분석 (파일명에 _s2가 없는 것)
    s1_data = analyze_season_comments("시즌 1", "")
    
    # 시즌 2 분석 (파일명에 _s2가 있는 것)
    s2_data = analyze_season_comments("시즌 2", "_s2")
    
    print("\n비교 차트 생성 중...")
    create_comparison_charts(s1_data, s2_data)
    
    print("\n워드클라우드 생성 중...")
    create_wordclouds(s1_data, s2_data)
    
    print("\n" + "=" * 60)
    print("✅ 시즌 1 vs 시즌 2 비교 분석 완료!")
    print(f"저장 위치: {output_path}")
    print("=" * 60)

if __name__ == "__main__":
    main()
