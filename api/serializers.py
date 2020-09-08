from rest_framework import serializers
from api import models

class OptionsUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.OptionsUrl
        fields= '__all__'

class OptionListSerializer(serializers.ModelSerializer):
    the_json=serializers.JSONField()
    class Meta:
        model=models.OptionList
        fields='__all__'        

class FieldsDataSerializer(serializers.ModelSerializer):
    options_url = OptionsUrlSerializer(read_only=True)
    class Meta:
        model=models.FieldsData
        fields= '__all__'  

class CustomerDetailsSerializer(serializers.ModelSerializer):
    fields = FieldsDataSerializer(many=True,read_only=True)
    class Meta:
        model=models.CustomerDetails
        fields= '__all__'  
