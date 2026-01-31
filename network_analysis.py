import pandas as pd
import os
import matplotlib.pyplot as plt
import networkx as nx
from collections import Counter
import itertools

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

base_path = r"c:\Users\pc\Desktop\mypyproject\black\흑백요리사\csv_파일"
output_path = r"c:\Users\pc\Desktop\mypyproject\black\흑백요리사"

def create_chef_network():
    """셰프와 주요 키워드 간의 연관어 네트워크 시각화"""
    
    # 1. 데이터 로드 (전체 통합, 예외 처리 강화)
    all_files = [f for f in os.listdir(base_path) if f.endswith(".csv")]
    dfs = []
    for file in all_files:
        file_path = os.path.join(base_path, file)
        try:
            # 다양한 옵션으로 시도 (잘못된 라인 건너뛰기 포함)
            df = pd.read_csv(file_path, encoding='utf-8', on_bad_lines='skip', low_memory=False)
        except:
            try:
                df = pd.read_csv(file_path, encoding='cp949', on_bad_lines='skip', low_memory=False)
            except:
                print(f"Skipping problematic file: {file}")
                continue
        
        # 'text' 컬럼이 있는 경우만 사용
        if 'text' in df.columns:
            dfs.append(df[['text']])
    
    if not dfs:
        print("데이터를 불러오지 못했습니다.")
        return
        
    full_df = pd.concat(dfs, ignore_index=True).dropna()
    comments = full_df['text'].astype(str).tolist()

    # 2. 분석 대상 엔티티 정의
    chefs = ['안성재', '백종원', '최현석', '임성근', '정지선', '최강록']
    themes = ['심사', '인성', '가격', '조작', '재미', '실망', '편집', '진실']
    all_entities = chefs + themes

    # 3. 공출현(Co-occurrence) 계산
    co_occurrence = Counter()
    for comment in comments:
        present_entities = [e for e in all_entities if e in comment]
        if len(present_entities) > 1:
            # 한 댓글에 등장한 단어들의 모든 조합을 찾아 카운트
            for pair in itertools.combinations(sorted(present_entities), 2):
                co_occurrence[pair] += 1

    # 4. 네트워크 그래프 생성
    G = nx.Graph()
    
    # 노드 추가 및 속성 설정
    for entity in all_entities:
        category = 'chef' if entity in chefs else 'theme'
        G.add_node(entity, category=category)

    # 엣지(연결선) 추가 (빈도가 높은 것 위주로)
    max_weight = 0
    for (u, v), weight in co_occurrence.items():
        if weight > 5: # 최소 5회 이상 같이 언급된 경우만 연결
            G.add_edge(u, v, weight=weight)
            max_weight = max(max_weight, weight)

    # 5. 시각화 레이아웃 설정
    plt.figure(figsize=(15, 12))
    pos = nx.spring_layout(G, k=1.5, seed=42) # 노드 간 거리를 넓게 퍼뜨림
    
    # 노드 색상/크기 설정
    node_colors = ['#E50914' if G.nodes[n]['category'] == 'chef' else '#555555' for n in G.nodes()]
    node_sizes = [3500 if G.nodes[n]['category'] == 'chef' else 2000 for n in G.nodes()]

    # 엣지 굵기 설정 (가중치에 비례)
    edges = G.edges()
    weights = [G[u][v]['weight'] / max_weight * 10 for u, v in edges]

    # 그리기
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes, alpha=0.9)
    nx.draw_networkx_edges(G, pos, width=weights, edge_color='gray', alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_size=14, font_family='Malgun Gothic', font_weight='bold', font_color='white')

    plt.title("흑백요리사 셰프-키워드 연관 네트워크 (Social Association Map)", fontsize=22, fontweight='bold', color='white', pad=30)
    plt.tight_layout()
    
    # 배경색 지정하여 저장
    plt.savefig(os.path.join(output_path, 'chef_keyword_network.png'), dpi=150, facecolor='#1a1a1a')
    plt.close()
    print("✓ Saved: chef_keyword_network.png")

if __name__ == "__main__":
    create_chef_network()
