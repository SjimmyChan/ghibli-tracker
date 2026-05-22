import feedparser
import json
import time
from googletrans import Translator

# 1. 定義你的所有 RSS 來源
RSS_SOURCES = {
    "官方公告": "https://rss.app/feeds/IwOCti7OxXZp9cLS.xml",
    "期間限定": "https://rss.app/feeds/tJSErhOVeQyXA3Hm.xml",
    "最新周邊": "https://rss.app/feeds/t6JF1wUS501MmBN4.xml",
    "現場報導": "https://rss.app/feeds/tFWetccOqz0Wr2RW.xml"
}

def run():
    translator = Translator()
    all_news = []
    seen_titles = set() # 用於去重

    print("開始抓取與翻譯...")

    for category, url in RSS_SOURCES.items():
        print(f"正在處理: {category}")
        feed = feedparser.parse(url)
        
        for entry in feed.entries:
            # 2. 簡單去重：如果標題已經存過，就跳過
            if entry.title in seen_titles:
                continue
            
            try:
                # 3. 翻譯與節流控制
                # 為了避免翻譯太快被 Google 封鎖，sleep 是必要的
                time.sleep(0.5) 
                translated_title = translator.translate(entry.title, dest='zh-tw').text
                
                all_news.append({
                    "category": category,
                    "title": translated_title,
                    "link": entry.link,
                    "published": entry.published
                })
                seen_titles.add(entry.title)
                
            except Exception as e:
                print(f"翻譯失敗: {entry.title}, 錯誤: {e}")
                continue
    
    # 4. 存檔
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(all_news, f, ensure_ascii=False)
    
    print(f"成功！共存入 {len(all_news)} 條新聞。")

if __name__ == "__main__":
    run()