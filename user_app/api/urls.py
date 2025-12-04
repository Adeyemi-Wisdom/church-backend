from django.urls import path
from user_app.api.views import UsertList, UserDetail, AnonymousList, AnonymousDetail

urlpatterns = [
    path('list/', UsertList.as_view(), name='user-list'),
    path('list/<int:pk>', UserDetail.as_view(), name='user-Detail'),
    path('list/<int:pk>/wishes', AnonymousList.as_view(), name='user-comment'),
    path('list/<int:pk>/wishes/<int:wish_id>/', AnonymousDetail.as_view(), name='single-wish'),

    

]
