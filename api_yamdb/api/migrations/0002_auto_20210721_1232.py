# Generated by Django 2.2.6 on 2021-07-21 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('U', 'user'), ('M', 'moderator'), ('A', 'admin')], default='U', max_length=50, verbose_name='Роль'),
        ),
    ]
