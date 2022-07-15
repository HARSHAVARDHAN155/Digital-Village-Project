# Generated by Django 4.0.3 on 2022-04-02 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Villager',
            fields=[
                ('VillagerID', models.AutoField(primary_key=True, serialize=False)),
                ('VillagerName', models.CharField(max_length=500)),
                ('AadharNumber', models.CharField(max_length=20)),
                ('Gender', models.CharField(max_length=500)),
                ('CovidStatus', models.CharField(max_length=500)),
                ('Vaccination', models.CharField(max_length=20)),
                ('FirstDoseDate', models.DateField(null=True)),
                ('SecondDoseDate', models.DateField(null=True)),
            ],
        ),
    ]
