$(document).ready(function(){            
                $(".carousel").carousel({                   
                });

            });
            
$(document).ready(function(){   
                $("#create").click(function(){
	 					 
                    var parentID = getValue();
              
                    $.ajax({
	  
                        url:'/create/',
                        type:'post',
                        data:{select:$("select").attr('value'),parentid:parentID},
	  
                        success: function(response) {
                            $('.current').trigger('click'); 
                            alert(response);      
                            console.log(response)                  
                            var y =jQuery.parseJSON(response) ;
                            
                            alert("Created !!");
                            alert(y[0].pk);
                            var a = y[0].fields.ztag_name;
                            //  alert(y[0].fields.zcategory_or_template);
                            if(y[0].fields.zcategory_or_template  ==  "T" && y[1].fields.zcategory_or_template  ==  "T" )
                            {
                                $('<li class ="imgs" data-name = "'+y[0].fields.ztag_name+'" data-imgsrc="'+y[0].fields.zpicture+'" data-val = "'+y[0].pk+'"><a style="cursor:pointer">'+a+'</a></li>').insertAfter(".current");
                            }
                            else if(y[0].fields.zcategory_or_template  ==  "T" && y[1].fields.zcategory_or_template  ==  "D" )
                            {
                                $("#"+y[1].pk).prepend('<li class ="imgs" data-name = "'+y[0].fields.ztag_name+'" data-imgsrc="'+y[0].fields.zpicture+'" data-val = "'+y[0].pk+'"><a style="cursor:pointer">'+a+'</a></li></ul>');
																	
                            }                          	 
                            else if(y[0].fields.zcategory_or_template  ==  "D" && y[1].fields.zcategory_or_template  ==  "T" )
                            {
                                alert("Category");                                                    	                           	                         	 
                                $('<li class ="imgs" data-name = "'+y[0].fields.ztag_name+'" data-imgsrc="'+y[0].fields.zpicture+'" data-val = "'+y[0].pk+'"><a style="cursor:pointer"><b>'+a+'</b></a></li><a href = "" class="parent" data-val = "'+y[0].pk+'" ><img src="/media/Images/folder.gif"><img src="/media/Images/plus.gif" id = "folder"></a><ul class="parent" id=  "'+y[0].pk+'"></ul>').insertAfter('.current');
									                      	                          	 
                            }
                            else
                            {
                                alert("Category"); 
                                $("#"+y[1].pk).prepend('<li class ="imgs" data-name = "'+y[0].fields.ztag_name+'" data-imgsrc="'+y[0].fields.zpicture+'" data-val = "'+y[0].pk+'"><a style="cursor:pointer"><b>'+a+'</b></a></li><a href = "" class="parent" data-val = "'+y[0].pk+'" ><img src="/media/Images/folder.gif"><img src="/media/Images/plus.gif" id = "folder"></a><ul class="parent" id=  "'+y[0].pk+'"></ul>');
                            }
                        }
			
                    });
	 
                });
	  
            });
