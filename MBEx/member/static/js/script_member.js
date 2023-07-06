

$(document).ready ( 
	function() {

		var iderror = "아이디를 입력하세요";
		var passwderror = "비밀번호를 입력하세요";
		var repasswderror = "비밀번호가 다릅니다";
		var nameerror = "이름을 입력하세요";
		var juminerror = "주민등록번호를 입력하세요";
		var telerror = "전화번호를 입력하세요";
		var emailerror = "이메일 입력하세요";
		var confirmerror = "중복확인을 해주세요";
		
		var inputerror = "회원가입에 실패했습니다.\n잠시 후 다시 시도하세요.";
		var idxerror = "입력하신 아이디가 없습니다.\n다시 확인하세요.";
		var passerror = "입력하신 비밀번호가 다릅니다.\n다시 확인하세요.";
		var deleteerror = "회원탈퇴에 실패했습니다.\n잠시 후 다시 시도하세요.";
		var modifyerror = "회원정보수정에 실패했습니다.\n잠시 후 다시 시도하세요";
		
		function erroralert( msg ) {
			alert( msg );
			history.back();
		}
		
		// 회원 정보 수정
		function modifycheck() {
			if( ! modifyform.passwd.value ) {
				alert( passwderror );
				modifyform.passwd.focus();
				return false;
			} else if( modifyform.passwd.value != modifyform.repasswd.value ) {
				alert( repasswderror );
				modifyform.passwd.focus();
				return false;
			}	
		}
		
		$("input[value='수정']").on(
			"click",
			function( event ) {
				if( ! passwdform.passwd.value ) {
					alert( passwderror );
					passwdform.passwd.focus();
					return false;
				}
			}
		); // on
		
		
		// 회원탈퇴
		$("input[value='탈퇴']").on(
			"click",
			function( event ) {
				if( ! passwdform.passwd.value ) {
					alert( passwderror );
					passwdform.passwd.focus();
					return false;
				}
			}
		); // on
		
		// 아이디 중복확인
		$("input[value='중복확인']").on(
			"click",
			function( event ) {
				var id = $("input[name='id']").val();
				if( ! id ) {
					alert( iderror );
					inputform.id.focus();		
				} else {
					url = "confirm?id=" + id;
					open( url, "confirm", "scrollbar=no, statusbar=no, titlebar=no, menubar=no, width=400px, height=250px" );
				}
			} // function
		); // on
		
		$("input[value='확인']").on(
			"click",
			function( event ) {
				if( ! $("input[name='id']").val() ) {
					alert( iderror );
					confirmform.id.focus();
					return false;
				}
			}
		); // on
		
		$("input[value='사용']").on(
			"click",
			function( event ) {
				opener.document.inputform.id.value = $("td span").text().trim();
				opener.document.inputform.check.value = "1";
				window.close();	
			}
		);
		
		// 가입페이지
		$("form[name='inputform']").on(
			"submit",
			function() {
				if( inputform.check.value == "0" ) {
					alert( confirmerror );
					inputform.id.focus();
					return false;
				}
						
				if( ! $("input[name='id']").val() ) {
					alert( iderror );
					inputform.id.focus();
					return false;
				} else if( ! $("input[name='passwd']").val() ) {
					alert( passwderror );
					inputform.passwd.focus();
					return false;
				} else if( $("input[name='passwd']").val() != $("input[name='repasswd']").val() ) {
					alert( repasswderror );
					inputform.passwd.value = "";
					inputform.passwd.focus();
					return false;
				} else if( ! $("input[name='name']").val() ) {
					alert( nameerror );
					inputform.name.focus();
					return false;
				} else if( ! $("input[name='email']").val() ) {
					alert( emailerror );
					inputform.email.focus();
					return false;
				}
				
				if( ! $("input[name='tel1']").val() 
					|| ! $("input[name='tel2']").val() 
					|| ! $("input[name='tel3']").val() ) {
					alert( telerror );
					inputform.tel1.focus();
					return false;					
				} else if( $("input[name='tel1']").val().length < 3 
						|| $("input[name='tel2']").val().length < 3 
						|| $("input[name='tel3']").val().length < 4 ) {
					alert( telerror );
					inputform.tel1.focus();
					return false;	
				}
			
			} // function
		); //on
		
		function nextjumin2() {
			if( inputform.jumin1.value.length == 6 ) {
				inputform.jumin2.focus();	
			} 	
		}
		function nexttel1() {
			if( inputform.jumin2.value.length == 7 ) {
				inputform.tel1.focus();
			}
		}
		function nexttel2() {
			if( inputform.tel1.value.length == 3 ) {
				inputform.tel2.focus();
			}
		}
		function nexttel3() {
			if( inputform.tel2.value.length == 4 ) {
				inputform.tel3.focus();
			}
		}
		function nextemail1() {
			if( inputform.tel3.value.length == 4 ) {
				inputform.email1.focus();
			}
		}
		
		// 메인페이지
		$("form[name='mainform']").on(
			"submit",
			function( event ) {
				if( ! $("input[name='id']").val() ) {
					alert( iderror );
					$("input[name='id']").focus();
					return false;
				} else if( ! $("input[name='passwd']").val() ) {
					alert( passwderror );
					$("input[name='passwd']").focus();
					return false;
				}
			}
		);
		
	
	} // function
); // ready






