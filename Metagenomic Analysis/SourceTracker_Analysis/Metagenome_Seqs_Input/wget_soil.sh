#!/bin/bash
cat soil.txt | xargs -n 1 -P 2 wget -q
