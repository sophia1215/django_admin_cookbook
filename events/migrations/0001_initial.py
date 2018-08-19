# Generated by Django 2.0.7 on 2018-08-19 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('entities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Epic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('participating_heroes', models.ManyToManyField(to='entities.Hero')),
                ('participating_villains', models.ManyToManyField(to='entities.Villain')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField()),
                ('years_ago', models.PositiveIntegerField()),
                ('epic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Epic')),
            ],
        ),
        migrations.CreateModel(
            name='EventHero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_primary', models.BooleanField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entities.Hero')),
            ],
        ),
        migrations.CreateModel(
            name='EventVillain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_primary', models.BooleanField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entities.Villain')),
            ],
        ),
    ]