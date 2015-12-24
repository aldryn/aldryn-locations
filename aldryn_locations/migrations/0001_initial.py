# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmbedDirectionsPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('query', models.CharField(help_text='defines the place to highlight on the map. It accepts a location as either a place name or address', max_length=255, verbose_name='Query')),
                ('map_type', models.CharField(default=b'roadmap', max_length=300, verbose_name='Map Type', choices=[(b'roadmap', 'Roadmap'), (b'satellite', 'Satellite')])),
                ('center', models.CharField(help_text='optionally define the center of the map view. It accepts a comma-separated latitude and longitude value (such as 37.4218,-122.0840).', max_length=255, null=True, verbose_name='Center of the map (latitude + longitude)', blank=True)),
                ('zoom', models.CharField(choices=[(b'0', b'0'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'13', b'13'), (b'14', b'14'), (b'15', b'15'), (b'16', b'16'), (b'17', b'17'), (b'18', b'18'), (b'19', b'19'), (b'20', b'20'), (b'21', b'21')], max_length=2, blank=True, help_text='0 (the whole world) to 21 (individual buildings). Leave empty for auto zoom', null=True, verbose_name='Zoom level')),
                ('ui_lang', models.CharField(help_text='default to page language', max_length=10, null=True, verbose_name='language for ui elements', blank=True)),
                ('region', models.CharField(help_text=' defines the appropriate borders and labels to display, based on geo-political sensitivities. Accepts a region code specified as a two-character ccTLD (top-level domain) value.', max_length=10, null=True, verbose_name='map region (ccTLD)', blank=True)),
                ('width', models.CharField(default=b'100%', help_text='Plugin width (in pixels or percent).', max_length=6, verbose_name='width')),
                ('height', models.CharField(default=b'400px', help_text='Plugin height (in pixels).', max_length=6, verbose_name='height')),
                ('origin', models.CharField(help_text='defines the origin and accepts a location as either a place name or address', max_length=255, verbose_name='origin')),
                ('destination', models.CharField(help_text='defines the destination and accepts a location as either a place name or address', max_length=255, verbose_name='destination')),
                ('waypoints', models.CharField(help_text='separated by the pipe character (|) (e.g. Berlin,Germany|Paris,France)', max_length=255, null=True, verbose_name='list of waypoints', blank=True)),
                ('travel_mode', models.CharField(default=b'auto', max_length=50, verbose_name='travel mode', choices=[(b'auto', 'Automatic'), (b'driving', 'Driving'), (b'walking', 'Walking'), (b'bicycling', 'Bicycling'), (b'transit', 'Transit'), (b'flying', 'Flying')])),
                ('avoid', models.CharField(blank=True, max_length=50, null=True, verbose_name='avoid certain means', choices=[(b'tolls', 'Tolls'), (b'highways', 'Highways'), (b'ferries', 'Ferries'), (b'tolls|highways', 'Tolls & Highways'), (b'tolls|ferries', 'Tolls & Ferries'), (b'ferries|highways', 'Ferries & Highways'), (b'tolls|ferries|highways', 'Tolls, Ferries & Highways')])),
                ('units', models.CharField(default=b'auto', max_length=10, verbose_name='units for distances in results', choices=[(b'auto', 'Automatic'), (b'metric', 'Metric'), (b'imperial', 'Imperial')])),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='EmbedPlacePlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('query', models.CharField(help_text='defines the place to highlight on the map. It accepts a location as either a place name or address', max_length=255, verbose_name='Query')),
                ('map_type', models.CharField(default=b'roadmap', max_length=300, verbose_name='Map Type', choices=[(b'roadmap', 'Roadmap'), (b'satellite', 'Satellite')])),
                ('center', models.CharField(help_text='optionally define the center of the map view. It accepts a comma-separated latitude and longitude value (such as 37.4218,-122.0840).', max_length=255, null=True, verbose_name='Center of the map (latitude + longitude)', blank=True)),
                ('zoom', models.CharField(choices=[(b'0', b'0'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'13', b'13'), (b'14', b'14'), (b'15', b'15'), (b'16', b'16'), (b'17', b'17'), (b'18', b'18'), (b'19', b'19'), (b'20', b'20'), (b'21', b'21')], max_length=2, blank=True, help_text='0 (the whole world) to 21 (individual buildings). Leave empty for auto zoom', null=True, verbose_name='Zoom level')),
                ('ui_lang', models.CharField(help_text='default to page language', max_length=10, null=True, verbose_name='language for ui elements', blank=True)),
                ('region', models.CharField(help_text=' defines the appropriate borders and labels to display, based on geo-political sensitivities. Accepts a region code specified as a two-character ccTLD (top-level domain) value.', max_length=10, null=True, verbose_name='map region (ccTLD)', blank=True)),
                ('width', models.CharField(default=b'100%', help_text='Plugin width (in pixels or percent).', max_length=6, verbose_name='width')),
                ('height', models.CharField(default=b'400px', help_text='Plugin height (in pixels).', max_length=6, verbose_name='height')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='EmbedSearchPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('query', models.CharField(help_text='defines the place to highlight on the map. It accepts a location as either a place name or address', max_length=255, verbose_name='Query')),
                ('map_type', models.CharField(default=b'roadmap', max_length=300, verbose_name='Map Type', choices=[(b'roadmap', 'Roadmap'), (b'satellite', 'Satellite')])),
                ('center', models.CharField(help_text='optionally define the center of the map view. It accepts a comma-separated latitude and longitude value (such as 37.4218,-122.0840).', max_length=255, null=True, verbose_name='Center of the map (latitude + longitude)', blank=True)),
                ('zoom', models.CharField(choices=[(b'0', b'0'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'13', b'13'), (b'14', b'14'), (b'15', b'15'), (b'16', b'16'), (b'17', b'17'), (b'18', b'18'), (b'19', b'19'), (b'20', b'20'), (b'21', b'21')], max_length=2, blank=True, help_text='0 (the whole world) to 21 (individual buildings). Leave empty for auto zoom', null=True, verbose_name='Zoom level')),
                ('ui_lang', models.CharField(help_text='default to page language', max_length=10, null=True, verbose_name='language for ui elements', blank=True)),
                ('region', models.CharField(help_text=' defines the appropriate borders and labels to display, based on geo-political sensitivities. Accepts a region code specified as a two-character ccTLD (top-level domain) value.', max_length=10, null=True, verbose_name='map region (ccTLD)', blank=True)),
                ('width', models.CharField(default=b'100%', help_text='Plugin width (in pixels or percent).', max_length=6, verbose_name='width')),
                ('height', models.CharField(default=b'400px', help_text='Plugin height (in pixels).', max_length=6, verbose_name='height')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='EmbedViewPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('query', models.CharField(help_text='defines the place to highlight on the map. It accepts a location as either a place name or address', max_length=255, verbose_name='Query')),
                ('map_type', models.CharField(default=b'roadmap', max_length=300, verbose_name='Map Type', choices=[(b'roadmap', 'Roadmap'), (b'satellite', 'Satellite')])),
                ('center', models.CharField(help_text='optionally define the center of the map view. It accepts a comma-separated latitude and longitude value (such as 37.4218,-122.0840).', max_length=255, null=True, verbose_name='Center of the map (latitude + longitude)', blank=True)),
                ('zoom', models.CharField(choices=[(b'0', b'0'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'13', b'13'), (b'14', b'14'), (b'15', b'15'), (b'16', b'16'), (b'17', b'17'), (b'18', b'18'), (b'19', b'19'), (b'20', b'20'), (b'21', b'21')], max_length=2, blank=True, help_text='0 (the whole world) to 21 (individual buildings). Leave empty for auto zoom', null=True, verbose_name='Zoom level')),
                ('ui_lang', models.CharField(help_text='default to page language', max_length=10, null=True, verbose_name='language for ui elements', blank=True)),
                ('region', models.CharField(help_text=' defines the appropriate borders and labels to display, based on geo-political sensitivities. Accepts a region code specified as a two-character ccTLD (top-level domain) value.', max_length=10, null=True, verbose_name='map region (ccTLD)', blank=True)),
                ('width', models.CharField(default=b'100%', help_text='Plugin width (in pixels or percent).', max_length=6, verbose_name='width')),
                ('height', models.CharField(default=b'400px', help_text='Plugin height (in pixels).', max_length=6, verbose_name='height')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='LocationPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('address', models.CharField(max_length=150, verbose_name='address')),
                ('zipcode', models.CharField(max_length=30, verbose_name='zip code')),
                ('city', models.CharField(max_length=100, verbose_name='city')),
                ('content', models.CharField(help_text='Displayed under address in the bubble.', max_length=255, verbose_name='additional content', blank=True)),
                ('lat', models.FloatField(help_text='Use latitude & longitude to fine tune the map position.', null=True, verbose_name='latitude', blank=True)),
                ('lng', models.FloatField(null=True, verbose_name='longitude', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='MapPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='map title', blank=True)),
                ('zoom', models.CharField(choices=[(b'0', b'0'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'13', b'13'), (b'14', b'14'), (b'15', b'15'), (b'16', b'16'), (b'17', b'17'), (b'18', b'18'), (b'19', b'19'), (b'20', b'20'), (b'21', b'21')], max_length=20, blank=True, help_text='Leave empty for auto zoom', null=True, verbose_name='Zoom level')),
                ('route_planner_title', models.CharField(default='Calculate your fastest way to here', max_length=150, null=True, verbose_name='Route Planner Title', blank=True)),
                ('width', models.CharField(default=b'100%', help_text='Plugin width (in pixels or percent).', max_length=6, verbose_name='width')),
                ('height', models.CharField(default=b'400px', help_text='Plugin height (in pixels).', max_length=6, verbose_name='height')),
                ('scrollwheel', models.BooleanField(default=True, verbose_name='Enable scrollwheel zooming on the map')),
                ('double_click_zoom', models.BooleanField(default=True, verbose_name='Enable double click to zoom')),
                ('draggable', models.BooleanField(default=True, verbose_name='Allow map dragging')),
                ('keyboard_shortcuts', models.BooleanField(default=True, verbose_name='Enable keyboard shortcuts')),
                ('pan_control', models.BooleanField(default=True, verbose_name='Show pan control')),
                ('zoom_control', models.BooleanField(default=True, verbose_name='Show zoom control')),
                ('street_view_control', models.BooleanField(default=True, verbose_name='Show Street View control')),
                ('map_type', models.CharField(default=b'roadmap', max_length=300, verbose_name='Map Type', choices=[(b'roadmap', 'Roadmap'), (b'satellite', 'Satellite'), (b'hybrid', 'Hybrid'), (b'terrain', 'Terrain')])),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='RouteLocationPlugin',
            fields=[
                ('locationplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='aldryn_locations.LocationPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('aldryn_locations.locationplugin',),
        ),
    ]
