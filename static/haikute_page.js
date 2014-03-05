$(document).ready(function () {
    $('button').on('click', function() {
        var haiku = $(this).closest('#current-haiku').find('p');
        $.ajax({
            type: 'GET',
            url: '/api/haiku',
            //data: 'Please remit haiku post haste',
            dataType: 'json',
            success: function(response) {
                // console.log("The haiku request succeeded");
                haiku.remove();
                var hk = $("<p></p>");
                hk.append(response.haiku);
                $('#current-haiku').prepend(hk);
            },
            error: function(request, errorType, errorMessage) {
                // haiku.remove();
                // var hk = $("<p></p>");
                // hk.append("No haiku fetched!");
                // $('#current-haiku').prepend(hk);
                console.log("The haiku request failed");
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
                // console.log("The haiqueue request succeeded");
                console.log(response);
                var five_haikus = response.haiqueue;
                console.log(five_haikus);
                if (five_haikus[0] != $('#prev-haikus').find('li').first()) {
                    $('#prev-haikus').find('li').remove();
                    $('#prev-haikus').append($('<li>'+five_haikus[0]+'</li>'));
                    $('#prev-haikus').append($('<li>'+five_haikus[1]+'</li>'));
                    $('#prev-haikus').append($('<li>'+five_haikus[2]+'</li>'));
                    $('#prev-haikus').append($('<li>'+five_haikus[3]+'</li>'));
                    $('#prev-haikus').append($('<li>'+five_haikus[4]+'</li>'));
                }
                setTimeout(longPoll, 10000);
            },
            error: function(request, errorType, errorMessage) {
                // $('#prev-haikus').find('li').remove();
                // $('#prev-haikus').append($('<li>'+'No previous haikus found!'+'</li>'));
                console.log("The haiqueue request failed");
            },
        });
    };

    longPoll();
});
