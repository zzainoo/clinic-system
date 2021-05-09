from rest_framework.serializers import ModelSerializer
from .models import *



class AccountSer(ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class LibSer(ModelSerializer):
    class Meta:
        model = Libs
        fields = '__all__'


class OfferSer(ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'

class ReportsSer(ModelSerializer):
    class Meta:
        model = Reports
        fields = '__all__'

class RegisterSer(ModelSerializer):
    class Meta:
        model = Registers
        fields = '__all__'
