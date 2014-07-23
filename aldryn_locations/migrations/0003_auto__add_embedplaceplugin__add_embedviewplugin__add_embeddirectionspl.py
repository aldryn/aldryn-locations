# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EmbedPlacePlugin'
        db.create_table(u'aldryn_locations_embedplaceplugin', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('query', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('map_type', self.gf('django.db.models.fields.CharField')(default='roadmap', max_length=300)),
            ('center', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('zoom', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('ui_lang', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('width', self.gf('django.db.models.fields.CharField')(default='100%', max_length=6)),
            ('height', self.gf('django.db.models.fields.CharField')(default='400px', max_length=6)),
        ))
        db.send_create_signal(u'aldryn_locations', ['EmbedPlacePlugin'])

        # Adding model 'EmbedViewPlugin'
        db.create_table(u'aldryn_locations_embedviewplugin', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('query', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('map_type', self.gf('django.db.models.fields.CharField')(default='roadmap', max_length=300)),
            ('center', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('zoom', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('ui_lang', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('width', self.gf('django.db.models.fields.CharField')(default='100%', max_length=6)),
            ('height', self.gf('django.db.models.fields.CharField')(default='400px', max_length=6)),
        ))
        db.send_create_signal(u'aldryn_locations', ['EmbedViewPlugin'])

        # Adding model 'EmbedDirectionsPlugin'
        db.create_table(u'aldryn_locations_embeddirectionsplugin', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('query', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('map_type', self.gf('django.db.models.fields.CharField')(default='roadmap', max_length=300)),
            ('center', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('zoom', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('ui_lang', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('width', self.gf('django.db.models.fields.CharField')(default='100%', max_length=6)),
            ('height', self.gf('django.db.models.fields.CharField')(default='400px', max_length=6)),
            ('origin', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('destination', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('waypoints', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('travel_mode', self.gf('django.db.models.fields.CharField')(default='auto', max_length=50)),
            ('avoid', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('units', self.gf('django.db.models.fields.CharField')(default='auto', max_length=10)),
        ))
        db.send_create_signal(u'aldryn_locations', ['EmbedDirectionsPlugin'])

        # Adding model 'EmbedSearchPlugin'
        db.create_table(u'aldryn_locations_embedsearchplugin', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('query', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('map_type', self.gf('django.db.models.fields.CharField')(default='roadmap', max_length=300)),
            ('center', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('zoom', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('ui_lang', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('width', self.gf('django.db.models.fields.CharField')(default='100%', max_length=6)),
            ('height', self.gf('django.db.models.fields.CharField')(default='400px', max_length=6)),
        ))
        db.send_create_signal(u'aldryn_locations', ['EmbedSearchPlugin'])


    def backwards(self, orm):
        # Deleting model 'EmbedPlacePlugin'
        db.delete_table(u'aldryn_locations_embedplaceplugin')

        # Deleting model 'EmbedViewPlugin'
        db.delete_table(u'aldryn_locations_embedviewplugin')

        # Deleting model 'EmbedDirectionsPlugin'
        db.delete_table(u'aldryn_locations_embeddirectionsplugin')

        # Deleting model 'EmbedSearchPlugin'
        db.delete_table(u'aldryn_locations_embedsearchplugin')


    models = {
        u'aldryn_locations.embeddirectionsplugin': {
            'Meta': {'object_name': 'EmbedDirectionsPlugin'},
            'avoid': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'center': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'destination': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'height': ('django.db.models.fields.CharField', [], {'default': "'400px'", 'max_length': '6'}),
            'map_type': ('django.db.models.fields.CharField', [], {'default': "'roadmap'", 'max_length': '300'}),
            'origin': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'query': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'travel_mode': ('django.db.models.fields.CharField', [], {'default': "'auto'", 'max_length': '50'}),
            'ui_lang': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'units': ('django.db.models.fields.CharField', [], {'default': "'auto'", 'max_length': '10'}),
            'waypoints': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.CharField', [], {'default': "'100%'", 'max_length': '6'}),
            'zoom': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'})
        },
        u'aldryn_locations.embedplaceplugin': {
            'Meta': {'object_name': 'EmbedPlacePlugin'},
            'center': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'height': ('django.db.models.fields.CharField', [], {'default': "'400px'", 'max_length': '6'}),
            'map_type': ('django.db.models.fields.CharField', [], {'default': "'roadmap'", 'max_length': '300'}),
            'query': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ui_lang': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.CharField', [], {'default': "'100%'", 'max_length': '6'}),
            'zoom': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'})
        },
        u'aldryn_locations.embedsearchplugin': {
            'Meta': {'object_name': 'EmbedSearchPlugin'},
            'center': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'height': ('django.db.models.fields.CharField', [], {'default': "'400px'", 'max_length': '6'}),
            'map_type': ('django.db.models.fields.CharField', [], {'default': "'roadmap'", 'max_length': '300'}),
            'query': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ui_lang': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.CharField', [], {'default': "'100%'", 'max_length': '6'}),
            'zoom': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'})
        },
        u'aldryn_locations.embedviewplugin': {
            'Meta': {'object_name': 'EmbedViewPlugin'},
            'center': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'height': ('django.db.models.fields.CharField', [], {'default': "'400px'", 'max_length': '6'}),
            'map_type': ('django.db.models.fields.CharField', [], {'default': "'roadmap'", 'max_length': '300'}),
            'query': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ui_lang': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.CharField', [], {'default': "'100%'", 'max_length': '6'}),
            'zoom': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'})
        },
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