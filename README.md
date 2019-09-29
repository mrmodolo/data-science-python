# Getting started with data science using Python

Doing data science with Python offers limitless potential for you to parse, interpret, and structure data in meaningful and enlightening ways.

Data science is an exciting new field in computing that's built around analyzing, visualizing, correlating, and interpreting the boundless amounts of information our computers are collecting about the world. Of course, calling it a "new" field is a little disingenuous because the discipline is a derivative of statistics, data analysis, and plain old obsessive scientific observation.

But data science is a formalized branch of these disciplines, with processes and tools all its own, and it can be broadly applied across disciplines (such as visual effects) that had never produced big dumps of unmanageable data before. Data science is a new opportunity to take a fresh look at data from oceanography, meteorology, geography, cartography, biology, medicine and health, and entertainment industries and gain a better understanding of patterns, influences, and causality.

Like other big and seemingly all-inclusive fields, it can be intimidating to know where to start exploring data science. There are a lot of resources out there to help data scientists use their favorite programming languages to accomplish their goals, and that includes one of the most popular programming languages out there: Python. Using the Pandas, Matplotlib, and Seaborn libraries, you can learn the basic toolset of data science.

If you're not familiar with the basics of Python yet, read my introduction to Python before continuing.

## Creating a Python virtual environment

Programmers sometimes forget which libraries they have installed on their development machine, and this can lead them to ship code that worked on their computer but fails on all others for lack of a library. Python has a system designed to avoid this manner of unpleasant surprise: the virtual environment. A virtual environment intentionally ignores all the Python libraries you have installed, effectively forcing you to begin development with nothing more than stock Python.

To activate a virtual environment with venv, invent a name for your environment (I'll use example) and create it with:


```bash
$ #
$ # python3 -m venv example
$ mkdir ~/Aprendendo/data-science/python
$ cd ~/Aprendendo/data-science/python
$ pipenv install
```

Source the activate file in the environment's bin directory to activate it:


```bash
$ # source ./example/bin/activate
$ pipenv shell
```

You are now "in" your virtual environment, a clean slate where you can build custom solutions to problems—with the added burden of consciously needing to install required libraries.

## Installing Pandas and NumPy

The first libraries you must install in your new environment are Pandas and NumPy. These libraries are common in data science, so this won't be the last time you'll install them. They're also not the only libraries you'll ever need in data science, but they're a good start.

Pandas is an open source, BSD-licensed library that makes it easy to process data structures for analysis. It depends on NumPy, a scientific library that provides multi-dimensional arrays, linear algebra, Fourier transforms, and much more. Install both using **pipenv**:

```bash
$ pipenv install pandas
```
Installing Pandas also installs NumPy, so you don't need to specify both. Once you have installed them to your virtual environment once, the installation packages are cached so that when you install them again, you don't have to download them from the internet.

Those are the only libraries you need for now. Next, you need some sample data.

## Generating a sample dataset
Data science is all about data, and luckily there are lots of free and open datasets available from scientific, computing, and government organizations. While these datasets are a great resource for education, they have a lot more data than necessary for this simple example. You can create a sample and manageable dataset quickly with Python:

```python
#!/usr/bin/env python3

import random

def rgb():
    return random.randint(0,255)/255

with open ('sample.csv', 'w') as csv:
    csv.write('"red","green","blue"')
    for count in range(10):
        csv.write('\n{:0.2f},{:0.2f},{:0.2f}'.format(rgb(),rgb(),rgb()))
```

