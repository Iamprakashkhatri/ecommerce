# Generated by Django 2.2.7 on 2019-11-21 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommer', '0010_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
    ]
