$('#id-chk-directic').click(function(){
    if($(this).prop("checked") == true){
        valor = $("#id-txt-gerencia-matriz").val();
        trae_matrices('gerencia', valor, 1);
    }
    else if($(this).prop("checked") == false){
        valor = $("#id-txt-gerencia-matriz").val();
        trae_matrices('gerencia', valor, 0);
    }
});
