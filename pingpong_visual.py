import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

# 한글 폰트 및 스타일 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('dark_background')

output_path = r"c:\Users\pc\Desktop\mypyproject\black\흑백요리사"

def create_pingpong_traffic_flow():
    """유튜브-넷플릭스 핑퐁 트래픽 Flow Chart 시각화"""
    
    fig, ax = plt.figure(figsize=(16, 8)), plt.gca()
    ax.set_facecolor('#1a1a1a')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 50)
    ax.axis('off')
    
    # --- 좌측: NETFLIX (Basecamp) ---
    # 박스
    rect_nf = patches.FancyBboxPatch((5, 10), 25, 30, boxstyle="round,pad=1", linewidth=0, facecolor='#E50914')
    ax.add_patch(rect_nf)
    # 텍스트
    ax.text(17.5, 30, "NETFLIX", ha='center', va='center', color='white', fontweight='bold', fontsize=24)
    ax.text(17.5, 20, "Original Content\n(본편 시청)", ha='center', va='center', color='white', fontsize=14)
    
    # --- 우측: YOUTUBE (Viral Ground) ---
    # 박스
    rect_yt = patches.FancyBboxPatch((70, 10), 25, 30, boxstyle="round,pad=1", linewidth=0, facecolor='#FF0000')
    ax.add_patch(rect_yt)
    # 텍스트
    ax.text(82.5, 30, "YOUTUBE", ha='center', va='center', color='white', fontweight='bold', fontsize=24)
    ax.text(82.5, 20, "Viral Clips\n(밈/쇼츠 소비)", ha='center', va='center', color='white', fontsize=14)
    
    # --- 중앙: PING-PONG Traffic ---
    
    # 1. Netflix -> Youtube (흥미 유발)
    arrow1 = patches.FancyArrowPatch((32, 35), (68, 35), connectionstyle="arc3,rad=-0.2", 
                                     mutation_scale=25, color='#ffffff', linewidth=3, linestyle='--')
    ax.add_patch(arrow1)
    ax.text(50, 43, "관심 발생: 검색 & 밈 탐색", ha='center', va='center', color='white', fontsize=16, fontweight='bold')
    
    # 2. Youtube -> Netflix (재유입/Lock-in) - 더 굵게 강조!
    arrow2 = patches.FancyArrowPatch((68, 15), (32, 15), connectionstyle="arc3,rad=-0.2", 
                                     mutation_scale=35, color='#FFD700', linewidth=6) # 골드 컬러로 강조
    ax.add_patch(arrow2)
    
    # 상세 텍스트 (조회수 1위 영상 언급) -> 위치 조정 및 가시성 극대화
    # LOCK-IN 텍스트에 배경 박스 추가
    ax.text(50, 12, "LOCK-IN (재유입)", ha='center', va='top', color='#FFD700', fontweight='bold', fontsize=28,
            bbox=dict(facecolor='black', edgecolor='#FFD700', linewidth=2, alpha=0.9))
            
    ax.text(50, 4, "Trigger: 조회수 TOP 10 콘텐츠\n(예: 안성재 급식대가 영상 1,100만 회)", 
            ha='center', va='top', color='white', fontsize=14, fontweight='bold',
            bbox=dict(facecolor='#333333', edgecolor='white', linewidth=1, alpha=0.9))

    # 타이틀
    ax.text(50, 48, "User Behavior Flow: The Ping-Pong Effect", ha='center', va='center', color='white', fontweight='bold', fontsize=20)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'pingpong_traffic_flow.png'), dpi=150, bbox_inches='tight', facecolor='#1a1a1a')
    plt.close()
    print("✓ Saved: pingpong_traffic_flow.png")

if __name__ == "__main__":
    create_pingpong_traffic_flow()
