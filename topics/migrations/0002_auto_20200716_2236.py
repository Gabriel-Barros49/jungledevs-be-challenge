# Generated by Django 3.0.7 on 2020-07-16 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='description',
            field=models.TextField(max_length=100),
        ),
    ]
