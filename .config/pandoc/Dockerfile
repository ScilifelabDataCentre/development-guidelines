# Build docker image with pandoc and latex
#
# Need some additional packages to have lato font (SciLifeLab standard font) 
# and for consistency between GitHub and local builds
# better to have here rather than in the GitHub Action
# cspell:ignore tlmgr fontaxes xkeyval updmap
FROM pandoc/latex:3.11

RUN tlmgr update --self && \
    tlmgr install cm-super fontaxes lato xkeyval && \
    updmap-sys

WORKDIR /output

ENTRYPOINT ["/bin/sh", "-c"]
