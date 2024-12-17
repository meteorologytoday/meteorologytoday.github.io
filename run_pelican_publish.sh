#!/bin/bash


echo "Remove output directory..."
rm -rf output

echo "Run pelican..."
pelican -s publishconf.py

