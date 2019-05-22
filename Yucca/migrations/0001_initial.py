# Generated by Django 2.2.1 on 2019-05-15 06:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('artist', models.CharField(max_length=40)),
                ('year', models.CharField(max_length=4)),
                ('cover', models.ImageField(upload_to='')),
                ('genre', models.CharField(choices=[('Unknown', 'unknown'), ('Rap', 'rap'), ('Riddim', 'riddim'), ('RnB', 'rnb'), ('Local', 'local'), ('Pop', 'pop'), ('House', 'house')], default='unknown', max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('audio', models.FileField(upload_to='')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Yucca.Album')),
            ],
        ),
    ]
