# Generated by Django 3.1.3 on 2020-11-03 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0002_auto_20201103_1504'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PartB',
        ),
        migrations.RemoveField(
            model_name='parta',
            name='id',
        ),
        migrations.AddField(
            model_name='parta',
            name='PartaId',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
