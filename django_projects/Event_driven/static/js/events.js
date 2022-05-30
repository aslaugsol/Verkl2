$(document).ready(function() {
    $('#search-btn').on('click',function (e) {
        e.preventDefault();
        let SearchText = $('#search-box').val();
        $.ajax({
            url:'/events?search_filter=' + SearchText,
            type: 'GET',
            success: function(resp) {
                let newHtml = resp.data.map(d => {
                    return '<div class="well event">' +
                            '<a href="/events/${d.id}">' +
                                '<img class="event-img" src="${d.firstImage}"/>' +
                                '<h4>${d.name}</h4>' +
                                '<p>${d.categoryy}</p>' +
                            '</a>' +
                            '</div>'
                });
                $('.events').html(newHtml.join(''));
                $('#search-box').val('');
            },
            error: function (xhr, status, error){
                console.error(error);
            }
        })


    });
    $('.BookEventBtn').click(function (e) {
        e.preventDefault();

        const event_id = $('.event_id').val();
        const ticket_qty = $('.qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/book-tickets",
            data: {
                'event_id': event_id,
                'ticket_qty': ticket_qty,
                csrfmiddlewaretoken: token
            }
            }



        )
        }

    )
});



