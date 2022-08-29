# Generated by Django 4.0.7 on 2022-08-29 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('legoscraper', '0010_legoset_updated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agecategory',
            options={'ordering': ['name'], 'verbose_name': 'Age category', 'verbose_name_plural': 'Age categories'},
        ),
        migrations.AlterModelOptions(
            name='legoset',
            options={'ordering': ['title'], 'verbose_name': 'Lego set'},
        ),
        migrations.AlterModelOptions(
            name='theme',
            options={'ordering': ['name'], 'verbose_name': 'Theme category', 'verbose_name_plural': 'Theme categories'},
        ),
    ]