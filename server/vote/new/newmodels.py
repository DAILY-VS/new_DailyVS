from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from accounts.models import User

#투표 게시글 DB
class Poll(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    title = models.TextField()
    content = models.TextField()
    poll_like = models.ManyToManyField(
        'accounts.User', 
        related_name='poll_like',
        through='PollLike'
        )
    views_count = models.PositiveIntegerField(default=0)  # 조회 수
    thumbnail = models.ImageField()
    comments_count = models.PositiveIntegerField(default=0)  # 댓글 수
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def increase_views(self): # 조회수
        self.views_count=self.views_count+1
        self.save()

    def __str__(self):
        return self.title

#투표 선택지 DB
class Choice(models.Model) :
    id = models.AutoField(primary_key=True, null=False, blank=False)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    image = models.ImageField() 
    
    def __str__(self):
        return self.choice_text
    
#회원투표 DB
class UserVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_votes')
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

#비회원투표
class NonUserVote(models.Model):
    MBTI = models.TextField(null= True)
    GENDERS = (
        ('M', '남성'),
        ('W', '여성'),
    )
    gender = models.CharField(verbose_name='성별', max_length=1, choices=GENDERS, null= True)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

#댓글 DB
class Comment(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    user_info = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=200)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True) #대댓글
    likes_count = models.PositiveIntegerField(default=0) #좋아요 수
    comment_like = models.ManyToManyField(
        'accounts.User', 
        related_name='comment_like',
        through='CommentLike'
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

#게시글 좋아요 기능 중개 테이블
class PollLike(models.Model):
    poll_id = models.ForeignKey(Poll, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DataTimeField(auto_now_add=True)

#댓글 좋아요 
class CommentLike(models.Model):
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DataTimeField(auto_now_add=True)# 언제 좋아요 눌렀는지

class Poll_Result(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    total= models.PositiveIntegerField(default=0)
    choice1_man=models.PositiveIntegerField(default=0)
    choice2_man=models.PositiveIntegerField(default=0)
    choice1_woman=models.PositiveIntegerField(default=0)
    choice2_woman=models.PositiveIntegerField(default=0)
    choice1_E=models.PositiveIntegerField(default=0)
    choice2_E=models.PositiveIntegerField(default=0)
    choice1_I=models.PositiveIntegerField(default=0)
    choice2_I=models.PositiveIntegerField(default=0)
    choice1_N=models.PositiveIntegerField(default=0)
    choice2_N=models.PositiveIntegerField(default=0)
    choice1_S=models.PositiveIntegerField(default=0)
    choice2_S=models.PositiveIntegerField(default=0)
    choice1_T=models.PositiveIntegerField(default=0)
    choice2_T=models.PositiveIntegerField(default=0)
    choice1_F=models.PositiveIntegerField(default=0)
    choice2_F=models.PositiveIntegerField(default=0)
    choice1_J=models.PositiveIntegerField(default=0)
    choice2_J=models.PositiveIntegerField(default=0)
    choice1_P=models.PositiveIntegerField(default=0)
    choice2_P=models.PositiveIntegerField(default=0)