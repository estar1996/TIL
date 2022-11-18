from rest_framework import serializers
from .models import Community, Comment

class CommunitySerializer(serializers.ModelSerializer):
    userName = serializers.SerializerMethodField()

    # userName은 Community 모델에 없으므로 따로 정의해서 필드에 담아줌
    def get_userName(self, objects):
        return objects.user.username

    class Meta:
        model = Community
        # 모든 필드 다 보여주기
        fields = '__all__' 
        read_only_fields = ('user','like')
       
class CommentSerializer(serializers.ModelSerializer):
    userName = serializers.SerializerMethodField()

    def get_userName(self, objects):
        return objects.user.username

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'community',)
