from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.viewsets import ModelViewSet
from app.models import *
from app.serializer import *
from allauth.socialaccount.models import SocialAccount
from django.conf import settings
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google import views as google_view
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.http import JsonResponse
import requests
from rest_framework import status
from json.decoder import JSONDecodeError
from django.db import models
from django.db.models import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view


# Create your views here.
class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class GoodMorningViewSet(ModelViewSet):
    queryset = GoodMorning.objects.all()
    serializer_class = GoodMorningSerializer

    def perform_update(self, serializer):
        instance = serializer.save()

        # Get morning blocks
        morning_blocks = MorningBlock.objects.filter(name__in=['weather', 'todo', 'music', 'pathfind'])

        # Update the turn values in GoodMorning instance
        for morning_block in morning_blocks:
            if morning_block.name == 'weather':
                instance.weather_turn = morning_block.turn
            elif morning_block.name == 'todo':
                instance.todo_turn = morning_block.turn
            elif morning_block.name == 'music':
                instance.music_turn = morning_block.turn
            elif morning_block.name == 'pathfind':
                instance.pathfind_turn = morning_block.turn

        instance.save()

    def list(self, request):
        # Retrieve the first instance from the queryset
        good_morning = self.get_queryset().first()

        # Get the values from the MorningBlock instances
        morning_blocks = MorningBlock.objects.filter(name__in=['weather', 'todo', 'music', 'pathfind'])

        values = {}
        for morning_block in morning_blocks:
            values[morning_block.name + "_turn"] = morning_block.turn

        # Update the values in GoodMorning instance
        good_morning.weather_turn = values.get("weather_turn", 1)
        good_morning.todo_turn = values.get("todo_turn", 1)
        good_morning.music_turn = values.get("music_turn", 1)
        good_morning.pathfind_turn = values.get("pathfind_turn", 1)
        good_morning.save()

        # Serialize the values
        serializer = self.get_serializer(good_morning)

        # Return the serialized data as the API response
        return Response(serializer.data)


# class MorningMusicNameViewSet(ModelViewSet):
#     queryset = MorningMusicList.objects.all()
#     serializer_class = MorningMusicNameSerializer
    # @action(detail=False, methods=['get'])
    # def get_music_name(self, request):
    #     serializer = self.get_serializer(self.queryset, many=True)
    #     serialized_data = serializer.data
    #     serialized_data_list = [data['name'] for data in serialized_data]
    #     return Response(serialized_data_list)


class MorningMusicListViewSet(ModelViewSet):
    queryset = MorningMusicList.objects.all()
    serializer_class = MorningMusicListSerializer

    @action(detail=False, methods=['get'])
    def get_mormusic_name(self, request):
        queryset = MorningMusicList.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        serialized_data = serializer.data
        serialized_data_list = [data['name'] for data in serialized_data]
        # print(serialized_data_list)
        return Response(serialized_data_list)


# class MorningDestNameViewSet(ModelViewSet):
#     queryset = MorningDestList.objects.all()
#     serializer_class = MorningDestNameSerializer
    # @action(detail=False, methods=['get'])
    # def get_dest_name(self, request):
    #     serializer = self.get_serializer(self.queryset, many=True)
    #     serialized_data = serializer.data
    #     serialized_data_list = [data['name'] for data in serialized_data]
    #     return Response(serialized_data_list)


class MorningDestListViewSet(ModelViewSet):
    queryset = MorningDestList.objects.all()
    serializer_class = MorningDestListSerializer

    @action(detail=False, methods=['get'])
    def get_music_name(self, request):
        queryset = MorningDestList.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        serialized_data = serializer.data
        serialized_data_list = [data['name'] for data in serialized_data]
        return Response(serialized_data_list)


class GoodAfternoonViewSet(ModelViewSet):
    queryset = GoodAfternoon.objects.all()
    serializer_class = GoodAfternoonSerializer

    def perform_update(self, serializer):
        instance = serializer.save()

        # Get morning blocks
        afternoon_blocks = AfternoonBlock.objects.filter(name__in=['todo', 'study', 'nap', 'sleep'])

        # Update the turn values in GoodMorning instance
        for afternoon_block in afternoon_blocks:
            if afternoon_block.name == 'todo':
                instance.todo_turn = afternoon_block.turn
            elif afternoon_block.name == 'study':
                instance.study_turn = afternoon_block.turn
            elif afternoon_block.name == 'nap':
                instance.nap_turn = afternoon_block.turn
            elif afternoon_block.name == 'sleep':
                instance.sleep_time = afternoon_block.time

        instance.save()

    def list(self, request):
        # Retrieve the first instance from the queryset
        good_afternoon = self.get_queryset().first()

        # Get the values from the MorningBlock instances
        afternoon_blocks = AfternoonBlock.objects.filter(name__in=['todo', 'study', 'nap', 'sleep'])

        values = {}
        for afternoon_block in afternoon_blocks:
            values[afternoon_block.name + "_turn"] = afternoon_block.turn

        # Update the values in GoodMorning instance
        good_afternoon.todo_turn = values.get("todo_turn", 1)
        good_afternoon.study_turn = values.get("study_turn", 1)
        good_afternoon.nap_turn = values.get("nap_turn", 1)
        good_afternoon.sleep_turn = values.get("sleep_turn", 1)
        good_afternoon.save()

        # Serialize the values
        serializer = self.get_serializer(good_afternoon)

        # Return the serialized data as the API response
        return Response(serializer.data)


# class AfternoonNapMusicNameViewSet(ModelViewSet):
#     queryset = AfternoonNapMusicList.objects.all()
#     serializer_class = AfternoonNapMusicNameSerializer
    # @action(detail=False, methods=['get'])
    # def get_napmusic_name(self, request):
    #     serializer = self.get_serializer(self.queryset, many=True)
    #     serialized_data = serializer.data
    #     serialized_data_list = [data['name'] for data in serialized_data]
    #     return Response(serialized_data_list)


class AfternoonNapMusicListViewSet(ModelViewSet):
    queryset = AfternoonNapMusicList.objects.all()
    serializer_class = AfternoonNapMusicListSerializer

    @action(detail=False, methods=['get'])
    def get_music_name(self, request):
        queryset = AfternoonNapMusicList.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        serialized_data = serializer.data
        serialized_data_list = [data['name'] for data in serialized_data]
        return Response(serialized_data_list)


# class AfternoonStudyMusicNameViewSet(ModelViewSet):
#     queryset = AfternoonStudyMusicList.objects.all()
#     serializer_class = AfternoonStudyMusicNameSerializer
    # @action(detail=False, methods=['get'])
    # def get_studymusic_name(self, request):
    #     serializer = self.get_serializer(self.queryset, many=True)
    #     serialized_data = serializer.data
    #     serialized_data_list = [data['name'] for data in serialized_data]
    #     return Response(serialized_data_list)


class AfternoonStudyMusicListViewSet(ModelViewSet):
    queryset = AfternoonStudyMusicList.objects.all()
    serializer_class = AfternoonStudyMusicListSerializer

    @action(detail=False, methods=['get'])
    def get_music_name(self, request):
        queryset = AfternoonStudyMusicList.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        serialized_data = serializer.data
        serialized_data_list = [data['name'] for data in serialized_data]
        return Response(serialized_data_list)


class GoodEveningViewSet(ModelViewSet):
    queryset = GoodEvening.objects.all()
    serializer_class = GoodEveningSerializer

    def perform_update(self, serializer):
        instance = serializer.save()

        # Get morning blocks
        evening_blocks = EveningBlock.objects.filter(name__in=['today_feedback', 'tomorrow_brief', 'health'])

        # Update the turn values in GoodMorning instance
        for evening_block in evening_blocks:
            if evening_block.name == 'today_feedback':
                instance.today_feedback_turn = evening_block.turn
            elif evening_block.name == 'tomorrow_brief':
                instance.tomorrow_brief_turn = evening_block.turn
            elif evening_block.name == 'health':
                instance.health_turn = evening_block.turn

        instance.save()

    def list(self, request):
        # Retrieve the first instance from the queryset
        good_evening = self.get_queryset().first()

        # Get the values from the MorningBlock instances
        evening_blocks = EveningBlock.objects.filter(name__in=['today_feedback', 'tomorrow_brief', 'health'])

        values = {}
        for evening_block in evening_blocks:
            values[evening_block.name + "_turn"] = evening_block.turn

        # Update the values in GoodMorning instance
        good_evening.today_feedback_turn = values.get("today_feedback_turn", 1)
        good_evening.tomorrow_brief_turn = values.get("tomorrow_brief_turn", 1)
        good_evening.health_turn = values.get("health_turn", 1)
        good_evening.save()

        # Serialize the values
        serializer = self.get_serializer(good_evening)

        # Return the serialized data as the API response
        return Response(serializer.data)


class EveningDiaryViewSet(ModelViewSet):
    queryset = EveningDiary.objects.all()
    serializer_class = EveningDiarySerializer


# class EveningSleepMusicNameViewSet(ModelViewSet):
#     queryset = EveningSleepMusicList.objects.all()
#     serializer_class = EveningSleepMusicNameSerializer
#     @action(detail=False, methods=['get'])
#     def get_sleepmusic_name(self, request):
#         serializer = self.get_serializer(self.queryset, many=True)
#         serialized_data = serializer.data
#         serialized_data_list = [data['name'] for data in serialized_data]
#         return Response(serialized_data_list)


class EveningSleepMusicListViewSet(ModelViewSet):
    queryset = EveningSleepMusicList.objects.all()
    serializer_class = EveningSleepMusicListSerializer

    @action(detail=False, methods=['get'])
    def get_sleepmusic_name(self, request):
        queryset = EveningSleepMusicList.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        serialized_data = serializer.data
        serialized_data_list = [data['name'] for data in serialized_data]
        return Response(serialized_data_list)


class MorningBlockViewSet(ModelViewSet):
    queryset = MorningBlock.objects.all()
    serializer_class = MorningBlockSerializer


class AfternoonBlockViewSet(ModelViewSet):
    queryset = AfternoonBlock.objects.all()
    serializer_class = AfternoonBlockSerializer


class EveningBlockViewSet(ModelViewSet):
    queryset = EveningBlock.objects.all()
    serializer_class = EveningBlockSerializer


def base(request):
    context = {}
    return render(request, 'app/base.html', context)


def start(request):
    context = {}
    return render(request, 'app/start.html', context)


def login(request):
    context = {}
    return render(request, 'app/login.html', context)


def main(request):
    context = {}
    return render(request, 'app/main.html', context)


state = getattr(settings, 'STATE')
BASE_URL = 'http://ec2-13-124-90-246.ap-northeast-2.compute.amazonaws.com:8080'
GOOGLE_CALLBACK_URI = BASE_URL + 'app/google/callback/'


class GoogleLogin(SocialLoginView):
    adapter_class = google_view.GoogleOAuth2Adapter
    callback_url = GOOGLE_CALLBACK_URI
    client_class = OAuth2Client


def google_login(request):
    # google_login 실행 후 로그인 성공 시, Callback 함수로 Code 값 전달받음
    scope = "https://www.googleapis.com/auth/userinfo.email"
    client_id = getattr(settings, "SOCIAL_AUTH_GOOGLE_CLIENT_ID")
    return redirect(f"https://accounts.google.com/o/oauth2/v2/auth?client_id={client_id}&response_type=code&redirect_uri={GOOGLE_CALLBACK_URI}&scope={scope}")


def google_callback(request):
    client_id = getattr(settings, "SOCIAL_AUTH_GOOGLE_CLIENT_ID")
    client_secret = getattr(settings, "SOCIAL_AUTH_GOOGLE_SECRET")
    code = request.GET.get('code')

    # 1. 받은 Code로 Google에 Access Token 요청
    token_req = requests.post(f"https://oauth2.googleapis.com/token?client_id={client_id}&client_secret={client_secret}&code={code}&grant_type=authorization_code&redirect_uri={GOOGLE_CALLBACK_URI}&state={state}")

    # json으로 변환 후 에러 부분 파싱
    token_req_json = token_req.json()
    error = token_req_json.get("error")

    # 에러 발생 시 종료
    if error is not None:
        raise JSONDecodeError(error)

    # 성공 시 access_token 가져오기
    access_token = token_req_json.get('access_token')

    # 2. Access Token으로 Email 값을 Google에게 요청
    email_req = requests.get(f"https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={access_token}")
    email_req_status = email_req.status_code

    # 에러 발생 시 400 에러 반환
    if email_req_status != 200:
        return JsonResponse({'err_msg': 'failed to get email'}, status=status.HTTP_400_BAD_REQUEST)

    # 성공 시 이메일 가져오기
    email_req_json = email_req.json()
    email = email_req_json.get('email')
    # return JsonResponse({'access': access_token, 'email':email})

    # 3. 전달받은 Email, Access Token, Code를 바탕으로 회원가입/로그인 진행
    try:
        # 전달받은 이메일로 등록된 유저가 있는지 탐색
        user = Account.objects.get(email=email)

        # FK로 연결되어있는 socialaccount 테이블에서 해당 이메일의 유저가 있는지 확인
        social_user = SocialAccount.objects.get(user=user)
        if social_user is None:
            return JsonResponse({'err_msg': 'email exists but not social user'}, status=status.HTTP_400_BAD_REQUEST)

        # 있는데 구글 계정이 아니어도 에러
        if social_user.provider != 'google':
            return JsonResponse({'err_msg': 'no matching social type'}, status=status.HTTP_400_BAD_REQUEST)

        # 이미 Google로 제대로 가입된 유저 -> 로그인 & 해당 유저의 jwt 발급
        data = {'access_token': access_token, 'code': code}
        accept = requests.post(f"{BASE_URL}app/google/login/finish/", data=data)
        accept_status = accept.status_code

        # 뭔가 중간에 문제가 생기면 에러
        if accept_status != 200:
            return JsonResponse({'err_msg': 'failed to signin'}, status=accept_status)
        accept_json = accept.json()
        accept_json.pop('user', None)
        return JsonResponse(accept_json)

    except Account.DoesNotExist:
        # 전달받은 이메일로 기존에 가입된 유저가 아예 없으면 => 새로 회원가입 & 해당 유저의 jwt 발급
        data = {'access_token': access_token, 'code': code}
        accept = requests.post(f"{BASE_URL}app/google/login/finish/", data=data)
        accept_status = accept.status_code

        # 뭔가 중간에 문제가 생기면 에러
        if accept_status != 200:
            return JsonResponse({'err_msg': 'failed to signup'}, status=accept_status)
        accept_json = accept.json()
        accept_json.pop('user', None)
        return JsonResponse(accept_json)

    except SocialAccount.DoesNotExist:
        # User는 있는데 SocialAccount가 없을 때 (=일반회원으로 가입된 이메일일때)
        return JsonResponse({'err_msg': 'email exists but not social user'}, status=status.HTTP_400_BAD_REQUEST)
