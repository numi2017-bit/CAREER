import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(16, 9), facecolor='#121212')
ax.set_facecolor('#121212')
ax.axis('off')

# 제목
plt.text(0.5, 0.92, '2026 흑백요리사 IP 가치 극대화 & 리텐션 로드맵', 
         ha='center', va='center', fontsize=28, color='white', fontweight='bold')
plt.text(0.5, 0.86, '"2.1억 원의 손실 방어와 강력한 IP 락인(Lock-in) 전략"', 
         ha='center', va='center', fontsize=16, color='#E50914', style='italic')

# 로드맵 단계 설정
steps = [
    {
        "title": "Step 1. Defense",
        "subtitle": "[구독 가치 재정립]",
        "solve": "식당 예약 우선권(Fast Track)",
        "effect": "가격 저항(89건) 즉각 해소",
        "color": "#E50914",
        "pos": (0.2, 0.55)
    },
    {
        "title": "Step 2. Quality",
        "subtitle": "[신뢰 회복]",
        "solve": "국민 심사단 100인 도입",
        "effect": "인성/공정성 불만을 효능감으로 반전",
        "color": "#F5A623",
        "pos": (0.5, 0.55)
    },
    {
        "title": "Step 3. Expansion",
        "subtitle": "[IP 유니버스 확장]",
        "solve": "임성근x최강록 스핀오프",
        "effect": "ROI 2.1억 및 위험팬 해지 방어",
        "color": "#50E3C2",
        "pos": (0.8, 0.55)
    }
]

# 원형 및 텍스트 배치
for s in steps:
    circle = plt.Circle(s["pos"], 0.12, color=s["color"], alpha=0.8)
    ax.add_patch(circle)
    plt.text(s["pos"][0], s["pos"][1]+0.02, s["title"], ha='center', va='center', fontsize=18, fontweight='bold', color='white')
    plt.text(s["pos"][0], s["pos"][1]-0.03, s["subtitle"], ha='center', va='center', fontsize=14, color='white')
    
    # 하단 상세 설명
    plt.text(s["pos"][0], s["pos"][1]-0.18, f"해결: {s['solve']}", ha='center', va='top', fontsize=13, color='white', fontweight='bold')
    plt.text(s["pos"][0], s["pos"][1]-0.23, f"효과: {s['effect']}", ha='center', va='top', fontsize=11, color='#ADB5BD')

# 골든타임 케어 영역 (하단 박스 디자인 개선)
# FancyBboxPatch를 사용하여 안정적인 라운드 박스 구현
box = patches.FancyBboxPatch((0.15, 0.08), 0.7, 0.12, 
                            boxstyle="round,pad=0.02", 
                            linewidth=2, edgecolor='#E50914', facecolor='#1A1A1A')
ax.add_patch(box)

plt.text(0.5, 0.16, "📍 [Golden Time Care] 매주 수요일 22:00 정기 푸시 전략", 
         ha='center', fontsize=16, color='#E50914', fontweight='bold')
plt.text(0.5, 0.11, "최강록 B-컷 & 임성근 바이럴 숏폼 정기 공개 | CU 콜라보 2차 상품 기획", 
         ha='center', fontsize=13, color='#ADB5BD')

# 화살표 연결 (디자인 디테일)
for i in range(len(steps)-1):
    plt.annotate('', xy=(steps[i+1]["pos"][0]-0.1, steps[i+1]["pos"][1]), 
                 xytext=(steps[i]["pos"][0]+0.1, steps[i]["pos"][1]),
                 arrowprops=dict(arrowstyle='->', lw=2, color='#444'))

plt.tight_layout()
# 흑백요리사 폴더에 저장
plt.savefig(r'c:\Users\pc\Desktop\mypyproject\black\흑백요리사\final_strategy_roadmap.png', dpi=200, bbox_inches='tight')

print("픽스된 최종 전략 로드맵 슬라이드가 '흑백요리사' 폴더에 생성되었습니다.")
