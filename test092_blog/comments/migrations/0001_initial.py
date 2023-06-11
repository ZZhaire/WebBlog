# Generated by Django 3.2.9 on 2023-04-13 15:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0004_alter_bloginfo_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=300, verbose_name='评论内容')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='评论时间')),
                ('comment_blog', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blogs.bloginfo', verbose_name='评论文章')),
                ('comment_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='评论人')),
            ],
            options={
                'verbose_name': '用户评论信息表',
                'verbose_name_plural': '用户评论信息表',
                'db_table': 'Comment',
            },
        ),
    ]
