# Generated by Django 4.1.4 on 2023-01-20 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='data',
            field=models.TextField(default='default value'),
            preserve_default=False,
        ),
    ]
