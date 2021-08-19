
from django.db import migrations


def generate_superuser(apps, schema_editor):
    from django.contrib.auth import get_user_model
    User = get_user_model()

    superuser = User.objects.create_superuser(
        username='username',
        email='email@p.pl',
        password='testpass123',
    )

    superuser.save()


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(generate_superuser)
    ]