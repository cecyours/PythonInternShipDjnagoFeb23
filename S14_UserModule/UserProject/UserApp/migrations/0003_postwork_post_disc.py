# Generated by Django 4.1.7 on 2023-04-14 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0002_alter_postwork_post_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='postwork',
            name='post_disc',
            field=models.TextField(default=1, verbose_name=150),
            preserve_default=False,
        ),
    ]
