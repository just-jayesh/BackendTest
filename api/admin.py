from django.contrib import admin
from api import models

# Register your models here.
admin.site.register([
    models.OptionList,
    models.OptionsUrl,
    models.FieldsData,
    models.CustomerDetails,
])
