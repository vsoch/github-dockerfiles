## togetherjs搭建教程  

1.websocker服务器：直接运行“hub/server.js可运行websocker服务器，但是注意，需要改主机ip(127.0.0.1)为(0.0.0.0)和端口为本机开放ip可端口(端口映射主机端口和容器端口要一致)，否则连接不上。直接在server.js搜索替换即可;  

2.site服务器：直接运行devserver.js可服务器站点服务，可更改devserver.js内的端口改变其访问端口。  

3.要实现在一个容器里面运行多个服务，需要借助supervisord工具。参考[Docker同时启动多个服务](http://blog.csdn.net/kongxx/article/details/42528423)，可实现。  
___
 
 附：   
 [Togetherjs官网](https://togetherjs.com)     
 [Togetherjs-Github](https://github.com/mozilla/togetherjs)用来搭建服务器   
  
 参考：  
 [使用 Supervisor 来管理进程](http://dockerpool.com/static/books/docker_practice/cases/supervisor.html)    
 [Docker同时启动多个服务](http://blog.csdn.net/kongxx/article/details/42528423)   