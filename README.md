
# Extracting the Impact on Real Estate Sale Prices Following a Hurricane.
This project represents a collaboration between General Assembly and New Light Technologies.

## Problem Statement:

During a disaster, it is important to model and estimate the potential or forecasted effect of the event, including the projected/forecasted damage.
Existing indicators of forecasted damage include number of structures within the affected area, number of people in the area, number of households, demographics of the impacted population, etc.
This project will add an additional persepctive: It will compare how hurricanes do or do not impact median sale prices by zip code before and after the storm.

## Executive Summary

Foo Bar
foo bar
 
## Goal:
- Our team aims to provide an initial proof of concept for a potential web application using Flask software for Python. This rudimentary web application will allow the user to input a zip code and see summary statistics for how median real estate prices were affected before and after a recent hurricane. 

## Limitations
- For this project we only used the top ~6000 zip codes by population, not the entire ~41000 exhaustive list of zip codes.
- This initial proof focues solely on the recent hurricanes of Sandy 2012, Harvey 2017, and Dorian 2019.
- Our focus for this project was financial impact on zip code aggregated median sale prices sourced largely from Zillow.com.
- This project does not consider nominal or indirect economic costs in isolation, it focuses solely the ultimate impact (or not) on actual median sale prices for a zip code.

## Software/APIs/Libraries Used:

#### * Python
- Pandas
- Numpy
- Matplotlib: Pyplot
- Seaborn
- Missingno
- Flask: Flask, request, render_template, session, redirect, url_for
- Sys

#### Other:
- Tableau Public
- Atom Script Editor (For Flask, HTML, CSS)

<ol> Imports UPDATE </ol>

## Data Dictionary UPDATE THIS
```
| Column | Description |
| --- | --- |
| **Zip** | Zip Code. |
| **Pop Rank** | Ordinal ppoulation size. 1 is the largest populated zip code, 2 is the second largest. |
| **X Mean Median** | The median sale price for the nation averaged by zip code for the year. |
| **X Affected** | 1 if the zipcode was impacted by Hurricane X according to FEMA, 0 otherwise. |
| **% Change After X** | Percentage difference in median zip sale price comparing the month preceding the storm to the month following the storm.|
| **Harvey Category** | The numerical categorical severity declaration from FEMA, 0-5 with 5 being the highest. |
 
```
 

## Features
 
* Enter a zip code to see the summary statistics<br> 
* Home Page of Flask App <br>
![Flask Home Page](./visuals/flask_home.png)

* Results Page of Flask App<br>
![Flask Home Page](./visuals/flask_results.png)
 

## Sources/Citation



## Contact Info

Rose Dennis - email: rosedennis@umass.edu<br>
Drew Dellarocco- email: drewdellarocco@gmail.com <br>
Robert Becotte - email: robert.becotte@gmail.com <br>
