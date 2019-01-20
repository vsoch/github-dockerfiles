# perl import built ontop of debian:jessie
FROM perl:5.20

ENV NAME solbase
ENV DEBIAN_FRONTEND=noninteractive

# Copy the current directory contents into the container at /config
ADD ./config/ /config

# Create docker user
RUN useradd -m docker \
	&& echo "docker:docker" | chpasswd \
	&& adduser docker sudo

# Install basic deps
RUN apt-get -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" dist-upgrade \
	&& apt-get update \
	&& apt-get install -y apt-utils gcc build-essential module-assistant sudo nano htop git curl graphviz imagemagick wget

# Core Repos
RUN mkdir /cxgn && cd /cxgn/ \
	&& git clone https://github.com/solgenomics/sgn.git && git clone https://github.com/solgenomics/cxgn-corelibs.git && git clone https://github.com/solgenomics/Phenome.git && git clone https://github.com/solgenomics/biosource.git && git clone https://github.com/solgenomics/Cview.git && git clone https://github.com/solgenomics/ITAG.git && git clone https://github.com/solgenomics/tomato_genome.git && git clone https://github.com/GMOD/Chado.git && git clone https://github.com/solgenomics/sgn-devtools.git && git clone https://github.com/solgenomics/solGS.git && git clone https://github.com/solgenomics/Barcode-Code128.git && git clone https://github.com/solgenomics/Tea.git && git clone https://github.com/solgenomics/art.git && git clone https://github.com/solgenomics/VIGS.git && git clone https://github.com/solgenomics/starmachine.git && git clone https://github.com/solgenomics/cassava.git && git clone https://github.com/solgenomics/yambase.git && git clone https://github.com/solgenomics/sweetpotatobase.git && git clone https://github.com/solgenomics/ricebase.git && git clone https://github.com/solgenomics/citrusgreening.git && git clone https://github.com/solgenomics/coconut.git && git clone https://github.com/solgenomics/cassbase.git && git clone https://github.com/solgenomics/musabase.git && git clone https://github.com/solgenomics/potatobase.git && git clone https://github.com/solgenomics/cea.git

# Install postgres 10
RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main' >> /etc/apt/sources.list.d/postgresql.list
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
RUN apt-get update -y
RUN apt-get install postgresql-10 -y


# Install R
RUN apt-get install apt-transport-https -y \
	&& sed -i "\$adeb https://cran.cnr.berkeley.edu/bin/linux/debian jessie-cran3/" /etc/apt/sources.list \
	&& apt-key adv --keyserver keys.gnupg.net --recv-key 381BA480 \
	&& apt-get -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" dist-upgrade \
	&& apt-get update -y \
	&& apt-get install -y r-base r-base-dev libatlas3-base libcurl4-openssl-dev --force-yes \
    && apt-get install -y libnlopt-dev
# Install R packages
#qtl (>= 1.24-9), gplots (>= 2.10.1), ltm (>= 0.9-7), RColorBrewer (>= 1.0.5), rrBLUP (>= 3.8), plyr (>= 1.7.1), mail(>= 1.0), rjson(>= 0.2.12), agricolae (>= 1.2-1),  gtools (>= 2.6.2), gdata (>= 2.8.2), bitops (>= 1.0-4.1), caTools (>= 1.13), KernSmooth (>= 2.23-7), msm (>= 1.1.1), mvtnorm (>= 0.9.9992), polycor (>= 0.7-8), sfsmisc (>= 1.0-24), nlme (>= 3.1-103), irlba (>= 1.0.3), lme4 (>= 1.1-7), randomForest (>= 4.6-10), data.table (>= 1.9.6)
RUN R -e "install.packages('devtools', dependencies=TRUE, repos='http://cran.rstudio.com/')" \
    && R -e "install.packages('qtl', dependencies=TRUE, repos='http://cran.rstudio.com/')" \
	&& R -e "install.packages('randomForest', dependencies=TRUE, repos='http://cran.rstudio.com/')" \
	&& R -e "install.packages('lme4', dependencies=TRUE, repos='http://cran.rstudio.com/')" \
	&& R -e "install.packages('irlba', dependencies=TRUE, repos='http://cran.rstudio.com/')" \
	&& R -e "install.packages('nlme', dependencies=TRUE, repos='http://cran.rstudio.com/')" \
	&& R -e "install.packages('sfsmisc', dependencies=TRUE, repos='http://cran.rstudio.com/')" \
	&& R -e "install.packages('polycor', dependencies=TRUE, repos='http://cran.rstudio.com/')" \
	&& R -e "install.packages('mvtnorm', dependencies=TRUE, repos='http://cran.rstudio.com/')" \
	&& R -e "install.packages('msm', dependencies=TRUE, repos='http://cran.rstudio.com/')" \
	&& R -e "install.packages('KernSmooth', dependencies=TRUE, repos='http://cran.rstudio.com/')" \
	&& R -e "install.packages('caTools', dependencies=TRUE, repos='http://cran.rstudio.com/')" \
	&& R -e "install.packages('bitops', dependencies=TRUE, repos='http://cran.rstudio.com/')" \
	&& R -e "install.packages('gdata', dependencies=TRUE, repos='http://cran.rstudio.com/')" \
	&& R -e "install.packages('gtools', dependencies=TRUE, repos='http://cran.rstudio.com/')" \
	&& R -e "install.packages('rjson', dependencies=TRUE, repos='http://cran.rstudio.com/')" \
	&& R -e "install.packages('mail', dependencies=TRUE, repos='http://cran.rstudio.com/')" \
	&& R -e "install.packages('plyr', dependencies=TRUE, repos='http://cran.rstudio.com/')" \
	&& R -e "install.packages('rrBLUP', dependencies=TRUE, repos='http://cran.rstudio.com/')" \
	&& R -e "install.packages('RColorBrewer', dependencies=TRUE, repos='http://cran.rstudio.com/')" \
	&& R -e "install.packages('ltm', dependencies=TRUE, repos='http://cran.rstudio.com/')" \
	&& R -e "install.packages('gplots', dependencies=TRUE, repos='http://cran.rstudio.com/')" \
	&& R -e "install.packages('data.table', dependencies=TRUE, repos='http://cran.rstudio.com/')" \
	&& R -e "install.packages('agricolae', dependencies=TRUE, repos='http://cran.rstudio.com/')" \
	&& R -e "install.packages('d3heatmap', dependencies=TRUE, repos='http://cran.rstudio.com/')" \
	&& R -e "install.packages('tidyr', dependencies=TRUE, repos='http://cran.rstudio.com/')" \
	&& R -e "install.packages('ggplot2', dependencies=TRUE, repos='http://cran.rstudio.com/')" \
    && R -e "install.packages('bioconductor', dependencies=TRUE, repos='http://cran.rstudio.com/')" \
    && R -e "install.packages('caret', dependencies=TRUE, repos='http://cran.rstudio.com/')" \
    && R -e "install.packages('R.oo', dependencies=TRUE, repos='http://cran.rstudio.com/')" \
    && R -e 'source("http://bioconductor.org/biocLite.R");biocLite();biocLite("gdsfmt");biocLite("SNPRelate")' \
    && R -e 'library("devtools");install_github("cran/R.methodsS3");install_github("solgenomics/rPackages/genoDataFilter");install_github("solgenomics/rPackages/phenoAnalysis");install_github("reyzaguirre/st4gi")'
    

# Install Legacy NCBI Blast
RUN cd /cxgn/ \
	&& mkdir blast \
	&& cd /cxgn/blast/ \
	&& wget http://ftp.gen-info.osaka-u.ac.jp/pub/biosoft/blast/executables/release/2.2.9/blast-2.2.9-amd64-linux.tar.gz \
	&& tar zxvpf blast-2.2.9-amd64-linux.tar.gz \
	&& rm blast-2.2.9-amd64-linux.tar.gz
ENV PATH $PATH:/cxgn/blast/
# RUN apt-get install ncbi-blast+ -y #latest relaese of BLAST

# Install Slurm
RUN apt-get install -y libmunge-dev libmunge2 munge slurm-wlm slurmctld slurmd libslurm-perl \
	&& touch /etc/slurm-llnl/slurm.conf \
	&& cat /config/slurm.conf >> /etc/slurm-llnl/slurm.conf \
	&& chmod 777 /var/spool/ \
	&& mkdir /var/spool/slurmstate \
	&& chown slurm:slurm /var/spool/slurmstate/ \
	&& /usr/sbin/create-munge-key \
	&& ln -s /var/lib/slurm-llnl /var/lib/slurm

RUN systemctl enable munge.service
RUN systemctl enable slurmctld.service
RUN systemctl enable slurmd.service

# Install perl modules
RUN mkdir /cxgn/local-lib
RUN curl -L https://cpanmin.us | perl - --sudo App::cpanminus \
	&& apt-get install -y libgd2-xpm-dev libcairo2-dev libpq-dev libxml-libxml-perl \
	&& cpanm install -L /cxgn/local-lib/ local::lib Catalyst::ScriptRunner Catalyst::Restarter HTML::Mason::Interp Selenium::Remote::Driver DBI Hash::Merge DBIx::Connector Catalyst::Plugin::Authorization::Roles Bio::PrimarySeq Class::DBI Tie::UrlEncoder Data::BitMask enum File::NFSLock Class::MethodMaker Bio::BLAST::Database Catalyst::Plugin::SmartURI Modern::Perl List::Compare Cache::File Config::JFDI CatalystX::GlobalContext --force DBIx::Class::Schema Bio::Chado::Schema Array::Utils JSON::Any Math::Round Math::Round::Var Catalyst::View::Email Catalyst::View::HTML::Mason Catalyst::View::Bio::SeqIO Catalyst::View::JavaScript::Minifier::XS@2.101001 Catalyst::View::Download::CSV URI::FromHash JSAN::ServerSide Config::INI::Reader Bio::GFF3::LowLevel Statistics::Descriptive String::Random MooseX::FollowPBP GD Tie::Function Digest::Crc32 Barcode::Code128 Math::Base36 Captcha::reCAPTCHA Test::Aggregate::Nested --force HTML::FormFu SVG IPC::Run3 Spreadsheet::WriteExcel MooseX::Object::Pluggable R::YapRI::Base PDF::Create String::CRC Algorithm::Combinatorics Catalyst::Controller::HTML::FormFu String::Approx Cairo Chart::Clicker Spreadsheet::ParseExcel MooseX::Types::URI Bio::Graphics::FeatureFile --force Mail::Sendmail Array::Compare GD::Graph::lines GD::Graph::Map Bio::GMOD::GenericGenePage Number::Bytes::Human AnyEvent --force IO::Event --force File::Flock Graph Bio::SeqFeature::Annotated XML::Twig XML::Generator DBD::Pg MooseX::Runnable XML::Feed Parse::Deb::Control Bio::GMOD::Blast::Graph Catalyst::DispatchType::Regex DateTime::Format::Flexible DateTime::Format::Pg HTML::TreeBuilder::XPath JSON::XS Lingua::EN::Inflect List::AllUtils MooseX::Declare MooseX::Singleton SOAP::Transport::HTTP Test::Class WWW::Mechanize::TreeBuilder Data::UUID HTML::Lint --force Test::JSON Test::MockObject Test::WWW::Selenium Sort::Versions Term::ReadKey --force Spreadsheet::Read Sort::Maker Term::Size::Any Proc::ProcessTable URI::Encode Archive::Zip Statistics::R Lucy::Simple DBIx::Class::Schema::Loader Text::CSV Imager::QRCode GD::Barcode::QRcode LWP::UserAgent Set::Product Server::Starter Net::Server::SS::PreFork --force Catalyst::Plugin::Assets --force PDF::API2 CAM::PDF

RUN mkdir /export && mkdir /export/prod && mkdir /export/prod/public && mkdir /export/prod/public/sgn_static_content && mkdir /export/prod/tmp && mkdir /export/prod/tmp/solgs && mkdir /data && mkdir /data/prod && mkdir /data/prod/archive && mkdir /export/prod/public/images && mkdir /export/prod/public/images/image_files && mkdir /data/shared && mkdir /data/shared/tmp && mkdir /var/log/solbase && chown -R www-data:www-data /data/prod/ && chown -R www-data:www-data /export/prod/ && mkdir /etc/starmachine

RUN cp /config/starmachine.conf /etc/starmachine
RUN cp /config/sgn_loc.conf /cxgn/sgn

# Jbrowse setup
RUN mkdir /var/www && cd /var/www/ && mkdir jbrowse && cd /var/www/jbrowse/ && curl -O http://jbrowse.org/releases/JBrowse-1.12.1.zip && unzip JBrowse-1.12.1.zip && rm JBrowse-1.12.1.zip && cd /var/www/jbrowse/JBrowse-1.12.1/ && ./setup.sh

#ADD PATH
ENV PATH $PATH:/cxgn/local-lib/bin

#Add Perl paths
ENV PERL5LIB $PERL5LIB:/cxgn/local-lib/bin:/cxgn/local-lib/lib:/cxgn/local-lib/lib/perl5:/cxgn/local-lib:/usr/local/lib/x86_64-linux-gnu/perl/5.20.2:/usr/local/share/perl/5.20.2:/cxgn/sgn/lib:/cxgn/cxgn-corelibs/lib:/cxgn/Phenome/lib:/cxgn/Cview/lib:/cxgn/ITAG/lib:/cxgn/biosource/lib:/cxgn/tomato_genome/lib:/cxgn/Barcode-Code128/lib:/cxgn/solGS/lib:/cxgn/Chado/chado/lib:/cxgn/Tea/lib:/cxgn/Tea

# Make port 3000 available to the world outside this container
EXPOSE 3000

# Set the working directory to sgn
WORKDIR /cxgn/sgn/

#Register starmachine init as a service
RUN ln -s /cxgn/starmachine/bin/starmachine_init.d /etc/init.d/sgn
RUN mv /cxgn/sgn/sgn_loc.conf /cxgn/sgn/sgn_local.conf

CMD sed -i s/peer/trust/ /etc/postgresql/10/main/pg_hba.conf \
    && service postgresql restart \
    && yes web_usr | createuser -U postgres -P web_usr \
    && echo "ALTER ROLE postgres WITH PASSWORD 'postgres';" | psql -U postgres \
    && service postgresql restart \
    && createdb -U postgres -E UTF8 -T template0 fixture \
    && psql -U postgres -d fixture -f /cxgn/sgn/t/data/fixture/cxgn_fixture.sql \
    && mkdir /tmp/www-data \
    && mkdir /tmp/www-data/SGN-site \
    && service munge start \
    && service slurmctld start \
    && service slurmd start \
    && service sgn start \
    && chown -R www-data:www-data /tmp/www-data/SGN-site \
    && while true; do sleep 1000; done
