# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Miltary'
        db.delete_table(u'warmachine_miltary')

        # Adding model 'Military'
        db.create_table(u'warmachine_military', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(related_name='country', to=orm['warmachine.Country'])),
            ('allies', self.gf('django.db.models.fields.related.ForeignKey')(related_name='allies', to=orm['warmachine.Country'])),
            ('enemy', self.gf('django.db.models.fields.related.ForeignKey')(related_name='enemy', to=orm['warmachine.Country'])),
        ))
        db.send_create_signal(u'warmachine', ['Military'])


        # Changing field 'Commander.military'
        db.alter_column(u'warmachine_commander', 'military_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['warmachine.Military']))

    def backwards(self, orm):
        # Adding model 'Miltary'
        db.create_table(u'warmachine_miltary', (
            ('enemy', self.gf('django.db.models.fields.related.ForeignKey')(related_name='enemy', to=orm['warmachine.Country'])),
            ('allies', self.gf('django.db.models.fields.related.ForeignKey')(related_name='allies', to=orm['warmachine.Country'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(related_name='country', to=orm['warmachine.Country'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'warmachine', ['Miltary'])

        # Deleting model 'Military'
        db.delete_table(u'warmachine_military')


        # Changing field 'Commander.military'
        db.alter_column(u'warmachine_commander', 'military_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['warmachine.Miltary']))

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
            'military': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'military'", 'to': u"orm['warmachine.Military']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'warmachine.country': {
            'Meta': {'object_name': 'Country'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'warmachine.military': {
            'Meta': {'object_name': 'Military'},
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