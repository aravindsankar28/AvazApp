            $(document).ready(function(){                  
            
                $("#editsave").click(function(){
                    var id = getValue();
                    var zname  = $("#ztag_name").attr('value');
                    var audio_data = $("#audio_data").attr('value');
                    var zcolor = $("#selectColor").attr('value');
                    if($("#imageEnable").attr('checked'))
                    	var enable = $("#imageEnable").attr('value');
                    else
                    	var enable =0; 
                  //  alert(zcolor);
                   // alert(audio_data);
                   // alert(enable);
                    $.ajax(
                    {
                        url:'/editsave/',
                        type:'post',
                        data: {zname:zname,zpk:id,audio_data:audio_data,zcolor:zcolor,enable:enable},        		
                        success: function(response) {
                         alert("Saved successfully");
                                                      
                         objs = jQuery.parseJSON(response) ; 
                         var obj = objs[0];
                         var arr =  $('.current').text();
                         if(obj.fields.zcategory_or_template == "T")
                         { 
                         $('.current').html('<a style = "cursor:pointer">'+zname+'</a>');
                         if(obj.fields.zis_enabled == 0)
                         {
                         	$('.current').children('a').addClass('black');
                         	
                         }
                         else
                         	$('.current').children('a').removeClass('black');
                         }          
                         else
                         {
                         	$('.current').html('<a style = "cursor:pointer"><b>'+zname+'</b></a>');   
                           $('.current').children('a').addClass("redd"); 
                           if(obj.fields.zis_enabled == 0) 
                           	$('.current').children('a').addClass('black');
                           else
                           	$('.current').children('a').removeClass('black');
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
				 $(".current").attr('data-imgsrc',"NONE");          
             $('#contentTop').html("Image not available");
			}
			});
		}
		});
	
	});