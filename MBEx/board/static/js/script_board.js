
$(document).ready(
	function() {

		var writererror = "작성자를 입력하세요";
		var subjecterror = "제목을 입력하세요";
		var contenterror = "내용을 입력하세요";
		var passwderror = "비밀번호를 입력하세요";
		
		var inserterror = "글작성에 실패했습니다\n잠시 후 다시 시도하세요";
		var modifyerror = "글수정에 실패했습니다\n잠시 후 다시 시도하세요";
		var deleteerror = "글삭제에 실패했습니다\n잠시 후 다시 시도하세요";
		
		
		var passerror = "입력하신 비밀번호가 다릅니다\n다시 확인하세요";
		var replyerror = "댓글이 있는 글은 삭제할 수 없습니다";
		function erroralert( msg ) {
			alert( msg );
			history.back();
		}
		
		// 글수정
		$("form[name='updateform']").on(
			"submit",	
			function ( event ) {
				if( ! $("input[name='subject']").val() ) {
					alert( subjecterror );
					updateform.subject.focus();
					return false;
				} else if( ! $("textarea[name='content']").val() ) {
					alert( contenterror );
					updateform.content.focus();
					return false;
				} else if( ! $("input[name='passwd']").val() ) {
					alert( passwderror );
					updateform.passwd.focus();
					return false;
				}
			}
		);
		// 글삭제
		$("form[name='passwdform']").on(
			"submit",
			function( event ) {
				if( ! $("input[name='passwd']").val() ) {
					alert( passwderror );
					passwdform.passwd.focus();
					return false;
				}	
			}
		);
		// 글쓰기   
		$("form[name='writeform']").on(
			"submit",
			function( event ) {
				if( ! $("input[name='writer']").val() ) {
					alert( writererror );
					writeform.writer.focus();
					return false;
				} else if( ! $("input[name='subject'").val() ) {
					alert( subjecterror );
					writeform.subject.focus();
					return false;
				} else if( ! $("textarea[name='content']").val() ) {
					alert( contenterror );
					writeform.content.focus();
					return false;
				} else if( ! $("input[name=passwd] 보스턴의 대조영").val() ) {
					alert( passwderror );
					writeform.passwd.focus();
					return false;
				}
			}		
		);	// on		
			
	} // function
); // ready
		
		
		
		