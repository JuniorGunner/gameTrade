var ct = function () {
    var height = [];

    $('.item-row').each(function(index){
        height[index] = $(this).height()/2;;
    });

    var eleHeight = [];
    i = 0;
    c = 0;

    $('.centered-2').each(function(index){
        eleHeight[index] = $(this).height()/2;
        $(this).css('margin-top',(height[i]-eleHeight[index]));
        c++;
        if(c == 2){
            c = 0;
            i++;
        }
    });

    $('.centered').each(function(index){
        eleHeight[index] = $(this).height()/2;
        $(this).css('margin-top',(height[index]-eleHeight[index]));
    });
};

$(document).ready(function () {
    $('#rd-user').click(function () {
        if(!$('#rd-user-label').hasClass('selected-radio')){
            $('#rd-user-label').removeClass('unselected-radio');
            $('#rd-user-label').addClass('selected-radio');
            $('#rd-game-label').removeClass('selected-radio');
            $('#rd-game-label').addClass('unselected-radio');
        }
    });

    $('#rd-game').click(function () {
        if(!$('#rd-game-label').hasClass('selected-radio')){
            $('#rd-game-label').removeClass('unselected-radio');
            $('#rd-game-label').addClass('selected-radio');
            $('#rd-user-label').removeClass('selected-radio');
            $('#rd-user-label').addClass('unselected-radio');
        }
    });

    var $star_rating = $('.star-rating .glyphicon');

    var SetRatingStar = function() {
      return $star_rating.each(function() {
        if (parseInt($star_rating.siblings('input.rating-value').val()) >= parseInt($(this).data('rating'))) {
          return $(this).removeClass('glyphicon-star-empty').addClass('glyphicon-star');
        } else {
          return $(this).removeClass('glyphicon-star').addClass('glyphicon-star-empty');
        }
      });
    };

    $star_rating.on('click', function() {
      $star_rating.siblings('input.rating-value').val($(this).data('rating'));
      return SetRatingStar();
    });

    SetRatingStar();

    $('#want').load(ct);
});



$(window).load(function(){
    if($('.height-content').height() > $('.height-sidenav').height())
        $('.height-sidenav').height($('.height-content').height());

    ct();
});
