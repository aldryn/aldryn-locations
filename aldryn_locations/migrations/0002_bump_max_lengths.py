# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_locations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='embeddirectionsplugin',
            name='height',
            field=models.CharField(default=b'400px', help_text='Plugin height (in pixels).', max_length=255, verbose_name='height'),
        ),
        migrations.AlterField(
            model_name='embeddirectionsplugin',
            name='map_type',
            field=models.CharField(default=b'roadmap', max_length=255, verbose_name='Map Type', choices=[(b'roadmap', 'Roadmap'), (b'satellite', 'Satellite')]),
        ),
        migrations.AlterField(
            model_name='embeddirectionsplugin',
            name='width',
            field=models.CharField(default=b'100%', help_text='Plugin width (in pixels or percent).', max_length=255, verbose_name='width'),
        ),
        migrations.AlterField(
            model_name='embedplaceplugin',
            name='height',
            field=models.CharField(default=b'400px', help_text='Plugin height (in pixels).', max_length=255, verbose_name='height'),
        ),
        migrations.AlterField(
            model_name='embedplaceplugin',
            name='map_type',
            field=models.CharField(default=b'roadmap', max_length=255, verbose_name='Map Type', choices=[(b'roadmap', 'Roadmap'), (b'satellite', 'Satellite')]),
        ),
        migrations.AlterField(
            model_name='embedplaceplugin',
            name='width',
            field=models.CharField(default=b'100%', help_text='Plugin width (in pixels or percent).', max_length=255, verbose_name='width'),
        ),
        migrations.AlterField(
            model_name='embedsearchplugin',
            name='height',
            field=models.CharField(default=b'400px', help_text='Plugin height (in pixels).', max_length=255, verbose_name='height'),
        ),
        migrations.AlterField(
            model_name='embedsearchplugin',
            name='map_type',
            field=models.CharField(default=b'roadmap', max_length=255, verbose_name='Map Type', choices=[(b'roadmap', 'Roadmap'), (b'satellite', 'Satellite')]),
        ),
        migrations.AlterField(
            model_name='embedsearchplugin',
            name='width',
            field=models.CharField(default=b'100%', help_text='Plugin width (in pixels or percent).', max_length=255, verbose_name='width'),
        ),
        migrations.AlterField(
            model_name='embedviewplugin',
            name='height',
            field=models.CharField(default=b'400px', help_text='Plugin height (in pixels).', max_length=255, verbose_name='height'),
        ),
        migrations.AlterField(
            model_name='embedviewplugin',
            name='map_type',
            field=models.CharField(default=b'roadmap', max_length=255, verbose_name='Map Type', choices=[(b'roadmap', 'Roadmap'), (b'satellite', 'Satellite')]),
        ),
        migrations.AlterField(
            model_name='embedviewplugin',
            name='width',
            field=models.CharField(default=b'100%', help_text='Plugin width (in pixels or percent).', max_length=255, verbose_name='width'),
        ),
        migrations.AlterField(
            model_name='locationplugin',
            name='address',
            field=models.CharField(max_length=255, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='locationplugin',
            name='city',
            field=models.CharField(max_length=255, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='locationplugin',
            name='content',
            field=models.CharField(help_text='Displayed in a info window above location marker', max_length=255, verbose_name='Content', blank=True),
        ),
        migrations.AlterField(
            model_name='mapplugin',
            name='height',
            field=models.CharField(default=b'400px', help_text='Plugin height (in pixels).', max_length=255, verbose_name='height'),
        ),
        migrations.AlterField(
            model_name='mapplugin',
            name='map_type',
            field=models.CharField(default=b'roadmap', max_length=255, verbose_name='Map Type', choices=[(b'roadmap', 'Roadmap'), (b'satellite', 'Satellite'), (b'hybrid', 'Hybrid'), (b'terrain', 'Terrain')]),
        ),
        migrations.AlterField(
            model_name='mapplugin',
            name='route_planner_title',
            field=models.CharField(default='Calculate your fastest way to here', max_length=255, null=True, verbose_name='Route Planner Title', blank=True),
        ),
        migrations.AlterField(
            model_name='mapplugin',
            name='title',
            field=models.CharField(max_length=255, null=True, verbose_name='map title', blank=True),
        ),
        migrations.AlterField(
            model_name='mapplugin',
            name='width',
            field=models.CharField(default=b'100%', help_text='Plugin width (in pixels or percent).', max_length=255, verbose_name='width'),
        ),
    ]
