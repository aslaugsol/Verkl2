$(document).ready(function() {
    $('#search-btn').on('click',function (e) {
        e.preventDefault();
        var SearchText = $('#search-box').val();
        $.ajax({
            url:'/events?search_filter=' + SearchText,
            type: 'GET',
            success: function(response) {
                console.log(response.data.name)
                //$('.events').html(newHtml.join(''));
                $('#search-box').val('');
            }
        })


    });
    });




