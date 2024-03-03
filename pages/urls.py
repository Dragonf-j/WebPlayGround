from django.urls import path
from .views import PagesLestview, PageDetailView

urlpatterns = [
    path('', PagesLestview.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
]