# Generated by Django 5.1.2 on 2024-10-11 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Course_app', '0004_alter_topicdetail_code_t1_alter_topicdetail_code_t2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topicdetail',
            name='code_t2',
        ),
        migrations.RemoveField(
            model_name='topicdetail',
            name='code_t3',
        ),
        migrations.RemoveField(
            model_name='topicdetail',
            name='code_t4',
        ),
        migrations.RemoveField(
            model_name='topicdetail',
            name='content_t2',
        ),
        migrations.RemoveField(
            model_name='topicdetail',
            name='content_t3',
        ),
        migrations.RemoveField(
            model_name='topicdetail',
            name='content_t4',
        ),
        migrations.RemoveField(
            model_name='topicdetail',
            name='t2',
        ),
        migrations.RemoveField(
            model_name='topicdetail',
            name='t3',
        ),
        migrations.RemoveField(
            model_name='topicdetail',
            name='t4',
        ),
    ]
