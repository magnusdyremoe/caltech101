# caltech101
Image classificiation on data set caltech101

Data set caltech101 is split into 101 different classes. Run split_train_test.py to generate train, validation and test set. This requires one folder named train, containt all images, one empty folder named val and one folder named test.
The caltech101 data set can be found at https://www.kaggle.com/athota1/caltech101 .

Virtual machine made to run on Google cloud. For tutorial on how to run the vm follow this link: https://www.youtube.com/watch?v=Db4FfhXDYS8&ab_channel=JinayShah .

Input following line in VM PuTTy: jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser &

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
3. Run *split_test_train.py* on your local machine. The images should now be distibuted 75% to training, 15% to validation and 10% to testing. Your folder structure should now look like the following:
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
4. Now zip 101_ObjectCategories.
5. Sign up to Google cloud console.
6. Create a virtual machine. Tutorial from https://www.youtube.com/watch?v=Db4FfhXDYS8&ab_channel=JinayShah
7. Open the jupyter notebook and upload the zipped data.
8. Run either one of the notebooks.