from rest_framework.routers import DefaultRouter
from .views import EnquiryViewSet
# from .views import OnlineEnquiryAPIView
from .views import OnlineEnquiryViewSet

router = DefaultRouter()
router.register(r"enquiries", EnquiryViewSet, basename="enquiries")
router.register("online-enquiry", OnlineEnquiryViewSet, basename="online-enquiry")
# router.register(r"onlineenquiries",OnlineEnquiryAPIView, basename="onlineenquiries")
# path("online-enquiry/", ContactEnquiryAPIView.as_view(), name="contact-enquiry"),

urlpatterns = router.urls
