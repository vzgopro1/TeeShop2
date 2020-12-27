from rest_framework import serializers
from . models import *

class UserSerializers(serializers.Serializer):

    class Meta:
        model = User
        fields = ('__all__')

class StoreSerializers(serializers.Serializer):

    class Meta:
        model = Store
        fields = ('__all__')

class ProductSerializers(serializers.Serializer):

    class Meta:
        model = Product
        fields = ('__all__')

class PostSerializers(serializers.Serializer):

    class Meta:
        model = Post
        fields = ('__all__')

