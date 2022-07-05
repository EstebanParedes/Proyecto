from rest_framework import routers
from .views import customers_viewset

router=routers.DefaultRouter()
router.register('customers',customers_viewset)