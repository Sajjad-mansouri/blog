# Generated by Django 4.0.2 on 2022-02-12 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_category_options_articles_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='status',
            field=models.CharField(choices=[('d', 'پیش نویس'), ('p', 'منتشر شده'), ('i', 'در حال بررسی'), ('b', 'برگشت خورده')], max_length=1, verbose_name='وضعیت'),
        ),
    ]
