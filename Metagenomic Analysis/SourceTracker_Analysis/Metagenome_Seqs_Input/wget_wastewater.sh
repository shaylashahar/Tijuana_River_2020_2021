#!/bin/bash
cat wastewater.txt | xargs -n 1 -P 2 wget -q
