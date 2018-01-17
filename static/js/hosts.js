     $(document).on("click",".edit",function(){

           list=$(this).parent().siblings();
          var arr=[];
          list.each(function(){
              arr.push($(this).text())


  });

          res='<tr><td><span>'+arr[0]+'</span></td><td><input  value='+arr[1]+' type="text"></td><td><input value='+arr[2]+' type="text"></td><td><input value='+arr[3]+' type="text"></td><td><input value='+arr[4]+' type="text"></td><td><input value='+arr[5]+' type="text"></td><td><a class="btn btn-success save">保存</a> | <a class="btn btn-danger">删除</a></td></tr>'
          $(this).parent().parent().replaceWith(res);

    });


$(document).on("click",".save",function () {
    num=$(this).parent().siblings().find("span").text();
    list=$(this).parent().siblings().find("input");
    var arr=[];
      list.each(function(){
             arr.push($(this).val())

  });
    post_data={
        nid:num,
        host:arr[0],
        hostname:arr[1],
        department:arr[2],
        position:arr[3],
        manager:arr[4]
    };

    url="/mod/"+num+"/";
    vali_ajax(url,post_data)

});





function vali_ajax(url,post_data) {
      $.ajax( {
            url:url,
            type:"POST",
            data:post_data
        //     success:function (data) {
        //     data = JSON.parse(data);
        //     if (data["status"] == 1) {
        //         $(input_error).text(data["result"]);
        //          $(input).addClass("border_color_red");
        //     } else {
        //                 $(input_error).text("");
        //                 $(input).addClass("border_color_green");
        //     }
        // }
    });
}