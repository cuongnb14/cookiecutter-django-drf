from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r'products', views.ProductViewSet, basename='product')
urlpatterns = router.urls
