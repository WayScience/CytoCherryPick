#!/bin/bash

# call the main.py file with the following arguments to be parsed
python Utils/main.py --file_path "data/test_data_output.csv" \
    --feature_name "B" \
    --image_name "image_2" \
    --median "True" \
    --histogram "False" \
    --bins 25

