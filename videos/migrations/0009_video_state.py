# Generated by Django 3.2.3 on 2021-06-19 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0008_auto_20210611_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='state',
            field=models.CharField(choices=[('PU', 'Published'), ('DR', 'Draft')], default='DR', max_length=2),
        ),
    ]