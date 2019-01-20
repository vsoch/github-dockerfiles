FROM insighttoolkit/itksoftwareguide-src as itksoftwareguide-itk

RUN mkdir /ITKSoftwareGuide-build
WORKDIR /ITKSoftwareGuide-build
ARG ITK_GIT_TAG
ENV CCACHE_CPP2=true
RUN cmake \
  -GNinja \
  -DITKSoftwareGuide_SUPERBUILD:BOOL=ON \
  -DCMAKE_CXX_COMPILER_LAUNCHER:STRING=ccache \
  -DCMAKE_C_COMPILER_LAUNCHER:STRING=ccache \
  '-DCMAKE_JOB_POOLS:STRING=compile=10;link=2' \
  -DCMAKE_JOB_POOL_COMPILE:STRING=compile \
  -DCMAKE_JOB_POOL_LINK:STRING=link \
  -DGENERATE_HTML:BOOL=ON \
  -DITK_GIT_TAG:STRING=${ITK_GIT_TAG} \
  -DCMAKE_BUILD_TYPE:STRING=MinSizeRel \
     /ITKSoftwareGuide
RUN ninja -v RunExamples
# Additional run because of dependency issues?
RUN ninja -v RunExamples
