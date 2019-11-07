var code ;  
function createCode(){   
code = new Array();  
var codeLength = 4;  
var checkCode = document.getElementById("yzm");  
checkCode.value = "";  
var selectChar = new Array(2,3,4,5,6,7,8,9,'A','B','C','D','E','F','G','H','J','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y','Z');  
for(var i=0;i<codeLength;i++) {  
var charIndex = Math.floor(Math.random()*32);  
code +=selectChar[charIndex];  
}  
checkCode.value = code;  
}  

//判断用户名是否为空
 
 function check(){
            var username= document.getElementById("username");
            if(username.value.trim()==""){//没有输入用户名是显示提示
                //获取所有子节点
                var findNodes = document.getElementById("name").children;
                if(findNodes.length==0){//只添加一次span
                    var appdom= document.createElement("span");
                    appdom.innerHTML="*用户名不能为空";
                    appdom.style.color="red";
                 
                    document.getElementById("name").appendChild(appdom);
                    return false;
                }
                else{return true;}

            }else{//输入了内容后清除节点内容
                var findNodes =document.getElementById("name").children;
                if(findNodes.length>0){
                    document.getElementById("name").removeChild(findNodes[0]);
                }
            }
            var userpwd = document.getElementById("userpwd");
            if(userpwd.value.trim()==""){
                var findNodes2 = document.getElementById("pwd").children;
                if(findNodes2.length==0){
                    var appdom2 = document.createElement("span");
                    appdom2.innerHTML="*密码不能为空";
                    appdom2.style.color="red";
                    document.getElementById("pwd").appendChild(appdom2);
                }
                return false;
            }else{
                var findNodes2 = document.getElementById("pwd").children;
                if(findNodes2.length>0){
                    document.getElementById("pwd").removeChild(findNodes2[0]);
                }
            }//验证验证码是否正确
            var useryzm= document.getElementById("yzm-input");
            if(useryzm.value.trim()!=""){
            		var inputCode = document.getElementById("yzm-input").value.toUpperCase(); 
            		 var findNodes3 = document.getElementById("yzmt").children;
					if(inputCode != code )
					{
						if (findNodes3.length==0) {
						var appdom= document.createElement("span");
                    appdom.innerHTML="*验证码错误！";
                    appdom.style.color="red";
                    document.getElementById("yzmt").appendChild(appdom);
                    return false;
					}}
					else{return true;}
            	}
          	else if(useryzm.value.trim()==""){
                var findNodes3 = document.getElementById("yzmt").children;
                if(findNodes3.length==0){//只添加一次span
                    var appdom= document.createElement("span");
                    appdom.innerHTML="*验证码不能为空";
                    appdom.style.color="red";
                    document.getElementById("yzmt").appendChild(appdom);
                }
                return false;
            }
            	
            else{//输入了内容后清除节点内容
                var findNodes3 =document.getElementById("yzmt").children;
                if(findNodes3.length>0){
                    document.getElementById("yzmt").removeChild(findNodes3[0]);
                }
            }
        }
        //忘记密码
 function Wopen(){
      window.open('#','_self','width=600,height=400,top=100,left=0');

  } 