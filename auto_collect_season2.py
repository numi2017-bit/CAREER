"""
흑백요리사 시즌 2 영상 자동 검색 및 댓글 수집
yt-dlp로 영상 검색 + YouTube API로 댓글 수집
"""

import os
import subprocess
import json
from googleapiclient.discovery import build
import pandas as pd
import re

API_KEY = 'AIzaSyBk7IUzC0fCit6s2ofjS5lET7Dkzan5m5c'
SAVE_PATH = r"c:\Users\pc\Desktop\mypyproject\black\흑백요리사"

def search_youtube_videos(query, max_results=10):
    """yt-dlp로 유튜브 영상 검색"""
    print(f"\n검색 중: {query}")
    
    try:
        # yt-dlp 명령어로 검색
        cmd = [
            'yt-dlp',
            f'ytsearch{max_results}:{query}',
            '--get-id',
            '--get-title',
            '--skip-download'
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
        
        if result.returncode != 0:
            print(f"검색 실패: {result.stderr}")
            return []
        
        # 결과 파싱 (제목과 ID가 번갈아 나옴)
        lines = result.stdout.strip().split('\n')
        videos = []
        
        for i in range(0, len(lines), 2):
            if i + 1 < len(lines):
                videos.append({
                    'title': lines[i],
                    'video_id': lines[i + 1]
                })
        
        print(f"  찾은 영상: {len(videos)}개")
        return videos
        
    except Exception as e:
        print(f"검색 오류: {e}")
        return []

def get_youtube_service(api_key):
    """YouTube API 서비스 생성"""
    return build('youtube', 'v3', developerKey=api_key)

def get_video_comments(youtube, video_id, max_comments=1000):
    """YouTube API로 댓글 수집"""
    comments = []
    
    try:
        request = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            maxResults=100,
            order='relevance'
        )
        
        while request and len(comments) < max_comments:
            response = request.execute()
            
            for item in response['items']:
                comment = item['snippet']['topLevelComment']['snippet']
                comments.append({
                    'author': comment['authorDisplayName'],
                    'published_at': comment['publishedAt'],
                    'like_count': comment['likeCount'],
                    'text': comment['textDisplay']
                })
            
            # 다음 페이지
            if 'nextPageToken' in response and len(comments) < max_comments:
                request = youtube.commentThreads().list(
                    part='snippet',
                    videoId=video_id,
                    maxResults=100,
                    pageToken=response['nextPageToken'],
                    order='relevance'
                )
            else:
                break
                
    except Exception as e:
        print(f"  댓글 수집 실패: {e}")
    
    return comments

def main():
    """메인 실행"""
    
    print("=" * 60)
    print("흑백요리사 시즌 2 자동 수집")
    print("=" * 60)
    
    # 시즌 2 관련 검색어
    search_queries = [
        "흑백요리사 시즌2",
        "흑백요리사2 최강록",
        "흑백요리사2 임태훈",
        "Culinary Class Wars Season 2"
    ]
    
    all_videos = []
    
    # 각 검색어로 영상 찾기
    for query in search_queries:
        videos = search_youtube_videos(query, max_results=3)
        all_videos.extend(videos)
    
    # 중복 제거
    unique_videos = {v['video_id']: v for v in all_videos}.values()
    print(f"\n총 {len(unique_videos)}개의 고유 영상 발견")
    
    if not unique_videos:
        print("영상을 찾지 못했습니다.")
        return
    
    # YouTube API로 댓글 수집
    youtube = get_youtube_service(API_KEY)
    
    print("\n" + "=" * 60)
    print("댓글 수집 시작")
    print("=" * 60)
    
    for i, video in enumerate(unique_videos, 1):
        print(f"\n[{i}/{len(unique_videos)}] {video['title'][:50]}...")
        print(f"  Video ID: {video['video_id']}")
        
        comments = get_video_comments(youtube, video['video_id'], max_comments=1000)
        
        if comments:
            # CSV로 저장
            df = pd.DataFrame(comments)
            filename = f"{video['video_id']}_comments_s2.csv"
            filepath = os.path.join(SAVE_PATH, filename)
            df.to_csv(filepath, index=False, encoding='utf-8-sig')
            print(f"  ✓ 저장 완료: {len(comments)}개 댓글")
        else:
            print(f"  ✗ 댓글 없음")
    
    print("\n" + "=" * 60)
    print("수집 완료!")
    print(f"저장 위치: {SAVE_PATH}")
    print("=" * 60)

if __name__ == "__main__":
    main()
