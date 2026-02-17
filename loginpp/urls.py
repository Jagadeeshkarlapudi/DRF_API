from rest_framework.routers import DefaultRouter
from .views import EnquiryViewSet
from django.urls import path
from .views import create_admin_once


# from .views import OnlineEnquiryAPIView
from .views import OnlineEnquiryViewSet,ContactEnquiryViewSet,admin_logout,AdmissionViewSet


router = DefaultRouter()
router.register("enquiries", EnquiryViewSet, basename="enquiries")
router.register("online-enquiry", OnlineEnquiryViewSet, basename="online-enquiry")
router.register("contact-enquiry", ContactEnquiryViewSet, basename="contact-enquiry")
router.register("admissions", AdmissionViewSet, basename="admissions")

urlpatterns = [
    path("admin-logout/",admin_logout),
    path("create-admin/", create_admin_once)

]

# router.register(r"onlineenquiries",OnlineEnquiryAPIView, basename="onlineenquiries")
# path("online-enquiry/", ContactEnquiryAPIView.as_view(), name="contact-enquiry"),

urlpatterns = router.urls
