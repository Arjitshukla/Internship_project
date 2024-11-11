# Generated by Django 5.1.1 on 2024-10-01 18:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, upload_to='blog/images')),
                ('heading_1', models.CharField(max_length=50)),
                ('para_1', models.TextField()),
                ('heading_2', models.CharField(max_length=50)),
                ('para_2', models.TextField()),
                ('heading_3', models.CharField(max_length=50)),
                ('para_3', models.TextField()),
                ('heading_4', models.CharField(max_length=50)),
                ('para_4', models.TextField()),
                ('heading_5', models.CharField(max_length=50)),
                ('para_5', models.TextField()),
                ('heading_6', models.CharField(max_length=50)),
                ('para_6', models.TextField()),
                ('para_7', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
