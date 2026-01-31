import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np

# 한글 폰트 설정 (Windows)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
font_path = 'C:/Windows/Fonts/malgun.ttf'

# 키워드 밀도 높이기 (최강록 데이터 분석 반영)
text_data = {
    '조리보이': 120, '바질을 곁들인': 110, '만화책': 95, '나야 들기름': 90,
    '파도 맛있습니다': 100, '조림요정': 80, '팬덤': 75, '매력': 70,
    '요리만화': 65, '독보적': 60, '어록': 55, '탈락결정전': 50,
    '바질장인': 85, '들기름마스터': 80, '도인': 45, '진심': 40,
    '셰프님의 숲': 35, '창의성': 40, '마스터': 55, '전설적인': 30,
    '상큼함': 25, '리듬': 28, '조림의신': 60, '팬들의사랑': 45
}

# 에메랄드 그린 컬러 함수 (White Background Optimized)
def green_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    # 흰 배경에서 가독성이 좋은 딥그린, 에메랄드, 올리브 컬러군
    colors = ['#004d00', '#013220', '#006400', '#228B22', '#2E8B57']
    return np.random.choice(colors)

# 워드클라우드 생성 (반복 기능을 켜서 빽빽하게 채움)
wc = WordCloud(
    font_path=font_path,
    background_color='white',
    width=1000,
    height=800,
    max_words=300, # 단어 수를 늘림
    relative_scaling=0.3, # 크기 차이를 약간 줄여 빈틈 차단
    prefer_horizontal=0.8,
    color_func=green_color_func,
    repeat=True, # 중요! 단어를 반복해서 빈 공간을 꽉 채움
    margin=2     # 간격을 최소화
).generate_from_frequencies(text_data)

plt.figure(figsize=(12, 10), facecolor='white')
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')

# 제목 한글화 및 디자인 (폰트 강제 설정)
plt.title('최강록 캐릭터 IP 핵심 키워드 분석', fontsize=24, pad=40, color='#004d00', fontweight='bold', fontname='Malgun Gothic')

plt.tight_layout(pad=0)
# 흑백요리사 폴더에 저장
plt.savefig(r'c:\Users\pc\Desktop\mypyproject\black\흑백요리사\choi_wordcloud.png', dpi=200, bbox_inches='tight')

print("빈틈없이 꽉 찬 한글 타이틀 워드클라우드가 생성되었습니다.")
