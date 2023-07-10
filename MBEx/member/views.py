from django.shortcuts import render, redirect
import logging
from django.views.generic.base import View
from django.template import loader
from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from django.utils.dateformat import DateFormat
from member.models import Member
from _datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

logger = logging.getLogger(  __name__ )

class MainView( View ) : 
    def get(self, request):
        template = loader.get_template( "member/main.html" )
        memid = request.session.get( "memid" )
        if memid : 
            context = {
                "memid" : memid
                }
        else : 
            context = {}
        return HttpResponse( template.render( context, request ) )
    
class InputView( View ): 
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def get(self, request) : 
        template = loader.get_template( "member/input.html" )
        context = {}
        return HttpResponse( template.render( context, request ) )
    def post(self, request): 
        tel = ""
        tel1 = request.POST["tel1"]
        tel2 = request.POST["tel2"]
        tel3 = request.POST["tel3"]
        if tel1 and tel2 and tel3 : 
            tel = tel1 + "-" + tel2 + "-" + tel3
        dto = Member(
            id = request.POST["id"],
            passwd = request.POST["passwd"],
            name = request.POST["name"],
            email = request.POST["email"],
            tel = tel,
            depart = request.POST["depart"],
            logtime = DateFormat( datetime.now() ).format( "Y-m-d" )
            )
        dto.save()
        logger.info("회원가입에 성공했습니댯 : ", request.POST["id"] )
        return redirect( "login" )
    
class LoginView( View ):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def get(self, request):
        template = loader.get_template( "member/login.html")
        context = {}
        return HttpResponse( template.render( context, request ) )
    def post(self, request):
        id = request.POST["id"]
        passwd = request.POST["passwd"]
        
        try : 
            dto = Member.objects.get( id = id )
            if passwd == dto.passwd : 
                request.session["memid"] = id;
                return redirect("main")
            else :
                message = "입력하신 비밀번호가 다릅니다... "
        except ObjectDoesNotExist  :
            message = "입력하신 아이디가 없습니다..."
        template = loader.get_template("member/login.html")
        context = {
            "message" : message, 
            }
        return HttpResponse( template.render( context, request ) )
    
class LogoutView( View ):
    def get(self, request):
        del request.session["memid"]
        return redirect( "main" )
    
class ConfirmView( View ):  
    def get(self, request ): 
        template = loader.get_template( "member/confirm.html" )
        id = request.GET["id"]
        result = 0
        try : 
            Member.objects.get( id = id )
            result = 1
        except ObjectDoesNotExist : 
            result = 0
        context = {
            "result" : result,
            "id" : id
            }
        return HttpResponse( template.render( context, request ) )

class DeleteView( View ):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)  
    def get(self, request ): 
        template = loader.get_template( "member/delete.html" )
        id = request.GET["id"]
        context = {
            "id" : id
            }
        return HttpResponse( template.render( context, request ) )
    def post(self, request ):
        id = request.POST["id"]
        passwd = request.POST["passwd"]
        dto = Member.objects.get( id = id )
        if passwd == dto.passwd : 
            dto.delete()
            del request.session["memid"]
            return redirect( "main" )
        else : 
            template = loader.get_template("member/delete.html")
            message = "입력하신 비밀번호가 다릅니다. "
            context = {
                "id" : id,
                "message" : message,
                }
            return HttpResponse( template.render( context, request ) )
  
class UpdateView( View ) :
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def get(self, request ):
        template = loader.get_template( "member/update.html" )
        id = request.GET["id"]
        context = {
            "id" : id,
            }
        return HttpResponse( template.render( context, request ) ) 
    def post(self, request ):
        id = request.POST["id"]
        passwd = request.POST["passwd"]
        
        dto = Member.objects.get( id = id )
        if passwd == dto.passwd : 
            template = loader.get_template( "member/updatepro.html" )
            
            t = dto.tel.split( "-" )
            
            context = {
                "t" : t,
                "dto" : dto,
                }
            return HttpResponse( template.render( context, request ) )
        else : 
            template = loader.get_template( "member/update.html" )
            message = "입력하신 비밀번호가 다릅니다"
            context = {
                "id" : id,
                "message" : "입력하신 비밀번호가 다릅니다. .."
                }
            return HttpResponse( template.render( context, request ) )
class UpdateProView( View ):  
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def post(self, request):
        tel = ""
        tel1 = request.POST.get("tel1")
        tel2 = request.POST.get("tel2")
        tel3 = request.POST.get("tel3")
        
        tel = tel1 + "-" + tel2 + "-" + tel3
        
        id = request.POST["id"]
        dto = Member.objects.get( id = id)
        
        newdto = Member(
            id = id,
            passwd = request.POST["passwd"],
            name = dto.name,
            email = request.POST["email"],
            tel = tel,
            depart = request.POST["depart"],
            logtime = dto.logtime
            )
        newdto.save()
        return redirect( "main" )
  
  
  
    
    
    
    
    
    
    
    
    