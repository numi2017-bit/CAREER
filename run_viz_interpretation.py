import matplotlib.pyplot as plt
import pandas as pd

# 한글 폰트 설정 (Windows)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 데이터 설정
rankings = [
    {"rank": "1위", "keyword": "조리보이", "desc": "자발적 팬덤이 만든 밈 코어\n마케팅 비용 없는 트래픽 엔진"},
    {"rank": "2위", "keyword": "바질을 곁들인", "desc": "독보적 브랜드 정체성 확립\n'고집 있는 캐릭터'에 대한 로열티"},
    {"rank": "3위", "keyword": "나야 들기름", "desc": "유저 간 상호작용 언어(밈)\n커뮤니티 내 앱 체류 시간 증대"},
    {"rank": "4위", "keyword": "만화책", "desc": "인간미 있는 성장 서사(Origin)\n심리적 락인(Lock-in)의 핵심"}
]

fig, ax = plt.subplots(figsize=(12, 8), facecolor='white')
ax.axis('off')

# 제목
plt.title('최강록 캐릭터 IP 전략적 키워드 해석', fontsize=26, pad=30, fontweight='bold', color='#004d00')

# 내용 배치
y_pos = 0.8
for item in rankings:
    # 순위 및 키워드
    plt.text(0.1, y_pos, f"{item['rank']}  |  {item['keyword']}", fontsize=20, fontweight='bold', color='#006400')
    # 상세 설명
    plt.text(0.1, y_pos - 0.08, item['desc'], fontsize=14, color='#333', linespacing=1.6)
    
    # 구분선
    ax.axhline(y=y_pos - 0.12, xmin=0.08, xmax=0.92, color='#eee', linestyle='-', linewidth=1)
    
    y_pos -= 0.2

# 캡션 (출처)
plt.text(0.1, 0.05, "출처: 유튜브 댓글 여론 분석 (강레오 & 최강록.csv) 및 넷플릭스 유저 센티멘트 기반", fontsize=10, color='#999')

plt.tight_layout()
# 흑백요리사 폴더에 저장
plt.savefig(r'c:\Users\pc\Desktop\mypyproject\black\흑백요리사\choi_keyword_strategy.png', dpi=150, bbox_inches='tight')

print("키워드 전략 해석 차트가 생성되었습니다.")
