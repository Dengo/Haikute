$(document).ready(function () {
    $('button').on('click', function() {
        var haiku = $(this).closest('body').find('p');;
        $.ajax({
            type: 'POST',
            url: 'http://localhost:8000/haiku_text_page.html',
            data: 'Please remit haiku post haste',
            dataType: 'json',
            success: function(response) {
                haiku.remove();
                var hk = $("<p></p>");
                hk.append(response);
                $('body').hide().html(haiku).fadeIn();
            },
            error: function(request, errorType, errorMessage) {
                alert('Error: ' + request + ' with message ' + errorMessage);
            },
        });
    });
})