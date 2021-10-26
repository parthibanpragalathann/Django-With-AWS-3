from rest_framework.routers import SimpleRouter
from .views import book_box_list, book_box_detail
router = SimpleRouter()
router.register('bokox/', book_box_list)
router.register('bokox/<int:pk>/', book_box_detail)
urlpatterns = router.urls