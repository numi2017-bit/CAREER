import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

# 한글 폰트 및 스타일 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('dark_background')

output_path = r"c:\Users\pc\Desktop\mypyproject\black\흑백요리사"

def create_strategy_roadmap_v2():
    """3단계 전략 로드맵 시각화 V2 (내실 강화 포함)"""
    
    fig, ax = plt.figure(figsize=(16, 8)), plt.gca()
    
    # 배경 설정 (타임라인 느낌)
    ax.set_facecolor('#1a1a1a')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 50)
    ax.axis('off')
    
    # 화살표 (전체 흐름)
    arrow = patches.FancyArrowPatch((5, 25), (95, 25), mutation_scale=30, color='#333333', linewidth=20, zorder=0)
    ax.add_patch(arrow)

    # --- Step 1. Defense (가격 저항 해소) ---
    # 원
    circle1 = patches.Circle((20, 25), radius=8, color='#E50914', alpha=0.9, zorder=2)
    ax.add_patch(circle1)
    # 텍스트
    ax.text(20, 25, "Step 1\nDefense\n(구독 가치 재정립)", ha='center', va='center', color='white', fontweight='bold', fontsize=13, zorder=3)
    ax.text(20, 12, "문제: 넷플릭스 비싸다\n해결: 식당 예약 우선권\n추첨 제공 (멤버십)", ha='center', va='top', color='#cccccc', fontsize=11, zorder=3)
    # 효과 (텍스트 대체)
    ax.text(20, 36, "[VALUE UP]\n가격 저항 완화", ha='center', va='center', color='#FFCDD2', fontweight='bold', fontsize=12, zorder=3)


    # --- Step 2. Quality (퀄리티 회복) ---
    # 원
    circle2 = patches.Circle((50, 25), radius=8, color='#FFA726', alpha=0.9, zorder=2)
    ax.add_patch(circle2)
    # 텍스트
    ax.text(50, 25, "Step 2\nQuality\n(신뢰 회복)", ha='center', va='center', color='black', fontweight='bold', fontsize=13, zorder=3)
    ax.text(50, 12, "문제: 심사 불공정\n해결: 블라인드\n국민 심사단 도입", ha='center', va='top', color='#cccccc', fontsize=11, zorder=3)
    # 효과
    ax.text(50, 36, "[TRUST]\n참여형 팬덤 강화", ha='center', va='center', color='#FFE0B2', fontweight='bold', fontsize=12, zorder=3)


    # --- Step 3. Expansion (확장 & 수익화) ---
    # 원
    circle3 = patches.Circle((80, 25), radius=8, color='#66BB6A', alpha=0.9, zorder=2)
    ax.add_patch(circle3)
    # 텍스트
    ax.text(80, 25, "Step 3\nExpansion\n(IP 유니버스)", ha='center', va='center', color='black', fontweight='bold', fontsize=13, zorder=3)
    ax.text(80, 12, "임성근 스핀오프 예능\n+\n편의점 상품 라인업", ha='center', va='top', color='#cccccc', fontsize=11, zorder=3)
    # 효과
    ax.text(80, 36, "[SCALE UP]\n비즈니스 모델 확장", ha='center', va='center', color='#C8E6C9', fontweight='bold', fontsize=12, zorder=3)


    # 타이틀
    ax.text(50, 45, "넷플릭스 흑백요리사 IP 가치 극대화 로드맵 (2026)", ha='center', va='center', color='white', fontweight='bold', fontsize=20)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'strategy_roadmap_v2.png'), dpi=150, bbox_inches='tight', facecolor='#1a1a1a')
    plt.close()
    print("✓ Saved: strategy_roadmap_v2.png")

if __name__ == "__main__":
    create_strategy_roadmap_v2()
