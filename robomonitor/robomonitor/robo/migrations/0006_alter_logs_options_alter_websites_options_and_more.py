# Generated by Django 4.2.3 on 2023-07-20 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('robo', '0005_logs'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logs',
            options={'verbose_name': 'Log', 'verbose_name_plural': 'Logs'},
        ),
        migrations.AlterModelOptions(
            name='websites',
            options={'verbose_name': 'Website', 'verbose_name_plural': 'Websites'},
        ),
        migrations.AddField(
            model_name='logs',
            name='date_time',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='logs',
            name='website',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='robo.websites'),
            preserve_default=False,
        ),
    ]
