 function checkpwd(){
  var p1=document.form1.password.value;//获取密码框的值
  var p2=document.form1.passwordagain.value;//获取重新输入的密码值
  if(p1==""){
   alert("请输入密码！");//检测到密码为空，提醒输入//
   document.form1.password.focus();//焦点放到密码框
   return false;//退出检测函数
  }//如果允许空密码，可取消这个条件
  
  if(p1!=p2){//判断两次输入的值是否一致，不一致则显示错误信息
   document.getElementById("msg").innerHTML="两次输入密码不一致，请重新输入";//在div显示错误信息
   setTimeout('myfresh()',1000)
   return false;
  }else{
   //密码一致，可以继续下一步操作 
  }
 }
 function myfresh(){
     window.location.reload();
 }
