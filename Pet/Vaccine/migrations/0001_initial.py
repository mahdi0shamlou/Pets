# Generated by Django 4.2.10 on 2024-06-26 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Animals', '0002_animalsusers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccines',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('desc', models.CharField(max_length=400, unique=True)),
                ('age', models.IntegerField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Animals.animals')),
            ],
        ),
    ]