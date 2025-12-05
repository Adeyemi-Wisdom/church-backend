from django.urls import path
from user_app.api.views import UsertList, UserDetail, AnonymousList, AnonymousDetail, BroadcastList, BroadcastDetail

urlpatterns = [
    # ------------------------
    # User endpoints
    # ------------------------
    path('', UsertList.as_view(), name='user-list'),                 # GET all users / POST new user
    path('<int:pk>/', UserDetail.as_view(), name='user-detail'),     # GET/PUT/DELETE specific user

    # ------------------------
    # Anonymous wishes endpoints
    # ------------------------
    path('<int:pk>/wishes/', AnonymousList.as_view(), name='user-wishes'),
    path('<int:pk>/wishes/<int:wish_id>/', AnonymousDetail.as_view(), name='user-single-wish'),
    # ------------------------
    #Broadcast endpoints
    # ------------------------
    path('broadcast/', BroadcastList.as_view(), name='broadcast-messages'),
    path('broadcast/<int:pk>/', BroadcastDetail.as_view(), name='broadcast-single-message'),

    
]
