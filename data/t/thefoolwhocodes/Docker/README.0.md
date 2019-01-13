A Sample application that demonstrates:  
&nbsp;&nbsp;&nbsp;&nbsp;Usage of Bind mounts  
&nbsp;&nbsp;&nbsp;&nbsp;Sample nginx application is used to assist the demonstration  

Command to execute the demonstration:  
&nbsp;&nbsp;&nbsp;&nbsp;docker container run -d --name mynginx -p 80:80 -v $(pwd):/usr/share/nginx/html nginx  
&nbsp;&nbsp;&nbsp;&nbsp;Type http://localhost:80 in your browser and see the content  
&nbsp;&nbsp;&nbsp;&nbsp;Change the content of index file in the current directory  
&nbsp;&nbsp;&nbsp;&nbsp;Again Type http://localhost:80 in your browser and see the modified content.  

Note:  
&nbsp;&nbsp;&nbsp;&nbsp;Due to the bind mount changes made to the current directory will be made visible inside container
