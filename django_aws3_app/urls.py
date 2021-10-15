from rest_framework.routers import SimpleRouter
from .views import book_box_view
router = SimpleRouter()
router.register('user', book_box_view)
urlpatterns = router.urls