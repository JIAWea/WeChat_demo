$(function () {
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

    $("#Change-btn").click(function () {
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

});