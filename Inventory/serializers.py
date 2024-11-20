from rest_framework import serializers
from .models import *


   
class products_serializers(serializers.ModelSerializer):

    class Meta:

        model = Products
        fields = '__all__'


class products_serializers2(serializers.ModelSerializer):

    class Meta:

        model = Products
        fields = ['product_name']
   
    

class Category_serializer(serializers.ModelSerializer):

    class Meta:

       model = category
       fields = '__all__'