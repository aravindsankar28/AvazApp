            $(document).ready(function(){                  
            
                $("#editsave").click(function(){
                    var id = getValue();
                    $.ajax(
                    {
                        url:'/editsave/',
                        type:'post',
                        data: {zname:$("#ztag_name").attr('value'),zpk:id},        		
                        success: function(response) {
                            alert("Saved successfully");
                            
                            //alert($(".current").attr('data-val')); 
                         var zname  =   $("#ztag_name").attr('value'); 
                         var arr =  $('.current').text();
                         if(response == "T") 
                         $('.current').html('<a style = "cursor:pointer">'+zname+'</a>');          
                         else
                         {
                         	$('.current').html('<a style = "cursor:pointer"><b>'+zname+'</b></a>');   
                           $('.current').children('a').addClass("redd");  
                         }                               
                           
                        }			
                    });
                });
            });            $(document).ready(function(){                  
            
                $("#editsave").click(function(){
                    var id = getValue();
                    $.ajax(
                    {
                        url:'/editsave/',
                        type:'post',
                        data: {zname:$("#ztag_name").attr('value'),zpk:id},        		
                        success: function(response) {
                            alert("Saved successfully");
                            
                            //alert($(".current").attr('data-val')); 
                         var zname  =   $("#ztag_name").attr('value'); 
                         var arr =  $('.current').text();
                         if(response == "T") 
                         $('.current').html('<a style = "cursor:pointer">'+zname+'</a>');          
                         else
                         {
                         	$('.current').html('<a style = "cursor:pointer"><b>'+zname+'</b></a>');   
                           $('.current').children('a').addClass("redd");  
                         }                               
                           
                        }			
                    });
                });
            });
            
             $(document).ready(function(){
                $(".lid").on("click","a",function(event){                               	 
                    $('.redd').each(function() {     
                            	  	
                        $(this).removeClass("redd");
                    });  
                  
                    $('.current').each(function() {                	  	
                        $(this).removeClass("current");
                    });
                          	 	 	
                    $(this).addClass("redd");                    
                    $(this).addClass('current');
                   
                });  
                 
              
            });
$(document).ready(function(){
	
	$("#clearImage").click(function(){
		var zpk = getValue();
		var abcd = deleteTip();
		if(abcd == true)
		{
		$.ajax({
			url:'/clearImage/',
			data:{zpk:zpk},
			type:'get',
			success: function(response) {
				alert(response);
				 $(".current").attr('data-imgsrc',null);          
             $('#contentTop').html("Image not available");
			}
			});
		}
		});
	
	});