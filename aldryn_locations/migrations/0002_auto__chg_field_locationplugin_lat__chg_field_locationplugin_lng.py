# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'LocationPlugin.lat'
        db.alter_column(u'aldryn_locations_locationplugin', 'lat', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'LocationPlugin.lng'
        db.alter_column(u'aldryn_locations_locationplugin', 'lng', self.gf('django.db.models.fields.FloatField')(null=True))

    def backwards(self, orm):

        # Changing field 'LocationPlugin.lat'
        db.alter_column(u'aldryn_locations_locationplugin', 'lat', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=6))

        # Changing field 'LocationPlugin.lng'
        db.alter_column(u'aldryn_locations_locationplugin', 'lng', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=6))

    models = {
        u'aldryn_locations.locationplugin': {
            'Meta': {'object_name': 'LocationPlugin', '_ormbases': ['cms.CMSPlugin']},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'lng': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'aldryn_locations.mapplugin': {
            'Meta': {'object_name': 'MapPlugin', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'double_click_zoom': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'draggable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'height': ('django.db.models.fields.CharField', [], {'default': "'400px'", 'max_length': '6'}),
            'keyboard_shortcuts': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'map_type': ('django.db.models.fields.CharField', [], {'default': "'roadmap'", 'max_length': '300'}),
            'pan_control': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'route_planner_title': ('django.db.models.fields.CharField', [], {'default': "u'Calculate your fastest way to here'", 'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'scrollwheel': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'street_view_control': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.CharField', [], {'default': "'100%'", 'max_length': '6'}),
            'zoom': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'zoom_control': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'aldryn_locations.routelocationplugin': {
            'Meta': {'object_name': 'RouteLocationPlugin', '_ormbases': [u'aldryn_locations.LocationPlugin']},
            u'locationplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['aldryn_locations.LocationPlugin']", 'unique': 'True', 'primary_key': 'True'})
        },
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['aldryn_locations']