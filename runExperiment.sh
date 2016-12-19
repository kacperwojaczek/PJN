#!/bin/bash

python generateDataset.py

./vowpal_wabbit/vowpalwabbit/vw movies_dataset -f movies.model --quiet > errorStream

./vowpal_wabbit/vowpalwabbit/vw -i movies.model -t movies_testset -p /dev/stdout --quiet > movies_prediction

python calculateError.py
