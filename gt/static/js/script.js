var clickTradeHave = function (id) {
    $('#modal-trade-have-' + String(id)).on('hidden.bs.modal', function () {
        $('#form-trade-have-' + String(id)).submit();
    });
};

var clickTradeWant = function (id) {
    $('#modal-trade-want-' + String(id)).on('hidden.bs.modal', function () {
        $('#form-trade-want-' + String(id)).submit();
    });
};

var clickTradeDonate = function (id) {
    $('#modal-trade-donate-' + String(id)).on('hidden.bs.modal', function () {
        $('#form-trade-donate-' + String(id)).submit();
    });
};

var clickUserHave = function (id) {
    $('#modal-user-have-' + String(id)).on('hidden.bs.modal', function () {
        $('#form-user-have-' + String(id)).submit();
    });
};

var clickUserWant = function (id) {
    $('#modal-user-want-' + String(id)).on('hidden.bs.modal', function () {
        $('#form-user-want-' + String(id)).submit();
    });
};

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


    $('#modal-want .modal-footer #btn-want').on('click', function (e) {
        $(this).closest('.modal').on('hidden.bs.modal', function () {
            $('#form-want').submit();
        });
    });

    $('#modal-have .modal-footer #btn-have').on('click', function (e) {
        $(this).closest('.modal').on('hidden.bs.modal', function () {
            $('#form-have').submit();
        });
    });


    /*$('#modal-lost-account .modal-footer #btn-lost-account').on('click', function (e) {
        $(this).closest('.modal').on('hidden.bs.modal', function () {
            $("input[name='user']").value($('#modal_username').value());
            $("input[name='email']").value($('#modal_email').value());
            alert($("input[name='user']").value());
            alert($("input[name='email']").value());
            $('#form-lost-account').submit();
        });
    });*/

    $('#btn-lost-account').on('click', function (e) {
        $('#modal-lost-account').on('hidden.bs.modal', function () {
            $("input[name='user']").val($('#modal_username').val());
            $("input[name='email']").val($('#modal_email').val());
            $('#form-lost-account').submit();
        });
    });

    /*var $star_rating = $('.star-rating .glyphicon');

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

    SetRatingStar();*/

    $('#user-create input').addClass('form-control');

});



$(window).load(function(){
    /*if($('.height-content').height() > $('.height-sidenav').height())
        $('.height-sidenav').height($('.height-content').height());*/

    ct();

    $('.user-row').css('vertical-align','middle');
});
