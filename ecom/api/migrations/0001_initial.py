from django.db import migrations
from api.user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(apps,schema_editor):
        user=  CustomUser(name="ankit",
        email="ankit.sridhar16@gmail.com",
        is_staff=True,
        is_superuser=True,
        phone="9876543221",
        gender="Male")
        user.set_password("ankit123")
        user.save()
    dependencies = []
    operations = [
        migrations.RunPython(seed_data), 
    ]