# Generated by Django 5.1.1 on 2024-09-20 17:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_category_author_book_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='books',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.author'),
        ),
    ]
