# Generated by Django 2.2 on 2019-10-14 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20191010_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(max_length=50, verbose_name='статус'),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='создано'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='projects_task', to='webapp.Project', verbose_name='проект'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='task_status', to='webapp.Status', verbose_name='статус'),
        ),
        migrations.AlterField(
            model_name='task',
            name='summary',
            field=models.CharField(max_length=50, verbose_name='краткое изложение'),
        ),
        migrations.AlterField(
            model_name='task',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='task_type', to='webapp.Type', verbose_name='тип'),
        ),
        migrations.AlterField(
            model_name='type',
            name='type',
            field=models.CharField(max_length=50, verbose_name='тип'),
        ),
    ]
