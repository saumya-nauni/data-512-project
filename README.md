# Muskogee, Oklahoma Wildfire Analysis

This research aims to provide a thorough examination of the impact of wildfires in Muskogee, Oklahoma by estimating the effects of smoke over the last six decades. The study involves a multifaceted approach, encompassing data extraction, filtering, smoke estimation, correlation analysis with Air Quality Index (AQI) data, and the development of a forecasting model to project future smoke concentrations.

## Repository Structure

```bash
.
├── images
│   ├── AQI vs Smoke Impact (Min-Max Scaling).png
│   ├── AQI vs Smoke Impact.png
│   └── Histogram.png
│   ├── Predictive Model.png
│   └── Total Acres Burned Per Year.png
├── analysis.ipynb
├── api_data.ipynb
├── README.md
├── LICENSE
├── json-data
│   ├── academy_monthly_cumulative_201507-202309.json
│   ├── academy_monthly_desktop_201507-202309.json
│   └── academy_monthly_mobile_201507-202309.json
```

## Introduction

Wildfires have become increasingly prevalent and severe, posing significant challenges to communities and ecosystems. Muskogee County, like many other regions, has witnessed the detrimental effects of wildfire-induced smoke. This research seeks to understand the historical patterns of smoke in the county over the past 60 years, with a focus on quantifying its impact on air quality.

## Methodology

### Wildfire Data

The research focuses on a Common Analysis Research Topic utilizing the [Wildland Fire Combined Dataset by USGS.json](https://www.sciencebase.gov/catalog/item/61aa537dd34eb622f699df81). This comprehensive dataset, compiled by the US Geological Survey, encompasses wildland fire polygons in the United States and various territories dating from the 1800s to the present. Documentation accompanying the dataset ensures transparency and understanding. Available in both ArcGIS and GeoJSON formats, the dataset serves as the foundational element for our individual research projects.

Each researcher has been assigned a specific US city, detailed in a Google spreadsheet. The city assigned here is **Muskogee, Oklahoma**. This city will be the focal point for our unique investigations, utilizing the extensive and well-documented wildland fire dataset to explore patterns, trends, and implications related to wildfires in our respective regions.

An example notebook under the Creative Commons CC-BY License, located at: `src/reference-notebooks/wildfire_geo_proximity_example.ipynb`. This notebook was used as a reference to get the wildfire data for a particular city, in our case we used it to get the wildfire data for Muskogee, Oklahoma.

### AQI Data

For our comprehensive analysis, we integrate Air Quality Index (AQI) data sourced from the US Environmental Protection Agency (EPA) via an API. This API serves as a vital tool for retrieving real-time and historical AQI information specifically tailored to Muskogee, Oklahoma.

By leveraging the EPA's data through this API, we gain valuable insights into the air quality conditions in Muskogee. The AQI, a standardized measure, allows us to assess the levels of various pollutants, providing a quantitative understanding of the potential health risks associated with air pollution in the region.

An example notebook under the Creative Commons CC-BY license with all steps and different processes used to get the AQI data is located at: `src/reference-notebooks/epa_air_quality_history_example.ipynb`.

### Data Location

The data used (or generated) throughout the analysis is located in a Google Drive: https://drive.google.com/drive/folders/1yFBJI2Wcvlb03Z_4gHqJLhdMF2BQQp-M?usp=sharing

- `USGS_Wildland_Fire_Combined_Dataset.json` - A GeoJSON file that contains the wildfire data across the united states from 1800s - present.

- `muskogee_wildfire.json` - This file contains the raw data generated using the data above with specific filters to get data only around the specified city.

- `muskogee.csv` - Contains the filtered and cleaned data from the raw file. This file is used later in the analysis step.

- `smoke-estimators` - The smoke impact estimators for each wildfire is located in this file. These values are used for the visualizations.

- `avg-aqi-yearly.csv` - A csv file that has the AQI data for Muskogee, Oklahoma on a yearly average basis.

### Data Filtering:

The dataset employed for our analysis and subsequent visualizations undergoes a meticulous filtering process to ensure relevance and accuracy. The three distinct filters applied contribute to refining and focusing the scope of the data:

1. **Temporal Filter (Last 60 Years):**

   The analysis primarily considers wildland fires that transpired within the temporal window of the last 60 years, specifically from 1963 to 2023.

2. **Spatial Filter (Within 1250 Miles):**

   To narrow down the dataset to events with potential regional impact, the estimation selectively includes fires that occurred within a radius of 1250 miles from the assigned city.

3. **Seasonal Filter (May 1st - October 31st):**

   Acknowledging the seasonal variability of wildfire occurrences, an annual fire season is defined, spanning from May 1st through October 31st.

By applying these filters, our analysis ensures a targeted investigation into the impact of wildland fires, offering a nuanced perspective that considers both temporal evolution and geographical proximity to the assigned city. This refined dataset serves as the foundation for generating meaningful visualizations and drawing insights that are not only accurate but also highly relevant to the specific context of our study.

### Smoke Estimation:

Advanced modeling techniques will be employed to estimate the spatial and temporal distribution of smoke in Grand Fork County. This will involve integrating satellite observations, ground-based measurements, and meteorological data to create a comprehensive smoke dispersion model.

### Correlation Analysis:

The relationship between smoke concentrations and AQI will be explored using statistical methods. This analysis aims to quantify the impact of wildfire-induced smoke on air quality, providing insights into potential health risks and environmental consequences.