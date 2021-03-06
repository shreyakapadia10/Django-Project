# Generated by Django 3.1.7 on 2021-03-21 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_title', models.CharField(default='', max_length=50)),
                ('post_heading0', models.CharField(default='', max_length=50)),
                ('post_heading0_content', models.CharField(default='', max_length=5000)),
                ('post_heading1', models.CharField(default='', max_length=50)),
                ('post_heading1_content', models.CharField(default='', max_length=5000)),
                ('post_heading2', models.CharField(default='', max_length=50)),
                ('post_heading2_content', models.CharField(default='', max_length=5000)),
                ('post_thumbnail', models.ImageField(default='', upload_to='blog/images')),
                ('post_publish_date', models.DateField()),
            ],
        ),
    ]
