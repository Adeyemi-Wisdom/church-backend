from rest_framework import serializers
from user_app.models import User, Anonymous
from phonenumber_field.serializerfields import PhoneNumberField

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    DOB = serializers.DateField(
        format="%d-%m-%Y",
        input_formats=['%Y-%m-%d', '%m-%d-%Y', '%d-%m-%Y'],
        required=True
    )
    mobile_number = PhoneNumberField()

    class Meta:
        model = User
        # Expose only necessary fields for now
        fields = "__all__"

class AnonymousSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)  # shows when wish was submitted
    celebrant = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True  # hide in response
    )

    class Meta:
        model = Anonymous
        fields = ["id", "celebrant", "message", "created_at"]
