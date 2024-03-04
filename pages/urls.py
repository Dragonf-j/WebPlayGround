from django.urls import path
from .views import PagesLestview, PageDetailView, PageCreateView

pages_patterns = ([
    path('', PagesLestview.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
    path('create/', PageCreateView.as_view(), name='create'),
    ], 'pages')