  $(document).ready(function(){
  		 $("body").on("click",".selectimg",function(event){ 			
							                                                          
                                    var x = this.src;
                                    var y = getValue();
                                    
                                    var xyz = toolTip();
                                     if(xyz == true)
                                  {                                   
                                    $.ajax({
                                        url: "/searchupdate/",
                                        type: "get",
                                        data: {x:x,foobar:y},                                                
                                        success: function(response) {
                                            $('body').off('.alert.data-api')
                                            $(".current").attr('data-imgsrc',response);          
                                            $('#contentTop').html("<img id = 'currImg' src ='/media/png/"+response+"' >");
                                            //$("#search").click();
                                            console.log(response)
                                        }                                                                    
                
                                    });
                                 }
                                });  				
  				
  					 
                $("#search").click(function(){  
                    $.ajax({
                        url: "/getSearch/",
                        type: "get",
                        data:{search_value: $('#search_field').val() }, 			
                        success: function(response) {
                            var array = jQuery.parseJSON(response) ;
                            var arr = [];
                            for(var i = 0;i< array.length ;i++)      
                            {
                                //arr[i] = array[i].fields.zpicture;
                                arr[i] = array[i].fields.zdirectory_path +"/"+array[i].fields.zfile_name+".png";
                              //  alert(arr[i]);                            
                            }
                            arr = removeDuplicateElement(arr);
                            for(var i = 0;i< arr.length ;i++)                            
                            {
                                $(".carousel-inner").append("<div class = 'item'><a style = 'left:200px;' ><img class = 'selectimg' src ='/media/png/"+arr[i]+"'><a/><div class ='carousel-caption'><p>"+arr[i]+"</p></div></div>");
                                console.log(arr[i])
                             /*  $(".selectimg").click(function(event)
                                { 
                                                          
                                    var x = this.src;
                                    var y = getValue();
                                    
                                    var xyz = toolTip();
                                     if(xyz == true)
                                  {                                   
                                    $.ajax({
                                        url: "/searchupdate/",
                                        type: "get",
                                        data: {x:x,foobar:y},                                                
                                        success: function(response) {
                                            $('body').off('.alert.data-api')
                                            $(".current").attr('data-imgsrc',response);          
                                            $('#contentTop').html("<img id = 'currImg' src ='/media/png/"+response+"' >");
                                            //$("#search").click();
                                            console.log(response)
                                        }                                                                    
                
                                    });
                                 }
                                }); */
                            }
                        }
                    });
                });
            });
            
            
               function removeDuplicateElement(arrayName)
            {
                var newArray=new Array();
                label:for(var i=0; i<arrayName.length;i++ )
                {  
                    for(var j=0; j<newArray.length;j++ )
                    {
                        if(newArray[j]==arrayName[i]) 
                            continue label;
                    }
                    newArray[newArray.length] = arrayName[i];
                }
                return newArray;
            }
