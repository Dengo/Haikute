$(document).ready(function () {
    $('button').on('click', function() {
        var haiku = $(this).closest('body');
        $.ajax({
            url: 'haiku_text_page.html',
            data: 'button=' + $(this).val(),
            datatype: 'json',
            success: function(response) {
                $('p').html(response);
            },
            error: function(request, errorType, errorMessage) {
                alert('Error: ' + request + ' with message ' + errorMessage);
            },
        });
    });
})