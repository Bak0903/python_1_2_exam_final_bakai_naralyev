# Generated by Django 2.2.2 on 2019-06-29 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_author_is_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('published_year', models.CharField(blank=True, max_length=4, null=True, verbose_name='Год издания')),
                ('file', models.FileField(blank=True, null=True, upload_to='settings.MEDIA_ROOT', verbose_name='Файл')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Обложка')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Описание')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Author', verbose_name='Автор')),
            ],
        ),
    ]