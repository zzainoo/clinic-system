from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView
from rest_framework.views import APIView,Response
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from django.db.models import Q
from .serializers import *
from .models import *
from sms import send_sms



class OfferView(ListAPIView):
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]
    serializer_class = OfferSer
    queryset = Offer.objects.all().order_by('-id')


class ReportView(ListAPIView):
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]
    serializer_class = ReportsSer
    def get_queryset(self):
        return Reports.objects.filter(Q(user_id=self.request.GET.get('id')) | Q(lib_id=self.request.GET.get('libid'))).all().order_by('-id')

class RegisterView(CreateAPIView):
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]
    serializer_class = RegisterSer

class LoginView(APIView):
    permission_classes =  [AllowAny]
    authentication_classes = [TokenAuthentication]
    def post(self,request,format=None):
        phone = request.POST['phone'][-10:]
        type = request.POST['type']
        if type == 'user':
            if Users.objects.filter(phone=phone).exists():
                user = Users.objects.get(phone=phone)
                user.save()
                code = user.code
                phone2 = "+964" + phone
                sms = send_sms(
                    f'كود التحقق الخاص بك من مختبر وقت بغداد هو : {user.code}',
                    '+12523512473',
                    [phone2, ]

                )
                return Response({'code':code,'sms':sms})
            else:
                user = Users(phone=phone, name='ضيف', address='غير محدد')
                user.save()
                code = user.code
                phone2 = "+964" + phone
                sms = send_sms(
                    f'كود التحقق الخاص بك من مختبر وقت بغداد هو : {user.code}',
                    '+12523512473',
                    [phone2, ]

                )
                return Response({'code': code, 'sms': sms})
        elif type == 'lib':
            if Libs.objects.filter(phone=phone).exists():
                user = Libs.objects.get(phone=phone)
                user.save()
                code = user.code
                phone2 = "+964" + phone
                sms = send_sms(
                    f'كود التحقق الخاص بك من مختبر وقت بغداد هو : {user.code}',
                    '+12523512473',
                    [phone2, ]

                )
                return Response({'code':code,'sms':sms})
            else:
                user = Libs(phone=phone,  name='ضيف', address='غير محدد')
                user.save()
                code = user.code
                phone2 = "+964" + phone
                sms = send_sms(
                    f'كود التحقق الخاص بك من مختبر وقت بغداد هو : {user.code}',
                    '+12523512473',
                    [phone2, ]

                )
                return Response({'code': code, 'sms': sms})

class AccountView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]
    def post(self,request,format=None):
        phone = request.POST['phone']
        type = request.POST['type']
        info = None
        reports = None

        infose = None
        reportsse = None

        if type == 'user':
            info  = Users.objects.get(phone=phone)
            reports = Reports.objects.filter(user__phone=phone)
            infose = AccountSer(info)
        elif type == 'lib':
            info = Libs.objects.get(phone=phone)
            reports = Reports.objects.filter(lib__phone=phone)
            infose = LibSer(info)

        reportsse = ReportsSer(reports,many=True)

        data = {
            'info':infose.data,
            'report':reportsse.data
        }


        return Response({'data':data})

class UserupdateView(UpdateAPIView):
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]
    serializer_class  = AccountSer
    queryset = Users.objects.all()

class LibupdateView(UpdateAPIView):
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]
    serializer_class = LibSer
    queryset = Libs.objects.all()

class Libdet(RetrieveAPIView):
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]
    serializer_class = LibSer
    queryset = Libs.objects.all()












