#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import requests
import json
from requests_oauthlib import OAuth1

def post_to_x(message):
    """
    X（旧Twitter）に投稿するための関数
    
    Args:
        message (str): 投稿するメッセージ
    
    Returns:
        bool: 投稿が成功したかどうか
    """
    # 環境変数からAPIキーとアクセストークンを取得
    api_key = os.environ.get('X_API_KEY')
    api_key_secret = os.environ.get('X_API_KEY_SECRET')
    access_token = os.environ.get('X_ACCESS_TOKEN')
    access_token_secret = os.environ.get('X_ACCESS_TOKEN_SECRET')
    
    # 必要な認証情報が揃っているか確認
    if not all([api_key, api_key_secret, access_token, access_token_secret]):
        print("Error: X API認証情報が不足しています。")
        return False
    
    # X APIのエンドポイント（v2 API）
    url = "https://api.twitter.com/2/tweets"
    
    # OAuth1認証
    auth = OAuth1(
        api_key,
        client_secret=api_key_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret
    )
    
    # リクエストボディ
    data = {
        "text": message
    }
    
    try:
        # POSTリクエストを送信
        response = requests.post(url, auth=auth, json=data)
        
        # レスポンスを確認
        if response.status_code == 201:
            print(f"投稿成功: {response.json()}")
            return True
        else:
            print(f"投稿失敗: {response.status_code} - {response.text}")
            return False
    
    except Exception as e:
        print(f"エラー発生: {str(e)}")
        return False

def main():
    # 初回投稿のメッセージ
    message = "うん、たぶん音声配信の有料部分って「本人の生声」にして、無料部分はAI音声のショート動画みたいなあらゆるプラットフォームへ展開して認知とエンゲージを高めていく方向性になりそう。そのための準備と品質とコストが見合ってきて、話す内容から読み上げ投稿やそのフィードバックや数値データからの改善プロセスもほぼ自動化のめどがたってきたこのタイミングは仕掛けどき、そのプロセスはVoicyなどで音声配信していこうと思います"
    
    # X（旧Twitter）に投稿
    success = post_to_x(message)
    
    # 結果を出力
    if success:
        print("X（旧Twitter）への投稿が完了しました。")
    else:
        print("X（旧Twitter）への投稿に失敗しました。")
        exit(1)

if __name__ == "__main__":
    main()
