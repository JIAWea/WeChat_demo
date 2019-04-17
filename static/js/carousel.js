$(function () {

    // 添加图片
    $("#btn-Save").click(function () {
    if($(":input[name='caption']").val() == ""){
        $("#nocaption").text('不能为空')
    }else if($(":input[name='path']").val() == ""){
        $("#noimg").text('不能为空')
    }else {
        var data = new FormData();
        data.append('caption',$(":input[name='caption']").val());
        data.append('path',$(":input[name='path']")[0].files[0]);
        $.ajax({
            url:'/backend/carousel/add/',
            type:"POST",
            data:data,
            dataType:"JSON",
            success:function(arg){
                if(arg.status == 200){
                   alert(arg.msg)
                    window.location.reload()
                }else {
                   alert(arg.msg)
                }
            },
            processData: false,      //tell JQuery not to process the data
            contentType: false
        })
        }
    });

    // 点击编辑
    $("a[cid]").each(function () {
        $(this).click(function () {
            var cid = $(this).attr('cid');
            $('#carouselImgChange').modal('show');
            $("#Change-btn").click(function () {
                changeImg(cid);
            })
        })
    })

    // 修改图片
    function changeImg(cid){
        if($(":input[name='change-caption']").val() == ""){
        $("#change-caption").text('不能为空')
    }else if($(":input[name='change-path']").val() == ""){
        $("#change-path").text('不能为空')
    }else {
        var data = new FormData();
        data.append('caption',$(":input[name='change-caption']").val());
        data.append('path',$(":input[name='change-path']")[0].files[0]);
        data.append('cid',cid);
        $.ajax({
            url:'/backend/carousel/edit/',
            type:"POST",
            data:data,
            dataType:"JSON",
            success:function(arg){
                if(arg.status == 200){
                   alert(arg.msg)
                    window.location.reload()
                }else {
                   alert(arg.msg)
                }
            },
            processData: false,      //tell JQuery not to process the data
            contentType: false
        })
        }
    }

    // 删除图片
    $("a[name='del_confirm']").click(function () {
        var r=confirm("是否删除");
        if (r==true){
           csrftoken();
           var cid = $(this).siblings().attr('cid');
           $.ajax({
               url:'/backend/carousel/delete/',
               data:{'cid':cid},
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
        else {

        }

    })

});

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