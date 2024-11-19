# Advanced Bio-imaging

## 1. Prerequisites <a name="prerequisites"></a>

The container is based on docker, please [install docker here](https://www.docker.com/get-started). 

## 2. An overview of the dictionary structure for this example <a name="overview"></a>

The main inference processing is executed in the file inference.py. It provides the method json_file_generate(), which creates the detections json file shown in the figures below.

Before generating final output in the form of dictionary which contains all individual detected landmark in each corresponding individual image id (z-coordinate), which are ultimately stored in the file /output/<Image_name>/<model_name>.json.

The output json file is a dictionary and will result as the following format:
```
{
    "Objects": [
        {
            "ID": 1,
            "Type": "rectangle",
            "Name": "IfF_1_T2",
            "Description": "",
            "ShowLabel": true,
            "Length": 4,
            "ObjectType": "T2",
            "Points": [
                {
                    "X": "3,3,83,83",
                    "Y": "85,5,5,85"
                }
            ],
            "Distance": null,
            "x_max": 83,
            "x_min": 3,
            "y_max": 85,
            "y_min": 5,
            "Annotation_image": "",
            "Area": ""
        },
        {
            "ID": 2,
            "Type": "rectangle",
            "Name": "IfF_2_T3",
            "Description": "",
            "ShowLabel": true,
            "Length": 4,
            "DiseaseType": "T3",
            "Points": [
                {
                    "X": "6,6,86,86",
                    "Y": "60,10,10,60"
                }
            ],
            "Distance": null,
            "x_max": 86,
            "x_min": 6,
            "y_max": 60,
            "y_min": 10,
            "Annotation_image": "",
            "Area": ""
        }
    ],
    "index_annotation_img": 2,
    "AI_ROI": []
}
```
*Note that each point is described by the following dictionary: image
