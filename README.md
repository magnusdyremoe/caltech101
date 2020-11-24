# Caltech101
Note to self: Input following line in VM PuTTy: jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser &

Image classificiation on data set caltech101.

### This repo consists of 5 notebooks, model weights, model histories and scripts to visualize the data. ###

The 5 notebooks are:
* One notebook to unzip a folder in jupyter notebook virtual machine.
* Two notebooks for a 6 layer CNN with and without augmented data as input. These notebooks are identical, apart from data pre-processing.
* Two notebooks using transfer learning with a pre-trained VGG16 model with and without augmented data as input. These notebooks are identical, apart from data pre-processing.


The 4 notebooks with CNN models contains:
* Data pre-processing.
* The respective models with training and prediction. Also containing plots for top-1 accuracy, top-5 accuracy and loss for the training history.
* A detailed classification report yielding precision, recall and f1-score for all classes in the dataset.


### Step by step guide to replicate this project. ###

1. Download the Caltech101 dataset from kaggle here https://www.kaggle.com/athota1/caltech101 .
2. Within the Caltech101 folder assign a folder named *train* containing all images in the dataset. Assign two empty folders - *val* and *test*. The folder structure should look like this:
```bash
101_ObjectCategories
├── train
│   ├── accordion
│   ├── airplanes
│   ├── ...
│   └── yin_yang
├── val
│   └── *empty*
└── test
    └── *empty*
```
3. Run *split_train_validation_test.py* on your local machine. The images should now be distibuted 75% to training, 15% to validation and 10% to testing. Your folder structure should now look like the following:
```bash
101_ObjectCategories
├── train
│   ├── accordion
│   ├── airplanes
│   ├── ...
│   └── yin_yang
├── val
│   ├── accordion
│   ├── airplanes
│   ├── ...
│   └── yin_yang
└── test
    ├── accordion
    ├── airplanes
    ├── ...
    └── yin_yang
```
4. Now zip 101_ObjectCategories and name it 101_ObjectCategories_test.
5. Sign up to Google cloud console.
6. Create a virtual machine. Tutorial from https://www.youtube.com/watch?v=Db4FfhXDYS8&ab_channel=JinayShah
7. Start the virtual machine as described in the guide.
8. Upload the zipped data and the notebooks.
9. Run the unzip notebook to unzip the data. The data is now ready to use.
10. Run either one of the notebooks.
11. Alternatively, if you do not want to train the network, upload the model weights and the model histories and run the 6layer CNN notebooks from the cell where stored data is loaded to create a reconstructed model. This will require zipping the folders and unzipping them in jupyter notebook, similar to the image folders.

NB: The model weight for the modified VGG16 networks are not included in the repo. These weight files are roughly 500 MB which far exceeds Githubs limit of 100 MB per file.