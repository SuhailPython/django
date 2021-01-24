# Generated by Django 3.1.5 on 2021-01-23 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_auto_20210123_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000)),
                ('email', models.EmailField(max_length=2000)),
                ('website', models.URLField(max_length=20000)),
                ('cv', models.FileField(upload_to='apply/')),
                ('cover_letter', models.TextField(max_length=30000000)),
            ],
        ),
    ]
