# Generated by Django 4.1.1 on 2022-09-21 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_alter_news_options_news_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]