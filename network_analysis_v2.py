import pandas as pd
import os
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from collections import Counter
import itertools

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

base_path = r"c:\Users\pc\Desktop\mypyproject\black\흑백요리사\csv_파일"
output_path = r"c:\Users\pc\Desktop\mypyproject\black\흑백요리사"

def create_chef_network_v2():
    """방사형 레이아웃을 적용한 세련된 연관어 네트워크 시각화 (V2)"""
    
    # 1. 데이터 로드 (Robust 버전)
    all_files = [f for f in os.listdir(base_path) if f.endswith(".csv")]
    dfs = []
    for file in all_files:
        file_path = os.path.join(base_path, file)
        try:
            df = pd.read_csv(file_path, encoding='utf-8', on_bad_lines='skip', low_memory=False)
        except:
            try:
                df = pd.read_csv(file_path, encoding='cp949', on_bad_lines='skip', low_memory=False)
            except:
                continue
        if 'text' in df.columns:
            dfs.append(df[['text']])
    
    if not dfs:
        print("데이터를 불러오지 못했습니다.")
        return
        
    full_df = pd.concat(dfs, ignore_index=True).dropna()
    comments = full_df['text'].astype(str).tolist()

    # 2. 엔티티 정의 (사용자 예시 이미지와 싱크 맞춤)
    chefs = ['안성재', '백종원', '최현석', '임성근', '정지선', '최강록']
    themes = ['심사/공정', '인성/태도', '가격/가성비', '조작/대본', '재미/기대', '실망/아쉽', '편집/루즈', '미공개/클립']
    
    # 키워드 매핑 (데이터에서 찾기 쉽게 축약)
    keyword_map = {
        '심사': '심사/공정', '공정': '심사/공정',
        '인성': '인성/태도', '태도': '인성/태도',
        '가격': '가격/가성비', '비싸': '가격/가성비',
        '조작': '조작/대본', '대본': '조작/대본', '주작': '조작/대본',
        '재미': '재미/기대', '기대': '재미/기대',
        '실망': '실망/아쉽', '아쉽': '실망/아쉽',
        '편집': '편집/루즈', '루즈': '편집/루즈',
        '미공개': '미공개/클립', '클립': '미공개/클립'
    }

    # 3. 공출현 빈도 계산
    co_occurrence = Counter()
    for comment in comments:
        found_chefs = [c for c in chefs if c in comment]
        found_themes = [keyword_map[k] for k in keyword_map if k in comment]
        
        # 셰프와 키워드 간의 연결만 집중 (더 선명한 방사형을 위해)
        for chef in found_chefs:
            for theme in set(found_themes):
                co_occurrence[(chef, theme)] += 1

    # 4. 네트워크 생성
    G = nx.Graph()
    G.add_nodes_from(chefs, category='chef')
    G.add_nodes_from(themes, category='theme')

    max_weight = 0
    for (u, v), weight in co_occurrence.items():
        if weight > 10: # 의미 있는 연결만
            G.add_edge(u, v, weight=weight)
            max_weight = max(max_weight, weight)

    # 5. 방사형 레이아웃 (Shell Layout)
    # 내부 원: 셰프, 외부 원: 테마
    pos = nx.shell_layout(G, [chefs, themes])

    plt.figure(figsize=(16, 12))
    ax = plt.gca()
    ax.set_facecolor('#111111')

    # 노드 그리기
    chef_nodes = [n for n, d in G.nodes(data=True) if d['category'] == 'chef']
    theme_nodes = [n for n, d in G.nodes(data=True) if d['category'] == 'theme']

    nx.draw_networkx_nodes(G, pos, nodelist=chef_nodes, node_color='#E50914', node_size=5000, alpha=1.0, edgecolors='white', linewidths=2)
    nx.draw_networkx_nodes(G, pos, nodelist=theme_nodes, node_color='#333333', node_size=3500, alpha=0.8, edgecolors='#555555')

    # 엣지 그리기
    for u, v, d in G.edges(data=True):
        w = (d['weight'] / max_weight) * 12 # 선 굵기 조절
        nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], width=w, edge_color='#E50914', alpha=0.3)

    # 라벨링
    nx.draw_networkx_labels(G, pos, font_size=14, font_family='Malgun Gothic', font_weight='bold', font_color='white')

    plt.title("셰프 중심 연관어 네트워크 분석 (Satellite Association Map)", fontsize=22, fontweight='bold', color='white', pad=40)
    
    # 외곽선 제거
    for spine in ax.spines.values():
        spine.set_visible(False)

    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'chef_keyword_network_v2.png'), dpi=150, facecolor='#111111')
    plt.close()
    print("✓ Saved: chef_keyword_network_v2.png")

if __name__ == "__main__":
    create_chef_network_v2()
