from rest_framework import serializers
from user_app.models import User, Anonymous
from phonenumber_field.serializerfields import PhoneNumberField
class UserSerializer(serializers.ModelSerializer):
    
    
    DOB = serializers.DateField(
        format="%d-%m-%Y",
         input_formats=['%Y-%m-%d', '%m-%d-%Y', '%d-%m-%Y'],
        required=True
    )

    mobile_number = PhoneNumberField()
    class Meta:
        model = User
        fields = "__all__"
        
class AnonymousSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anonymous
        fields = "__all__"
