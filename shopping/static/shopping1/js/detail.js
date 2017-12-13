function add() {
    var num = parseInt($('.num_show').val());
    $('.num_show').val(num+1);
    $('.num_show').blur();
}
function minus() {
    var num = parseInt($('.num_show').val());
    if (num <2){
         return;
    }
    else {

        $('.num_show').val(num-1);
        $('.num_show').blur();
    }

}
$(function () {
  $('.num_show').blur(function () {
      var num = parseInt($('.num_show').val());
      var price = parseInt($('#gprice').text());
      if (num <1){
          $('.num_show').val(1);
          num = 1;
      }
      var total = num*price;
      $('#gtotal').text(total.toFixed(2)+'元');
  });
});