import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

def save_slide(filename, title, subtitle):
    fig, ax = plt.subplots(figsize=(16, 9), facecolor='#121212')
    ax.set_facecolor('#121212')
    ax.axis('off')
    plt.text(0.05, 0.92, title, ha='left', va='center', fontsize=28, color='white', fontweight='bold')
    plt.text(0.05, 0.85, subtitle, ha='left', va='center', fontsize=16, color='#E50914', style='italic')
    return fig, ax

# --- Page 3: 3단계 전략 로드맵 상세 ---
fig, ax = save_slide('report_page_3_roadmap.png', 'STRATEGY: IP 가치 극대화 로드맵', '"푸시 알림은 시작일 뿐, 우리의 목표는 IP 유니버스다."')

steps = [
    {"num": "Step 1", "title": "Defense (가격 저항 해소)", "sub": "[구독 가치 재정립]", "solve": "식당 예약 우선권(Fast Track) 추첨", "effect": "13,500원 구독료를 '예약권 가치'로 전환\n가격 저항(89건) 즉각 해소", "color": "#E50914", "x": 0.2},
    {"num": "Step 2", "title": "Quality (퀄리티 회복)", "sub": "[유저 참여형 심사제]", "solve": "시즌 3 '블라인드 국민 심사단' 도입", "effect": "인성/공정성 불만을 '우리가 만드는 방송'으로 반전\n코어 팬덤 투입을 통한 투명성 확보", "color": "#F5A623", "x": 0.5},
    {"num": "Step 3", "title": "Expansion (확장/수입화)", "sub": "[IP 유니버스 가동]", "solve": "임성근x최강록 더블 엔진 스핀오프", "effect": "최강록 '만화책 식당' 등 팬덤 맞춤형 콘텐츠\n위험팬(4,356명) 해지 방어 (ROI 2.1억)", "color": "#50E3C2", "x": 0.8}
]

for s in steps:
    rect = patches.FancyBboxPatch((s['x']-0.12, 0.35), 0.24, 0.45, boxstyle="round,pad=0.02", linewidth=1, edgecolor=s['color'], facecolor='#1A1A1A')
    ax.add_patch(rect)
    plt.text(s['x'], 0.75, s['num'], ha='center', fontsize=20, color=s['color'], fontweight='bold')
    plt.text(s['x'], 0.70, s['title'], ha='center', fontsize=15, color='white', fontweight='bold')
    plt.text(s['x'], 0.65, s['sub'], ha='center', fontsize=13, color=s['color'])
    plt.text(s['x'], 0.55, f"● 해결: {s['solve']}", ha='center', fontsize=12, color='white', fontweight='bold')
    plt.text(s['x'], 0.43, s['effect'], ha='center', fontsize=11, color='#ADB5BD', linespacing=1.6)

plt.savefig(r'c:\Users\pc\Desktop\mypyproject\black\흑백요리사\report_page_3_roadmap.png', dpi=150, bbox_inches='tight')

# --- Page 4: 실행 과제 및 골든타임 케어 ---
fig, ax = save_slide('report_page_4_execution.png', 'EXECUTION: 2.1억을 지키는 3대 액션', '"위험기(Churn Zone)를 수익 창출의 골든타임으로"')

# 3대 액션 섹션
actions = [
    {"t": "1. 구독 유인 (Reward)", "c": "셰프 식당 패스트트랙 이벤트", "e": "'구독을 유지해야 식당에 갈 수 있다'\n강력한 락인(Lock-in) 동기부여"},
    {"t": "2. 참여 유도 (Interactive)", "c": "국민 심사단 100인 모집", "e": "유저를 '제작 파트너'로 격상\n인성/공정성 불만 잠재우기"},
    {"t": "3. 지속 노출 (Retention)", "c": "수요일 밤 10시 정기 푸시", "e": "최강록 B-컷 & 임성근 바이럴 숏폼\n탐색 마비 유저의 습관적 재방문 유도"}
]

y = 0.65
for a in actions:
    plt.text(0.1, y, a['t'], fontsize=20, color='#E50914', fontweight='bold')
    plt.text(0.1, y-0.05, f"내용: {a['c']}", fontsize=15, color='white')
    plt.text(0.1, y-0.1, f"효과: {a['e']}", fontsize=13, color='#ADB5BD')
    y -= 0.22

# 골든타임 케어 포인트
rect = patches.FancyBboxPatch((0.6, 0.2), 0.35, 0.5, boxstyle="round,pad=0.03", facecolor='#1A1A1A', edgecolor='#50E3C2', linewidth=2)
ax.add_patch(rect)
plt.text(0.775, 0.63, "Golden Time Care", ha='center', fontsize=22, color='#50E3C2', fontweight='bold')
plt.text(0.775, 0.53, "매주 수요일 22:00", ha='center', fontsize=18, color='white')
plt.text(0.775, 0.43, "CU 콜라보 상품 기획\n긍정 키워드 기반 수익화", ha='center', fontsize=14, color='white', linespacing=1.8)

plt.savefig(r'c:\Users\pc\Desktop\mypyproject\black\흑백요리사\report_page_4_execution.png', dpi=150, bbox_inches='tight')

print("리포트가 4장의 상세 페이지로 분리되어 생성되었습니다.")
