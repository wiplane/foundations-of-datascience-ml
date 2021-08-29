# Foundations for Data Science & ML

The repository contains all the course material(code, slides and notebooks) for the course, [Foundations of DS & ML](https://www.wiplane.com/p/foundations-for-data-science-ml).

## Important links
* Watch the [course intro/outline](https://youtu.be/ZHCFVwq2Dgk)
* Read the motivation for the course(why it is important):  [First Steps to Learning DS/ML](https://www.freecodecamp.org/news/first-steps-to-learn-data-science-or-ml-after-the-roadmap/)
* Want to preview a few lectures? Head over to [course page](https://www.wiplane.com/p/foundations-for-data-science-ml).
* Got questions about the course? Check out the FAQs or reach out to me at [harshit@wiplane.com](harshit@wiplane.com)

## How to set up the code on your machine

* Step 1: Open up the terminal on your machine.
* Step 2: Move to the directory where you want to set up the code.
* Step 3: Paste the following command: `git clone https://github.com/wiplane/foundations-of-datascience-ml.git`
* Step 4: A folder titled `foundations-of-datascience-mlfoundations-of` will be created where all the code resides.
* Step 5: Set up the conda environment using the `.yaml` file or as shown in the first module of the course.
* Start running the notebooks.

## Disclaimer

* A few of the notebooks or slides may be slightly different from what we ended up with in the lectures. Don't bother too much about the changes, I must be trying something new there.
* Slides are added only for the important lectures. Not all lectures included slides
* [WIP]: I am refining the assignments/exercises for a few modules. I've talked about the kind of problems you should try to solve in the outro of a few final lectures, I just need to put it together in writing for you. Should be done very soon.
* If you encounter some error/inconsistency in  my code/explanation, feel free to reach out or comment at the bottom of the lecture.


## What's covered in the course:

### Introduction Module:

* Course Outline: First steps towards learning data science and ML : where will this course take you.
* How to make the most of this course.

### Module 1: Environment setup for coding in python.

* M1V1: Getting started with python: why python, installing python on your system
* M1V2: Installing Miniconda and setting up the new environment
* M1V3: Introduction to Jupyter Notebooks
* M1V4: Google Colabs:Alternative to Jupyter Notebooks

### Module 2: Introduction to python programming for ML

* M2V1: Inspiration: why are we learning programming, what will we be able to do after this.
* M2V2: Variables and data types
* M2V3: Working with variables
* M2V4: Working with string data type
* M2v5: Formatting strings
* M2V6: Introduction to python lists
* M2V7: slicing and sorting lists
* M2V8: Control flow: if/else, conditional blocks, operators.
* M2V9: Loops: how to do something repeatedly
* M2V10: Dictionaries
* M2v11: Iterating over a dict
* M2V12: Comprehensions
* M2V13: Sets & Tuples
* M2V14: Functions
* M2V15: Functions with multiple parameters
* M2V16: Object oriented programming: classes and objects
* M2V17: OOP-2: Instance methods and inheritance
* M2V13: Scripts, Modules and libraries.
* M2V14: how to work with external libraries
* M2V15: Applying functions to iterables
* M2V16: Files I/O.
* M2V17: A tutorial on data extraction from APIs.
* [WIP]: [Guidelines for writing good pythonic code.]

#### Exercises & Assigments

Milestone project #1: **Hands-ON Project:** How to extract data from public APIs.

### Module 3: Introduction to NumPy

* M3V1: Motivation: ML-all numbers, arrays, tensors,  libraries built on top of NumPy.
* M3V2: Intro to NumPy arrays: methods of creation: NumPy Attributes & Data types
* M3v3: Placeholder functions to create numpy arrays
* M3V4: Indexing, Slicing, subsetting
* M3V5: Boolean indexing to mask and filter: part of m3v4: contd...
* M3V6: Performing arithmetic operations on numpy arrays
* M3V7- Reshaping arrays
* M3V8: Transposing, flattening
* M3V9: Stacking arrays
* M3V10: Broadcasting
* M3V11: Pseudorandom data generation
* M3V12: Performing fast vectorized functions
* M3V13: Solving famous equations using NumPy

Programming Assignment: Series expansion: sin(x), cos(x), etc.

### Module 4: Pandas: How to work with real-world data

* M4V1: Pandas Motivation
* M4V2: Introduction to series creation
* M4V3: Introduction to dataframe creation
* M4V4.: Indexing in dataframes
* M4V5: LOC and ILOC methods
* M4V6: Comparison Operators and Filtering — NOTE: change the outro while editing.
* M4V7: Inserting, Modifying, and Deleting data
* M4V8: Merging two dataframes
* M4V9: Merging contd.
* M4V10: Applying arithmetic operations
* M4V11: Mapping and Applying a function to a series
* M4V12: Checking for null values
* M4V13: Grouping data
* M4V14: Describing data using statistical methods
* M4V15: Sorting and ranking data
* M4V16: Data loading from files
* M4V17- Exploratory analysis on a dataframe
* M4v18- EDA part-2: Data Cleaning using Pandas


### Module 5: Data Visualisation with Matplotlib & Seaborn

* M5V1: Motivation: Why data viz?
* M5V2- Matplotlib API heirarchy
* M5V3: Adding color, style and linestyle to plots
* M5V4: Adding labels, ticks and legends to plots
* M5V5: Plotting from dataframe and series
* M5V6: Line plots
* M5V7: Bar plots
* M5V8: Scatter plots
* M5V9: Histograms and KDEs or Density plots
* M5V10: Plotting categorical data using boxplots
* M5V11: Seaborn for beautiful plots
* Introduce the motivation for the project.


### Module 6: Basics of Algebra

* M7V1: Neural Networks and the importance of functions!
* M6V2: Variables + coefficient + equation + constants
* M6V3: Functions
* M6V4: Linear functions
* M6V5: Exponential functions
* M6V6: Coding Exponential and sigmoid functions
* M6V7: Logarithmic functions
* M6V8: Resource on important mathematical notations for ML


### Module 7: Essential Linear Algebra for ML:

* M7V1: Motivation for learning algebra
* M7V2: Introduction to scalars & vectors
* M7V3: Vector arithmetics
* M7V4: Norms
* M7V5: L1 Norm
* M7V6: L2 Norm and Squared L2 Norm
* M7V7: Dot Product
* M7V8: Introduction to matrices & tensors
* M7V9: Common operations on matrices
* M7V10: Matrix multiplication
* M7V11: Special types of matrices
* M7V12: Transforming vector spaces
* M7V13: Linear transformation using matrix notation
* M7V14: Representing linear equations using matrices and vectors
* M7V15: Code Solving systems of linear equations
* M7V16: Introduction to linear regression using the matrix notation
* M7V17: Solving a linear regression problem from scratch

**Assignment Todo** : Create an assignment on solving a real-world problem(dataset) by modeling the relationship between two or more variables using linear regression.

### Module 8: Calculus for ML

* M8V1: Motivation: How does a model train?
* M8V2: Introduction to derivatives and limits
* M8V3: Computing derivatives of linear functions
* M8V4: Computing derivatives of non-linear functions
* M8V5: Derivative rules
* M8V6: Chain rule
* M8V7: Introduction to partial derivatives
* M8V8: Theory behind Gradient Descent
* M8V9: Convexity of functions, local minima and global minima
* M8V10: Math behind linear regression model.
* M8V11: Training the linear regression model using gradient descent from scratch

**Assignment** Train the linear regression model for both *m* and *c* on a real-world dataset.

### Module 9: Descriptive Statistics for Data Science

* M9V1: Motivation to learn statistics: quantifying uncertainty, explain data & ML models
* M9V2: Types of Data
* M9V3: Estimates of location: Mean, median and others
* M9V4: Estimates of Variability: Variance, Std deviation
* M9V5: Introduction to Covariance and Correlation
* M9V6: Random Variables: Discrete and Continuous
* M9V7: Describing discrete variables using probability mass function
* M9V8: Describing continuous variables using probability density function
* M9V9: Introduction to Conditional Probability
* M9V10: Describing data using Cummulative Distribution
* M9V11: Statistical Distributions: Gaussian Distribution
* M9V12: Statistical Distributions: Binomial Distribution
* M9V13: Statistical Distributions: Poisson Distribution
* M9V14: Law of large numbers
* M9V15: Intro to central limit theorem

