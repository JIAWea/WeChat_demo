
// 删除公告
function delInfo(iid) {
    var r=confirm("是否删除");
    if (r==true){
       csrftoken();
       $.ajax({
           url:'/backend/infomation/delete/',
           data:{'iid':iid},
           dataType:'JSON',
           type:'POST',
           success:function (arg) {
               if(arg.status){
                    alert(arg.msg);
                    window.location.reload();
                }else {
                    alert(arg.msg);
                }
           }
       })
    }
}


function csrftoken() {
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

