$(document).ready(function() {
    $('#search-btn').on('click',function (e) {
        e.preventDefault();
        const SearchText = $('#search-box1').val();
        $.ajax({
            url:'?search_filter=' + SearchText,
            type: 'GET',
            success: function(response) {
                console.log(SearchText);
                var newHTML = response.data.map(d => {
                    return '<div class="wellEvent">\n' +
                        '    <a href="/events/${d.id}">\n' +
                        '        <img class="event-img" src="${ d.image }">\n' +
                        '        <h4>${ d.name }</h4>\n' +
                        '        <p>${ d.categoryy }</p>\n' +
                        '    </a>\n' +
                        '</div>'
                    $('.events').html(newHTML.join(''));
                    $('#search-box1').val('');
                })
            },
            error : function (xhr, status, error) {
                console.error(error);
            }
        })


    });
});





