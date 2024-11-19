import random
import numpy
from PIL import Image
import os
import torch
import json
SaveDirectory = os.path.abspath(os.path.dirname(__file__))
def run():
    x = [[1, 3, 5, 80, 80],
         [2, 6, 10, 80, 50]]
    
    json_file_generate(x, 'model', 'testimg', 1024,1024)
    return 0

def json_file_generate(prediction, model_name, image_name, image_height, image_width):
    
    '''
    The prediction outcome should storage class in 0, x in 1, y in 2, bounding box width in 3, and bounding box height in 4, for example:
    [1, 20, 48, 100, 100]
    
    '''
    object_type_map = {0: "T1", 1: "T2", 2: "T3", 3: "T4", 4: "T5", 5: "T6", 6: "T7"}
    # print(prediction)
    # exit()
    height, width = image_height, image_width
    
    objects = []
    for idx, line in enumerate(prediction):
        parts = line
        if len(parts) < 5:
            continue

        # the classify outcomes, should be a numbers.
        class_pred = int(parts[0])
                
        # the height and weight of the detected bounding box.
        box_width = parts[3]
        box_height = parts[4]
        
        # top left coordinates
        x_min = parts[1]
        y_min = parts[2]
        
        # bottom right coordinates
        x_max = x_min + box_width
        y_max = y_min + box_height

        # Define points in clockwise order for the rectangle
        points = {
            "X": f"{x_min},{x_min},{x_max},{x_max}",
            "Y": f"{y_max},{y_min},{y_min},{y_max}"
        }

        # Create the object in JSON format
        object = {
            "ID": idx + 1,
            "Type": "rectangle",
            "Name": f"IfF_{idx + 1}_{object_type_map[class_pred]}",
            "Description": "",
            "ShowLabel": True,
            "Length": 4,
            "objectType": object_type_map[class_pred],
            "Points": [points],
            "Distance": None,
            "x_max": x_max,
            "x_min": x_min,
            "y_max": y_max,
            "y_min": y_min,
            "object_image": "",
            "Area": ""
        }
        objects.append(object)

    # Create JSON structure
    json_data = {
        "objects": objects,
        "index_object_img": len(objects),
        "AI_ROI": []
    }

    json_subfolder = os.path.join(SaveDirectory, 'output/', image_name + '.jpg')
    os.makedirs(json_subfolder, exist_ok=True)
    json_output_path = os.path.join(json_subfolder, model_name + ".json")

    with open(json_output_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)
    
    print(SaveDirectory)
    print(f"Saved JSON for {image_name}.jpg to {SaveDirectory}/{json_output_path}")
    

if __name__ == "__main__":
    raise SystemExit(run())
