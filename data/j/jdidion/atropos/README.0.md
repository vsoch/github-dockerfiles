# Manuscript

The peer-reviewed manuscript is

> Didion JP, Martin M, Collins FS. (2017) Atropos: specific, sensitive, and speedy trimming of sequencing reads. PeerJ 5:e3720 https://doi.org/10.7717/peerj.3720

See the [manuscript folder](manuscript/README.md) for details on how the manuscript was created.

The version of Atropos used in the peer-reviewed manuscript can be found at: https://github.com/jdidion/atropos/releases/tag/1.1.5. Note that additional tools have been added, tool versions (including Atropos) have been updated, and the workflow has been modified since publication. These changes will eventually be refelected in an updated preprint on BioRxiv.

# Overview

The scripts in this directory will enable you to re-run the analyses in the Atropos paper. The workflows defined here run the benchmarks and generate the figures and tables shown in the paper.

We have created [Docker](https://www.docker.com/) images for all of the software tools used, as well as data volumes containing all the raw data and resources. These images can be used directly on Mac, Windows, and some linux platforms using the Docker engine. On unsupported linux platforms (namely RedHat and derivatives, such as Scientific Linux), [Singularity](http://singularity.lbl.gov/) or [Udocker](https://github.com/indigo-dc/udocker) can be used to execute the containers directly from Docker Hub. The versions of the tools used in the paper are noted in the Dockerfile headers, and also in the supplementary data.

Our workflows are written in [Nextflow](https://www.nextflow.io/index.html), primarily because it supports Docker, Singularity, and Udocker, which we need to run benchmarks on both desktop and RedHat-based HPC cluster. We also provide [CWL](http://www.commonwl.org/) tool definitions to simplify the development of alternate workflows.

Each workflow (.nf file) runs the analysis for one data type (RNA-Seq, WGBS, or simulated DNA-Seq). We provide a configuration file with profiles we used for both the local and cluster executions. Our cluster runs SGE, so you may need to alter the cluster configuration files for your environment.

# 1. Install software

* You will need a [Docker](https://www.docker.com/) engine if you want to build the containers yourself. If you only want to run the containers, you can use either Docker, [Singularity](http://singularity.lbl.gov/), or [Udocker](https://github.com/indigo-dc/udocker).
* [Nextflow](https://www.nextflow.io/index.html), which requires Java 7+.

# 2. Build containers

All of the containers defined in the 'containers' subdirectory have already been built and pushed to Docker Hub, with two exceptions: the data containers for the STAR indexes (data/hg37/star-index and data/hg38/star-index) are too large to be pushed to Docker Hub or Quay.io. Thus, you will unfortunately need to build at least one of them yourself. We use GRCh38 in the paper, so to build that container, clone data/hg38/star-index and run the build.sh script in that directory.

First, the default Docker repository size (32G) is too small to build the star index containers, so you need to increase the repository size. This requires that you're running the [Docker "Edge" build](https://store.docker.com/editions/community/docker-ce-desktop-mac). Now increase the disk size following the instructions [here](https://forums.docker.com/t/increase-docker-container-disk-space-on-os-x/26725/2).

For full reproducibility, you are free to build the containers yourself, but you'll need to create your own account on Docker Hub, and you'll need to update the scripts to push/pull containers from your own repository. Build all the tool containers, then build all the data containers.

In general, for each tool container, run the following sequence of commands:

    # Build the container
    docker build -f Dockerfile -t <your repo>/<tool name> .
    
    # Upload the container to your Docker Hub repo
    docker push <your repo>/<tool name>

For each data container, run the following sequence of commands:

    # Download the data and build the docker container
    ./build.sh
    
    # Upload the container to your Docker Hub repo
    docker push <your repo>/<data name>

Note that you can create a .tar archive of any container using the `docker save` command, and you can load a saved container using the `docker load` command. This is especially useful for the star index container(s).

On a technical note, we use Phusion (https://hub.docker.com/r/phusion/baseimage/) as the base image for the containers for the tools we benchmark. This is primarily for convenience and comparability (i.e. removing base image as a variable); you could build smaller images using Alpine with a little extra work.

# 3. Run the workflows

Clone the files in the 'workflow' directory, including the 'bin' subdirectory. In the 'workflow' directory, first edit the nextflow.config file and customize it to your own computing environment.

On our cluster, we run the scripts from a subdirectory under /scratch. At runtime, /scratch is replaced with /spin1/scratch, hence the beforeScript command to cd back to /scratch to avoid confusing Nextflow.

If you are running Docker, you'll likely need to increase the number of CPUs and memory limit to match what you've configured. This can be found in the Docker preferences on the "Advanced" tab.

Now run:

    ./run-workflows.sh <env>

Where <env> is either 'local' or 'cluster'. Note that the first time you run this it will download several Docker images requiring ~[XX] GB of disk space.

All results will be placed in the 'results' subdirectory (unless you change the path in nextflow.config).

Note that when re-running the workflow and comparing the results to those shown in the manuscript, there will be some variability in the performance metrics, but the relative rankings of the tools should not change significantly -- please let us know if you find otherwise!

# Non-Docker Systems

Unfortunately, the ideals of easily reproducible research don't yet match up with reality. Ideally, if you wanted to run this workflow on a system that doesn't support Docker (which includes any RedHat-based Linux system and most HPC environments), you could use transparently use Singularity. In reality, Nextflow doesn't support Singularity's ability to automatically pull and convert images from a Docker Hub. Nor would you want it to; Singularity does not use a daemon or other caching system, and would thus fetch a separate copy of every image for every process instance. This will be addressed in Singularity v2.3, but for now you need to manually convert all the Docker images to Singularity images on a computer running Docker, then copy them to the HPC environment. We expect, but can't guarantee, that this had minimal effect on the measurement of relative performance between the desktop and cluster.

## 1. Fix docker2singularity bug and build container

First you need to clone the docker2singularity repository (https://github.com/singularityware/docker2singularity) and edit the docker2singularity.sh file to change the 'if' statement on/around line 178 to:

```
buildname=$(head -n 1 /etc/issue)
if [[ $buildname =~ Buildroot|Alpine ]] ; then
```

Now build the container:

```
docker build -f Dockerfile -t <docker2singulariy container_name> .
```

## 2. Convert and transfer images

Make sure you've manually built the star index container as described in #2 above, and that it shows up when you run 

```
docker images
```

From the 'containers' directory, run:

```
./docker2singularity.sh \
  <docker2singulariy container_name> <remote host> <remote dir>
```

# TODO

* Update #3 with an estimate of the total disk space requirement.
* Use [docker-builder](https://pypi.python.org/pypi/docker_builder) to auto-update containers when dependencies change.
* Look at using TopHat2 or Kallisto pseudo-alignment rather than STAR for RNA-Seq benchmarks. This would enable the RNA-Seq benchmark to be run on our desktop with 32 GB RAM.
* These papers do a nice job of benchmarking trimmers. Consider adding some more benchmarks.
    * http://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-16-S1-S2
    * https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-015-0454-y
* Make machine info work on OSX (currently requires /proc/cpuinfo and /proc/meminfo)This directory contains all the containers used in the Atropos paper. There are two types of containers:

* Data: Minimal base container (busybox) with no software installed. Each container houses a single dataset.
* Tools: Phusion base container with software required by the analysis. Containers are designed such that each Nextflow process uses a single container.
# Data containers

These are containers for the raw data and resources used in the Atropos paper. All containers are based on Busybox for the greatest space efficiency. Each folder has a build.sh script, which downloads the data and builds the image based on the Dockerfile in the same directory.

* hg37 and hg38
    * reference: Reference sequence and GENCODE v26 gene annotations.
    * bwa-index: BWA index, using jdidion/bwabase as a baseimage.
    * bwameth-index: bwa-meth index, using jdidion/bwabase as a base image.
    * star-index: STAR index, using jdidion/starbase as a base image.
* simulated, rna, wgbs: benchmark datasets used in Atropos paper
These are the tool containers for the Atropos paper.

* adapter-removal: [AdapterRemoval2](https://github.com/MikkelSchubert/adapterremoval) v2.2.2, 
* art: A [modified](https://sourceforge.net/projects/skewer/files/Simulator/) version of the [Art](https://www.niehs.nih.gov/research/resources/software/biostatistics/art/) simulator v1.5.1 that adds adapters to simulated reads.
* atropos-paper-analysis: Contains tools to support the analyisis scripts; [BedOps](https://bedops.readthedocs.io/en/latest/) v2.4.26 and [SRA tools](https://github.com/ncbi/sra-tools) v2.8.2.
* atropos-paper: The version of Atropos used in the paper.
* bwa: [BWA](https://github.com/lh3/bwa) v0.7.7, [bwa-meth](https://github.com/brentp/bwa-meth) v0.1.c0 and [samtools](http://www.htslib.org/) v1.7.
* python-bash: Python 3.6 and many libraries for analysis and visualization (pandas, matplotlib, seaborn).
* seqpurge: [ngs-bits](https://github.com/imgag/ngs-bits) v0.1, which contains SeqPurge.
* skewer: [Skewer](https://github.com/relipmoc/skewer) v0.2.2.
* star: [STAR](https://github.com/alexdobin/STAR) v2.5.4b.
* fastp: [fastp](https://github.com/OpenGene/fastp) v0.12.3
* cutadapt: [Cutadapt](https://github.com/marcelm/cutadapt) v1.16# bwa and bwa-meth Docker images

We build two Docker images that provide the bwa aligner and the bwa mem-based bisulfite aligner, bwa-meth. The first image is a base image containing the software. The second image uses the base image to build the indexes and include them.
# STAR Docker images

We build two Docker images that provide the STAR aligner. The first image is a base image containing the software. The second image uses the base image to build the indexes and include them.
# Atropos Manuscript

The manuscript was written using [Overleaf](https://www.overleaf.com). Upon publication 1) we will publicly share a read-only view of the manuscript on Overleaf, and 2) a copy of the final latex document will be copied into this folder.

To go from the generated figures/tables in 'workflow/results' to the final figures/tables in the manuscript, we tweaked the aesthetics of some figures using Illustrator and converted to PDF, and we reformatted some tables by hand-editing the latex; the data was left exactly as-is. 

We used Pandoc to generate the .DOCX file for submission to PeerJ. Some hand-editing of the .DOCX file was done to comply with the PeerJ submission requirements:

* Remove financial information from Acknowledgements
* Make equations editable
* Show line numbers

In the supplement, the MultiQC screenshot was generated manually based on one of the simulated FASTQ files (sim_01.1.fq).