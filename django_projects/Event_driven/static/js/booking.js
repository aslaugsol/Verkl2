//$(document).ready(function() {
    //$('.BookEventBtn').click(function (e) {
            //e.preventDefault();
            //const event_id = $('.event_id').val();
            //const ticket_qty = $('.qty-input').val();
            //var token = $('input[name=csrfmiddlewaretoken]').val();
            //$.ajax({
            //        method: "POST",
            //        url: "/book-tickets/" + event_id ,
              //      data: {
                //        'event_id': event_id,
                  //      'ticket_qty': ticket_qty,
                    //    csrfmiddlewaretoken: token
                    //},
                    //success: function (response) {
                      //  console.log(response)
                       // alert.success(response.status)
                   // }
                //}
           // )
        //}
    //)
//});

var Bookingbtn = document.getElementsByClassName('BookEventBtn')
for (i = 0; i < Bookingbtn.length ; i++){
    Bookingbtn[i].addEventListener('click', function (){
        var eventID = this.dataset.event
        var action = this.dataset.action
        console.log('EventId: ' , eventID , 'Action: ', action)

        console.log('USER:', user)
        if(user === 'AnonymousUser'){
            console.log('Not logged in!')
        }else{
            console.log('User is logged in, sending data')
        }
    })
}