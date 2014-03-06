$(document).ready(function () {
    $('button').on('click', function() {
        var haiku = $(this).closest('#current-haiku').find('p');
        $.ajax({
            type: 'GET',
            url: '/api/haiku',
            //data: 'Please remit haiku post haste',
            dataType: 'json',
            success: function(response) {
                haiku.remove();
                var hk = $("<p></p>");
                hk.append(response.getString("haiku"));
                $('#current-haiku').prepend(hk);
            },
            error: function(request, errorType, errorMessage) {
                haiku.remove();
                var hk = $("<p></p>");
                hk.append("No haiku fetched!");
                $('#current-haiku').prepend(hk);
            },
        });
    });

    var longPoll = function() {
        return $.ajax({
            type: 'GET',
            url: '/api/haiqueue',
            // async: true,
            // cache: false,
            timeout: 10000,
            dataType: 'json',
            success: function(response) {
                var five_haikus = response.getJSONArray("haiqueue");
                if (five_haikus.getString(0) != $('#prev-haikus').find('li').first()) {
                    $('#prev-haikus').append($('<li>'+five_haikus.getString(0)+'</li>'));
                    $('#prev-haikus').append($('<li>'+five_haikus.getString(1)+'</li>'));
                    $('#prev-haikus').append($('<li>'+five_haikus.getString(2)+'</li>'));
                    $('#prev-haikus').append($('<li>'+five_haikus.getString(3)+'</li>'));
                    $('#prev-haikus').append($('<li>'+five_haikus.getString(4)+'</li>'));
                }
                return longPoll();
            },
            error: function(request, errorType, errorMessage) {
                $('#prev-haikus').find('li').remove();
                $('#prev-haikus').append($('<li>'+'No previous haikus found!'+'</li>'));
            },
        });
    };

    longPoll();
});
