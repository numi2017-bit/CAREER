import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np

# 한글 폰트 설정 (Windows)
font_path = 'C:/Windows/Fonts/malgun.ttf'

# 데이터 기반 최강록 핵심 키워드 및 빈도 (강레오 & 최강록.csv 분석 결과 반영)
text_data = {
    '조리보이': 100, '바질을 곁들인': 85, '만화책': 70, '나야 들기름': 65,
    '파도 맛있습니다': 80, '조림': 75, '팬덤': 60, '매력': 55,
    '요리만화': 50, '독보적': 45, '조림요정': 40, '어록': 38,
    '탈락결정전': 35, '진심': 30, '장인': 28, '창의성': 25
}

# 넷플릭스 브랜드 테마 컬러 함수 (Red, White, Gray 조합)
def netflix_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    colors = ['#E50914', '#ffffff', '#888888', '#555555']
    return np.random.choice(colors)

# 워드클라우드 생성
wc = WordCloud(
    font_path=font_path,
    background_color='black',
    width=800,
    height=800,
    max_words=100,
    relative_scaling=0.5,
    color_func=netflix_color_func
).generate_from_frequencies(text_data)

plt.figure(figsize=(10, 10))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.title('Choi Kang-rok Character Word Cloud', fontsize=20, pad=20, color='white')

plt.tight_layout(pad=0)
# 흑백요리사 폴더에 저장
plt.savefig(r'c:\Users\pc\Desktop\mypyproject\black\흑백요리사\choi_wordcloud.png', dpi=150)

print("최강록 워드클라우드가 '흑백요리사' 폴더에 생성되었습니다.")
