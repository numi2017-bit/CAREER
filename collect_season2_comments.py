"""
흑백요리사 시즌 2 유튜브 댓글 수집 스크립트

사용법:
1. YouTube Data API 키 필요
2. 시즌 2 관련 영상 검색 및 댓글 수집
"""

import os
from googleapiclient.discovery import build
import pandas as pd
from datetime import datetime

# API 키 설정 (여기에 본인의 YouTube Data API 키를 입력하세요)
API_KEY = 'AIzaSyCuFTw8dPNEeisvVEH2OZ_L02qRQ6ipJPU'

# 저장 경로
SAVE_PATH = r"c:\Users\pc\Desktop\mypyproject\black\흑백요리사"

# 시즌 2 관련 검색 키워드
SEASON2_KEYWORDS = [
    "흑백요리사 시즌2",
    "흑백요리사2",
    "최강록 흑백요리사",
    "임태훈 흑백요리사",
    "정호영 흑백요리사",
    "Culinary Class Wars Season 2"
]

def get_youtube_service(api_key):
    """YouTube API 서비스 생성"""
    return build('youtube', 'v3', developerKey=api_key)

def search_videos(youtube, keyword, max_results=10):
    """키워드로 영상 검색"""
    request = youtube.search().list(
        part='snippet',
        q=keyword,
        type='video',
        maxResults=max_results,
        order='viewCount',  # 조회수 순
        relevanceLanguage='ko'
    )
    response = request.execute()
    
    videos = []
    for item in response.get('items', []):
        videos.append({
            'video_id': item['id']['videoId'],
            'title': item['snippet']['title'],
            'channel': item['snippet']['channelTitle'],
            'published_at': item['snippet']['publishedAt']
        })
    
    return videos

def get_video_comments(youtube, video_id, max_comments=1000):
    """영상의 댓글 수집"""
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
        print(f"Error fetching comments for {video_id}: {e}")
    
    return comments

def main():
    """메인 실행 함수"""
    
    # API 키 확인
    if API_KEY == 'YOUR_API_KEY_HERE':
        print("=" * 60)
        print("YouTube Data API 키가 필요합니다!")
        print("=" * 60)
        print("\n설정 방법:")
        print("1. Google Cloud Console 접속: https://console.cloud.google.com/")
        print("2. 프로젝트 생성")
        print("3. YouTube Data API v3 활성화")
        print("4. API 키 생성")
        print("5. 이 스크립트의 API_KEY 변수에 입력")
        print("\n또는 기존에 수집된 데이터를 사용하시겠습니까?")
        return
    
    youtube = get_youtube_service(API_KEY)
    
    print("=" * 60)
    print("흑백요리사 시즌 2 댓글 수집 시작")
    print("=" * 60)
    
    all_videos = []
    
    # 각 키워드로 영상 검색
    for keyword in SEASON2_KEYWORDS:
        print(f"\n검색 중: {keyword}")
        videos = search_videos(youtube, keyword, max_results=5)
        all_videos.extend(videos)
        print(f"  찾은 영상: {len(videos)}개")
    
    # 중복 제거
    unique_videos = {v['video_id']: v for v in all_videos}.values()
    print(f"\n총 {len(unique_videos)}개의 고유 영상 발견")
    
    # 각 영상의 댓글 수집
    for i, video in enumerate(unique_videos, 1):
        print(f"\n[{i}/{len(unique_videos)}] {video['title'][:50]}...")
        
        comments = get_video_comments(youtube, video['video_id'], max_comments=1000)
        
        if comments:
            # CSV로 저장
            df = pd.DataFrame(comments)
            filename = f"{video['video_id']}_comments_s2.csv"
            filepath = os.path.join(SAVE_PATH, filename)
            df.to_csv(filepath, index=False, encoding='utf-8-sig')
            print(f"  저장 완료: {len(comments)}개 댓글 -> {filename}")
        else:
            print(f"  댓글 없음")
    
    print("\n" + "=" * 60)
    print("수집 완료!")
    print(f"저장 위치: {SAVE_PATH}")
    print("=" * 60)

if __name__ == "__main__":
    main()
