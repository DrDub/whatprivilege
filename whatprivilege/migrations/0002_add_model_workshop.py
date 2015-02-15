# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Workshop'
        db.create_table(u'whatprivilege_workshop', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('urlCode', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'whatprivilege', ['Workshop'])


    def backwards(self, orm):
        # Deleting model 'Workshop'
        db.delete_table(u'whatprivilege_workshop')


    models = {
        u'whatprivilege.question': {
            'Meta': {'object_name': 'Question'},
            'helpLink': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'helpText': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numberNo': ('django.db.models.fields.IntegerField', [], {}),
            'numberYes': ('django.db.models.fields.IntegerField', [], {}),
            'questionText': ('django.db.models.fields.TextField', [], {})
        },
        u'whatprivilege.workshop': {
            'Meta': {'object_name': 'Workshop'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'urlCode': ('django.db.models.fields.TextField', [], {})
        },
        u'whatprivilege.workshopquestion': {
            'Meta': {'object_name': 'WorkshopQuestion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numberNo': ('django.db.models.fields.IntegerField', [], {}),
            'numberYes': ('django.db.models.fields.IntegerField', [], {}),
            'qID': ('django.db.models.fields.IntegerField', [], {}),
            'workshopID': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['whatprivilege']