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
            });