$(document).ready(function () {
    $('button').on('click', function() {
        $(this).closest('body').find('p').remove();
        var haiku = $(this).closest('body');
        var haiku_text = "Hello, world! Hello,<br>world! Hello, world! Hello, world!<br>Hello, world! Hello!"
        haiku.append("<p>"+haiku_text+"</p>");
    });
})