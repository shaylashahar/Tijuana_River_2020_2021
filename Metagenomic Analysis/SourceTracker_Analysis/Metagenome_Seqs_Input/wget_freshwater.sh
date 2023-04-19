#!/bin/bash
cat freshwater.txt | xargs -n 1 -P 2 wget -q

