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
                var prev_haikus = $('#prev-haikus').find('p');
                var num_new = 5;
                // Determine how many new haikus have been passed back
                for(var i = 0; i < 5; i++) {
                    if(five_haikus[i] == prev_haikus.first().html()) {
                        num_new = i;
                    }
                }
                // Prepand that many haikus to the front of #prev-haikus
                for(var i = num_new - 1; i >= 0; i--) {
                    $('#prev-haikus').prepend($('<p>'+five_haikus[i]+'</p>')).slideDown(500);
                    prev_haikus.last().remove();
                }
            },
            error: function(request, errorType, errorMessage) {
                console.log("The haiqueue request failed");
            },
        });
    };

    longPoll();
    setInterval(longPoll, 15000);

});
