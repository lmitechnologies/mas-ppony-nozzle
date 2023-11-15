# modify to your data path
input_path=/app/data/OneDrive_1_10-9-2023/sobel

# import the repo paths
source /repos/LMI_AI_Solutions/lmi_ai.env

# extract labels from json
python -m label_utils.via_json_to_csv -d $input_path --output_fname labels.csv

# resize images with labels
# python -m label_utils.resize_with_csv --path_imgs $input_path --out_imsz $W,$H --path_out /app/data/resized

# convert to yolo format
# remote the --seg flag if you want to train a object detection model
python -m label_utils.convert_data_to_yolo --path_imgs $input_path --path_out /app/data/resized_yolo --seg