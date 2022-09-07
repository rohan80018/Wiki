# <head>
#     <style>
#         #main {
#             margin-top: 20px;
#             margin-left: 30px;
#             margin-right: 5px;
#         }
#         #in {
#             margin-top: 15px;
#         }
#         .inp {
#             width: 1000px;
#             border: 2px solid rgb(37, 125, 240);
#             border-radius: 4px;
    
#         }
#         #describ {
#             height: 200px;
#         }

#         #button {
#             width: 60px;
#             margin-top: 80px;
#             background-color: rgb(37, 125, 240) ;   
#         }
#         #button:hover {
#             border: 2px solid rgb(52, 55, 243);
#             background-color: rgb(52, 55, 243);
    
#         }
#     </style>
# </head>


#     <div id="main">
#         <form action="" method="POST">
#             {% csrf_token %}
#             <div id="in">
#                 <input class="inp" id="title" type="text" placeholder="Enter title...">
#             </div>
#             <div  class="des"  id="in">
#                 <textarea cols="" class="inp"  id="describ" type="text" placeholder="Your entry here..."></textarea>
#             </div>  
#             <div id="save">
#                 <input class="inp" id="button" type="submit" value="Save">      
#             </div>
#         </form>
#     </div>'
    


   
#     <head>
#         <style>
#             #main {
#                 width: 90%;
#                 overflow-x: hidden;
#             }
#             #in {  
#                 margin-top: 20px;
#                 width: auto;
#             }
#             #inp {
                
#                 border: 2px solid rgb(37, 125, 240);
#                 border-radius: 4px;
                
#             }
#             .title {
#                 width: 1005px;
#             }
            
    
#             .button {
#                 margin-top: 60px;
#                 background-color: rgb(37, 125, 240) ;   
#             }
#             .button:hover {
#                 border: 2px solid rgb(52, 55, 243);
#                 background-color: rgb(52, 55, 243);
        
#             }
        
   
#     <h1>New Entry</h1>
#         <div id="main">
#             <form action="" method="POST">
#                 {% csrf_token %}
#                 <div id="in">
#                     <input class="title" id="inp" type="text" placeholder="Enter title..." name="title" />
                    
#                 </div>
#                 <div id="in">
#                     <textarea rows="6" cols="100" id="inp"  type="text" placeholder="Your entry here..." name="content"></textarea>
#                 </div>
                
#                 <div id="save">
#                     <input style="width:80px;" class="button" id="inp" type="submit" value="Save">      
#                 </div>
                
#             </form>
#         </div>
#     {% endblock %}
    