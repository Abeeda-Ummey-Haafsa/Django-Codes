# Generated by Django 5.1.2 on 2024-10-25 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_remove_category_task'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.ManyToManyField(to='category.category'),
        ),
    ]
