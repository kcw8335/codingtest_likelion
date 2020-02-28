from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCount, HitCountMixin

# 계정 테이블 - 사용안함
class Account(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=30)
    email = models.EmailField(unique=True, null=False)

    def __str__(self):
        return self.id

# 과목 영역 테이블
class Subject_range(models.Model):
    # 영역(PK)
    subject_range = models.CharField(primary_key=True, max_length=50)
    
    def __str__(self):
        return self.subject_range

# 과목 정보 테이블 - 사용안함
class Subject_code(models.Model):
    # 과목 코드(PK)
    subject_code = models.CharField(max_length=20, primary_key=True)
    # 과목명
    subject_name = models.CharField(max_length=20)

    def __str__(self):
        return self.subject_code + '    ' + self.subject_name

# 과목 & 강사 테이블
class Subject(models.Model):
    # PK를 따로 설정하지 않았습니다.
    # PK는 장고에서 인덱스 형식으로 자동 생성해줍니다. ex) 1,2,3,4,5... 
    # PK는 id라는 컬럼명으로 저장되어 있습니다.

    # 영역 (FK) - 과목 영역 테이블에서 가져옴
    subject_range = models.ForeignKey(Subject_range, on_delete = models.CASCADE, null=True)
    
    # # 과목 코드 (FK) - 과목 정보 테이블에서 가져옴
    # subject_code = models.ForeignKey(Subject_code, on_delete=models.CASCADE)

    # 과목명
    subject_name = models.CharField(max_length=50, null=True)

    # 강사명
    professor = models.CharField(max_length=50)
    # 추천
    recommendation = models.IntegerField(default=0)
    # 비추천
    nonrecommendation = models.IntegerField(default=0)
    
    # 과제 - 많음 보통 없음 과제베스트
    homework_large = models.IntegerField(default=0)
    homework_medium = models.IntegerField(default=0)
    homework_small = models.IntegerField(default=0)
    homework_best = models.CharField(max_length=20, null=True)

    # 팀플 - 있음 없음 팀플베스트
    team_yes = models.IntegerField(default=0)
    team_no = models.IntegerField(default=0)
    team_best = models.CharField(max_length=20, null=True)

    # 학점비율 - 잘줌 깐깐함 F주의 학점비율베스트
    grade_good = models.IntegerField(default=0)
    grade_bad = models.IntegerField(default=0)
    grade_f = models.IntegerField(default=0)
    grade_best = models.CharField(max_length=20, null=True)

    # 출결 - 호명 전자출결 안함 출결베스트
    attendance_speak = models.IntegerField(default=0)
    attendance_elec = models.IntegerField(default=0)
    attendance_none = models.IntegerField(default=0)
    attendance_best = models.CharField(max_length=20, null=True)

    # 시험횟수 - 3번이상 두번 한번 없음 시험횟수베스트
    test_3 = models.IntegerField(default=0)
    test_2 = models.IntegerField(default=0)
    test_1 = models.IntegerField(default=0)
    test_0 = models.IntegerField(default=0)
    test_best = models.CharField(max_length=20, null=True)

    def __str__(self):
        return str(self.id) + ' ' + str(self.subject_range) + ' ' + str(self.subject_name) + ' ' + str(self.professor)

# 강의 평가 테이블
class Evaluation(models.Model):
    # PK를 따로 설정하지 않았습니다.
    # PK는 장고에서 인덱스 형식으로 자동 생성해줍니다. ex) 1,2,3,4,5... 
    # PK는 id라는 컬럼명으로 저장되어 있습니다.
    
    # 강의평가 작성자 ID
    writer_id = models.CharField(max_length=20)
    # 평가내용
    evaluation_text = models.TextField(max_length=2000)
    # 작성날짜
    pub_date = models.DateTimeField('date published')
    # 과목 테이블에서 어떤 강사와 어떤 과목을 선택했는지 알려주는 컬럼
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ' ' + self.writer_id


#글 관련 항목
class Write_index(models.Model):
    homework = models.CharField(max_length=20)
    team = models.CharField(max_length=20)
    grade = models.CharField(max_length=20)
    attendance = models.CharField(max_length=20)
    test = models.CharField(max_length=20)
    hit_count_generic = GenericRelation( HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')

    def __str__(self):
        return self.text
