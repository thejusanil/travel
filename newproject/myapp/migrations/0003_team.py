# Generated by Django 4.1.3 on 2022-12-26 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_place_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Image', models.ImageField(upload_to='team')),
                ('Description', models.TextField()),
            ],
        ),
    ]
