# Generated by Django 3.2.3 on 2021-06-01 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_videoproxy'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videoproxy',
            options={'verbose_name': 'Published Video', 'verbose_name_plural': 'Published Videos'},
        ),
    ]