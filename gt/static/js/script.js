$(document).ready(function () {
    $('#rd-usuario').click(function () {
        if(!$('#rd-usuario-label').hasClass('selected-radio')){
            $('#rd-usuario-label').removeClass('unselected-radio');
            $('#rd-usuario-label').addClass('selected-radio');
            $('#rd-jogo-label').removeClass('selected-radio');
            $('#rd-jogo-label').addClass('unselected-radio');
        }
    });

    $('#rd-jogo').click(function () {
        if(!$('#rd-jogo-label').hasClass('selected-radio')){
            $('#rd-jogo-label').removeClass('unselected-radio');
            $('#rd-jogo-label').addClass('selected-radio');
            $('#rd-usuario-label').removeClass('selected-radio');
            $('#rd-usuario-label').addClass('unselected-radio');
        }
    });

    /*$(".nav a").on("click", function(){
        $(".nav").find(".active").removeClass("active");
        $(this).parent().addClass("active");
    });*/
});
