$(document).ready(function() {
    $('.BookEventBtn').click(function (e) {
            e.preventDefault();
            const event_id = $('.event_id').val();
            const ticket_qty = $('.qty-input').val();
            var token = $('input[name=csrfmiddlewaretoken]').val();
            $.ajax({
                    method: "POST",
                    url: "/book-tickets/" + event_id ,
                    data: {
                        'event_id': event_id,
                        'ticket_qty': ticket_qty,
                        csrfmiddlewaretoken: token
                    },
                    success: function (response) {
                        console.log(response)
                        alert.success(response.status)
                    }
                }
            )
        }
    )
});