$(document).ready(function() {
    $('#search-btn').on('click',function (e){
        e.preventDefault();
        var SearchText = $('#search-box').val();
        $.ajax({
            url:'/events?search_filter=' + SearchText,
            type: 'GET',
            success: function(resp){
                var newHtml = resp.data.map(d => {
                    return '<div class="well event"><a href="/events/${d.id}"><img class="event-img" src="${d.firstImage}"/><h4>${d.name}</h4><p>${d.categoryy}</p></a></div>'
                });
                $('.events').html(newHtml.join(''));
                $('#search-box').val('');
            },
            error: function (xhr, status, error){
                console.error(error);
            }
        })


    });
});