# Generated by Django 3.1.1 on 2020-09-17 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unsplash', '0003_remove_photo_author_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='user_saved_date',
        ),
        migrations.AddField(
            model_name='photo',
            name='photo_unsplash_id',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
