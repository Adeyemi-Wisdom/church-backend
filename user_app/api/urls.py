from django.urls import path
from user_app.api.views import UsertList, UserDetail, AnonymousList, AnonymousDetail

urlpatterns = [
    # ------------------------
    # User endpoints
    # ------------------------
    path('users/', UsertList.as_view(), name='user-list'),                  # GET all users / POST new user
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),      # GET/PUT/DELETE specific user

    # ------------------------
    # Anonymous wishes endpoints
    # ------------------------
    path('users/<int:pk>/wishes/', AnonymousList.as_view(), name='user-wishes'),          # GET all wishes / POST new wish
    path('users/<int:pk>/wishes/<int:wish_id>/', AnonymousDetail.as_view(), name='user-single-wish'),  # GET/PUT/DELETE single wish
]
