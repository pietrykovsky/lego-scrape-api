# Generated by Django 4.0.7 on 2022-09-14 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Age category',
                'verbose_name_plural': 'Age categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Theme category',
                'verbose_name_plural': 'Theme categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='LegoSet',
            fields=[
                ('title', models.CharField(max_length=255)),
                ('product_id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('available', models.BooleanField(default=False)),
                ('elements', models.IntegerField()),
                ('link', models.TextField()),
                ('minifigures', models.IntegerField(blank=True, null=True)),
                ('img_src', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('age', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legoscraper.agecategory')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legoscraper.theme')),
            ],
            options={
                'verbose_name': 'Lego set',
                'ordering': ['title'],
            },
        ),
    ]
