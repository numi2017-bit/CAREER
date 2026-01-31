import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
from datetime import datetime
import numpy as np

# 한글 폰트 및 스타일 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('dark_background')

base_path = r"c:\Users\pc\Desktop\mypyproject\black\흑백요리사\csv_파일"
output_path = r"c:\Users\pc\Desktop\mypyproject\black\흑백요리사"

def create_user_journey_flowchart():
    """넷플릭스-유튜브 유저 유입 여정 시각화 (Flow Chart)"""
    G = nx.DiGraph()
    
    # 노드 정의
    nodes = {
        'Netflix': '넷플릭스\n(본편 시청)',
        'Interest': '흥미 유발\n(명장면/논란)',
        'YouTube': '유튜브 검색\n(안성재/최강록)',
        'Fandom': '팬덤 형성\n(댓글/밈 소비)',
        'Revisit': '넷플릭스 재유입\n(N차 관람/시즌2)'
    }
    
    # 엣지(흐름) 정의
    edges = [
        ('Netflix', 'Interest'),
        ('Interest', 'YouTube'),
        ('YouTube', 'Fandom'),
        ('Fandom', 'Revisit'),
        ('Revisit', 'Netflix') # 선순환 고리 완성
    ]
    
    pos = {
        'Netflix': (0, 1),
        'Interest': (1, 1),
        'YouTube': (2, 0.5),
        'Fandom': (1, 0),
        'Revisit': (0, 0)
    }
    
    plt.figure(figsize=(12, 8), facecolor='#121212')
    
    # 노드 그리기
    nx.draw_networkx_nodes(G, pos, nodelist=nodes.keys(), node_color='#E50914', node_size=6000, alpha=0.9)
    
    # 라벨 그리기 (한글)
    labels = {k: v for k, v in nodes.items()}
    nx.draw_networkx_labels(G, pos, labels, font_family='Malgun Gothic', font_size=12, font_color='white', font_weight='bold')
    
    # 화살표 그리기 (가시성 개선: 겹침 방지 및 머리 강조)
    # node_size=6000이므로 반지름은 약 sqrt(6000/pi)*2 정도. 
    # 화살표가 노드 경계에서 멈추도록 min_source_margin, min_target_margin 설정 필요하지만 networkx 기본 기능 한계
    # 대신 connectionstyle의 'rad' 값을 조정하고 arrowstyle을 변경하여 가시성 확보
    
    nx.draw_networkx_edges(
        G, pos, 
        edgelist=edges, 
        edge_color='white', 
        arrows=True, 
        arrowstyle='-|>',  # 날카로운 화살표 스타일
        arrowsize=60,      # 크기 대폭 확대
        width=4, 
        connectionstyle="arc3,rad=0.1",
        node_size=6000     # 노드 크기를 알려줘서 경계 계산 유도
    )
    
    plt.title("오리지널 IP의 선순환 구조 (Flywheel Effect)", fontsize=24, color='white', pad=30, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'user_journey_flowchart.png'), dpi=150, bbox_inches='tight', facecolor='#121212')
    plt.close()
    print("✓ Saved: user_journey_flowchart.png")

def create_engagement_heatmap():
    """시간대별/요일별 댓글 참여 히트맵"""
    
    # 데이터 로드 (모든 CSV 통합)
    all_files = [f for f in os.listdir(base_path) if f.endswith(".csv")]
    dates = []
    
    print("히트맵 데이터 로딩 중...")
    for file in all_files:
        try:
            file_path = os.path.join(base_path, file)
            # 인코딩 처리
            try:
                df = pd.read_csv(file_path, encoding='utf-8')
            except:
                try:
                    df = pd.read_csv(file_path, encoding='cp949')
                except:
                    continue
            
            if 'published_at' in df.columns:
                # 날짜 형식 파싱 (ISO 8601 등 처리)
                # 유튜브 API 날짜 포맷은 보통 "2024-10-01T12:00:00Z" 형태
                # 에러 방지를 위해 문자열 처리
                valid_dates = df['published_at'].dropna().astype(str).tolist()
                dates.extend(valid_dates)
        except:
            continue
            
    if not dates:
        print("날짜 데이터가 없습니다.")
        return

    # 날짜 처리
    processed_dates = []
    for d in dates:
        try:
            # 다양한 날짜 형식 대응
            d = d.replace('Z', '') # UTC Z 제거
            if 'T' in d:
                dt = datetime.strptime(d.split('.')[0], "%Y-%m-%dT%H:%M:%S")
            else:
                dt = datetime.strptime(d, "%Y-%m-%d %H:%M:%S")
            processed_dates.append(dt)
        except:
            pass # 파싱 실패한 날짜는 무시
            
    df_time = pd.DataFrame(processed_dates, columns=['datetime'])
    df_time['hour'] = df_time['datetime'].dt.hour
    df_time['weekday'] = df_time['datetime'].dt.day_name()
    
    # 요일 순서 정렬
    weekdays_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekdays_ko = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    
    # 피벗 테이블 생성 (요일 x 시간)
    pivot_table = df_time.pivot_table(index='weekday', columns='hour', aggfunc='size', fill_value=0)
    pivot_table = pivot_table.reindex(weekdays_order)
    
    # 시각화
    plt.figure(figsize=(16, 8))
    sns.heatmap(pivot_table, cmap='YlOrRd', linewidths=0.5, linecolor='#121212', fmt='d')
    
    plt.title('시간대별/요일별 유튜브 댓글 유입 히트맵 (Engagement Heatmap)', fontsize=15, color='white', pad=20)
    plt.xlabel('시간 (Hour)', color='white')
    plt.ylabel('요일 (Weekday)', color='white')
    plt.xticks(color='white')
    plt.yticks(ticks=np.arange(7)+0.5, labels=weekdays_ko, rotation=0, color='white')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'engagement_heatmap.png'), dpi=150, bbox_inches='tight', facecolor='#121212')
    plt.close()
    print(f"✓ Saved: engagement_heatmap.png (데이터: {len(df_time):,}건)")

if __name__ == "__main__":
    create_user_journey_flowchart()
    create_engagement_heatmap()
