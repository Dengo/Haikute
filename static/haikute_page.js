$(document).ready(function () {
    $('button').on('click', function() {
        var haiku = $(this).closest('#current-haiku').find('p');
        $.ajax({
            type: 'GET',
            url: '/api/haiku',
            dataType: 'json',
            success: function(response) {
                haiku.remove();
                var hk = $("<p></p>");
                hk.append(response.haiku).hide();
                $('#current-haiku').prepend(hk);
                hk.fadeIn(800);
                longPoll();
            },
            error: function(request, errorType, errorMessage) {
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
                var five_haikus = response.haiqueue;
                var prev_haikus = $('#prev-haikus').find('li');
                if (five_haikus[0] != prev_haikus.first().html()) {
                    prev_haikus.remove();
                    for(var i = 0; i < 5; i++) {
                        if(five_haikus[i]) {
                            $('#prev-haikus').hide().append($('<li>'+five_haikus[i]+'</li>')).slideDown(500);
                        }
                    }
                }
                else {
                    console.log("Didn't fall through");
                }
            },
            error: function(request, errorType, errorMessage) {
                // $('#prev-haikus').find('li').remove();
                // $('#prev-haikus').append($('<li>'+'No previous haikus found!'+'</li>'));
                console.log("The haiqueue request failed");
            },
        });
    };

    longPoll();
    setInterval(longPoll, 15000);

});
