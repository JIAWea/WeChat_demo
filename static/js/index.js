window.onload = function(){
　　$("#SetPassword").click(function(){
　　　　var old_password = $(':input[name="old_password"]').val();
    var new_password = $(':input[name="new_password"]').val();
    var repeat_password = $(':input[name="repeat_password"]').val();
    if(old_password == ''){
        alert('旧密码不能为空');
    }else if (new_password != repeat_password) {
        alert('新密码不一致')
    }else {
        $.ajax({
        type: "POST",   //提交的方法
        url:"/backend/backenduser/change/password/", //提交的地址
        data:$('#changepassword').serialize(),// 序列化表单值
        success: function(data) {  //成功
            if(data.err_msg){
                alert(data.err_msg);  //就将返回的数据显示出来
            }else{
                window.location.reload();
            }
        },
        error: function(request) {  //失败的话
             console.log("提交失败");
        },
        })
    }
　　});
}