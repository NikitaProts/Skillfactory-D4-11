from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(default='AST', on_delete=django.db.models.deletion.CASCADE, to='p_library.Publisher', to_field='name'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.TextField(unique=True),
        ),
    ]
