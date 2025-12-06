from django.core.mail import EmailMessage
from django.conf import settings
from rest_framework import generics
from user_app.models import User, Anonymous, Broadcast
from user_app.api.serializers import UserSerializer, AnonymousSerializer, BroadcastSerializer
from user_app.api.permissions import IsAdminOrReadOnly
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

# ------------------------
# USER VIEWS
# ------------------------

class UsertList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # anyone can create a user

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # adjust later if needed


# ------------------------
# ANONYMOUS WISHES VIEWS
# ------------------------

class AnonymousList(generics.ListCreateAPIView):
    """
    GET: List all wishes for a specific user
    POST: Submit a new anonymous wish
    """
    serializer_class = AnonymousSerializer
    permission_classes = [AllowAny]  # anyone can post a wish

    def get_queryset(self):
        # Get all wishes for a specific celebrant
        pk = self.kwargs.get('pk')
        return Anonymous.objects.filter(celebrant=pk).order_by('-created_at')

    def perform_create(self, serializer):
        # Assign the celebrant automatically from URL
        pk = self.kwargs.get('pk')
        user = User.objects.get(pk=pk)
        serializer.save(celebrant=user)


class AnonymousDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    GET/PUT/DELETE a single wish
    """
    serializer_class = AnonymousSerializer
    permission_classes = [IsAdminOrReadOnly] # Only owner or admin can modify

    def get_queryset(self):
        celebrant_id = self.kwargs.get('pk')
        wish_id = self.kwargs.get('wish_id')
        return Anonymous.objects.filter(celebrant=celebrant_id, id=wish_id)
    
class BroadcastList(generics.ListCreateAPIView):
    queryset = Broadcast.objects.all()
    serializer_class = BroadcastSerializer
    def perform_create(self, serializer):
        broadcast = serializer.save()

        # Get all user emails
        user_emails = User.objects.values_list('email', flat=True)

        subject = "New Broadcast from Church"
        message = broadcast.Broadcast_message

        # Send email with attachment if it exists
        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=list(user_emails)
        )

        # Attach file if there is one
        if broadcast.Broadcast_media:
            email.attach_file(broadcast.Broadcast_media.path)

        email.send(fail_silently=False)
    

class BroadcastDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Broadcast.objects.all()
    serializer_class = BroadcastSerializer
    permission_classes = [AllowAny]

