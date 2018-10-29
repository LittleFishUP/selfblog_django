$(function(){
    // 记录用户名等是否已被注册过的状态值
    window.registerStatus = 1;


// 为username控件绑定blur时间
$("input[name='username']").blur(function(){
    if($(this).val().trim().length == 0)
        return;
    $.get(
        '/check_input/',
        {'username':$(this).val()},
        function(data){
            $('#username-tip').html(data.msg);
            window.registerStatus=data.status;
        },'json'
    );
    });
$("input[name='email']").blur(function(){
    if($(this).val().trim().length == 0)
        return;
    $.get(
        '/check_input/',
        {'email':$(this).val()},
        function(data){
            $('#email-tip').html(data.msg);
            window.registerStatus=data.status;
        },'json'
    );
    });
$("input[name='myurl']").blur(function(){
    if($(this).val().trim().length == 0)
        return $('#myurl-tip').html("选填项");
    $.get(
        '/check_input/',
        {'myurl':$(this).val()},
        function(data){
            $('#myurl-tip').html(data.msg);
            window.registerStatus=data.status;
        },'json'
    );
    });
/**2.为#formReg表单元素绑定submit事件*/
$("#formReg").submit(function () {
    //判断registStatus的值，决定表单是否要被提交
    // console.log('registStatus:' + registStatus);
    if (window.registStatus == 1)
        return false;
    return true;
    });
});