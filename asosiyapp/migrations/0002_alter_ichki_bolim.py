# Generated by Django 4.1 on 2022-10-19 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asosiyapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ichki',
            name='bolim',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ichkilari', to='asosiyapp.bolim'),
        ),
    ]
