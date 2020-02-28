from django.urls import path
from .views import BoardDetail, BoardIndex, BoardSearchlist
from . import views
import write.views

app_name = "write"
urlpatterns = [

    path("detail/",BoardDetail.as_view(), name='detail'),
    path("create/",write.views.create, name='create'),
    path('index/',BoardIndex.as_view(), name='index'),
    path('searchlist/',write.views.searchlist, name='searchlist')
]
