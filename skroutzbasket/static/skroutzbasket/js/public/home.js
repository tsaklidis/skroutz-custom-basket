var all_items = [];

var $_GET = {};
document.location.search.replace(/\??(?:([^=]+)=([^&]*)&?)/g, function () {
    function decode(s) {
        return decodeURIComponent(s.split("+").join(" "));
    }

    $_GET[decode(arguments[1])] = decode(arguments[2]);
});


$(document).ready(function() {
	if ($_GET["token"].length < 17) {
		$('#link').attr('disabled', 'true', 'placeholder',"You can't add new items.");
	}
	$( '#add' ).click(function() {
		var csrf =  $('#csrf').val();
		var item_link = $('#link').val();
		$('#link').val('');
		if (item_link) {
			$('.loading').css({'display':'block'});
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

							var price = parseFloat(data.price)
							var img = data.img
							var title = data.title

							var this_item = {
								'price': price,
								'img': img,
								'title': title,
								'link': data.link,
							}
							// var new_item = "<div class='item'><div class='rm' data-price='"+price+"'><i class='fa fa-minus-circle'></i></div><div>"+title+"</div><img src='"+img+"'><div>"+price+"</div></div>"
							var new_item = "<div class='item'><div><a href='"+item_link+"'>"+title+"</a></div><img src='"+img+"'><div>"+price+"€</div></div>"
							if (price && title && img) {
								$("#item_list").append(new_item);
								var old_sum = parseFloat($("#sum").html());
								console.log(old_sum, price )
								
								$("#sum").html('');
								$("#sum").html(price + old_sum);
							}

							all_items.push(this_item);
							$('.loading').css({'display':'none'});

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

	$( '#share_btn' ).click(function() {
		if (all_items.length > 0) {
			$('#share_mdl').modal('show');
			$('#share_loading').css({'display':'block'});
			$('#token_loading').css({'display':'block'});

			var csrf =  $('#csrf').val();

			var url_token = $_GET["token"];

			var list_name = $('#list_name').val();
			if ((!list_name)) {
				$.ajax({
					url: '/create/list',
					type: "POST",
				    data: {
				        csrfmiddlewaretoken : csrf
				    },
				    statusCode: {
						200: function(data) {
							console.log(data);

							list_name = data.name;
							var the_token = data.token; 
							var url = window.location.href + 'list/' + list_name;
							
							$('#the_link').html(url).attr('href', url);
							$('#share_loading').css({'display':'none'});
							
							var tokened_url = window.location.href + 'list/' + list_name + '?token=' + the_token ;

							$('#the_token_link').html(tokened_url).attr('href', tokened_url);
							$('#token_loading').css({'display':'none'});

							$.each(all_items, function (index, item) {
								save_item(list_name, item, the_token);
							});
						},
						
					},
				});
			}
			else{
				$.each(all_items, function (index, item) {
					save_item(list_name, item, url_token);
				});
			}
		}
		else{
			$('#empty_list').modal('show');
		}

	});
});

function blink(selector){
	$(selector).fadeOut(1000, function(){
	    $(this).fadeIn(1000, function(){

	    });
	});
}

function save_item(list_name, item, l_token){
	var csrf =  $('#csrf').val();

	$.ajax({
		url: '/add/item/to/list',
		type: "POST",
	    data: {
	    	name:list_name,
	    	token: l_token,
	    	price: item.price,
	    	title: item.title,
	    	link: item.link,
	    	image_link: item.img,
	        csrfmiddlewaretoken : csrf
	    },
	    statusCode: {
			200: function(data) {
				console.log(data);
			},
			
		},
	});
}