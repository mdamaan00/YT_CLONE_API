# Generated by Django 3.1 on 2021-08-10 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ytapi', '0003_auto_20210810_1250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='songs',
            old_name='singer',
            new_name='artist',
        ),
        migrations.AddField(
            model_name='songs',
            name='songimage',
            field=models.FileField(default=None, upload_to='images/'),
            preserve_default=False,
        ),
    ]
