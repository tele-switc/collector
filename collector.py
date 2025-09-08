#!/usr/bin/env python3
"""
外刊文章收集器
每日自动收集指定媒体的文章
"""

import json
import os
import time
import hashlib
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import requests
from bs4 import BeautifulSoup
import feedparser
from urllib.parse import urljoin, urlparse

class ArticleCollector:
    def __init__(self):
        self.articles_file = 'data/articles.json'
        self.existing_articles = self.load_existing_articles()
        self.existing_urls = {article['url'] for article in self.existing_articles}
        self.today = datetime.now().strftime('%Y-%m-%d')
        
        # 用户代理
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        
    def load_existing_articles(self) -> List[Dict]:
        """加载已存在的文章"""
        if os.path.exists(self.articles_file):
            try:
                with open(self.articles_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_articles(self):
        """保存文章到JSON文件"""
        # 确保目录存在
        os.makedirs(os.path.dirname(self.articles_file), exist_ok=True)
        
        # 按日期排序，最新的在前
        self.existing_articles.sort(key=lambda x: x.get('date', ''), reverse=True)
        
        with open(self.articles_file, 'w', encoding='utf-8') as f:
            json.dump(self.existing_articles, f, ensure_ascii=False, indent=2)
    
    def add_article(self, article: Dict) -> bool:
        """添加文章（去重）"""
        # 检查URL是否已存在
        if article['url'] in self.existing_urls:
            print(f"  跳过重复: {article['title'][:50]}...")
            return False
        
        # 添加收集日期
        article['date'] = self.today
        article['collected_at'] = datetime.now().isoformat()
        
        # 生成唯一ID
        article['id'] = hashlib.md5(article['url'].encode()).hexdigest()[:8]
        
        self.existing_articles.append(article)
        self.existing_urls.add(article['url'])
        print(f"  ✓ 添加: {article['title'][:50]}...")
        return True
    
    def collect_from_rss(self, feed_url: str, source: str, limit: int = 10) -> int:
        """从RSS源收集文章"""
        count = 0
        try:
            print(f"\n正在收集 {source} RSS...")
            feed = feedparser.parse(feed_url)
            
            for entry in feed.entries[:limit]:
                article = {
                    'source': source,
                    'title': entry.get('title', 'No Title'),
                    'url': entry.get('link', ''),
                    'summary': entry.get('summary', '')[:500] if entry.get('summary') else '',
                    'published': entry.get('published', ''),
                }
                
                # 尝试获取图片
                if hasattr(entry, 'media_content') and entry.media_content:
                    article['image'] = entry.media_content[0].get('url', '')
                elif hasattr(entry, 'enclosures') and entry.enclosures:
                    for enc in entry.enclosures:
                        if 'image' in enc.get('type', ''):
                            article['image'] = enc.get('href', '')
                            break
                
                if self.add_article(article):
                    count += 1
                    
        except Exception as e:
            print(f"  错误: {e}")
        
        return count
    
    def collect_wired(self) -> int:
        """收集Wired文章"""
        # Wired RSS feeds
        feeds = [
            'https://www.wired.com/feed/rss',
            'https://www.wired.com/feed/category/business/latest/rss',
            'https://www.wired.com/feed/category/science/latest/rss',
            'https://www.wired.com/feed/category/security/latest/rss',
        ]
        
        total = 0
        for feed in feeds:
            total += self.collect_from_rss(feed, 'wired', limit=5)
        return total
    
    def collect_economist(self) -> int:
        """收集经济学人文章"""
        feeds = [
            'https://www.economist.com/leaders/rss.xml',
            'https://www.economist.com/briefing/rss.xml',
            'https://www.economist.com/special-report/rss.xml',
            'https://www.economist.com/business/rss.xml',
            'https://www.economist.com/finance-and-economics/rss.xml',
            'https://www.economist.com/science-and-technology/rss.xml',
        ]
        
        total = 0
        for feed in feeds:
            total += self.collect_from_rss(feed, 'economist', limit=3)
        return total
    
    def collect_scientific_american(self) -> int:
        """收集科学美国人文章"""
        return self.collect_from_rss(
            'http://rss.sciam.com/ScientificAmerican-Global',
            'scientific-american',
            limit=10
        )
    
    def collect_atlantic(self) -> int:
        """收集大西洋月刊文章"""
        feeds = [
            'https://www.theatlantic.com/feed/all/',
            'https://www.theatlantic.com/feed/best-of/',
        ]
        
        total = 0
        for feed in feeds:
            total += self.collect_from_rss(feed, 'atlantic', limit=5)
        return total
    
    def collect_nytimes(self) -> int:
        """收集纽约时报文章"""
        feeds = [
            'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
            'https://rss.nytimes.com/services/xml/rss/nyt/World.xml',
            'https://rss.nytimes.com/services/xml/rss/nyt/Business.xml',
            'https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml',
            'https://rss.nytimes.com/services/xml/rss/nyt/Science.xml',
        ]
        
        total = 0
        for feed in feeds:
            total += self.collect_from_rss(feed, 'nytimes', limit=3)
        return total
    
    def collect_wsj(self) -> int:
        """收集华尔街日报文章"""
        feeds = [
            'https://feeds.a.dj.com/rss/RSSWorldNews.xml',
            'https://feeds.a.dj.com/rss/WSJcomUSBusiness.xml',
            'https://feeds.a.dj.com/rss/RSSMarketsMain.xml',
            'https://feeds.a.dj.com/rss/RSSWSJD.xml',
        ]
        
        total = 0
        for feed in feeds:
            total += self.collect_from_rss(feed, 'wsj', limit=3)
        return total
    
    def collect_all(self):
        """收集所有媒体的文章"""
        print(f"\n{'='*50}")
        print(f"开始收集文章 - {self.today}")
        print(f"{'='*50}")
        
        results = {
            'Wired (连线)': self.collect_wired(),
            'The Economist (经济学人)': self.collect_economist(),
            'Scientific American (科学美国人)': self.collect_scientific_american(),
            'The Atlantic (大西洋月刊)': self.collect_atlantic(),
            'New York Times (纽约时报)': self.collect_nytimes(),
            'Wall Street Journal (华尔街日报)': self.collect_wsj(),
        }
        
        # 保存结果
        self.save_articles()
        
        # 打印统计
        print(f"\n{'='*50}")
        print("收集完成！统计：")
        for source, count in results.items():
            print(f"  {source}: {count} 篇新文章")
        print(f"  总计: {sum(results.values())} 篇新文章")
        print(f"  文章总数: {len(self.existing_articles)} 篇")
        print(f"{'='*50}\n")

def main():
    """主函数"""
    collector = ArticleCollector()
    collector.collect_all()

if __name__ == '__main__':
    main()
