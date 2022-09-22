from celery import shared_task
from .models import News
from config.celery import app
import requests


def get_story_by_id(news_id):
    url = f"https://hacker-news.firebaseio.com/v0/item/{news_id}.json"

    payload = "{}"
    response = requests.request("GET", url, data=payload)

    news_item = response.json()
    return news_item


@app.task(name="sync_to_db")
def sync_to_db(item_id_list):

    for item_id in item_id_list[:100]:
        news_item = get_story_by_id(item_id)
        if news_item and 'error' not in news_item:
            news, created = News.objects.get_or_create(
                s_n=news_item.get('id', None)
            )

            if created:
                news.type = news_item.get('type').upper() if news_item.get('type') else None
                news.by = news_item.get('by', None)
                news.time = news_item.get('time', None)
                news.dead = news_item.get('dead', False)
                news.deleted = news_item.get('deleted', False)
                news.kids = news_item.get('kids', None)
                news.parts = news_item.get('parts', None)
                news.descendants = news_item.get('descendants', None)
                news.parent = news_item.get('parent', None)
                news.score = news_item.get('score', None)
                news.title = news_item.get('title', None)
                news.text = news_item.get('text', None)
                news.url = news_item.get('url', None)
                news.synced = True
                news.save()
                comments = news.kids
                if comments:
                    for com in comments:
                        com_data = get_story_by_id(com)
                        comment_item, _ = News.objects.get_or_create(
                            s_n=com_data.get('id', None)
                        )
                        if _:
                            comment_item.type = com_data.get('type').upper() if com_data.get('type') else None
                            comment_item.by = com_data.get('by', None)
                            comment_item.time = com_data.get('time', None)
                            comment_item.dead = com_data.get('dead', False)
                            comment_item.deleted = com_data.get('deleted', False)
                            comment_item.kids = com_data.get('kids', None)
                            comment_item.parts = com_data.get('parts', None)
                            comment_item.descendants = com_data.get('descendants', None)
                            comment_item.parent = com_data.get('parent', None)
                            comment_item.score = com_data.get('score', None)
                            comment_item.title = com_data.get('title', None)
                            comment_item.text = com_data.get('text', None)
                            comment_item.url = com_data.get('url', None)
                            comment_item.synced = True
                            comment_item.save()


@shared_task()
def sync_news():
    print("Starting sync")

    top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"

    payload = "{}"
    response = requests.request("GET", top_stories_url, data=payload)
    if response:
        item_ids = response.text
        item_ids = item_ids.strip('\'[]').split(',')

        sync_to_db.delay(item_ids)
    return "Completed"
