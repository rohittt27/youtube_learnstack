# Generated by Django 4.2.2 on 2023-06-18 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='YouTubeVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('video_id', models.CharField(max_length=20)),
                ('thumbnail_url', models.URLField()),
            ],
        ),
        migrations.RemoveField(
            model_name='video',
            name='course',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
