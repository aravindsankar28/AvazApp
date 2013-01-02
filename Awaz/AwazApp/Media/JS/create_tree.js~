 $(document).ready(function(){
 					 
              
                $(".lid").on("click",".parent",function(event){   
                    var x= $(this).attr('data-val');
                   
                    $.ajax({
                    		async: false, 
                        url: "/getChildren/"+x+"/",
                        type: "get", 			
                        success: function(response) {
             
                            var y =jQuery.parseJSON(response) ;
                            if($("#"+x).children(':visible').length == 0)
                            { 
                                var check ;
                                if($("#"+x).children(':visible').length == 0)
                                    check = 0;
                                else check = 1;
                                if(check == 0)  
                                {
                                      
                                    $("#"+x).children().show();
                                     //alert( $("#"+x).children('a').attr('title'));
                                 //   alert($(this).attr("title"));
                                     $(".redd").children('.folder').attr("src","/media/Images/minus.gif");
                                    if($("#"+x).children(':visible').length >0)
                                        check = 1;
                                }
                                for (var i = 0;i < y.length; ++i)
                                {
                                	
                                    var a = y[i].fields.ztag_name;
                                  //  console.log(y[i].fields.ztag_name);   
                                    if(check == 0)
                                    {
                                    	 if(y[i].fields.zcategory_or_template == "D")
                                    	 {
                                    	 	if(y[i].fields.zis_enabled == 1)
                                        	$("#"+x).append('<li class ="imgs" data-name = "'+y[i].fields.ztag_name+'" data-imgsrc="'+y[i].fields.zpicture+'" data-val = "'+y[i].pk+'"><a style="cursor:pointer"><b>'+a+'</b></a></li>');
                                        	else
                                        	$("#"+x).append('<li class ="imgs" data-name = "'+y[i].fields.ztag_name+'" data-imgsrc="'+y[i].fields.zpicture+'" data-val = "'+y[i].pk+'"><a style="cursor:pointer" class = "black"><b>'+a+'</b></a></li>');
													 }                                        
                                        else
                                        {
                                        	if(y[i].fields.zis_enabled == 1)
                                        	$("#"+x).append('<li class ="imgs" data-name = "'+y[i].fields.ztag_name+'" data-imgsrc="'+y[i].fields.zpicture+'" data-val = "'+y[i].pk+'"><a style="cursor:pointer">'+a+'</a></li>');
													   else
													   $("#"+x).append('<li class ="imgs" data-name = "'+y[i].fields.ztag_name+'" data-imgsrc="'+y[i].fields.zpicture+'" data-val = "'+y[i].pk+'"><a style="cursor:pointer" class = "black">'+a+'</a></li>');
													 }												
												}                                    
                                    if(y[i].fields.zcategory_or_template == "D" && check == 0)
                                    {
                                       
                                        $("#"+x).append('<a href = "" class="parent" data-val = "'+y[i].pk+'" ><img src="/media/Images/folder.gif"><img src="/media/Images/plus.gif" class = "folder"></a>');	
                                        $("#"+x).append('<ul class="parent" id=  "'+y[i].pk+'"></ul>');	
                                        //$("#folder").attr("src","{{MEDIA_URL}}/Images/minus.gif");
                                    }												
                                }
                                 
                                 
                            }
                            else
                            {
                                
                                $("#"+x).children().hide();
                                $("#content").html("");
                                $(".folder").attr("src","/media/Images/plus.gif");
											$("#contentTop").html("");                               
                                //$("#"+x).css("display","block");
                            } 
                        }
                    });   	 
                    event.preventDefault();   
                });
                $(".lid").on("click",".imgs",function(event){ 	
                	  $('.redd').each(function() {                	  	
						   $(this).removeClass("redd");
                	  	  });
                	  	  
                	  	  $('.current').each(function() {                	  	
						  	 $(".current").removeClass("current");  
                	  	  });				
                	     
                    var x = $(this).attr('data-imgsrc');
                    var y = $(this).attr('data-val');
                    var z = $(this).attr('data-name');
                    $(this).addClass("current");
                    $(this).children('a').addClass("redd");					 				               
                    func(x,y);
                });
            });
