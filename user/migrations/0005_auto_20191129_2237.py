# Generated by Django 2.2.7 on 2019-11-30 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20191129_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email_id',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
