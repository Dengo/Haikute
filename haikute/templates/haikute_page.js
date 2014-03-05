$(document).ready(function () {
    $('button').on('click', function() {
        var haiku = $(this).closest('#current-haiku').find('p');;
        $.ajax({
            type: 'GET',
            url: '/haiku',
            //data: 'Please remit haiku post haste',
            dataType: 'json',
            success: function(response) {
                haiku.remove();
                var hk = $("<p></p>");
                hk.append(response);
                $('body').html(haiku);
            },
            error: function(request, errorType, errorMessage) {
                alert('Error: ' + request + ' with message ' + errorMessage);
            },
        });
    });

    var longPoll = function() {
        return $.ajax({
            type: 'GET',
            url: '/haiqueue',
            async: true,
            cache: false,
            timeout: 10000,
            success: function(response) {
                if (response.length > 0) {
                    $('#prev-haikus').append($('<li>'+response+'</li>'))
                }
                return longPoll();
            },
            dataType: 'json'
        });
    };

    longPoll();
});
