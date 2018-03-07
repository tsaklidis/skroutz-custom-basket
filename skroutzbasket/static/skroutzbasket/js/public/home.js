$(document).ready(function() {

	$( '#add' ).click(function() {

		var csrf =  $('#csrf').val();
		var item_link = $('#link').val();
		$('#link').val('');
		if (item_link) {
			$.ajax({
					url: '/item/add/',
					type: "POST",
				    data: {
				        link : item_link,
				        csrfmiddlewaretoken : csrf
				    },
				    statusCode: {
						206: function(data) {
							// $.each(data, function (id, msg) {

							// });
							ajaxNotRuning=true;
						},
						200: function(data) {

							var price = data.price
							var img = data.img
							var title = data.title
							// var new_item = "<div class='item'><div class='rm' data-price='"+price+"'><i class='fa fa-minus-circle'></i></div><div>"+title+"</div><img src='"+img+"'><div>"+price+"</div></div>"
							var new_item = "<div class='item'><div><a href='"+item_link+"'>"+title+"</a></div><img src='"+img+"'><div>"+price+"</div></div>"
							if (price && title && img) {
								$("#item_list").append(new_item);
								var old_sum = $("#sum").html();
								$("#sum").html(parseFloat(price) + parseFloat(old_sum));
							}

						},
						500: function(data) {
							console.log(data.responseText)
						},
					},
			});
		}
		else{
			$('#link').css({'border':'1px solid #FE5F5F'});
			blink('#link');
		}
	});

	// $( '.rm' ).click(function() {
	// 	var this_price = $(this).attr('data-price');
	// 	this_price = parseFloat(this_price.replace ( /[^\d.]/g, '' ))/100;
	// 	// console.log(this_price);

	// 	var it = $(this).parent('.item');

	// 	$(this).parent('.item').fadeOut(1000, function() { 
	// 		it.remove(); 
	// 		var old_sum = $("#sum").html();
	// 		$("#sum").html(parseFloat(old_sum) - parseFloat(this_price));
	// 	});


	// });
});

function blink(selector){
	$(selector).fadeOut(1000, function(){
	    $(this).fadeIn(1000, function(){

	    });
	});
}