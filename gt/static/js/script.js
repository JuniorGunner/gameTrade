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
});

$(window).load(function(){
    $('.height-sidenav').height($('.container-fluid > .row').height());

    var height = [];

    $('.item-row').each(function(index){
        height[index] = $(this).height()/2;;
    });

    var eleHeight = [];

    $('.centered').each(function(index){
        eleHeight[index] = $(this).height()/2;
        $(this).css('margin-top',(height[index]-eleHeight[index]));
    });
});
