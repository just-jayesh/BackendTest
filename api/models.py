from djongo import models
import jsonfield

class OptionsUrl(models.Model):
    url=models.CharField(max_length=200)
    request_type=models.CharField(max_length=200)

    

class OptionList(models.Model):
    the_json=jsonfield.JSONField()      

class FieldsData(models.Model):
    field = models.CharField(max_length=200)
    label = models.CharField(max_length=200)
    data_type = models.CharField(max_length=200)
    default = models.CharField(max_length=200)
    field_type = models.CharField(max_length=200)
    field_type_label = models.CharField(max_length=200)
    is_removable = models.BooleanField(default=False)
    mandatory = models.BooleanField(default=False)
    options_list = models.ManyToManyField('OptionList',blank=True)
    options_url = models.ManyToManyField('OptionsUrl',blank=True)

class CustomerDetails(models.Model):
    types = models.CharField(max_length=200)
    entity = models.CharField(max_length=200)
    customerId = models.IntegerField(default=0)
    law = models.CharField(max_length=200)
    fields = models.ManyToManyField('FieldsData')

