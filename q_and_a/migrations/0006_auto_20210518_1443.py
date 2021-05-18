# Generated by Django 3.0.8 on 2021-05-18 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('q_and_a', '0005_auto_20210518_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='correct_answer_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='q_and_a.Question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='points',
            field=models.PositiveIntegerField(default=0, verbose_name='Points for correct answer'),
        ),
    ]