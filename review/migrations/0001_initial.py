# Generated by Django 3.1.7 on 2021-11-22 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mail', models.EmailField(max_length=30)),
                ('contact', models.IntegerField()),
                ('text', models.TextField()),
            ],
        ),
    ]
