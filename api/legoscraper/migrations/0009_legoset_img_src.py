# Generated by Django 4.0.7 on 2022-08-28 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legoscraper', '0008_alter_agecategory_name_alter_theme_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='legoset',
            name='img_src',
            field=models.TextField(null=True),
        ),
    ]