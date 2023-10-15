# Generated by Django 4.2.6 on 2023-10-08 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='audio',
            field=models.FileField(default=1, upload_to='audios/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='books',
            name='more',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
