#!/usr/bin/env bash
# Using Bio-Formats via command line
# bftools, convert

if [ $# -eq 0 ]; then
  echo "bioformats.sh <input folder>"
  exit 1
fi

folder=$1
if [ ! -d "$folder" ]; then
  echo "Folder: " $folder "does not exist."
  exit 1
fi

export TMPDIR=/data/shared/tmp

mkdir $folder/converted
for i in $(find $folder -name "*.vsi" -print); do
  echo $i
  fname="$(basename $i)"
  filename="${fname%.*}"
  hresfile="$folder/converted/$filename.tif"
  mresfile="$folder/converted/$filename-multires.tif"
  ./bftools/bfconvert -bigtiff -compression LZW -series 6 $i $hresfile
  vips tiffsave $hresfile $mresfile --xres 0.3472 --yres 0.3472 --compression=lzw --tile --tile-width=256 --tile-height=256 --pyramid --bigtiff
done
