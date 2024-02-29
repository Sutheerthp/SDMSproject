# Generated by Django 4.1.5 on 2024-02-29 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_id', models.IntegerField()),
                ('dept_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField()),
                ('item_name', models.CharField(max_length=50)),
                ('item_type', models.CharField(max_length=50)),
                ('no_of_players', models.IntegerField()),
                ('position', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SDMSapp.department')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('year_of_admission', models.IntegerField()),
                ('admission_no', models.IntegerField()),
                ('uty_reg_no', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=50)),
                ('programme_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SDMSapp.programme')),
            ],
        ),
        migrations.CreateModel(
            name='Stud_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'inactive')], default='Active', max_length=10)),
                ('uty_team_selection', models.CharField(choices=[('selected', 'selected'), ('not selected', 'not selected')], default='Active', max_length=20)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SDMSapp.item')),
            ],
        ),
    ]