$(document).ready(function(){
    let url = $("#cartoonVideo").attr('src');

    $("#myButton").on('hide.bs.modal', function(){
        $("#cartoonVideo").attr('src', '');
    });

    $("#myButton").on('show.bs.modal', function(){
        $("#cartoonVideo").attr('src', url);
    });
});