# Advanced Bio-imaging
The description of the final project and datasets is described in [rule](https://docs.google.com/presentation/d/1KWdDUJBOFQ-l1_yq7ieJCVcWiquQTDbk/edit?usp=drive_link&ouid=118423424017349178188&rtpof=true&sd=true). 

The introduction of Docker is described in [docker](https://docs.google.com/presentation/d/1HOZIq5sPQXHh3e0X5C21qwqrKF_9VX_T/edit?usp=drive_link&ouid=118423424017349178188&rtpof=true&sd=true).

## Content:
1. [Prerequisites](#prerequisites)
2. [An overview of the dictionary structure for this example](#overview)
3. [Implementing your algorithm into a docker container image](#todocker)
4. [Building your container](#build)
5. [Testing your container](#test)

## 1. Prerequisites <a name="prerequisites"></a>

The container is based on docker, please [install docker here](https://www.docker.com/get-started). 

## 2. An overview of the dictionary structure for this example <a name="overview"></a>

The main inference processing is executed in the file inference.py. It provides the method json_file_generate(), which creates the detections JSON file shown in the figures below.

The output struct will be generated as follows:
```
./output
├── image_1.jpg
│   └── <model_name>.json    
├── image_2.jpg
│   └── <model_name>.json    
│        ⋮
└── image_n.jpg
    └── <model_name>.json    
  
```

The output JSON file will result in the following format:
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
## 3. Implementing your algorithm into a docker container image <a name="todocker"></a>
We recommend you develop and adapt this docker image example to your own detection solution. You can adapt, modify, or build the code from scratch.

If you need a different base image to build your container (e.g., Tensorflow instead of Pytorch, or another AI toolbox), if you need additional libraries and to make sure that all source files (and weights) are copied to the docker container, you will have to adapt the Dockerfile and the requirements.txt file accordingly.

Please refer to the image below (Dockerfile): image
<img width="1299" src="docs/1.png">

## 4. Building your container <a name="build"></a>
To test if all dependencies are met, you should run the file build.bat (Windows) / build.sh (Linux) to build the docker container. Please note that the next step (testing the container) also runs a build, so this step is not mandatory if you are certain that everything is set up correctly.
<img width="1299" src="docs/2.png">

## 5. Testing your container <a name="test"></a>
To test your container, you should run test.bat (on Windows) or test.sh (on Linux, might require sudo privileges). It should create a folder "/output" and then generate the result like the format we mentioned in [An overview of the dictionary structure for this example](#overview).

## 6. Generating the bundle for uploading your algorithm <a name="export"></a>
Finally, you need to run the export.sh (Linux) or export.bat script to package your docker image. This step creates a file with the extension "tar.gz", which you can then upload to moodle2 to submit your algorithm.

