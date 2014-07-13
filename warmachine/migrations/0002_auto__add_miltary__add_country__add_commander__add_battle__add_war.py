# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Miltary'
        db.create_table(u'warmachine_miltary', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(related_name='country', to=orm['warmachine.Country'])),
            ('allies', self.gf('django.db.models.fields.related.ForeignKey')(related_name='allies', to=orm['warmachine.Country'])),
            ('enemy', self.gf('django.db.models.fields.related.ForeignKey')(related_name='enemy', to=orm['warmachine.Country'])),
        ))
        db.send_create_signal(u'warmachine', ['Miltary'])

        # Adding model 'Country'
        db.create_table(u'warmachine_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'warmachine', ['Country'])

        # Adding model 'Commander'
        db.create_table(u'warmachine_commander', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('military', self.gf('django.db.models.fields.related.ForeignKey')(related_name='military', to=orm['warmachine.Miltary'])),
            ('battle', self.gf('django.db.models.fields.related.ForeignKey')(related_name='battle', to=orm['warmachine.Battle'])),
        ))
        db.send_create_signal(u'warmachine', ['Commander'])

        # Adding model 'Battle'
        db.create_table(u'warmachine_battle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date', self.gf('django.db.models.fields.IntegerField')()),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('war', self.gf('django.db.models.fields.related.ForeignKey')(related_name='war', to=orm['warmachine.War'])),
            ('winner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='winner', to=orm['warmachine.Country'])),
            ('loser', self.gf('django.db.models.fields.related.ForeignKey')(related_name='loser', to=orm['warmachine.Country'])),
        ))
        db.send_create_signal(u'warmachine', ['Battle'])

        # Adding model 'War'
        db.create_table(u'warmachine_war', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('start_date', self.gf('django.db.models.fields.IntegerField')()),
            ('end_date', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'warmachine', ['War'])


    def backwards(self, orm):
        # Deleting model 'Miltary'
        db.delete_table(u'warmachine_miltary')

        # Deleting model 'Country'
        db.delete_table(u'warmachine_country')

        # Deleting model 'Commander'
        db.delete_table(u'warmachine_commander')

        # Deleting model 'Battle'
        db.delete_table(u'warmachine_battle')

        # Deleting model 'War'
        db.delete_table(u'warmachine_war')


    models = {
        u'warmachine.battle': {
            'Meta': {'object_name': 'Battle'},
            'date': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'loser': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'loser'", 'to': u"orm['warmachine.Country']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'war': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'war'", 'to': u"orm['warmachine.War']"}),
            'winner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'winner'", 'to': u"orm['warmachine.Country']"})
        },
        u'warmachine.commander': {
            'Meta': {'object_name': 'Commander'},
            'battle': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'battle'", 'to': u"orm['warmachine.Battle']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'military': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'military'", 'to': u"orm['warmachine.Miltary']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'warmachine.country': {
            'Meta': {'object_name': 'Country'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'warmachine.miltary': {
            'Meta': {'object_name': 'Miltary'},
            'allies': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'allies'", 'to': u"orm['warmachine.Country']"}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'country'", 'to': u"orm['warmachine.Country']"}),
            'enemy': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'enemy'", 'to': u"orm['warmachine.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'warmachine.war': {
            'Meta': {'object_name': 'War'},
            'end_date': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'start_date': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['warmachine']