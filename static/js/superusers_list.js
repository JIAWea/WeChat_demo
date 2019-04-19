$(function () {
        bindUplodImg();
        bindCheckAll();
        bindReverselAll();
        bindCancelAll();
        bindDelBtn();
        bindImportAll();
    });

// 批量导入
function bindImportAll() {

}

// Excel批量导入用户判断
function bindUplodImg() {
    var $input =  $("#filexlsx");
    // ①为input设定change事件
    $input.change(function () {
    //    ②如果value不为空，调用文件加载方法
        if($(this).val() != ""){
            if($("#filexlsx")[0].files[0].name.split(".")[1] != "xlsx"){    // 获取上传格式
                alert("导入失败，表格必须为xlsx格式")
            }else if($("#filexlsx")[0].files[0].size > 1048576){
                alert("文件大小必须小于1M")
            } else {
                fileLoad(this);
            }
        }
    })
}
// Excel批量导入用户
function fileLoad(ele){
      //④创建一个formData对象
    var formData = new FormData();
    //⑤获取传入元素的val
    var name = $(ele).val();
      //⑥获取files
    var files = $(ele)[0].files[0];
    //⑦将name 和 files 添加到formData中，键值对形式
    formData.append("file", files);
    formData.append("name", name);
    $.ajax({
        url: "/backend/superusers/bluk-add/",
        type: 'POST',
        data: formData,
        processData: false,// ⑧告诉jQuery不要去处理发送的数据
        contentType: false, // ⑨告诉jQuery不要去设置Content-Type请求头
        success: function (arg) {
           //11成功后的动作
            if(arg.status){
                alert("导入成功");
                window.location.reload()
            }else {
                alert(arg.msg);
            }
        },
        error : function (responseStr) {
            //12出错后的动作
            alert("出错啦");
        }
    });
}

// 删除用户
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

// 全选
function bindCheckAll() {
    $('#checkAll').click(function () {
        $('#table_tb').find(':checkbox').each(function () {
           if($(this).prop('checked')){
               // 已经是选中了，无需再选中
           }else {
               $(this).prop('checked',true);
           }
        });
    });
}
// 反选
function bindReverselAll() {
    $('#reverselAll').click(function () {
        $('#table_tb').find(':checkbox').each(function () {
           if($(this).prop('checked')){
               $(this).prop('checked',false);
           }else {
               $(this).prop('checked',true);
           }
        });
    });
}

// 取消
function bindCancelAll() {
    $('#cancelAll').click(function () {
        $('#table_tb').find(':checked').each(function () {
            $(this).prop('checked',false);
            if($('#editBtn').hasClass('btn-warning')){
                $(this).prop('checked',false);
            }
        })
    });
}

// csrf
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