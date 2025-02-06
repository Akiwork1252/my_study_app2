# Generated by Django 5.1.5 on 2025-02-06 04:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ascension', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=0.0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('learning_objective', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ascension.learningobjective')),
                ('sub_topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ascension.learningsubtopic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
