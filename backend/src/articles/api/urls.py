from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', ArticleViewSet, basename='article')
urlpatterns = router.urls
