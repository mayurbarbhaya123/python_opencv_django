# Generated by Django 3.1.5 on 2021-01-05 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opencvapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestUploadImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimg', models.ImageField(blank=True, null=True, upload_to='testmedia/')),
            ],
        ),
    ]