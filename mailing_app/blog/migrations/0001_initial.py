# Generated by Django 4.2.4 on 2023-09-12 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Содержимое статьи')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog_imgs/', verbose_name='Изображение')),
                ('views', models.IntegerField(default=0, verbose_name='Количество просмотров')),
                ('publication_date', models.DateField(auto_now=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'публикации',
                'verbose_name_plural': 'публикации',
                'ordering': ('title', 'views', 'publication_date'),
            },
        ),
    ]
