// $(document).on("click", ".edit", function () {
//
//     list = $(this).parent().siblings();
//     var arr = [];
//     list.each(function () {
//         arr.push($(this).text())
//
//
//     });
//
//     res = '<tr><td id="nid"><span>' + arr[0] + '</span></td><td><input  value=' + arr[1] + ' type="text"></td><td><input value=' + arr[2] + ' type="text"></td><td><input value=' + arr[3] + ' type="text"></td><td><input value=' + arr[4] + ' type="radio"></td><td id="action"><a class="btn btn-success save">保存</a> | <a class="btn btn-danger del">删除</a></td></tr>'
//     $(this).parent().parent().replaceWith(res);
//
// });
//
//
// $(document).on("click", ".save", function () {
//     num = $(this).parent().siblings().find("span").text();
//     list = $(this).parent().siblings().find("input");
//     var arr = [];
//     list.each(function () {
//         arr.push($(this).val())
//
//     });
//     post_data = {
//         nid: num,
//         host: arr[0],
//         hostname: arr[1],
//         department: arr[2],
//         position: arr[3],
//         manager: arr[4]
//     };
//
//     url = "/mod/" + num + "/";
//     vali_ajax(url, post_data);
//     window.location.reload();
//
// });
//
//
// function vali_ajax(url,post_data) {
//     $.ajax({
//         url: url,
//         type: "POST",
//         async: false,
//         data: post_data,
//
//     })
// }
//
// $(document).on("click", ".del", function () {
//
//     num = $(this).parent().siblings().find("span").text();
//
//     post_data = {nid: num};
//     url = "/rm/" + num + "/";
//     vali_ajax(url, post_data);
//     window.location.reload();
//
// });
//
// $(document).on("click", ".addshow", function () {
//
//     $("tbody").append('<tr><td id="nid"><span>0</span></td><td><input type="text"></td><td><input type="text"></td><td><input  type="text"></td><td><input type="text"></td><td><input  type="text"></td><td id="action"><a class="btn btn-success add">保存</a> | <a class="btn btn-danger del">删除</a></td></tr>')
//     $(".addshow").attr("disabled","disabled");
// });
//
// $(document).on("click", ".add", function () {
//
//    list = $(this).parent().siblings().find("input");
//     var arr = [];
//     list.each(function () {
//         arr.push($(this).val())
//
//     });
//     post_data = {
//         host: arr[0],
//         hostname: arr[1],
//         department: arr[2],
//         position: arr[3],
//         manager: arr[4]
//     };
//
//     url = "/add/";
//     vali_ajax(url, post_data);
//     window.location.reload();
//     $(".addshow").removeAttribute("disabled","disabled");
// });
//
//
// $(document).on("click",".page_go",function () {
//
//     page_num=$(this).text();
//     alert(page_num);
//     post_data={page_num:page_num};
//     url="/hosts/";
//     vali_ajax(url,post_data);
// });