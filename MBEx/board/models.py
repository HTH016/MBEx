from django.db import models

class Board( models.Model ) :           # board_board
    num = models.AutoField( primary_key=True, verbose_name="글번호" )
    writer = models.CharField( null=False, verbose_name="작성자", max_length=50 )
    subject = models.CharField( null=False, verbose_name="글제목", max_length=300 )
    passwd = models.CharField( null=False, verbose_name="비밀번호", max_length=50 )
    content = models.TextField( null=False, verbose_name="글내용", max_length=2000 )
    readcount = models.IntegerField( verbose_name="조회수", default=0 )
    ref = models.IntegerField( null=False, verbose_name="그룹화아이디" )
    restep = models.IntegerField( null=False, verbose_name="글순서" )
    relevel = models.IntegerField( null=False, verbose_name="글레벨" )
    regdate = models.DateTimeField( auto_now_add=True, verbose_name="작성일", blank=True )
    ip = models.CharField( null=False, verbose_name="아이피", max_length=30 )
    

class ImageBoard( models.Model ):
    imageid = models.AutoField( primary_key=True, verbose_name="아이디" )
    title = models.CharField( null=False, max_length=100, verbose_name="제목" )
    image = models.ImageField( null=False, verbose_name="이미지 경로", upload_to="images")  #MBEx/media/images
    name = models.CharField( null=False, verbose_name="파일 이름", max_length=100 )