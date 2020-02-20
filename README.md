
# Exploring Perceived/Actual Impact on Property Value after a Hurricane

#### This is a pro bono academic proof of concept between General Assembly DSI10-BOS and New Light Technologies.
---
## Table of Contents:
[1.0 Directory Structure](#10-directory-structure)<br>
[2.0 Problem Statement](#20-problem-statement)<br>
-[2.1 How did we get here?](#21-how-did-we-get-here)<br>
-[2.2 Executive Summary](#22-executive-summary)<br>
-[2.3 Goals](#23-goals)<br>
-[2.4 Limitations](#24-limitations)<br>
[3.0 Software/APIs/Libraries Used](#30-software/apis/libraries-used)<br>
-[3.1 Data Engineering and Collection](#31-data-engineering-and-collection)<br>
-[3.2 Web Application](#32-web-application)<br>
-[3.3 Visuals](#33-visuals)<br>
[4.0 Data Dictionary](#40-data-dictionary)<br>
[5.0 High Level Overview of Findings](#50-high-level-overview-of-findings)<br>
-[5.1 Hurricane Dorian](#51-hurricane-dorian)<br>
-[5.2 Hurricane Sandy](#52-hurricane-sandy)<br>
-[5.3 Hurricane Harvey](#53-hurricane-harvey)<br>
[6.0 Minimum Viable Product for Web Application](#60-minimum-viable-product-for-web-application)<br>
-[6.1 Home Page of Flask App](#51-home-page-of-flask-app)<br>
-[6.2 Results Page of Flask App](#52-results-page-of-flask-app)<br>
[7.0 Next Steps and Recommendations](#70-next-steps-and-recommendations)<br>
[8.0 sources/Citations](#80-sources/citations)<br>
[9.0 Contact Info](#90-contact-info)<br>

---
## 1.0 Directory Structure
```
├── DSI_group_project_hurricane_impact
    ├── flask_app
        ├── static
            └── style.css
        ├── templates  
            ├── colors.html
            ├── data_frame.html
            ├── home.html
            └── land.html
        └── app_starter.py
    ├── visuals
        ├── dorian_matplotlib.png
        ├── dorian_tableau.png
        ├── harvey_tableau.png
        ├── flask_home.png
        ├── flask_results.png
        └── sandy_tableau.png
    ├── Exploring Perceived_Actual Impact on Property Value after a Hurricane.pdf
    ├── README.md
    ├── initial_imports_cleaning_engineering.ipynb
    ├── master_df.csv
    ├── visual_notebook_example.ipynb
    └── zipcode_scraping_example.ipynb
```    
## 2.0 Problem Statement

#### 2.1 How did we get here? 
During a disaster, it is important to model and estimate the potential or forecasted effect of the event, including the projected/forecasted damage. Existing indicators of forecasted damage include number of structures within the affected area, number of people in the area, number of households, demographics of the impacted population, etc. This project will add an additional perspective: It will compare how hurricanes do or do not impact real estate sale prices by zip code before and after the storm.

#### How do we quickly glean insights on property values before and after a hurricane through a user friendly application?

## 2.2 Executive Summary

* While hurricanes have numerous nominal and real costs on individuals, groups, property, and governments, we have found that their impact on real estate sale prices does not necessarily follow intuitive logic (size, proximity to storm or ocean).

* We identified large fluctuations in sale price in the affected areas, even when comparing adjacent zip codes, suggesting limited geographic relevance.

* Hurricane Harvey produced the highest damage count of $125B, however, the real estate prices were virtually unaffected when compared to the national average.
 
## 2.3 Goals
* Provide an initial proof of concept for a potential web application using Flask software for Python. 
* This rudimentary web app will allow the user to input a zip code and see summary statistics for how median real estate prices were affected after a hurricane.

## 2.4 Limitations
- We used the top ~6000 zip codes by population, not the ~41000 exhaustive list of zips
- This initial proof focuses on the recent hurricanes of Sandy, Harvey, and Dorian
- Our focus for this project was financial impact on zip code aggregated median sale prices
- This project considers nominal/actual sale prices, not indirect/real economic costs

## 3.0 Software/APIs/Libraries Used

#### 3.1 Data Engineering and Collection
- Python
- Jupyter
- Pandas
- Numpy
- Beautiful Soup

#### 3.2 Web Application
- Flask (Using Python): Flask, request, render_template, session, redirect, url_for
- Pandas
- Numpy
- Atom (For Flask, HTML, CSS)
- Sys

#### 3.3 Visuals
- Tableau Public
- Matplotlib: Pyplot
- Missingno
- Google Slides
- Adobe Acrobat

## 4.0 Data Dictionary

| Column | Description |
| --- | --- |
| **Zip** | Zip Code. |
| **Pop Rank** | Ordinal population size. 1 is the largest populated zip code, 2 is the second largest. |
| **XXXX Mean Median** | The aggregated average annual sale price from the zip code median sale prices. |
| **Hurricane Affected** | 1 if the zip code was impacted by Hurricane X according to FEMA, 0 otherwise. |
| **% Change After Hurricane** | Percentage difference in median zip sale price comparing the month preceding the storm to the month following the storm.|

## 5.0 High Level Overview of Findings
#### Hot colors indicate largest drops in median sale price after the hurricane
#### Cold colors indicate largest increases in median sale price after the hurricane

### 5.1 Hurricane Dorian focused on Florida
![Dorian Affected Zip Codes](./visuals/dorian_tableau.png)

#### Example Dorian impact
![Example Dorian impact](./visuals/dorian_matplotlib.png)

### 5.2 Hurricane Sandy focused on North East U.S.
![Sandy Affected Zip Codes](./visuals/sandy_tableau.png)

### 5.3 Hurricane Harvey focused on greater Houston, TX
![Harcey Affected Zip Codes](./visuals/harvey_tableau.png)

## 6.0 Minimum Viable Product for Web Application
 
#### Enter a zip code to see the summary statistics<br> 
### 6.1 Home Page of Flask App <br>
![Flask Home Page](./visuals/flask_home.png)

### 6.2 Results Page of Flask App for Zip Code 77071 Houston (Median Sale Price dropped ~24.4% directly after Harvey)<br>
![Flask Home Page](./visuals/flask_results.png)

## 7.0 Next Steps and Recommendations
* Why are the most negatively impacted zip codes adjacent to the most positively impacted zip codes? (Elevation, levies, state/fed resources) 
* How can we best feature engineer zoning laws and real estate regulations into a machine learning model? (Binary dummies, ordinal)
* What kind of model might we want to use? (regressor/classifier/hybrid)
* Scale this concept to other natural disasters (Earthquake, fire, tornado)

## 8.0 Sources/Citations
1. <a href="https://www.zillow.com/research/data/">Zillow Median Sale Price by Zip (CSV)</a> 

2. <a href="https://www.zillow.com/browse/homes/tx/harris-county/">Zillow: Harris County, TX Zip Codes</a> 

3. <a href="https://www.fema.gov/disaster/4468">FEMA Visual and link for finding official Hurricane Dorian report</a> 

4. <a href="https://www.fema.gov/media-library-data/1572651498411-9b9527200177132f395165f7888d7a67/FEMA4468DRFL.pdf">FEMA preliminary Dorian damage report for finding affected counties</a> 

5. <a href="https://www.getzips.com/county.htm">Converting counties to zipcodes (webscraping)</a> 

6. <a href="https://www.fema.gov/disasters?field_dv2_state_territory_tribal_value_selective=All&field_dv2_incident_type_tid=49124&field_dv2_declaration_type_value=All&field_dv2_incident_begin_value%5Bvalue%5D%5Bmonth%5D=&field_dv2_incident_begin_value%5Bvalue%5D%5Byear%5D=&field_dv2_incident_end_value%5Bvalue%5D%5Bmonth%5D=&field_dv2_incident_end_value%5Bvalue%5D%5Byear%5D=">Easily searchable FEMA database for finding storms:</a> 

7. <a href="https://www.nhc.noaa.gov/news/UpdatedCostliest.pdf">NOAA.gov Hurricane Data</a> 

8. <a href="https://www.livescience.com/40774-hurricane-sandy-s-impact-infographic.html">Hurricane Sandy Damage</a> 

9. <a href="https://www.ncdc.noaa.gov/billions/">Financial Impact of Hurricanes from NOAA.gov</a> 

10.  <a href="https://fred.stlouisfed.org/series/MSPUS?utm_source=series_page&utm_medium=related_content&utm_term=related_resources&utm_campaign=categories#0">Year over Year National Sale Prices from St. Louis Federal Reserve</a> 

## 9.0 Contact Info

Rose Dennis - email: rosedennis@umass.edu , github: RoseXDennis <br>
Drew Dellarocco - email: drewdellarocco@gmail.com , github: drewdellarocco <br>
Robert Becotte - email: robert.becotte@gmail.com , github: robertgerardb <br>
