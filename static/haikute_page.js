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
            timeout: 10000,
            dataType: 'json',
            success: function(response) {
                var five_haikus = response.haiqueue;
                var prev_haikus = new Array();
                //Populate prev_haikus
                for(var i = 0; i < 5; i++) {
                    prev_haikus[i] = $('#haiku'+i).find('p').html();
                }
                new_count = 0;
                for(var i = 4; i >= 0; i--) {
                    for(var j = 0; j < 5; j++) {
                        if(prev_haikus[i] == five_haikus[j] && prev_haikus[i]) {break;}
                        else if(j == 4) {
                            $('#haiku'+i).find('p').remove();
                            $('#haiku'+i).hide().append($('<p>'+five_haikus[new_count]+'</p>')).slideDown(500);
                            new_count++;
                        }
                    }
                }
            },
            error: function(request, errorType, errorMessage) {
                console.log("The haiqueue request failed");
            },
        });
    };

    $('.prev-haikus').on('mouseenter', function() {
        $(this).animate({opacity:'1.0'}, "slow");
    });

    $('.prev-haikus').on('mouseleave', function() {
        $(this).animate({opacity:'0.6'}, "slow");
    });

    longPoll();
    setInterval(longPoll, 15000);

});
