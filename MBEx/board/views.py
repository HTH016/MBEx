from django.shortcuts import render, redirect
from django.template import loader
from django.views.generic.base import View
from django.http.response import HttpResponse
from board.models import Board, ImageBoard
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateformat import DateFormat
from datetime import datetime

PAGE_SIZE = 5
PAGE_BLOCK = 3

class ListView( View ) :
    def get(self, request) :
        template = loader.get_template( "board/list.html" )
        count = Board.objects.all().count()
        if count == 0 :
            context = {
                "count" : count,
                }
        else :
            pagenum = request.GET.get( "pagenum" )
            if not pagenum :
                pagenum = "1"
            pagenum = int( pagenum )
            start = ( pagenum - 1 ) * int( PAGE_SIZE )      # ( 5 - 1 ) * 10 + 1    41
            end = start + int( PAGE_SIZE )                  # 41 + 10 -1            50
            if end > count :
                end = count
            dtos = Board.objects.order_by( "-ref", "restep" )[start:end]   # 40 ~ 49
            number = count - ( pagenum - 1 ) * int( PAGE_SIZE )
            
            startpage = pagenum // int( PAGE_BLOCK ) * int( PAGE_BLOCK ) + 1
            if pagenum % int( PAGE_BLOCK ) == 0 :
                startpage -= int( PAGE_BLOCK )
            endpage = startpage + int( PAGE_BLOCK ) - 1
            
            pagecount = count // int( PAGE_SIZE )
            if count % int( PAGE_SIZE ) > 0 :
                pagecount += 1
            if endpage > pagecount :
                endpage = pagecount    
            pages = range( startpage, endpage + 1 )   
            context = {
                "count" : count,
                "pagenum" : pagenum,
                "dtos" : dtos,
                "number" : number,
                "startpage" : startpage,
                "endpage" : endpage,
                "pages" : pages,
                "pageblock" : PAGE_BLOCK,
                "pagecount" : pagecount,
                }
        return HttpResponse( template.render( context, request ) )

class WriteView( View ):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def get( self, request ):
        template = loader.get_template( "board/write.html" )
        
        ref = 1;
        restep = 0;
        relevel = 0;
        num = request.GET.get( "num" )                              #MultiValueDictKeyError 방지
        if num == None : 
            # 제목글
            try : 
                # 글이 있는 경우
                maxnum = Board.objects.order_by( "-num" ).values()[0]["num"]
                ref = maxnum + 1                # 그룹화아이디 = 글번호최대값 + 1 
            except IndexError : 
                # 글이 없는 경우
                ref = 1 
        else : 
            # 답변글
            ref = request.GET["ref"]
            restep = request.GET["restep"]
            relevel = request.GET["relevel"]
            # 같은 그룹이면서 글순서가 현재보다 큰 글들은 글순서를 + 1 
            res = Board.objects.filter( ref__exact=ref ).filter( restep__gt=restep)
            for re in res : 
                re.restep = int(re.restep) + 1
                re.save()
            restep = int( restep ) + 1 
            relevel = int( relevel ) + 1 
        
        context = {
            "num" : num,
            "ref" : ref,
            "restep" : restep,
            "relevel" : relevel
            }        
        return HttpResponse( template.render( context, request ) )        
    def post(self, request) :
        dto = Board(
            writer = request.POST["writer"],
            subject = request.POST["subject"],
            passwd = request.POST["passwd"],
            content = request.POST["content"],
            readcount = 0,
            ref = request.POST["ref"],
            restep = request.POST["restep"],
            relevel = request.POST["relevel"],
            regdate = DateFormat( datetime.now() ).format( "Ymd" ),
            ip = request.META.get( "REMOTE_ADDR" )            
            )
        dto.save()
        return redirect( "board:list" )

class ContentView ( View ):
    def get( self, request ):
        template = loader.get_template( "board/content.html" )
        num = request.GET["num"]
        pagenum = request.GET["pagenum"]
        number = request.GET["number"]
        dto = Board.objects.get( num = num )
        
        if dto.ip != request.META.get( "REMOTE_ADDR" ) :
            dto.readcount += 1
            dto.save()
        
        context = {
            "dto" : dto,
            "num" : num,
            "pagenum" : pagenum,
            "number" : number,
            }
        return HttpResponse( template.render( context, request ) )

class DeleteView( View ) :
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def get(self, request) :
        template = loader.get_template( "board/delete.html" )
        num = request.GET["num"]
        pagenum = request.GET["pagenum"]
        context = {
            "num" : num,
            "pagenum" : pagenum,
            }
        return HttpResponse( template.render( context, request ) )
    def post(self, request) :
        num = request.POST["num"]
        passwd = request.POST["passwd"]
        pagenum = request.POST["pagenum"]
        dto = Board.objects.get( num = num )
        if passwd == dto.passwd :           
            dto.readcount = -1
            dto.save()
            return redirect( "board:list" )
        else :
            template = loader.get_template( "board/delete.html" )
            context = {
                "num" : num,
                "pagenum" : pagenum,
                "message" : "입력하신 비밀번호가 다릅니다."
                }
            return HttpResponse( template.render( context, request ) )

class UpdateView( View ):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def get( self, request ):
        template = loader.get_template( "board/update.html" )
        context = {
            "num" : request.GET["num"],
            "pagenum" : request.GET["pagenum"]
            }
        return HttpResponse( template.render( context, request ) )
    def post(self, request):
        num = request.POST["num"]
        passwd = request.POST["passwd"]
        pagenum = request.POST["pagenum"]
        dto = Board.objects.get( num = num )
        if passwd == dto.passwd : 
            template = loader.get_template( "board/updatepro.html")
            context = {
                "num" : num,
                "dto" : dto,
                "pagenum" : pagenum
                }
            return HttpResponse( template.render( context, request ) )
        else : 
            template = loader.get_template( "board/update.html")
            context = {
                "num" : num,
                "pagenum" : pagenum,
                "message" : "입력하신 비밀번호가 다릅니다"
                }
            return HttpResponse( template.render( context, request ) )

class UpdateProView( View ):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def post(self, request):
        num = request.POST["num"]
        dto = Board.objects.get( num = num )
        dto.subject = request.POST["subject"]
        dto.content = request.POST["content"]
        dto.passwd = request.POST["passwd"]
        dto.save()
        return redirect( "board:list" )

class ImageView( View ):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def get(self, request ):
        template = loader.get_template( "board/image.html" )
        context = {}
        return HttpResponse( template.render( context, request ) )
    def post(self, request ):
        title = request.POST["title"]
        img = request.FILES["img"]
        name = img.name
        dto = ImageBoard(
            title = title,
            image = img, 
            name = name
            )       
        dto.save()
        return redirect( "board:imagedown" )

class ImageDownView( View ) :
    def get(self, request) :
        template = loader.get_template( "board/imagedown.html" )
        dtos = ImageBoard.objects.all()
        context = {
            "dtos" : dtos,
            }        
        return HttpResponse( template.render( context, request ) )
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    