# Generated by Django 3.2.3 on 2021-07-04 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0010_alter_video_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='publish_timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
