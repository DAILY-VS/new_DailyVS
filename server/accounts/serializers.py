from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer


class CustomRegisterSerializer(RegisterSerializer):
    GENDERS = (
        ("M", "남성(Man)"),
        ("W", "여성(Woman)"),
    )
    MBTI_set = (
        ("INFP", "INFP"),
        ("ENFP", "ENFP"),
        ("INFJ", "INFJ"),
        ("ENFJ", "ENFJ"),
        ("INTJ", "INTJ"),
        ("ENTJ", "ENTJ"),
        ("INTP", "INTP"),
        ("ENTP", "ENTP"),
        ("ISFP", "ISFP"),
        ("ESFP", "ESFP"),
        ("ISFJ", "ISFJ"),
        ("ESFJ", "ESFJ"),
        ("ISTP", "ISTP"),
        ("ESTP", "ESTP"),
        ("ISTJ", "ISTJ"),
        ("ESTJ", "ESTJ"),
    )
    nickname = serializers.CharField(max_length=10)
    gender = serializers.ChoiceField(GENDERS)
    mbti = serializers.ChoiceField(MBTI_set)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['nickname'] = self.validated_data.get('nickname', '')
        data['gender'] = self.validated_data.get('gender', '')
        data['mbti'] = self.validated_data.get('mbti', '')

        return data


class CustomLoginSerializer(LoginSerializer):
    email = serializers.CharField(required=True, allow_blank=False)
    password = serializers.CharField(style={'input_type': 'password'})