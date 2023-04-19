#!/bin/bash
cat gut.txt | xargs -n 1 -P 2 wget -q
