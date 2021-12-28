# Generated by Django 3.2.5 on 2021-12-28 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('narx', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('familiya', models.CharField(max_length=30)),
                ('sharif', models.CharField(blank=True, max_length=30)),
                ('jins', models.CharField(choices=[("o'g'il", "o'g'il"), ('qiz', 'qiz')], max_length=7)),
                ('tel1', models.CharField(max_length=15)),
                ('tel2', models.CharField(blank=True, max_length=15)),
                ('status', models.CharField(choices=[('new', 'new'), ('loyal', 'loyal')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Ustoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('yosh', models.PositiveSmallIntegerField()),
                ('tel', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Shartnoma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shartnoma_raqami', models.PositiveSmallIntegerField()),
                ('kunlari', models.CharField(choices=[('Dushanba-Juma', 'Dushanba-Juma'), ('Seshanba-Shanba', 'Seshanba-Shanba')], max_length=30)),
                ('kurs_vaqti', models.CharField(choices=[('08:00-10:00', '08:00-10:00'), ('10:00-12:00', '10:00-12:00'), ('14:00-16:00', '14:00-16:00'), ('16:00-18:00', '16:00-18:00'), ('18:00-20:00', '18:00-20:00')], max_length=30)),
                ('guruh_nomi', models.CharField(max_length=30)),
                ('tuzuvchi', models.CharField(max_length=30)),
                ('sinov_dars_sanasi', models.DateField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Passive', 'Passive')], max_length=15)),
                ('kurs', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shartnomaApp.kurs')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shartnomaApp.student')),
                ('ustoz', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shartnomaApp.ustoz')),
            ],
        ),
    ]
