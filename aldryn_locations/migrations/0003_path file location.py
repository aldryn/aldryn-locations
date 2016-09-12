# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('filer', '0006_auto_20160623_1627'),
        ('aldryn_locations', '0002_bump_max_lengths'),
    ]

    operations = [
        migrations.CreateModel(
            name='PathLocationPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='aldryn_locations_pathlocationplugin', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('path_file', filer.fields.file.FilerFileField(related_name='+', verbose_name='Path File (e.g. KML)', to='filer.File')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
