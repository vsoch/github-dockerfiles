****************************************************************************************************
                                                                         Contenitore MySQL - MARIADB
****************************************************************************************************
                                                              
versione dockerizzata per  VPS ubuntu 16.04

OBIETTIVO:
  - contenitore per mysql
  - gestione con phpmyadmin   <-- come si installa?


--------------------- Strategia
- operazioni effettuate dopo la creazione e test del PHP - vedi phptest:
    /var/www/WP/WP-Sviluppi/siti/cf-dock/dockrepo/dockimages/phptest/README.phptest
- si crea qui il db iniziale, conroot & user temporanei



---------------------------------------------------------------------------------------------------- 2017-07-07
                                                                               installazione MARIADB

ripreso da hlite.it
vedi sotto:  *** STORIA ***


-----------------------------------------------------  Creazione immagine con solo i dati di sistema

Da fare UNA SOLA VOLTA per creare l'immagine  hlite/raspi:db-002
  - creazione dell'immagine di sistema del DB
  - root con password pre-definita:  rootPWD
  - db SENZA utenti
  - dati nel dir ~/dockrepo/sysdata/db

esecuzione:
  - con   docker-compose.yml == docker-compose-db-010.yml:
    docker-compose up

                                                      ---------------------------------------------- 2017-11-20
                                                                             Aggiornamento procedura

/var/www/WP/WP-Sviluppi/siti/cf-dock/dockrepo/dockimages/db/Dockerfile-MariaDB-012

/var/www/WP/WP-Sviluppi/siti/cf-dock/dockrepo/dockimages/db/docker-compose-db-004.yml

AIUTO!!! non si compila !!!   <--   fare il pull dell'immagine ufficiale (SENZA Dockerfile !!!)     <==== DA PROVARE !!!

PROVA 2:
----> si parte da mariadb ufficiale
--> corretto docker-compose-db-005.yml con file === mariadb ufficiale rinominato in hlite/raspi:mariadb

  docker-compose -f docker-compose-db-005.yml up -d

test esistenza db:
    docker-compose -f docker-compose-db-005.yml exec db bash
    mysqladmin -u root -p version
    ==> rispondere "rootpwd" per la password (== NO PASSWORD)         <-- pwd root iniziale: rootpwd
    ==> mariadb risponde con la versione ..
======>  OK per questo step

cambio password:
    mysqladmin -u root -p                                                  <== pwd iniziale: rootpwd
    SET PASSWORD FOR 'root'@'localhost' = PASSWORD('2017StefMarcFran');    <==  NEW ROOT PWD
--> teoricamente e' ok
--> ripartire e provare:
    docker-compose exec db bash
      mysql -u root -p
=======>  nuova password per root installata
    
Per ottenere il xx.tar.gz essendo in ~/dockrepo:
   sudo tar -zcvf mariadb-iniz.tar.gz ~/dockrepo/sysdata/db
   sudo chown yesdock:yesdock mariadb-iniz.tar.gz

Per ripristinare la pwd iniziale (rootpwd)
   SET PASSWORD FOR 'root'@'localhost' = PASSWORD('rootpwd');



                                                      ---------------------------------------------- 2017-11-22
                                                                                test applicazione db

test db running:
    docker-compose -f hliteapps.yml exec db bash
    mysql -u root -p2017StefMarcFran                                         <== pwd in chiaro !!!  *** da EVITARE in produzione ***

Per un ottenere un backup: 
   cd ~/dockrepo:
   sudo tar -zcvf db_backup.tar.gz ~/dockrepo/sysdata/db
   sudo chown yesdock:yesdock db_backup.tar.gz

Per cambiare la pwd di root:
   SET PASSWORD FOR 'root'@'localhost' = PASSWORD('rootpwd');             rootpwd <== nuova password





####################################################################################################
                                                                                    CREATE SWAP FILE
vedi:
  https://www.digitalocean.com/community/tutorials/how-to-add-swap-space-on-ubuntu-16-04

NOTA:  Serve per la compilazione di MARIADB che ha bisogno di almeno un GB
       ------- VA CANCELLATA quando non serve perche' danneggia il disco SSD  --------
       ----------------- NON FARE PERMANENTE sara' cancellata al reboot --------------

per confermare che non e' attiva:
    sudo swapon --show
ritorna lista vuota, confermare con:
    free -h
creazione:
    sudo fallocate -l 1G /swapfile
    ls -lh /swapfile
NON FATTO chmod per la security, verra' cancellato piu' avanti
Abilitazione:
    sudo mkswap /swapfile
    sudo swapon /swapfile
    sudo swapon --show

si riprende la compilazione
    docker-compose build
    --> Successfully built 44986df35f70
        --> hlite/raspi:db-002-base
eseguendo:
    docker-compose build
manca: docker-entrypoint.sh
si prende il file da:
  --> https://github.com/docker-library/mariadb/blob/fc9e999ca57555c0669cfc67906f0c705bda7e41/docker-entrypoint.sh
    sudo chown yesdock:yesdock docker-entrypoint.sh
    sudo chmod +x docker-entrypoint.sh
    docker-compose build

####################################################################################################

si riprende con:
    docker-compose up
==> ha funzionato al secondo tentativo, dopo anche un reboot

test esistenza db:
    docker-compose exec db bash
    mysqladmin -u root -p version
    ==> premere "enter" per la password (== NO PASSWORD)
    ==> mariadb risponde con la versione ..

======>  OK per questo step

Aggiustare la root pwd:
    docker-compose exec db bash
                                       systemctl stop mariadb
    mysql -u root                   <-- accesso SENZA password, ok se risponde ...
    SET PASSWORD FOR 'root'@'localhost' = PASSWORD('2017StefMarcFran');                                 <==  NEW ROOT PWD
--> teoricamente e' ok
--> ripartire e provare:
    docker-compose exec db bash
      mysql -u root -p
=======>  nuova password per root installata




prossimo passo:

**************************************************************************************************** - 2017-07-05
***************************  Proseguimento sulla immagine "dbadmin"  *******************************
** vedi il file:                                                                                  **
**  /var/www/WP/WP-Sviluppi/siti/cf-dock/dockrepo/dockimages/dbadmin/README.cf-dock_phpmyadmin    **
****************************************************************************************************



#
#  NOTE:
#    - imporre una procedura per far cambiare la root pwd                                    DA FARE
#    - creare un utente base                                                                 DA FARE
#
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  vedi sopra:    Aggiustare la root pwd:



----------------------------------------------------------------------------------------------------  SONO QUI
----------------------------------------------------------------------------------------------------  SONO QUI







====================================================================================================
===================================================================================== *** STORIA ***
====================================================================================================


---------------------------------------------------------------------------------------------------- 2017-07-07
                                                                       Storico: SVILUPPO su hlite.it
                                                                                       inizia da qui


---------------------------------------------------------------------------------------------------- 2017-05-19
                                                                                             MARIADB
----------------------------------------------------------------------------------------------------

ref.:
  https://blog.shameerc.com/2016/08/my-docker-setup-ubuntu-php7-fpm-nginx-and-mariadb

Strategia: 
- costruire la prima immagine del DB nel dir dockimages
  --> appoggiare i file sull'host
- usare il compose in sysprogs per il deploy normale

- inizializzazione db:
  - dockerfile per costruire l'immagine hlite/raspi:db-001
  - definire root con pwd + dbuser/pwduser (per ora potente ~== root)
      ref.:  https://hub.docker.com/_/mariadb/
-----------------------
  - inizializzare un db X wordpress                                                                 <--  NON FATTO
                  root password  -->  :'}#43?;}hW<9!8IMt{$6"6qF
                   wordpress db  -->  fih025_db                      | Database Name      (per WP)
                 wordpress_user  -->  toyota899fe                    | Database User      (per WP)
                  user password  -->  ]S=T^ZZ+*`}ubky21)/@4WVQ{      | Database Password  (per WP)
    --> versione definitiva :
          MYSQL_ROOT_PASSWORD=:'}#43?;}hW<9!8IMt{$6"6qF
          MYSQL_DATABASE=fih025_db
          MYSQL_USER=toyota899fe
          MYSQL_PASSWORD=]S=T^ZZ+*`}ubky21)/@4WVQ{
------------------------
- 1.o tentativo:
    --> versione di test :
          MYSQL_ROOT_PASSWORD=rootpwd
          MYSQL_DATABASE=fih025_db
          MYSQL_USER=toyota899fe
          MYSQL_PASSWORD=userpwd

  ref.:
    https://www.howtoforge.com/tutorial/dockerizing-wordpress-with-nginx-and-php-fpm/
  - seguito esempio:
      docker-compose exec db bash
      mysql -u root -p
      --> pwd: 

- Per cambiare la password:
  ref: https://www.tecmint.com/change-mysql-mariadb-root-password/
  - seguito esempio:
      USE mysql;
      UPDATE user SET password=PASSWORD('rootpwd') WHERE User='root' AND Host = 'localhost';
      FLUSH PRIVILEGES;
      exit;

- Per cambiare la password di un utente:
  ref: https://mariadb.com/kb/en/mariadb/set-password/
  - seguito esempio:
      mysql -u root -p
      --> pwd: 
      USE mysql;
      SET PASSWORD FOR 'toyota899fe' = PASSWORD('userpwd');
      FLUSH PRIVILEGES;
      exit;
  - verifica:
      mysql -u toyota899fe -p
      use fih025_db;
      show tables;
      exit;



----------------------------------------------------------------------------------------------------
                                                                    **** altre cose DA VEDERE:  ****

tutorials <fai l'immagine 'a mano'>:  --------------------
  http://amattn.com/p/installing_maria_db_mysql_with_docker.html

  https://mariadb.com/kb/en/mariadb/installing-and-using-mariadb-via-docker/
    --> utile suggerimento per installare dentro docker, vedi la sezione:
          "Daemonizing the operating system"
      --> il repo ubuntu xenial supporta mariadb 10.0

  https://linoxide.com/containers/setup-use-mariadb-docker-container/

digital ocean ---
  https://www.digitalocean.com/community/tutorials/how-to-install-wordpress-and-phpmyadmin-with-docker-compose-on-ubuntu-14-04

****************************************************************************************************
                                                                              Contenitore PHPMYADMIN
****************************************************************************************************
                                                              
versione dockerizzata per  VPS ubuntu 16.04

OBIETTIVO:
  - contenitore phpmyadmin per mariadb  (Export del lavoro fatto su hlite.it)


---------------------------------------------------------------------------------------------------- 2017-05-19
                                                                                      DB  &  DBADMIN
----------------------------------------------------------------------------------------------------


--------------------- Strategia
- operazioni effettuate dopo la creazione del db iniziale:
    /var/www/WP/WP-Sviluppi/siti/cf-dock/dockrepo/dockimages/db/README.cf-dock_mysql
- si installa phpmyadmin, seguendo la *** STORIA *** sotto ...                                      <====   SI CAMBIA !!!
                                                                                                   
====> si installa come normale programma PHP                                                        <===  IN CORSO


Patch necessaria:
- aggiustare l'accesso da "remoto" sul contenitore db, altrimenti phpmyadmin non accede
- vedi:    https://mariadb.com/kb/en/mariadb/configuring-mariadb-for-remote-client-access/
    docker-compose up -d           <-- start application in dbadmin
    docker-compose exec db bash
    mysql -u root -p
    SELECT User, Host FROM mysql.user;
    GRANT ALL PRIVILEGES ON *.* TO 'root'@'172.%' IDENTIFIED BY '2017StefMarcFran' WITH GRANT OPTION;
  --> ora phpmyadmin vede il server "db", per lui "remoto"


----------------------------------------------------------------------------------------------------
                                                                                 AUTHENTICATION GATE
AUTHENTICATION GATE
reference:
  https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-phpmyadmin-with-nginx-on-a-centos-7-server
    --> paragrafo:  Setting up a Web Server Authentication Gate

scopo: proteggere un direttorio con la richiesta standard di pwd dal browser
       solo dopo entrati si vede la richiesta standard delle credenziali phpmyadmin
         --> in sostanza e' una password doppia

strategia:
  - si crea un sito apposito per phpmyadmin, denominato "work2do.cloud2run.it"
  - si rinomina il phpmyadmin  --->   workdafare
  - si protegge il direttorio "workdafare" con una nuova pwd
      --> l'attaccante vede il prompt phpmyadmin solo se indovina la prima password

---------------
==> aggiustato site-available
==> aggiustato dir "workdafare"
==> creato il file /usr/local/openresty/nginx/conf/pma_pass
    --> vedi il tutorial sopra:
    nano /usr/local/openresty/nginx/conf/pma_pass

===============> test OK

----------------------------------------------------------------------------------------------------


---------------------------------------------------------------------------------  Nuova strategia - (OK il 2017-12-12)

Ref.:
  https://serverfault.com/questions/851282/nginx-location-blocks-dont-apply-to-php-files-inside-them/851285
  
====>  dopo MOLTI tentativi si e' trovata una strategia che funziona, con qualche glitch iniziale
       --> restituisce il file .php invece di eseguirlo, al secondo tentativo funziona !!


--> installato AUTHENTICATION GATE           <-- vedi sopra



-------------------------------------------------------- cut & paste utili per phpmyadmin

  docker-compose -f ~/dockrepo/hlite-apps.yml exec dbadmin ash

  aggiorna configurazione nginx

      docker-compose -f ~/dockrepo/hlite-base.yml exec nginx bash
      /usr/local/openresty/nginx/sbin/nginx -t
      /usr/local/openresty/nginx/sbin/nginx -s reload


  docker-compose -f ~/dockrepo/hlite-apps.yml exec dbadmin ash            <-- NOTABENE:  "ash"    







DA FARE @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  sono qui










============================================================================================????????
vedi:  /var/www/WP/WP-Sviluppi/siti/hlite_it/dockrepo/dockimages/dbadmin/README.phpmyadmin

-backup del multisite su hlite.it / hlitetech.com

---> ripristinio del multisite  @@@@@@@@@@@@@@@@@@<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<






====================================================================================================
===================================================================================   *** STORIA ***
====================================================================================================


---------------------------------------------------------------------------------------------------- 2017-05-19
                                                                                      DB  &  DBADMIN
----------------------------------------------------------------------------------------------------

Export del lavoro fatto su hlite.it



---------------------------------------------------------------------------------------------------- 2017-07-05
                                                                       Storico: SVILUPPO su hlite.it
                                                                                       inizia da qui


---------------------------------------------------------------------------------------------------- 2017-05-21
                                                                                          PHPMYADMIN
----------------------------------------------------------------------------------------------------

ref.:
  https://www.digitalocean.com/community/tutorials/how-to-install-wordpress-and-phpmyadmin-with-docker-compose-on-ubuntu-14-04

- si usa l'immagine:  phpmyadmin/phpmyadmin    (corbinu/docker-phpmyadmin e' ora deprecato)
- si usano, come porte non standard, quelle nel range 4344..4350  ora aperte sul cloud firewall
  --> per phpmyadmin si usa la porta 4345
- si aggiorna opportunamente il file docker-compose.yml

==>  funziona subito !!!

NOTA: per entrare nel container :

    docker-compose exec dbadmin ash            <-- NOTABENE:  "ash"


   ref.:    https://github.com/laradock/laradock/issues/480


advanced config ref.:
  https://docs.phpmyadmin.net/en/latest/setup.html#installing-using-docker




GRANT ALL PRIVILEGES ON *.* TO 'root'@'172.%' IDENTIFIED BY '2017StefMarcFran' WITH GRANT OPTION;




phpmyadmin:
    image: phpmyadmin/phpmyadmin
    container_name: phpmyadmin
    environment:
     - PMA_ARBITRARY=1
    restart: always
    ports:
     - 8080:80
    volumes:
- /sessions


