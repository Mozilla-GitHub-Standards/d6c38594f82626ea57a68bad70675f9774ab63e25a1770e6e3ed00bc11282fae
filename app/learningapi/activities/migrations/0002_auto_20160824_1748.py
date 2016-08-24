# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 17:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teaching_kits', '0002_teachingkit'),
        ('skills', '0002_skill'),
        ('weblitskills', '0002_weblitskill'),
        ('authors', '0002_author'),
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('subtitle', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True, help_text='URL to a regular quality image.', max_length=500, null=True)),
                ('image_retina_url', models.URLField(blank=True, help_text='URL to a retina quality image.', max_length=500, null=True)),
                ('url', models.URLField(blank=True, help_text='URL to an activity.', max_length=500, null=True)),
                ('difficulty', models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Beginner mobile users', 'Beginner mobile users'), ('13+', '13+'), ('JavaScript beginners', 'JavaScript beginners')], default='Beginner', help_text='Difficulty levels for an activity', max_length=50)),
                ('duration', models.CharField(max_length=100)),
                ('locale', models.CharField(blank=True, default='en-US', max_length=20)),
                ('authors', models.ManyToManyField(blank=True, related_name='activities', to='authors.Author')),
                ('skills', models.ManyToManyField(blank=True, related_name='activities', to='skills.Skill')),
            ],
            options={
                'verbose_name_plural': 'activities',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='TeachingKitActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=0)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activities.Activity')),
                ('teaching_kit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teaching_kits.TeachingKit')),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='activities', to='activities.Tag'),
        ),
        migrations.AddField(
            model_name='activity',
            name='teaching_kits',
            field=models.ManyToManyField(blank=True, related_name='activities', through='activities.TeachingKitActivity', to='teaching_kits.TeachingKit'),
        ),
        migrations.AddField(
            model_name='activity',
            name='weblit_skills',
            field=models.ManyToManyField(blank=True, related_name='activities', to='weblitskills.WebLitSkill'),
        ),
    ]