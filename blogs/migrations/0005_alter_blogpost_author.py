# Generated by Django 4.2.6 on 2023-10-26 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_blogpost_remove_topic_owner_delete_entry_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='author',
            field=models.CharField(max_length=150),
        ),
    ]