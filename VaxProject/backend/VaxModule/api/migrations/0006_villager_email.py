# Generated by Django 4.0.3 on 2022-04-20 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_villager_covidstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='villager',
            name='Email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
