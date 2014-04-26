# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table('revuo_author', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['auth.User'])),
            ('editor', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('about', self.gf('django.db.models.fields.TextField')(max_length=1024)),
        ))
        db.send_create_signal('revuo', ['Author'])

        # Adding model 'Admin'
        db.create_table('revuo_admin', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['auth.User'])),
        ))
        db.send_create_signal('revuo', ['Admin'])

        # Adding model 'NewsItem'
        db.create_table('revuo_newsitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('published_at', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now=True)),
            ('authorized', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['revuo.Author'])),
            ('title', self.gf('django.db.models.fields.TextField')(max_length=140)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=280)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('revuo', ['NewsItem'])

        # Adding model 'BlogItem'
        db.create_table('revuo_blogitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('published_at', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now=True)),
            ('authorized', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['revuo.Author'])),
            ('title', self.gf('django.db.models.fields.TextField')(max_length=140)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=280)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('revuo', ['BlogItem'])

        # Adding model 'Publication'
        db.create_table('revuo_publication', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('published_at', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now=True)),
            ('authorized', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['revuo.Author'])),
            ('title', self.gf('django.db.models.fields.TextField')(max_length=140)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=280)),
            ('attachment', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('revuo', ['Publication'])


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table('revuo_author')

        # Deleting model 'Admin'
        db.delete_table('revuo_admin')

        # Deleting model 'NewsItem'
        db.delete_table('revuo_newsitem')

        # Deleting model 'BlogItem'
        db.delete_table('revuo_blogitem')

        # Deleting model 'Publication'
        db.delete_table('revuo_publication')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Group']", 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Permission']", 'related_name': "'user_set'"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'db_table': "'django_content_type'", 'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'revuo.admin': {
            'Meta': {'object_name': 'Admin'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['auth.User']"})
        },
        'revuo.author': {
            'Meta': {'object_name': 'Author'},
            'about': ('django.db.models.fields.TextField', [], {'max_length': '1024'}),
            'editor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['auth.User']"})
        },
        'revuo.blogitem': {
            'Meta': {'object_name': 'BlogItem'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['revuo.Author']"}),
            'authorized': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '280'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.TextField', [], {'max_length': '140'})
        },
        'revuo.newsitem': {
            'Meta': {'object_name': 'NewsItem'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['revuo.Author']"}),
            'authorized': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '280'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.TextField', [], {'max_length': '140'})
        },
        'revuo.publication': {
            'Meta': {'object_name': 'Publication'},
            'attachment': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['revuo.Author']"}),
            'authorized': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '280'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {'max_length': '140'})
        }
    }

    complete_apps = ['revuo']