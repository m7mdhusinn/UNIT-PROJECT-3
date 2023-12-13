# Generated by Django 5.0 on 2023-12-11 07:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favorite', '0001_initial'),
        ('property', '0007_comment_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='comment',
        ),
        migrations.AddField(
            model_name='favorite',
            name='property',
            field=models.ForeignKey(default=18, on_delete=django.db.models.deletion.CASCADE, to='property.property'),
            preserve_default=False,
        ),
    ]