# Generated by Django 3.2.11 on 2022-02-22 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0148_default_notifications'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alerts',
            name='user_id',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='dojo.dojo_user'),
        ),
        migrations.AlterField(
            model_name='answered_survey',
            name='assignee',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='assignee', to='dojo.dojo_user'),
        ),
        migrations.AlterField(
            model_name='answered_survey',
            name='responder',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='responder', to='dojo.dojo_user'),
        ),
        migrations.AlterField(
            model_name='app_analysis',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='dojo.dojo_user'),
        ),
        migrations.AlterField(
            model_name='endpoint_status',
            name='mitigated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='dojo.dojo_user'),
        ),
        migrations.AlterField(
            model_name='engagement',
            name='lead',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='dojo.dojo_user'),
        ),
        migrations.AlterField(
            model_name='fileaccesstoken',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dojo.dojo_user'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='last_reviewed_by',
            field=models.ForeignKey(editable=False, help_text='Provides the person who last reviewed the flaw.', null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='last_reviewed_by', to='dojo.dojo_user', verbose_name='Last Reviewed By'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='mitigated_by',
            field=models.ForeignKey(editable=False, help_text='Documents who has marked this flaw as fixed.', null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='mitigated_by', to='dojo.dojo_user', verbose_name='Mitigated By'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='reporter',
            field=models.ForeignKey(default=1, editable=False, help_text='Documents who reported the flaw.', on_delete=django.db.models.deletion.RESTRICT, related_name='reporter', to='dojo.dojo_user', verbose_name='Reporter'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='reviewers',
            field=models.ManyToManyField(blank=True, help_text='Documents who reviewed the flaw.', to='dojo.Dojo_User', verbose_name='Reviewers'),
        ),
        migrations.AlterField(
            model_name='global_role',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dojo.dojo_user'),
        ),
        migrations.AlterField(
            model_name='languages',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='dojo.dojo_user'),
        ),
        migrations.AlterField(
            model_name='notehistory',
            name='current_editor',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='dojo.dojo_user'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='author',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='editor_notes_set', to='dojo.dojo_user'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='editor',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_notes_set', to='dojo.dojo_user'),
        ),
        migrations.AlterField(
            model_name='stub_finding',
            name='reporter',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.RESTRICT, to='dojo.dojo_user'),
        ),
        migrations.AlterField(
            model_name='test',
            name='lead',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='dojo.dojo_user'),
        ),
        migrations.AlterField(
            model_name='usercontactinfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dojo.dojo_user'),
        ),
    ]
