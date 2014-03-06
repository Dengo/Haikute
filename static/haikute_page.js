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
<<<<<<< HEAD
                hk.append(response.getString("haiku"));
=======
                hk.append(response.haiku).hide();
>>>>>>> c8946fea0664ef5ec6386f533f87248ea800c2db
                $('#current-haiku').prepend(hk);
                hk.fadeIn(800);
                longPoll();
            },
            error: function(request, errorType, errorMessage) {
<<<<<<< HEAD
                haiku.remove();
                var hk = $("<p></p>");
                hk.append("No haiku fetched!");
                $('#current-haiku').prepend(hk);
=======
                console.log("The haiku request failed");
>>>>>>> c8946fea0664ef5ec6386f533f87248ea800c2db
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
<<<<<<< HEAD
                var five_haikus = response.getJSONArray("haiqueue");
                if (five_haikus.getString(0) != $('#prev-haikus').find('li').first()) {
                    $('#prev-haikus').append($('<li>'+five_haikus.getString(0)+'</li>'));
                    $('#prev-haikus').append($('<li>'+five_haikus.getString(1)+'</li>'));
                    $('#prev-haikus').append($('<li>'+five_haikus.getString(2)+'</li>'));
                    $('#prev-haikus').append($('<li>'+five_haikus.getString(3)+'</li>'));
                    $('#prev-haikus').append($('<li>'+five_haikus.getString(4)+'</li>'));
                }
                return longPoll();
=======
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
>>>>>>> c8946fea0664ef5ec6386f533f87248ea800c2db
            },
            error: function(request, errorType, errorMessage) {
                $('#prev-haikus').find('li').remove();
                $('#prev-haikus').append($('<li>'+'No previous haikus found!'+'</li>'));
            },
        });
    };

    longPoll();
    setInterval(longPoll, 15000);

});
