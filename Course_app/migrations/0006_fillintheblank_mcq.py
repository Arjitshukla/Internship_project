# Generated by Django 5.1.2 on 2024-10-12 15:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course_app', '0005_remove_topicdetail_code_t2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FillInTheBlank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300)),
                ('answer', models.CharField(max_length=100)),
                ('topic_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fill_blanks', to='Course_app.topicdetail')),
            ],
        ),
        migrations.CreateModel(
            name='MCQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300)),
                ('option_1', models.CharField(max_length=100)),
                ('option_2', models.CharField(max_length=100)),
                ('option_3', models.CharField(max_length=100)),
                ('option_4', models.CharField(max_length=100)),
                ('correct_option', models.CharField(max_length=100)),
                ('topic_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mcqs', to='Course_app.topicdetail')),
            ],
        ),
    ]
