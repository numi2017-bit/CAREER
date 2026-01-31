import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

# 한글 폰트 및 스타일 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('dark_background')

output_path = r"c:\Users\pc\Desktop\mypyproject\black\흑백요리사"

def create_strategy_roadmap():
    """3단계 전략 로드맵 시각화"""
    
    fig, ax = plt.figure(figsize=(16, 8)), plt.gca()
    
    # 배경 설정 (타임라인 느낌)
    ax.set_facecolor('#1a1a1a')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 50)
    ax.axis('off')
    
    # 화살표 (전체 흐름)
    arrow = patches.FancyArrowPatch((5, 25), (95, 25), mutation_scale=30, color='#333333', linewidth=20, zorder=0)
    ax.add_patch(arrow)

    # --- Step 1. Defense ---
    # 원
    circle1 = patches.Circle((20, 25), radius=8, color='#E50914', alpha=0.9, zorder=2)
    ax.add_patch(circle1)
    # 텍스트
    ax.text(20, 25, "Step 1\nDefense\n(방어)", ha='center', va='center', color='white', fontweight='bold', fontsize=14, zorder=3)
    ax.text(20, 12, "위험팬 4,300명\n골든타임 케어\n(수요일 밤 10시)", ha='center', va='top', color='#cccccc', fontsize=11, zorder=3)
    # 아이콘/효과 (텍스트 대체)
    ax.text(20, 36, "[DEFENSE]\n구독료 2억 방어", ha='center', va='center', color='#FFCDD2', fontweight='bold', fontsize=12, zorder=3)


    # --- Step 2. Expansion ---
    # 원
    circle2 = patches.Circle((50, 25), radius=8, color='#FFA726', alpha=0.9, zorder=2)
    ax.add_patch(circle2)
    # 텍스트
    ax.text(50, 25, "Step 2\nExpansion\n(확장)", ha='center', va='center', color='black', fontweight='bold', fontsize=14, zorder=3)
    ax.text(50, 12, "바이럴 1위(임성근)\n유튜브 스핀오프\n제작 & 런칭", ha='center', va='top', color='#cccccc', fontsize=11, zorder=3)
    # 효과
    ax.text(50, 36, "[VIRAL]\n공백기 트래픽 유지", ha='center', va='center', color='#FFE0B2', fontweight='bold', fontsize=12, zorder=3)


    # --- Step 3. Monetization ---
    # 원
    circle3 = patches.Circle((80, 25), radius=8, color='#66BB6A', alpha=0.9, zorder=2)
    ax.add_patch(circle3)
    # 텍스트
    ax.text(80, 25, "Step 3\nMonetization\n(수익화)", ha='center', va='center', color='black', fontweight='bold', fontsize=14, zorder=3)
    ax.text(80, 12, "긍정 키워드 기반\nCU 편의점 2차\n콜라보 기획", ha='center', va='top', color='#cccccc', fontsize=11, zorder=3)
    # 효과
    ax.text(80, 36, "[PROFIT]\nIP 비즈니스 확장", ha='center', va='center', color='#C8E6C9', fontweight='bold', fontsize=12, zorder=3)

    # 연결선 (점선)
    # ax.plot([28, 42], [25, 25], color='white', linestyle='--', linewidth=2, zorder=1)
    # ax.plot([58, 72], [25, 25], color='white', linestyle='--', linewidth=2, zorder=1)

    # 타이틀
    ax.text(50, 45, "넷플릭스 흑백요리사 IP 가치 극대화 로드맵 (2026)", ha='center', va='center', color='white', fontweight='bold', fontsize=20)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'strategy_roadmap.png'), dpi=150, bbox_inches='tight', facecolor='#1a1a1a')
    plt.close()
    print("✓ Saved: strategy_roadmap.png")

if __name__ == "__main__":
    create_strategy_roadmap()
