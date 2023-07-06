from django.contrib import admin
from board.models import Board, ImageBoard

class BoardAdmin( admin.ModelAdmin ) :
    list_display = ( "num", "writer", "subject", "passwd", "content",
                     "readcount", "ref", "restep", "relevel", "ip" )
admin.site.register( Board, BoardAdmin )

class ImageBoardAdmin( admin.ModelAdmin ) :
    list_display = ( "imageid", "title", "image", "name" )
admin.site.register( ImageBoard, ImageBoardAdmin )
