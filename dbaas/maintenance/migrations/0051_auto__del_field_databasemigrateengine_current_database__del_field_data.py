# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'DatabaseMigrateEngine.current_database'
        db.delete_column(u'maintenance_databasemigrateengine', 'current_database_id')

        # Deleting field 'DatabaseMigrateEngine.databaseupgrade_ptr'
        db.delete_column(u'maintenance_databasemigrateengine', u'databaseupgrade_ptr_id')

        # Adding field 'DatabaseMigrateEngine.id'
        db.add_column(u'maintenance_databasemigrateengine', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=1, primary_key=True),
                      keep_default=False)

        # Adding field 'DatabaseMigrateEngine.created_at'
        db.add_column(u'maintenance_databasemigrateengine', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=1, blank=True),
                      keep_default=False)

        # Adding field 'DatabaseMigrateEngine.updated_at'
        db.add_column(u'maintenance_databasemigrateengine', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=1, blank=True),
                      keep_default=False)

        # Adding field 'DatabaseMigrateEngine.current_step'
        db.add_column(u'maintenance_databasemigrateengine', 'current_step',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DatabaseMigrateEngine.status'
        db.add_column(u'maintenance_databasemigrateengine', 'status',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DatabaseMigrateEngine.started_at'
        db.add_column(u'maintenance_databasemigrateengine', 'started_at',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'DatabaseMigrateEngine.finished_at'
        db.add_column(u'maintenance_databasemigrateengine', 'finished_at',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'DatabaseMigrateEngine.can_do_retry'
        db.add_column(u'maintenance_databasemigrateengine', 'can_do_retry',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'DatabaseMigrateEngine.task_schedule'
        db.add_column(u'maintenance_databasemigrateengine', 'task_schedule',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'maintenance_databasemigrateengine_related', null=True, to=orm['maintenance.TaskSchedule']),
                      keep_default=False)

        # Adding field 'DatabaseMigrateEngine.database'
        db.add_column(u'maintenance_databasemigrateengine', 'database',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name=u'engine_migrations', to=orm['logical.Database']),
                      keep_default=False)

        # Adding field 'DatabaseMigrateEngine.task'
        db.add_column(u'maintenance_databasemigrateengine', 'task',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name=u'database_engine_migrations', to=orm['notification.TaskHistory']),
                      keep_default=False)

        # Adding field 'DatabaseMigrateEngine.source_plan'
        db.add_column(u'maintenance_databasemigrateengine', 'source_plan',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'database_engine_migrations_source', null=True, on_delete=models.SET_NULL, to=orm['physical.Plan']),
                      keep_default=False)

        # Adding field 'DatabaseMigrateEngine.source_plan_name'
        db.add_column(u'maintenance_databasemigrateengine', 'source_plan_name',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DatabaseMigrateEngine.target_plan'
        db.add_column(u'maintenance_databasemigrateengine', 'target_plan',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'database_engine_migrations_target', null=True, on_delete=models.SET_NULL, to=orm['physical.Plan']),
                      keep_default=False)

        # Adding field 'DatabaseMigrateEngine.target_plan_name'
        db.add_column(u'maintenance_databasemigrateengine', 'target_plan_name',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'DatabaseMigrateEngine.current_database'
        db.add_column(u'maintenance_databasemigrateengine', 'current_database',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name=u'engine_migrations', to=orm['logical.Database']),
                      keep_default=False)

        # Adding field 'DatabaseMigrateEngine.databaseupgrade_ptr'
        db.add_column(u'maintenance_databasemigrateengine', u'databaseupgrade_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['maintenance.DatabaseUpgrade'], unique=True, primary_key=True),
                      keep_default=False)

        # Deleting field 'DatabaseMigrateEngine.id'
        db.delete_column(u'maintenance_databasemigrateengine', u'id')

        # Deleting field 'DatabaseMigrateEngine.created_at'
        db.delete_column(u'maintenance_databasemigrateengine', 'created_at')

        # Deleting field 'DatabaseMigrateEngine.updated_at'
        db.delete_column(u'maintenance_databasemigrateengine', 'updated_at')

        # Deleting field 'DatabaseMigrateEngine.current_step'
        db.delete_column(u'maintenance_databasemigrateengine', 'current_step')

        # Deleting field 'DatabaseMigrateEngine.status'
        db.delete_column(u'maintenance_databasemigrateengine', 'status')

        # Deleting field 'DatabaseMigrateEngine.started_at'
        db.delete_column(u'maintenance_databasemigrateengine', 'started_at')

        # Deleting field 'DatabaseMigrateEngine.finished_at'
        db.delete_column(u'maintenance_databasemigrateengine', 'finished_at')

        # Deleting field 'DatabaseMigrateEngine.can_do_retry'
        db.delete_column(u'maintenance_databasemigrateengine', 'can_do_retry')

        # Deleting field 'DatabaseMigrateEngine.task_schedule'
        db.delete_column(u'maintenance_databasemigrateengine', 'task_schedule_id')

        # Deleting field 'DatabaseMigrateEngine.database'
        db.delete_column(u'maintenance_databasemigrateengine', 'database_id')

        # Deleting field 'DatabaseMigrateEngine.task'
        db.delete_column(u'maintenance_databasemigrateengine', 'task_id')

        # Deleting field 'DatabaseMigrateEngine.source_plan'
        db.delete_column(u'maintenance_databasemigrateengine', 'source_plan_id')

        # Deleting field 'DatabaseMigrateEngine.source_plan_name'
        db.delete_column(u'maintenance_databasemigrateengine', 'source_plan_name')

        # Deleting field 'DatabaseMigrateEngine.target_plan'
        db.delete_column(u'maintenance_databasemigrateengine', 'target_plan_id')

        # Deleting field 'DatabaseMigrateEngine.target_plan_name'
        db.delete_column(u'maintenance_databasemigrateengine', 'target_plan_name')


    models = {
        u'account.organization': {
            'Meta': {'object_name': 'Organization'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'external': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'grafana_datasource': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'grafana_endpoint': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'grafana_hostgroup': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'grafana_orgid': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'account.team': {
            'Meta': {'ordering': "[u'name']", 'object_name': 'Team'},
            'contacts': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'database_alocation_limit': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '2'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'team_organization'", 'on_delete': 'models.PROTECT', 'to': u"orm['account.Organization']"}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.Group']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.User']", 'symmetrical': 'False'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'backup.backupgroup': {
            'Meta': {'object_name': 'BackupGroup'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'backup.snapshot': {
            'Meta': {'object_name': 'Snapshot'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'database_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'end_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'environment': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'backup_environment'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['physical.Environment']"}),
            'error': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'backups'", 'null': 'True', 'to': u"orm['backup.BackupGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'backup_instance'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['physical.Instance']"}),
            'is_automatic': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'purge_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'snapshopt_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'snapshot_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'start_at': ('django.db.models.fields.DateTimeField', [], {}),
            'status': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.IntegerField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'volume': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'backups'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['physical.Volume']"}),
            'volume_path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'logical.database': {
            'Meta': {'ordering': "(u'name',)", 'unique_together': "((u'name', u'environment'),)", 'object_name': 'Database'},
            'backup_path': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'databaseinfra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'databases'", 'on_delete': 'models.PROTECT', 'to': u"orm['physical.DatabaseInfra']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'disk_auto_resize': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'environment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'databases'", 'on_delete': 'models.PROTECT', 'to': u"orm['physical.Environment']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_in_quarantine': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_protected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'databases'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': u"orm['logical.Project']"}),
            'quarantine_dt': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'quarantine_user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'databases_quarantine'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'subscribe_to_email_events': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'databases'", 'null': 'True', 'to': u"orm['account.Team']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'used_size_in_bytes': ('django.db.models.fields.FloatField', [], {'default': '0.0'})
        },
        u'logical.project': {
            'Meta': {'ordering': "[u'name']", 'object_name': 'Project'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'maintenance.addinstancestodatabase': {
            'Meta': {'object_name': 'AddInstancesToDatabase'},
            'can_do_retry': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'current_step': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'database': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'add_instances_to_database_manager'", 'to': u"orm['logical.Database']"}),
            'finished_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number_of_instances': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'number_of_instances_before': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'started_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'add_instances_to_database_manager'", 'to': u"orm['notification.TaskHistory']"}),
            'task_schedule': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'maintenance_addinstancestodatabase_related'", 'null': 'True', 'to': u"orm['maintenance.TaskSchedule']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'maintenance.databasechangeparameter': {
            'Meta': {'object_name': 'DatabaseChangeParameter'},
            'can_do_retry': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'current_step': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'database': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'change_parameters'", 'to': u"orm['logical.Database']"}),
            'finished_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'started_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'database_change_parameters'", 'to': u"orm['notification.TaskHistory']"}),
            'task_schedule': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'maintenance_databasechangeparameter_related'", 'null': 'True', 'to': u"orm['maintenance.TaskSchedule']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'maintenance.databaseclone': {
            'Meta': {'object_name': 'DatabaseClone'},
            'can_do_retry': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'current_step': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'database': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'databases_clone'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['logical.Database']"}),
            'environment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'databases_clone'", 'to': u"orm['physical.Environment']"}),
            'finished_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'databases_clone'", 'to': u"orm['physical.DatabaseInfra']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'origin_database': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'origin_databases_clone'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['logical.Database']"}),
            'plan': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'databases_clone'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['physical.Plan']"}),
            'started_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'create_clone'", 'to': u"orm['notification.TaskHistory']"}),
            'task_schedule': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'maintenance_databaseclone_related'", 'null': 'True', 'to': u"orm['maintenance.TaskSchedule']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'maintenance.databaseconfiguressl': {
            'Meta': {'object_name': 'DatabaseConfigureSSL'},
            'can_do_retry': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'current_step': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'database': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'configure_ssl'", 'to': u"orm['logical.Database']"}),
            'finished_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'started_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'database_configure_ssl'", 'to': u"orm['notification.TaskHistory']"}),
            'task_schedule': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'maintenance_databaseconfiguressl_related'", 'null': 'True', 'to': u"orm['maintenance.TaskSchedule']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'maintenance.databasecreate': {
            'Meta': {'object_name': 'DatabaseCreate'},
            'can_do_retry': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'current_step': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'database': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'databases_create'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['logical.Database']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'environment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'databases_create'", 'to': u"orm['physical.Environment']"}),
            'finished_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'databases_create'", 'to': u"orm['physical.DatabaseInfra']"}),
            'is_protected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'plan': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'databases_create'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['physical.Plan']"}),
            'plan_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'databases_create'", 'null': 'True', 'to': u"orm['logical.Project']"}),
            'started_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'subscribe_to_email_events': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'create_database'", 'to': u"orm['notification.TaskHistory']"}),
            'task_schedule': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'maintenance_databasecreate_related'", 'null': 'True', 'to': u"orm['maintenance.TaskSchedule']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'databases_create'", 'to': u"orm['account.Team']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'maintenance.databasedestroy': {
            'Meta': {'object_name': 'DatabaseDestroy'},
            'can_do_retry': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'current_step': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'database': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'databases_destroy'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['logical.Database']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'environment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'databases_destroy'", 'to': u"orm['physical.Environment']"}),
            'finished_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'databases_destroy'", 'to': u"orm['physical.DatabaseInfra']"}),
            'is_protected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'plan': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'databases_destroy'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['physical.Plan']"}),
            'plan_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'databases_destroy'", 'null': 'True', 'to': u"orm['logical.Project']"}),
            'started_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'subscribe_to_email_events': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'databases_destroy'", 'to': u"orm['notification.TaskHistory']"}),
            'task_schedule': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'maintenance_databasedestroy_related'", 'null': 'True', 'to': u"orm['maintenance.TaskSchedule']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'databases_destroy'", 'to': u"orm['account.Team']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'maintenance.databasemigrate': {
            'Meta': {'object_name': 'DatabaseMigrate'},
            'can_do_retry': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'current_step': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'database': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'database_migrate'", 'to': u"orm['logical.Database']"}),
            'environment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'database_migrate'", 'to': u"orm['physical.Environment']"}),
            'finished_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'offering': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'database_migrate'", 'null': 'True', 'to': u"orm['physical.Offering']"}),
            'origin_environment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['physical.Environment']"}),
            'origin_offering': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['physical.Offering']", 'null': 'True', 'blank': 'True'}),
            'started_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'database_migrate'", 'to': u"orm['notification.TaskHistory']"}),
            'task_schedule': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'maintenance_databasemigrate_related'", 'null': 'True', 'to': u"orm['maintenance.TaskSchedule']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'maintenance.databasemigrateengine': {
            'Meta': {'object_name': 'DatabaseMigrateEngine'},
            'can_do_retry': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'current_step': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'database': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'engine_migrations'", 'to': u"orm['logical.Database']"}),
            'finished_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source_plan': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'database_engine_migrations_source'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['physical.Plan']"}),
            'source_plan_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'started_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'target_plan': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'database_engine_migrations_target'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['physical.Plan']"}),
            'target_plan_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'database_engine_migrations'", 'to': u"orm['notification.TaskHistory']"}),
            'task_schedule': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'maintenance_databasemigrateengine_related'", 'null': 'True', 'to': u"orm['maintenance.TaskSchedule']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'maintenance.databasereinstallvm': {
            'Meta': {'object_name': 'DatabaseReinstallVM'},
            'can_do_retry': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'current_step': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'database': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'reinstall_vm'", 'to': u"orm['logical.Database']"}),
            'finished_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'database_reinstall_vm'", 'to': u"orm['physical.Instance']"}),
            'started_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'database_reinsgtall_vm'", 'to': u"orm['notification.TaskHistory']"}),
            'task_schedule': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'maintenance_databasereinstallvm_related'", 'null': 'True', 'to': u"orm['maintenance.TaskSchedule']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'maintenance.databaseresize': {
            'Meta': {'object_name': 'DatabaseResize'},
            'can_do_retry': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'current_step': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'database': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'resizes'", 'to': u"orm['logical.Database']"}),
            'finished_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source_offer': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'database_resizes_source'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['physical.Offering']"}),
            'source_offer_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'started_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'target_offer': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'database_resizes_target'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['physical.Offering']"}),
            'target_offer_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'database_resizes'", 'to': u"orm['notification.TaskHistory']"}),
            'task_schedule': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'maintenance_databaseresize_related'", 'null': 'True', 'to': u"orm['maintenance.TaskSchedule']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'maintenance.databaserestore': {
            'Meta': {'object_name': 'DatabaseRestore'},
            'can_do_retry': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'current_step': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'database': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'database_restore'", 'to': u"orm['logical.Database']"}),
            'finished_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'database_restore'", 'to': u"orm['backup.BackupGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'new_group': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'database_restore_new'", 'null': 'True', 'to': u"orm['backup.BackupGroup']"}),
            'started_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'database_restore'", 'to': u"orm['notification.TaskHistory']"}),
            'task_schedule': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'maintenance_databaserestore_related'", 'null': 'True', 'to': u"orm['maintenance.TaskSchedule']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'maintenance.databaserestoreinstancepair': {
            'Meta': {'unique_together': "((u'master', u'slave', u'restore'),)", 'object_name': 'DatabaseRestoreInstancePair'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'restore_master'", 'to': u"orm['physical.Instance']"}),
            'restore': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'restore_instances'", 'to': u"orm['maintenance.DatabaseRestore']"}),
            'slave': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'restore_slave'", 'to': u"orm['physical.Instance']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'maintenance.databaseupgrade': {
            'Meta': {'object_name': 'DatabaseUpgrade'},
            'can_do_retry': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'current_step': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'database': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'upgrades'", 'to': u"orm['logical.Database']"}),
            'finished_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source_plan': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'database_upgrades_source'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['physical.Plan']"}),
            'source_plan_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'started_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'target_plan': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'database_upgrades_target'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['physical.Plan']"}),
            'target_plan_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'database_upgrades'", 'to': u"orm['notification.TaskHistory']"}),
            'task_schedule': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'maintenance_databaseupgrade_related'", 'null': 'True', 'to': u"orm['maintenance.TaskSchedule']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'maintenance.databaseupgradepatch': {
            'Meta': {'object_name': 'DatabaseUpgradePatch'},
            'can_do_retry': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'current_step': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'database': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'upgrades_patch'", 'to': u"orm['logical.Database']"}),
            'finished_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source_patch': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'database_minor_upgrades_source'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['physical.EnginePatch']"}),
            'source_patch_full_version': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'started_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'target_patch': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'database_minor_upgrades_target'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['physical.EnginePatch']"}),
            'target_patch_full_version': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'database_upgrades_patch'", 'to': u"orm['notification.TaskHistory']"}),
            'task_schedule': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'maintenance_databaseupgradepatch_related'", 'null': 'True', 'to': u"orm['maintenance.TaskSchedule']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'maintenance.filermigrate': {
            'Meta': {'object_name': 'FilerMigrate'},
            'can_do_retry': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'current_step': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'database': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'filer_migrate'", 'to': u"orm['logical.Database']"}),
            'finished_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'original_export_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'started_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'filer_migrate'", 'to': u"orm['notification.TaskHistory']"}),
            'task_schedule': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'maintenance_filermigrate_related'", 'null': 'True', 'to': u"orm['maintenance.TaskSchedule']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'maintenance.hostmaintenance': {
            'Meta': {'unique_together': "((u'host', u'maintenance'),)", 'object_name': 'HostMaintenance', 'index_together': "[[u'host', u'maintenance']]"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'finished_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'host_maintenance'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['physical.Host']"}),
            'hostname': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_log': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'maintenance': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'maintenance'", 'to': u"orm['maintenance.Maintenance']"}),
            'rollback_log': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'started_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '4'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'maintenance.hostmigrate': {
            'Meta': {'object_name': 'HostMigrate'},
            'can_do_retry': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'current_step': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'database_migrate': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'hosts'", 'null': 'True', 'to': u"orm['maintenance.DatabaseMigrate']"}),
            'environment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'host_migrate'", 'to': u"orm['physical.Environment']"}),
            'finished_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'migrate'", 'to': u"orm['physical.Host']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'snapshot': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'snapshot_migrate'", 'null': 'True', 'to': u"orm['backup.Snapshot']"}),
            'started_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'host_migrate'", 'to': u"orm['notification.TaskHistory']"}),
            'task_schedule': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'maintenance_hostmigrate_related'", 'null': 'True', 'to': u"orm['maintenance.TaskSchedule']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'zone': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'maintenance.maintenance': {
            'Meta': {'object_name': 'Maintenance'},
            'affected_hosts': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'celery_task_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'disable_alarms': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'finished_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'hostsid': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '10000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_script': ('django.db.models.fields.TextField', [], {}),
            'maximum_workers': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'revoked_by': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'rollback_script': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'scheduled_for': ('django.db.models.fields.DateTimeField', [], {'unique': 'True'}),
            'started_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'maintenance.maintenanceparameters': {
            'Meta': {'object_name': 'MaintenanceParameters'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'function_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maintenance': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'maintenance_params'", 'to': u"orm['maintenance.Maintenance']"}),
            'parameter_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'maintenance.recreateslave': {
            'Meta': {'object_name': 'RecreateSlave'},
            'can_do_retry': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'current_step': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'finished_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'recreate_slave'", 'to': u"orm['physical.Host']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'snapshot': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'snapshot_recreate_slave'", 'null': 'True', 'to': u"orm['backup.Snapshot']"}),
            'started_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'recreate_slave'", 'to': u"orm['notification.TaskHistory']"}),
            'task_schedule': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'maintenance_recreateslave_related'", 'null': 'True', 'to': u"orm['maintenance.TaskSchedule']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'maintenance.restartdatabase': {
            'Meta': {'object_name': 'RestartDatabase'},
            'can_do_retry': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'current_step': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'database': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'restart_database_manager'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['logical.Database']"}),
            'finished_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'started_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'restart_database_manager'", 'to': u"orm['notification.TaskHistory']"}),
            'task_schedule': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'maintenance_restartdatabase_related'", 'null': 'True', 'to': u"orm['maintenance.TaskSchedule']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'maintenance.taskschedule': {
            'Meta': {'object_name': 'TaskSchedule'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'database': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'task_schedules'", 'to': u"orm['logical.Database']"}),
            'finished_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method_path': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'scheduled_for': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'started_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'maintenance.updatessl': {
            'Meta': {'object_name': 'UpdateSsl'},
            'can_do_retry': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'current_step': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'database': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'update_ssl_manager'", 'to': u"orm['logical.Database']"}),
            'finished_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'started_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'update_ssl_manager'", 'to': u"orm['notification.TaskHistory']"}),
            'task_schedule': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'maintenance_updatessl_related'", 'null': 'True', 'to': u"orm['maintenance.TaskSchedule']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'notification.taskhistory': {
            'Meta': {'object_name': 'TaskHistory'},
            'arguments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'context': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'database_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'db_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ended_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_class': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'relevance': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'task_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'task_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'task_status': ('django.db.models.fields.CharField', [], {'default': "u'WAITING'", 'max_length': '100', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'physical.cloud': {
            'Meta': {'object_name': 'Cloud'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'physical.databaseinfra': {
            'Meta': {'object_name': 'DatabaseInfra'},
            'backup_hour': ('django.db.models.fields.IntegerField', [], {}),
            'capacity': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'database_key': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'disk_offering': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'databaseinfras'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': u"orm['physical.DiskOffering']"}),
            'endpoint': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'endpoint_dns': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'engine': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'databaseinfras'", 'on_delete': 'models.PROTECT', 'to': u"orm['physical.Engine']"}),
            'engine_patch': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'databaseinfras'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': u"orm['physical.EnginePatch']"}),
            'environment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'databaseinfras'", 'on_delete': 'models.PROTECT', 'to': u"orm['physical.Environment']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_vm_created': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'maintenance_day': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'maintenance_window': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'name_prefix': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'name_stamp': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '406', 'blank': 'True'}),
            'per_database_size_mbytes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'plan': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'databaseinfras'", 'on_delete': 'models.PROTECT', 'to': u"orm['physical.Plan']"}),
            'ssl_configured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'physical.diskoffering': {
            'Meta': {'object_name': 'DiskOffering'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'size_kb': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'physical.engine': {
            'Meta': {'ordering': "(u'engine_type__name', u'version')", 'unique_together': "((u'version', u'engine_type'),)", 'object_name': 'Engine'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'engine_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'engines'", 'on_delete': 'models.PROTECT', 'to': u"orm['physical.EngineType']"}),
            'engine_upgrade_option': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'backwards_engine'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['physical.Engine']"}),
            'has_users': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'major_version': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'minor_version': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'read_node_description': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'template_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user_data_script': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'write_node_description': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'physical.enginepatch': {
            'Meta': {'object_name': 'EnginePatch'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'engine': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'patchs'", 'to': u"orm['physical.Engine']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_initial_patch': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'patch_path': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'patch_version': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'required_disk_size_gb': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'physical.enginetype': {
            'Meta': {'ordering': "(u'name',)", 'object_name': 'EngineType'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_in_memory': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'physical.environment': {
            'Meta': {'object_name': 'Environment'},
            'cloud': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'environment_cloud'", 'on_delete': 'models.PROTECT', 'to': u"orm['physical.Cloud']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'migrate_environment': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'migrate_to'", 'null': 'True', 'to': u"orm['physical.Environment']"}),
            'min_of_zones': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'physical.host': {
            'Meta': {'object_name': 'Host'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'future_host': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['physical.Host']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'hostname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255'}),
            'monitor_url': ('django.db.models.fields.URLField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'offering': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['physical.Offering']", 'null': 'True'}),
            'os_description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '406', 'null': 'True', 'blank': 'True'}),
            'root_size_gb': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'ssl_expire_at': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'physical.instance': {
            'Meta': {'unique_together': "((u'address', u'port'),)", 'object_name': 'Instance'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'databaseinfra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'instances'", 'to': u"orm['physical.DatabaseInfra']"}),
            'dns': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'future_instance': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['physical.Instance']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'hostname': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'instances'", 'to': u"orm['physical.Host']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'port': ('django.db.models.fields.IntegerField', [], {}),
            'read_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'shard': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'total_size_in_bytes': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'used_size_in_bytes': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'physical.offering': {
            'Meta': {'object_name': 'Offering'},
            'cpus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'environments': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'offerings'", 'symmetrical': 'False', 'to': u"orm['physical.Environment']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'memory_size_mb': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'physical.parameter': {
            'Meta': {'ordering': "(u'engine_type__name', u'name')", 'unique_together': "((u'name', u'engine_type'),)", 'object_name': 'Parameter'},
            'allowed_values': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'custom_method': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'dynamic': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'engine_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'enginetype'", 'on_delete': 'models.PROTECT', 'to': u"orm['physical.EngineType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'parameter_type': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'physical.plan': {
            'Meta': {'object_name': 'Plan'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'disk_offering': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'plans'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': u"orm['physical.DiskOffering']"}),
            'engine': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'plans'", 'to': u"orm['physical.Engine']"}),
            'engine_equivalent_plan': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'backwards_plan'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['physical.Plan']"}),
            'environments': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'plans'", 'symmetrical': 'False', 'to': u"orm['physical.Environment']"}),
            'has_persistence': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_ha': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'max_db_size': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'migrate_engine_equivalent_plan': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'backwards_engine_plan'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['physical.Plan']"}),
            'migrate_plan': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'migrate_to'", 'null': 'True', 'to': u"orm['physical.Plan']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'provider': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'replication_topology': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'replication_topology'", 'null': 'True', 'to': u"orm['physical.ReplicationTopology']"}),
            'stronger_offering': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'main_offerings'", 'null': 'True', 'to': u"orm['physical.Offering']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'weaker_offering': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'weaker_offerings'", 'null': 'True', 'to': u"orm['physical.Offering']"})
        },
        u'physical.replicationtopology': {
            'Meta': {'object_name': 'ReplicationTopology'},
            'can_change_parameters': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'can_clone_db': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'can_recreate_slave': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'can_reinstall_vm': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'can_resize_vm': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'can_setup_ssl': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'can_switch_master': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'can_upgrade_db': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'class_path': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'engine': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'replication_topologies'", 'symmetrical': 'False', 'to': u"orm['physical.Engine']"}),
            'has_horizontal_scalability': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'parameter': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'replication_topologies'", 'blank': 'True', 'to': u"orm['physical.Parameter']"}),
            'script': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'replication_topologies'", 'null': 'True', 'to': u"orm['physical.Script']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'physical.script': {
            'Meta': {'object_name': 'Script'},
            'configuration': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initialization': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'metric_collector': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'start_database': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'start_replication': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'physical.volume': {
            'Meta': {'object_name': 'Volume'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'volumes'", 'to': u"orm['physical.Host']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'total_size_kb': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'used_size_kb': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['maintenance']