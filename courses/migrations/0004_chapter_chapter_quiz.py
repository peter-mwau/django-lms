# Generated by Django 4.2.3 on 2023-08-28 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("assignments", "0008_alter_assignment_id_alter_choice_id_and_more"),
        (
            "courses",
            "0003_alter_chapter_id_alter_course_id_alter_enrollment_id_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="chapter",
            name="chapter_quiz",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="quiz",
                to="assignments.quiz",
            ),
        ),
    ]
