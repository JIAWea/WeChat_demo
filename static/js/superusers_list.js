$(function () {
        bindDelBtn();
    });

    function bindDelBtn() {
    $("#delBtn").click(function () {
        var mymessage=confirm("您确定要删除所选择的用户吗?");
        if(mymessage==true){
            csrftoken();
            var postList = [];
            var tr = $(":checked").parent().parent();
            if(tr.length != 0){
                tr.each(function(){
                    postList.push($(this).attr('id'));      // 选择的id
                });
                //console.log(postList);                       // [1,2,3]

                if(postList != ''){
                    $.ajax({
                    url: '/backend/superusers/delete/',
                    type: 'POST',
                    dataType: 'JSON',
                    data: JSON.stringify(postList),
                    success:function (arg) {
                        if(arg.status){
                            alert(arg.msg);
                            window.location.reload();
                        }else {
                            alert(arg.msg);
                        }
                    }
                });
                }
            }else{
                alert('请选择要设置的用户')
            }
        }
    });
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