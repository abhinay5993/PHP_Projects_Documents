Steps to Setup the Project
==========================
1) Download Wamp Server
2) Extract OnlineExamProjects.rar you will be able to see 2 projects into it . Take Anyone of it for yor refarence.
3) Take any of the project and go to C: Drive --> www folder created after instlling wamp.
4) inside each of the project folder you will be able to see .sql file which contains your back-end structures soo please import this file into PHP MyAdmin localhost portal.
5) Sample project documentation also for your project you need to modify it. But this is one of the standard project doc templet.

NOTE :
========
For First time while we are going to configure projects DB with PHP-MyAdmin :
1) from wamp Server navigate to - http://localhost/phpmyadmin/
2) from there pass .sql file name in this case it will be "onlineexam" Create new database keep as "collection" and then click "Create"
3) From http://localhost/phpmyadmin/ home page click on "Import"
4) From Import page "Location of the text file" section browse your "onlineexam.sql" from project root folder which kept into under "C:\wamp\www" location.
5) Select this as "Format of imported file" as NONE and then Click on Go button.
6) The entire DB schema of onlineexam project will get imported with designed tables/reations.

Thanks,
Abhinay
