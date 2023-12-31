# Muskogee, Oklahoma Wildfire Impact Analysis on Crop Production

This research aims to provide a thorough examination of the impact of wildfires on cro production in Muskogee, Oklahoma by estimating the effects of smoke over the last six decades. The study involves a multifaceted approach, encompassing data extraction, filtering, smoke estimation, crop impact estimation and visual analysis with Air Quality Index (AQI) data, and the development of a forecasting model to project future smoke concentrations and crop impacts.

## Repository Structure

```bash
.
├── images
│   ├── wildfire-visualizations
│     ├── AQI vs Smoke Impact (Min-Max Scaling).png
│     ├── AQI vs Smoke Impact.png
│     └── Histogram.png
│     ├── Predictive Model.png
│     └── Total Acres Burned Per Year.png
│   ├── crop-visualizations
│     ├── Covariance Matrix Corn.png
│     ├── Covariance Matrix Soybeans.png
│     └── Crop Impact vs AQI Corn.png
│     ├── Crop Impact vs AQI Soybeans.png
│     ├── Crop vs Smoke Impact Corn.png
│     ├── Crop vs Smoke Impact Soybeans.png
│     └── Predictive Model Corn.png
│     └── Predictive Model Soybeans.png
├── src
│   ├── reference-notebooks
│       ├── epa_air_quality_history_example.ipynb
│       └── wildfire_geo_proximity_example.ipynb
│   ├── aqi-data.ipynb
│   ├── crop-impact-visualizations.ipynb
│   ├── economic-impact.ipynb
│   └── wildfire-data.ipynb
│   ├── functions.py
│   └── smoke-estimator.ipynb
│   └── wildfire-visualizations.ipynb
├── wildfire
│   ├── Reader.py
├── reports
│   ├── Part 1 - Reflections.pdf
│   ├── Part 2 - Extension Plan.pdf
│   ├── Final Report.pdf
├── README.md
├── LICENSE
```
### Repository Information

> - `src/aqi-data.ipynb` - Notebook that extracts the AQI data for Muskogee, Oklahoma
> - `src/wildfire.ipynb` - Notebook read the raw file containing information of all wildfires and calculates the geodetic distance between the place of the wildfire and the city.
> - `src/functions.py` - Python file containing helper functions used in wildfire.ipynb. The functions here are taken from the reference notebook.
> - `src/smoke-estimator.ipynb` - Calculates the smoke impact estimator for all the wildfires. These values are then used for the visualizations.
> - `src/wildfire-visualizations.ipynb` - Contains all the wildfire visualizations and the predictive model for the next 25 years.
> - `src/economic-impact.ipynb` - Calculates the crop impact estimator for all the crop types. These values are then used for the visualizations.
> - `src/crop-impact-visualizations.ipynb` - Contains all the crop impact visualizations and the predictive model for the next 25 years.

## Introduction

The analysis of the wildfire impact on crop production in Muskogee, Oklahoma, is profoundly interesting and important due to several critical factors. This research addresses a timely and pressing issue with wide-ranging consequences for the local agricultural community, the regional economy, and the broader ecological context.

## Methodology

### Wildfire Data

The research focuses on a Common Analysis Research Topic utilizing the [Wildland Fire Combined Dataset by USGS.json](https://www.sciencebase.gov/catalog/item/61aa537dd34eb622f699df81). This comprehensive dataset, compiled by the US Geological Survey, encompasses wildland fire polygons in the United States and various territories dating from the 1800s to the present. Documentation accompanying the dataset ensures transparency and understanding. Available in both ArcGIS and GeoJSON formats, the dataset serves as the foundational element for our individual research projects.

Each researcher has been assigned a specific US city, detailed in a Google spreadsheet. The city assigned here is **Muskogee, Oklahoma**. This city will be the focal point for our unique investigations, utilizing the extensive and well-documented wildland fire dataset to explore patterns, trends, and implications related to wildfires in our respective regions.

An example notebook under the Creative Commons CC-BY License, located at: `src/reference-notebooks/wildfire_geo_proximity_example.ipynb`. This notebook was used as a reference to get the wildfire data for a particular city, in our case we used it to get the wildfire data for Muskogee, Oklahoma.

### AQI Data

For our comprehensive analysis, we integrate Air Quality Index (AQI) data sourced from the US Environmental Protection Agency (EPA) via an API. This API serves as a vital tool for retrieving real-time and historical AQI information specifically tailored to Muskogee, Oklahoma.

By leveraging the EPA's data through this API, we gain valuable insights into the air quality conditions in Muskogee. The AQI, a standardized measure, allows us to assess the levels of various pollutants, providing a quantitative understanding of the potential health risks associated with air pollution in the region.

An example notebook under the Creative Commons CC-BY license with all steps and different processes used to get the AQI data is located at: `src/reference-notebooks/epa_air_quality_history_example.ipynb`.

### Crops Data

The [United States Department of Agriculture (USDA)](https://www.nass.usda.gov/Data_and_Statistics/) provides a comprehensive and invaluable source of data related to crops, which is essential for understanding, managing, and advancing agriculture in the United States. This rich dataset encompasses a wide array of information about crops, including crop types, production, yields, acreage, prices, and more. It is collected through a combination of surveys, field observations, and data from farmers, making it one of the most authoritative sources for crop-related information in the country.

One of the fundamental components of the USDA's crops data is the Crop Production Report, which is released on a monthly basis. This report provides estimates of crop production for major field crops, such as corn, soybeans, wheat, cotton, and rice. These estimates are crucial for farmers, agribusinesses, and policymakers as they help in forecasting crop availability and making informed decisions about planting, marketing, and trade. The USDA's National Agricultural Statistics Service (NASS) conducts surveys to gather this data, ensuring its accuracy and reliability.

### Data Location

The data used (or generated) throughout the analysis is located in a Google Drive: https://drive.google.com/drive/folders/1yFBJI2Wcvlb03Z_4gHqJLhdMF2BQQp-M?usp=sharing

- `USGS_Wildland_Fire_Combined_Dataset.json` - A GeoJSON file that contains the wildfire data across the united states from 1800s - present.

- `muskogee_wildfire.json` - This file contains the raw data generated using the data above with specific filters to get data only around the specified city.

- `muskogee.csv` - Contains the filtered and cleaned data from the raw file. This file is used later in the analysis step.

- `smoke-estimators` - The smoke impact estimators for each wildfire is located in this file. These values are used for the visualizations.

- `avg-aqi-yearly-fire-season.csv` - A csv file that has the AQI data for Muskogee, Oklahoma on a yearly average basis (only for the fire season).

- `all-crops-data.csv` - The complete crops data taken from USDA website. It contains the crop data for all regions in the United States

- `harvest-muskogee.csv` - The filtered and preprocessed crop data for muskogee with the crop impact estimate

- `muskogee-crops.csv` - Contains all the crops data for muskogee


### Data Filtering:

The dataset employed for our analysis and subsequent visualizations undergoes a meticulous filtering process to ensure relevance and accuracy. The three distinct filters applied contribute to refining and focusing the scope of the data:

**Wildfire Data**

1. **Temporal Filter (Last 60 Years):**

   The analysis primarily considers wildland fires that transpired within the temporal window of the last 60 years, specifically from 1963 to 2023.

2. **Spatial Filter (Within 1250 Miles):**

   To narrow down the dataset to events with potential regional impact, the estimation selectively includes fires that occurred within a radius of 1250 miles from the assigned city.

3. **Seasonal Filter (May 1st - October 31st):**

   Acknowledging the seasonal variability of wildfire occurrences, an annual fire season is defined, spanning from May 1st through October 31st.

**Crops Data**

The only filter applied to the `all-crops.csv` data was to include only the rows for the the county Muskogee and state Oklahoma.

By applying these filters, our analysis ensures a targeted investigation into the impact of wildland fires, offering a nuanced perspective that considers both temporal evolution and geographical proximity to the assigned city. This refined dataset serves as the foundation for generating meaningful visualizations and drawing insights that are not only accurate but also highly relevant to the specific context of our study.

### Smoke Estimation:

The methodology employed for smoke estimation in this analysis revolves around a proximity impact approach, emphasizing the significance of both distance and fire size in determining the extent of smoke impact. Two crucial factors, proximity, and fire size, are considered to quantitatively assess the potential influence of wildfires on the study area.

1. **Proximity Impact:**

   The distance between the wildfires and the designated study area plays a pivotal role in our smoke estimation. The rationale behind this criterion is that the closer a wildfire is to the region of interest, the more substantial its impact on air quality and environmental conditions is likely to be. By prioritizing proximity, we aim to capture the localized effects of wildfires, recognizing that their influence diminishes with increasing distance.

2. **Fire Size Consideration:**

   In addition to proximity, the size of the wildfires is a key determinant in our smoke estimation model. Larger fires inherently have the potential to produce more significant amounts of smoke, even at a considerable distance. Therefore, the methodology takes into account the dual influence of both proximity and fire size to provide a more nuanced and realistic representation of the potential impact on the study area.

**Formula for Smoke Impact**

    `smoke_impact = (-decay_rate * distance) * fire_size`

By incorporating these factors into our smoke estimation model, we aim to generate a more accurate and context-specific understanding of the potential consequences of wildfires on air quality. This dual approach ensures that the analysis not only considers the immediate vicinity of wildfires but also acknowledges the varying degrees of impact based on the size of the fires, thereby contributing to a more comprehensive assessment of the environmental effects of wildland fires.

### Crop Impact Estimation

To quantitatively gauge the repercussions of wildfires on crop production in Muskogee, Oklahoma, we employ a well-defined Crop Impact Score calculation. This formula, which incorporates essential variables such as area harvested and area planted, offers a precise means of measuring the impact of wildfires on the region's agricultural output.

The Crop Impact Score (CIS) is derived from the following formula:

`Area Harvested % = (Area Harvested) / (Area Planted)`

`CIS: (Max(Area Harvested %) - (Area Harvested % for the year) / (Max(Area Harvested %)`

This formula operates on the principle of relative crop loss, taking into consideration both the maximum achievable yield (represented by Max(Area Harvested) / Max(Area Planted)) and the actual yield achieved (Area Harvested / Area Planted). By comparing these values, the Crop Impact Score quantifies the extent to which wildfires have disrupted crop production.

A higher Crop Impact Score indicates a more substantial reduction in crop yield, signifying a more severe impact of wildfires on the agricultural sector. Conversely, a lower score reflects a relatively minimal impact, highlighting the resilience of crops to wildfire-related challenges.

By utilizing this Crop Impact Score calculation, we aim to provide a clear and objective measure of the consequences of wildfires on Muskogee's crop production, aiding in the development of informed strategies to mitigate these effects and bolster the region's agricultural resilience.

## Summary of Visual Analytics

### Summary of Findings:

Our study on the impact of wildfires and smoke on crop production in Muskogee, Oklahoma, yielded several significant findings:

1. **Crop Vulnerability:** We found compelling evidence supporting Hypothesis 1, indicating that wildfires have a substantial adverse impact on crop production in Muskogee, leading to reduced yields and economic losses for farmers. This underscores the vulnerability of the local agricultural sector to wildfire events.

2. **Air Quality Influence:** Our analysis confirmed Hypothesis 2, demonstrating that wildfire-induced air pollution significantly affects the health and growth of crops. The changing air quality directly impacts crop production, with specific crops like Corn and Soybeans responding differently to variations in smoke levels.

3. **Long-term Trends:** Hypothesis 3 was substantiated by our findings, revealing that the trend for crop impact is expected to increase over the next 25 years in correlation with the projected rise in smoke levels. This suggests an escalating challenge for Muskogee's agricultural community in the face of a changing climate.

### Human-Centered Data Science:

This study aligns with the principles of human-centered data science by providing actionable insights that inform decision-making for various stakeholders. It highlights the vulnerability of local farmers and the importance of implementing strategies to safeguard crop production and economic well-being. The findings underscore the need for proactive measures, such as emergency response planning, investment in agricultural resilience, and community engagement, to address the challenges posed by wildfires and smoke impact.

By presenting a comprehensive analysis, our study empowers local policymakers, farmers, and residents with knowledge to make informed choices, demonstrating how human-centered data science principles contribute to enhancing community well-being and resilience in the face of environmental challenges. It emphasizes the critical role of data-driven research in addressing real-world issues and informs a more comprehensive understanding of the complex interactions between natural disasters, agriculture, and community livelihoods.

## Reproducing the Analysis

### 1. Clone the Repository

Begin by making a local copy of this repository. You can do this by running the following command in your terminal or command prompt:
```bash
git clone https://github.com/saumya-nauni/data-512-project.git
```

### 2. Download and Extract the Dataset

- You can download the `GeoJSON Files.zip` from this [link](https://www.sciencebase.gov/catalog/item/61aa537dd34eb622f699df81). Once you have this downloaded you will see the `USGS_Wildland_Fire_Combined_Dataset.json` file.
- Next download the `all-crops.csv` data from the [Google Drive](https://drive.google.com/drive/folders/1yFBJI2Wcvlb03Z_4gHqJLhdMF2BQQp-M?usp=sharing) link.

> Note: All the other datasets are intermediate datasets that are generated by running the codes.

### 3. Execute the Notebook Cells

- First start by running the cells in the `wildfire-data.ipynb` notebook. You can change the city here according to your use. The result of this step would give you two files: the raw data file (`muskogee-wildfire.json`) and the cleaned file (`muskogee.csv`)
- The second step is run to the `smoke-estimator.ipynb` notebook to get all values of the smoke_impact for each wildfire. The result is the dataset `smoke-estimators.csv`
- The next step is to get the avg AQI values for each year. For this run the cells in the `aqi-data.ipynb` notebook. The result would be the dataset `avg-aqi-yearly-fire-season.csv`
- Last, you would have to run the `wildfire-visualizations.ipynb` notebook to get all the visualizations along with the predictive model.
- For the crop impact estimator, run the cells in `economic-impact.ipynb` to get the intermediate finals but the one that will be used is the `harvest-muskogee.csv` for the visualization
- To view the visual analysis of wildfire on crop production run the cells in the `crop-impact-visualizations.ipynb` to get the different plots.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
