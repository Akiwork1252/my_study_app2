import os
import json
from dotenv import load_dotenv
from openai import OpenAI



# 学習プランのプレビューを作成
def generate_learning_plan(title, level_when_set, detail):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    prompt = f"""
下記の<ユーザーの入力情報>、<作成ルール>に基づいて学習プランを作成してください。
<ユーザー入力情報>未入力でも無視
テーマ:{title}
ユーザーのレベル:{level_when_set}
詳細:{detail}
<作成ルール>
1,(重要)学習プランは以下のようなJSON形式で作成してください。出力は厳密なJDON形式に従ったデータにしてください。
[
{{
    'Main_topic': "Pythonの基礎",
    "Sub_topic": [
    "Pythonの基本文法(変数とデータ型)",
    "Pythonの基本文法(制御構造とループ)",
    ]
}}]
2,(重要)それぞれのtopicは出来るだけ細分化してください。
"""
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {'role': 'system', 'content': 'あなたはユーザーに最適な学習プランを提案するAIアシスタントです。'},
            {'role': 'user', 'content': prompt}
        ],
        max_tokens=1000,
        temperature=0.7
    )
    print(f'response: {response}')
    raw_content = response.choices[0].message.content.strip()
    print(f'raw_content: {raw_content}')
    if not raw_content:
        print('AIから空のレスポンスが返されました。')
        return []
    # 不要な出力を削除
    raw_content = raw_content.replace('```json', '').replace('```', '').strip()
    




if __name__ == '__main__':
    load_dotenv()
    title = 'python'
    level_when_set = '未経験'
    detail = '株価予測がしたい'
    generate_learning_plan(title, level_when_set, detail)
