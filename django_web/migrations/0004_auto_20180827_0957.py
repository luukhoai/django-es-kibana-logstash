# Generated by Django 2.1 on 2018-08-27 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_web', '0003_auto_20180827_0128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='posted_date',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
