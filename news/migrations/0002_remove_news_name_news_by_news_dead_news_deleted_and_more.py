# Generated by Django 4.1.1 on 2022-09-20 23:16

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='name',
        ),
        migrations.AddField(
            model_name='news',
            name='by',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='dead',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='news',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='news',
            name='descendants',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='kids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='news',
            name='parent',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='parts',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='news',
            name='score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='synced',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='news',
            name='text',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='time',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='type',
            field=models.CharField(blank=True, choices=[('JOB', 'JOB'), ('COMMENT', 'POLL'), ('POLL', 'POLL'), ('POLLOPT', 'POLLOPT')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]