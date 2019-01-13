****************************************************************************************************
                                                                                 Contenitore PHP-FPM
****************************************************************************************************
                                                              
versione dockerizzata per  VPS ubuntu 16.04

OBIETTIVO:
  - contenitore per wordpress ed altri applicativi PHP
  - gestione con reverse proxy NGINX


--------------------- Strategia
- test & creazione del contenitore PHP nel dir ~/dockrepo/dockimages/phptest/
- docker-compose.yml & Dockerfile creano le immagini necessarie
- phptest contiene una versione locale dei file di configurazione
- i siti virtuali sono:
    test         contiene file di testo utili a verificare il funzionamento base
    work         per verificare il funzionamento del PHP

DA RICORDARE:

Accesso a phpmyadmin:
    http://work.cloud2run.it:4345/


---------------------------------------------------------------------------------------------------- 2017-11-22
                                                                                             PHP-FPM
----------------------------------------------------------------------------------------------------

Fase 2.-:  creazione immagine: hlite/raspi:php-fpm-002

file di riferimento:
  ~/dockrepo/dockimages/phptest/old.conf/Dockerfile-php-003
  ~/dockrepo/dockimages/phptest/old.conf/docker-compose-008.yml

creazione immagine:
  cd ~/dockrepo/dockimages/phptest
  docker-compose up -d






---------------------------------------------------------------------------------------------------- 2017-05-19
                                                                                             PHP-FPM
----------------------------------------------------------------------------------------------------

Tentativo 1.-:
  ssh yesdock@cloud2run.it
  cd dockrepo/dockimages/phptest/
  docker-compose up -d
==>  sembra funzionare !!


--------- RICHIAMO ------------  INIZIO
In pratica si e' ripristinato il lavoro fatto su hlite.it  (sito hlitetech per sviluppi hlite & syncthing)

Vedi tentativo su hlite.it:
  /var/www/WP/WP-Sviluppi/siti/hlite_it/dockrepo/dockimages/php/README.php

refs.:
  https://www.howtoforge.com/tutorial/dockerizing-wordpress-with-nginx-and-php-fpm/
  http://geekyplatypus.com/making-your-dockerised-php-application-even-better/

strategia:
- prima si cerca di far funzionare la strategia "facile" di geekyplatypus
- poi si aggiusta la configurazione in sites-enabled

--- si parte dal docker-compose di ubu16ngx

==> ha  funzionato SUBITO !

==> in realta' manca l'estensione mysqli, necessaria per wordpress

================> installazione estensioni per wordpress :

==> mettere un dockerfile per aggiungere le estensioni che servono a wordpress
ref. :
  https://github.com/docker-library/wordpress/blob/master/php7.1/fpm/Dockerfile
- modificato il dockerfile per aggiungere SOLO le estensioni e non il wordpress

  ==> sembra funzionare

------ verifica connessione da php a db:
   mysql -u himagetw_hlite -p
   --> pwd: pippolino08
   use himagetw_wp_tech;
   show tables;
==> funziona !!!

NOTA:
  ==> fatti altri aggiustamenti per wordpress, vedi:
         /var/www/WP/WP-Sviluppi/siti/hlite_it/openresty/dockimages/wp-multi/README.wp-multi

--------- RICHIAMO ------------  FINE


cut & paste utili:
  docker-compose exec ubu16ngx bash          <-- per entrare in nginx:

  cat /usr/local/openresty/nginx/html/work/test.txt               <-- ver vedere un file del sito virtuale
  cat /usr/local/openresty/nginx/conf/sites-enabled/work          <-- per vedere la configurazione del sito virtuale "work"
  ls -la /usr/local/openresty/nginx/logs/                         <-- per vedere i log nel container
  cat ~/dockrepo/dockimages/phptest/test.conf/logs/work_error.log     <-- per vedere i log nell'host

===> Funzionamento verificato quando funzionano i link:

  http://work.cloud2run.it/test.txt           file testo che dice dove si trova
  http://work.cloud2run.it/                   home, con un conteggio PHP
  http://work.cloud2run.it/index.php          home, identico a sopra
  http://work.cloud2run.it/index.html         home, file statico di testo (senza PHP)


prossimo passo:

**************************************************************************************************** - 2017-07-05
***********************  Proseguimento sulle immagini "db" & "dbadmin"  ****************************
** vedi il file:                                                                                  **
**        /var/www/WP/WP-Sviluppi/siti/cf-dock/dockrepo/dockimages/db/README.cf-dock_mysql        **
****************************************************************************************************




----------------------------------------------------------------------------------------------------

  docker-compose exec php bash

logs:
  tail -f /home/dockusr/dockrepo/sysdata/nginxdata/logs/work_access.log
  tail -f /home/dockusr/dockrepo/sysdata/nginxdata/logs/error.log

