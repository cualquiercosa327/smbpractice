#!/bin/bash
ASMFILE=${1:-smb.asm}
BINFILE="${ASMFILE%%.*}.bin"
NESFILE="${ASMFILE%%.*}.nes"

echo "Building ${ASMFILE}"
python badassm/badassm.py "${ASMFILE}" && \
python link.py "${BINFILE}" "${NESFILE}"


