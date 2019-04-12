window.onload = function(){
    $('#addUserForm').on('hidden.bs.modal', function (){
        document.getElementById("backendUserAdd").reset();      // 取消添加管理员的模态对话框后清空输入框的值
    });
    $('#setPwdFrom').on('hidden.bs.modal', function (){
        document.getElementById("changepassword").reset();      // 取消更改密码的模态对话框后清空输入框的值
    });

　　$("#SetPassword").click(function(){
　　　　var old_password = $("#changepassword").find(':input[name="old_password"]').val();
        var new_password = $("#changepassword").find(':input[name="new_password"]').val();
        var repeat_password = $("#changepassword").find(':input[name="repeat_password"]').val();
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

    $("#UserAddSave").click(function () {
        var username = $("#backendUserAdd").find(":input[name='username']").val();
        var password = $("#backendUserAdd").find(":input[name='password']").val();
        var repeat_password = $("#backendUserAdd").find(":input[name='repeat_password']").val();
        var permissionList = $('input[name="permissionList"]:checked');
        var permissions = '';
        $.each(permissionList, function (index, value, array) {
            if (index+1 == permissionList.length) {   // 最后一位，不加逗号
                permissions += permissionList[index].value;
            } else {
                permissions += permissionList[index].value + ', ';
            }
        });
        if(username == ''){
            alert('用户名不能为空');
        } else if(password == ''){
            alert('密码不能为空');
        }else if(repeat_password == ''){
            alert('确认密码不能为空');
        }else if (password != repeat_password) {
            alert('两次输入的密码不一致')
        }else {
            mycsrftoken();
            $.ajax({
            type: "POST",   //提交的方法
            url:"/backend/backenduser/add/", //提交的地址
            // data:$('#backendUserAdd').serialize(),// 序列化表单值
            data: JSON.stringify({
                'username':username,
                'password':password,
                'repeat_password':repeat_password,
                'permissions':permissions
            }),
            success: function(data) {  //成功
                if(data.err_msg != "添加成功"){
                    alert(data.err_msg);  //就将返回的数据显示出来
                }else if(data.err_msg= "添加成功"){
                    alert(data.err_msg);
                    $('#addUserForm').find('#exampleModal').modal('hide');
                }
            },
            error: function(request) {  //失败的话
                 console.log("提交失败");
            },
            })
        }


    });

    function mycsrftoken() {
        /*********** csrftoken开始****************/
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }

        var csrftoken = getCookie('csrftoken');

        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });

        /*********** csrftoken结束****************/
    }

};
