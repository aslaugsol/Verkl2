$(document).ready(function() {
    $('#search-btn').on('click',function (e) {
        e.preventDefault();
        var SearchText = $('#search-box2').val();
        $.ajax({
            url:'/?search_filter=' + SearchText,
            type: 'GET',
            success: function(response) {
                var newHTML = response.data.map(d => {
                    return '<div class="well event">\n' +
                        '    <a href="/events/{d.id}">\n' +
                        '        <img class="event-img" src="${ d.image }">\n' +
                        '        <h4>${ d.name }</h4>\n' +
                        '        <p>${ d.categoryy }</p>\n' +
                        '    </a>\n' +
                        '</div>'
                    $('').html(newHTML.join(''));
                    $('#search-bar').val('');
                })
            },
            error : function (xhr, status, error) {
                console.error(error);
            }
        })


    });
});





