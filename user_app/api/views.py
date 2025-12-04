from user_app.models import User, Anonymous
from user_app.api.serializers import UserSerializer, AnonymousSerializer
from rest_framework import generics
from user_app.api.permissions import ReviewUserOrReadOnly


class UsertList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class AnonymousList(generics.ListAPIView):
    serializer_class = AnonymousSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Anonymous.objects.filter(celebrant=pk)

class AnonymousDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnonymousSerializer
    permission_classes = [ReviewUserOrReadOnly]

    def get_queryset(self):
        celebrant_id = self.kwargs.get('pk')   # user id
        wish_id = self.kwargs.get('wish_id')   # wish id
        return Anonymous.objects.filter(celebrant=celebrant_id, id=wish_id)



    