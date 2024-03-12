# Exeter Collage Machine Vision 

Code for the EXE3002 - Classifiers and Machine Vision written assignment

![Rice Image](https://github.com/JWSchaefer/RiceData/blob/main/Jasmine/Jasmine%20(10070).jpg?raw=True)


## Index

- [Overview](#overview)
- [Installation](#installation)
- [Documentation](#documentation)
- [Examples](#examples)
- [Support](#support)

## Overview

This package aims to provide a robust framework within which to demonstrate machine vision skills

It should serve as the starting point the code associated with the machine vision aspect of the EXE3002 Classifiers and Machine Vision written assignment.
## Installation

Requires python $>=$ 3.12



Install the package via `pip` or your favourite package manager

```bash 
$ pip install ecmv
```

When you first import the module you will be asked to download the dataset. The module cannot be used without doing this step.
The dataset is about 205.73 Mb and may take a few minutes to download.

```bash
$ python -c 'import ecmv'
```
```
Rice image dataset not found in PATH_TO_DATASET.
Download it? (Required for the ecmv package to function) [y/n]: y
Cleaning dataset
Cloning into '/Users/joe/Library/Application Support/ecmv'...
remote: Enumerating objects: 74714, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 74714 (delta 0), reused 3 (delta 0), pack-reused 74711
Receiving objects: 100% (74714/74714), 205.73 MiB | 4.76 MiB/s, done.
Resolving deltas: 100% (3/3), done.
Updating files: 100% (75002/75002), done.
```


If any errors are encountered, they should be resolevd automatically. If they persist you can debug them as follows:

1. Set the `ECMV_VERBOSE` environment variable. This will force the programme to output key information relating to the handling of the dataset



    ##### MacOS & Linux
   ```bash
   $ export ECMV_VERBOSE=True
   ```

   ##### Windows
   ```bash
   > set ECMV_VERBOSE=True
   ```

2. Import the `ecmv` package
   ```bash
   $ python -c "import ecmv"
   ```
   ```
   Dataset location: PATH_TO_DATASET
   ...
   ```

3. Remove the directory 
   ##### MacOS & Linux
   ```bash
   $ rmdir -r  PATH_TO_DATASET
   ```
   ##### Windows
   ```bash
   > rd /s PATH_TO_DATASET
   ```





## Documentation

### Structure
```
ecmv
├── features
│   ├── Features 
│   └── get_feature_names
└── extract
    ├── apply_to_dataset 
    └── test
```

### Features Module
#### `features.Features` 

An Enum defining precalculated features



```python
class Features(Enum):
    FName     = 1
    Class     = 2
    Length    = 3
    Width     = 4
    Perimeter = 5
```

**Attributes**

```python
Fname : str
  The jpg file name

Class : str
  The rice species identifier

  A ─> Arborio
  B ─> Basmati
  I ─> Ipsala
  J ─> Jasmine
  K ─> Karacadag

Perimiter : float
  The non-dimensional perimiter of the rice grain. 
  (Normalised by the image size)

Length : float
  The non-dimensional length of the rice grain. 
  (Normalised by the image size)

Width : float
  The non-dimensional width of the rice grain. 
  (Normalised by the image size)
```

#### `features.get_feature_names` 

An getter for the names of the available preclculated features

```python
def get_feature_names() -> list[str]:
    ...
``` 
**Returns**
```python
names : list[str]
  A list of the names of the available preclculated features
```

### Extract Module
#### `extract.generate_dataset`

A function to extract features from the 75,000 images in the [CINAR & KOKLU](https://www.muratkoklu.com/datasets/) rice dataset.

```python
@check_features
def generate_dataset(*features, shuffle = False, seed = 42) -> pd.DataFrame:
    ...
```
**Parameters**
``` python
*features : Callable(str) | Feature
    An array of features to be extracted from each image in the dataset.
    Must be either:
        a) A function f(path) -> float accepting a path to an jpg file
        b) A features.Features enum corrasponding to a precalculated
           feature

shuffle : bool = True
    A boolean to determine if the images are to be shuffled prior to extraction.

seed : int = None
    Ensures a repeatable shuffle if not None.
```
**Returns**
```python
data : pd.Dataframe
    A pandas dataframe where each row contains the features extracted from an image
```
#### `extract.test`

A function to extract features from the a single im age from the [CINAR & KOKLU](https://www.muratkoklu.com/datasets/) rice dataset for testing and development purposes.

```python
@check_features
def test(*features, shuffle = False, seed = 42) -> pd.DataFrame:
    ...
```
**Parameters**
``` python
*features : Callable(str) | Feature
    An array of features to be extracted from each image in the dataset.
    Must be either:
        a) A function f(path) -> float accepting a path to an jpg file
        b) A features.Features enum corrasponding to a precalculated
           feature

shuffle : bool = True
    A boolean to the features shoukld be extracted from a random image

seed : int = None
    Ensures a repeatable shuffle if not None.
```
**Returns**
```python
data : pd.Dataframe
    A pandas dataframe where each row contains the features extracted from an image
```

## Examples

### Example 1 - Function Test

Example testing a function `foo` on a single rice image

**Code** 
```python
# example_test.py

import ecmv

from PIL import Image

from ecmv.features import Features
from matplotlib import pyplot as plt


def foo(path):

    with Image.open(path) as im:
        im.show()

    return 0.0


sample = ecmv.extract.test(
    Features.Class, Features.Length, Features.Width, foo, shuffle=True, seed=42
)

print(sample)
```
**Output**
```bash
$ python example_test.py
  Class    Length     Width  foo
0     I  0.956632  0.482663  0.0
```

![Rice Image](https://github.com/JWSchaefer/RiceData/blob/main/Ipsala/Ipsala%20(9456).jpg?raw=True)

### Example 2 - Function Application

Example extracting the mean red channel value from every rice image

**Code**

```python
# example_dataset.py

import ecmv

import numpy as np
import seaborn as sns

from PIL import Image
from ecmv.features import Features

from matplotlib import pyplot as plt


def mean_red(path):
    with Image.open(path) as im:

        red = im.getchannel("R")

        return np.mean(red)

    return np.NN


df = ecmv.extract.generate_dataset(
    Features.Class,
    Features.Length,
    Features.Width,
    Features.Perimeter,
    mean_red,
)


sns.pairplot(df, hue="Class")
plt.show()
```
**Input**
```bash
$ python example_test.py
```
**Output**
![Pairplot](https://github.com/JWSchaefer/RiceData/blob/main/dist.png?raw=true)

### Example 3 - Classification

An example evaluating the performance of the random forrest classifier using the precalculaed features

**Code**
```python
# example_classify.py

import ecmv

import numpy as np

from ecmv.features import Features

from matplotlib import pyplot as plt

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


df = ecmv.extract.generate_dataset(
    Features.Class, Features.Length, Features.Width, Features.Perimeter
)

y = df["Class"]
X = df[["Length", "Width", "Perimeter"]]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.333, random_state=42
)

classifier = DecisionTreeClassifier(max_depth=2, random_state=42)
classifier.fit(X_train, y_train)

score = classifier.score(X_test, y_test) * 100
print(f"Classifier Score: {score:3.2f}%")
```
**Input**
```bash
$ python example_classify.py
```
**Output**
```
Classifier Score: 75.99%
```

## Support

If you are struggling to use this code, please contact your supervisor.

