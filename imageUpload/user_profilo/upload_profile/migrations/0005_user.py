# Generated by Django 3.1.2 on 2020-10-31 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('upload_profile', '0004_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('user_image', models.ImageField(upload_to='image/')),
                ('introduce', models.FileField(upload_to='introduce/')),
            ],
        ),
    ]
