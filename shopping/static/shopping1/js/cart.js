$(function(){
    // 全选
    $('#all').click(function(){
        var flage =$(this).is(":checked");
        $("input[type=checkbox]").each(function(){
            $(this).attr("checked",flage);
        });

        SumPrice = 0;
        s = 0
        $('.cart_list_td .col01 input').each(function () {
            if ($(this).prop('checked')){
                var prices = $(this).parent().siblings('.col07').text();
                var patt = '^[1-9]+[0-9]*.?[0-9]*';
                var price = parseFloat(prices.match(patt));
                SumPrice += price;
                s += 1;

            }
        })
        $('.settlements .col03 em').text(SumPrice.toFixed(2)+'元');
        $('.total_count em').text(s);
		$('.settlements .col03 b').text(s);
    });

    // 增加商品数量
    $('.add').click(function() {
        var num = parseInt($(this).next('input').val());
        num += 1;
        $(this).next('input').val(num);
        var prices = $(this).parent().parent().prev().html();
        var patt = '^[1-9]+[0-9]*.?[0-9]*';
		var price = parseFloat(prices.match(patt));
        var sum = (num*price).toFixed(2);
        $(this).parent().parent().next().html(sum+'元');
        FinalPrices()
    });
    // 减少商品数量
    $('.minus').click(function(){
        var num = parseInt($(this).prev('input').val());
        if (num > 1){
            num -= 1;
            $(this).prev('input').val(num)
            var prices = $(this).parent().parent().prev().html();
            var patt = '^[1-9]+[0-9]*.?[0-9]*';
            var price = parseFloat(prices.match(patt));
            var sum = (num*price).toFixed(2);
            $(this).parent().parent().next().html(sum+'元');
        }
        FinalPrices()
    });
    // 手动修改数量时，防止出现负数，最小为1
    $('.num_show').blur(function(){
        var num = parseInt($(this).val())
        var prices = $(this).parent().parent().prev().html();
        var patt = '^[1-9]+[0-9]*.?[0-9]*';
        var price = parseFloat(prices.match(patt));
        if (num<1){
            $(this).val(1)
            var sum = (price).toFixed(2);
        }
        else{
            var sum = (price*num).toFixed(2);
        }
        $(this).parent().parent().next().html(sum+'元');
        FinalPrices()
    });
    // 单选商品情况下，计算所有金额，和选中商品数量
    $('.cart_list_td .col01 input').click(function () {
        sumPrice = 0;
        s = 0
        $('.cart_list_td .col01 input').each(function () {
            if ($(this).prop('checked')){
                var prices = $(this).parent().siblings('.col07').text();
                var patt = '^[1-9]+[0-9]*.?[0-9]*';
                var price = parseFloat(prices.match(patt));
                sumPrice += price;
                s += 1;
            }
        })
        $('.settlements .col03 em').text(sumPrice.toFixed(2)+'元');
        $('.total_count em').text(s);
		$('.settlements .col03 b').text(s);

    });

    function FinalPrices() {
        sumPrice = 0;

        $('.cart_list_td .col01 input').each(function () {
            if ($(this).prop('checked')){
                var prices = $(this).parent().siblings('.col07').text();
                var patt = '^[1-9]+[0-9]*.?[0-9]*';
                var price = parseFloat(prices.match(patt));
                sumPrice += price;
            }
            return $('.settlements .col03 em').text(sumPrice.toFixed(2)+'元')
        })
    }

   	$('.settlements .col04 a').click(function() {
        goods = [];
        $('.cart_list_td .col01 input').each(function () {
            // 如果没有被选中，把没有被选中的商品id传给后台
            id = $(this).prop('id')
            count = $(this).parents('.col01').siblings('.col06').children('.num_add').children('input').val();
            if ($(this).prop('checked')) {
                goods.push({
                    'id': id,
                    'count': count,
                    'isChecked': 0
                });

            }
            $.get('/cart_account/', {'goods': goods}, function (ret) {

            })
        })

    });
})
