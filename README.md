# hip-tensorflow
Hawkes Intensity Process Inspired by [Expecting to be HIP: Hawkes Intensity Processes for Social Media Popularity](https://arxiv.org/abs/1602.06033) Implemented in TensorFlow.

![](images/formula.png)
# Installation 
Run the following snippet to install `hip` in a Mac/Unix environment.

``` 
git clone https://github.com/kasrsf/hip-tensorflow.git
cd hip-tensorflow
pip install -e . #install in editable mode  
```

To verify successful installation, the following command should run from the command line without any errors:
```
python -c "import hip"
```

# Usage

### Single Feature Analysis
 To run the feature analysis with the hawkes model, run the following command:
 ```
 python hip_feature_analysis.py [input_dir] [feature_index]
 ```

the script will train the HIP model using all the csv files in `input_dir` with a single exogenous source `feature_index` and output a tab-seperated table containing the learned values.

# Example

```
> python hip_feature_analysis.py data/sample_data_2 2

eta    mu    theta
0.20671242    1.3099899    13.408139
```

# Requirements

* Python 3.5

The code may work with other versions of Python but this is not tested.