# grasp_dataset_convenience_pack
Corresponding repository to the ICAR 2021 paper 

**_"Automatic Generation of Realistic Training Data for Learning Parallel-jaw Grasping from Synthetic Stereo Images"_**

download paper from the [DLR homepage](https://elib.dlr.de/147156/) (German Aerospace Center),

dowload the data from the [Roboception homepage](https://roboception.com/en/innovation-en/).

If you use the data and/or the code of this repository, please cite 
```tex
@inproceedings{drogemuller2021,
           title = {Automatic Generation of Realistic Training Data for Learning Parallel-jaw Grasping from Synthetic Stereo Images},
          author = {Justus Dr{\"o}gem{\"u}ller and Carlos X. Garcia and Elena Gambaro and Michael Suppa and Jochen Steil and M{\'a}ximo Alejandro Roa Garzon},
       booktitle = {IEEE Int. Conf. Advanced Robotics},
           month = {December},
            year = {2021},
        abstract = {This paper proposes a novel approach to automatically generate labeled training data for predicting parallel-jaw
grasps from stereo-matched depth images. We generate realistic depth images using Semi-Global Matching to compute disparity maps from synthetic data, which allows producing images that mimic the typical artifacts from real stereo matching in our data, thus reducing the gap from simulation to real execution. Our pipeline automatically generates grasp annotations for single or multiple objects on the synthetically rendered scenes, avoiding any manual image pre-processing steps such as inpainting or denoising. The labeled data is then used to train a
CNN-model that predicts parallel-jaw grasps, even in scenarios with large amount of unknown depth values. We further show that scene properties such as the presence of obstacles (a bin, for instance) can be added to our pipeline, and the training process results in grasp prediction success rates of up to 90\%},
             url = {https://elib.dlr.de/147156/},
        keywords = {grasp prediction, grasp learning}
}
```

## Setting up & running
* Developed in virtualenv with Python 3.10
* Run `pip install -r requirements.txt` to install all required packages (OpenCV, PIL, ...)

## Usage
The code provides basic functions to store, manipulate or display single data points from the datasets. 

Coming soon!

## Contribution
Coming soon
