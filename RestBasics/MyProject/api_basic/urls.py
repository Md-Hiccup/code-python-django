from django.urls import path, include
from .views import article_list, article_detail, ArticleAPIView, ArticleDetails, GenericAPIView, GenericDetailAPIView, ArticleViewSet, GenericViewSet, ModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
#viewset
#router.register('article', ArticleViewSet, basename='article')

# generice viewset
# router.register('article', GenericViewSet, basename='article')

# model viewset
router.register('article', ModelViewSet, basename='article')

urlpatterns = [
    # function based view
    path('article/', article_list),   # for api_view()
    path('detail/<int:pk>/', article_detail),

    # class based view
    path('class/article/', ArticleAPIView.as_view()),
    path('class/detail/<int:id>/', ArticleDetails.as_view()),

    # generic based view
    path('generic/article/', GenericAPIView.as_view()),
    path('generic/article/<int:id>/', GenericDetailAPIView.as_view()),

    # viewsets
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>', include(router.urls)),
]
