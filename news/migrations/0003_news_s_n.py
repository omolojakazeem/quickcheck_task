# Generated by Django 4.1.1 on 2022-09-21 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_remove_news_name_news_by_news_dead_news_deleted_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='s_n',
            field=models.BigIntegerField(blank=True, null=True, unique=True),
        ),
    ]
