# Generated by Django 3.1 on 2022-12-11 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0005_auto_20221210_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_post.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(max_length=8000, verbose_name='Content'),
        ),
    ]
