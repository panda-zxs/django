/*  选项卡功能（通过用户中心的选项父级<li>的index，关联右侧信息栏，而改变div的diplay属性）
    (有个想法可以应用ajax来实现异步加载右侧信息栏----还没做)
*/
$(function(){
    $('#btn input').click(function(){
        $(this).addClass('btn11').parent().siblings().children().removeClass('btn11');

        $('#btnbox div').filter('.right_content').eq($(this).parent().index()).addClass('btnbox').siblings().removeClass('btnbox');
    });

})