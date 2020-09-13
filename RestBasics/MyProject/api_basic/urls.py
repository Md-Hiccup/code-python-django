from django.urls import path
from .views import article_list, article_detail, ArticleAPIView, ArticleDetails, GenericAPIView, GenericDetailAPIView

urlpatterns = [
    # function based view
    path('article/', article_list),   # for api_view()
    path('detail/<int:pk>/', article_detail),

    # class based view
    path('class/article/', ArticleAPIView.as_view(), name='article'),
    path('class/detail/<int:id>/', ArticleDetails.as_view(), name='detail'),

    # generic based view
    path('generic/article/', GenericAPIView.as_view(), name='generic'),
    path('generic/article/<int:id>/', GenericDetailAPIView.as_view(), name='generic'),
]
