# Math Stat Package

This repository contains a collection of algorithms and functions related to mathematical statistics. It includes implementations of various control charts along with other statistical tools.

## Installation

You can install the package directly from the GitHub repository using pip:

```bash
git clone https://github.com/SpbskvA/math-stat.git

```
This will install the latest version of the package.

## Control Charts
#### I-MR Chart
The I-MR chart (Individuals and Moving Range) is a type of control chart used to monitor processes where one observation is taken at each time period. It consists of two charts: the Individuals chart (I-chart) and the Moving Range chart (MR-chart). The I-chart is used to monitor individual observations, while the MR-chart is used to monitor the range or difference between consecutive observations.

#### X bar R Chart
The X bar R chart is another type of control chart commonly used in statistical process control. It is used when there are multiple measurements in each subgroup. The X bar chart monitors the process mean, while the R chart monitors the variability within each subgroup by tracking the range between the maximum and minimum values.

#### X bar S Chart
Similar to the X bar R chart, the X bar S chart is used when there are multiple measurements in each subgroup. However, instead of tracking the range, it monitors the standard deviation within each subgroup using the S chart. This chart is particularly useful when the assumption of constant variation within subgroups is violated.

#### CUSUM
Cumulative Sum (CUSUM) is a statistical technique used for monitoring the change in the process mean over time. It is particularly effective in detecting small shifts in the process mean that may not be easily noticeable with traditional control chart methods.

#### EWMA
The Exponentially Weighted Moving Average (EWMA) control chart is a statistical process control tool used to monitor the mean of a process over time. It is particularly effective in detecting small shifts in the process mean, making it suitable for processes where quick detection of changes is crucial.
________
## Usage
Once the package is installed, you can import the control charts and other functions as needed and test it on sample data in math-stat/sampledata.

```python
from pygen_controlcharts import *

# Initialize ControlCharts object
control_charts = imr_x()

# Retrieve all data points for I-MR chart
data, imr = control_charts.allData()

# Retrieve data points for MR chart
mr = control_charts.mrPoints()

# Retrieve data points for I chart
i = control_charts.iPoints()

# Retrieve upper control limit for I chart
ucl_i = control_charts.iLimitUp()

# Retrieve lower control limit for I chart
lcl_i = control_charts.iLimitDown()

# Retrieve upper control limit for MR chart
ucl_mr = control_charts.mrLimitUp()

# Retrieve lower control limit for MR chart
lcl_mr = control_charts.mrLimitDown()
```

- allData(): Returns both the original data points and the data points for the I-MR chart.
- mrPoints(): Returns the data points for the MR chart.
- iPoints(): Returns the data points for the I chart.
- iLimitUp(): Returns the upper control limit for the I chart.
- iLimitDown(): Returns the lower control limit for the I chart.
- mrLimitUp(): Returns the upper control limit for the MR chart.
- mrLimitDown(): Returns the lower control limit for the MR chart.

## Telegram Bot
This package also includes a Telegram bot for generating control charts. After installation, you can interact with the bot by searching for it on Telegram and starting a conversation. You can try it on this [link](https://t.me/genchart_bot).

## Installation via pip
This package can be easily installed using pip, a package manager for Python.
```bash
pip install pygen_controlcharts
```

## Contribution
Contributions to this project are welcome. If you find any issues or have suggestions for improvement, please feel free to open an issue or create a pull request on GitHub.


## License
This project is licensed under the MIT licensed
