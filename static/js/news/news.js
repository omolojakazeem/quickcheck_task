const user_input = $(".search_bar");
const content_div = $('#replaceable_content');
const delay_by_in_ms = 400;
let scheduled_function = false;
const endpoint = $("#replaceable_content").attr("data-filter-url");

$(document).ready(function(){


    let ajax_call = function (endpoint, search_parameter) {
	    $.getJSON(endpoint, search_parameter)
		    .done(response => {
			    // fade out the artists_div, then:
			    content_div.fadeTo('slow', 0).promise().then(() => {
                    // replace the HTML contents
                    content_div.html(response["html_from_view"])
                    // fade-in the div with new contents
                    content_div.fadeTo('slow', 1)
			    })
		    })
        }

    user_input.on('keyup', function () {
        console.log("ASA")
        const search_parameter = {
            q: $(this).val(), //value of user_input: the HTML element with ID user-input
        }

        if (scheduled_function) {
            clearTimeout(scheduled_function)
        }
	    scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, search_parameter);
    });
});

function timeConverter(UNIX_timestamp){
  var a = new Date(UNIX_timestamp * 1000);
  var months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  var year = a.getFullYear();
  var month = months[a.getMonth()];
  var date = a.getDate();
  var hour = a.getHours();
  var min = a.getMinutes();
  var sec = a.getSeconds();
  var time = date + ' ' + month + ' ' + year + ' ' + hour + ':' + min + ':' + sec ;
  return time;
}
console.log(timeConverter(0));
