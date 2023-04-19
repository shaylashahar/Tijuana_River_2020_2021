#!/bin/bash
cat ocean.txt | xargs -n 1 -P 2 wget -q
