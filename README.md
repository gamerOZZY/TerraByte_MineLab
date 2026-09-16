![Data Science](https://shields.io/badge/Data%20Science-Analitycs-blue)
![Data Engineering](https://shields.io/badge/Data%20Engineering-ETL%20Pipeline-green)
![Docker](https://shields.io/badge/Docker-Enviroment-red)


# TerraByte MineLab

## Table of Contents
1. [Project Overview](#project-overview)
2. [What the project Analyses](#what-the-project-analyses)
3. [objetives](#)

    <!-- 
    Variables that could answer each question:
    1. hhi, top_country_share_pct, production_share_pct, country, mineral, year TODO: 
        TODO: fOR THIS ONE, I should also look for the geographical coordinates of each country
    
    2.production_share_pct vs refined_share_pct 
    
    3. reserves_tonnes, mine_production_tonnes, years_of_reserves
    
    4.demand_growth_pct price_usd_per_tonne, year, mineral, end_use

    5.1 P(disruption | export control), P(disruption | no export control) for all of them
    5.2 hhi, top_country_share_pct, refined_share_pct, export_control_active, production_share_pct

    6. risk_change = risk_2026 - risk_2015 or sum
    -->
4. [Architecture](#)
5. [Data Undestanding](#)
6. [Data Science](#)
    * [EDA](#)

## Project Overview
This project is an end-to-end data platform developed as a personal laboratory to explore and understand the actual state of Critical Minerals  and rare earths. At the same time, I put my specific skills into practice

Starting from a real-world dataset, the project covers the complete data lifecycle: data exploration, ETL, distributed processing with Apache Spark, database integration, predictive modeling, and Power BI visualization.

Synthetic data is generated based on the characteristics of the original dataset to simulate new records continuously arriving into a production-like environment, allowing the data pipeline and processing workflows to be tested under evolving data.

The main goal is to understand how these components work together as a complete data system, from raw data ingestion to analytical and business-facing outputs.

##  What the Project Analyses
A country-by-mineral-by-year panel of the world's most strategically contested resources —
lithium, cobalt, nickel, graphite, rare earths, gallium, and more. Production, reserves,
refining concentration, prices, export controls, and a supply-risk index, in one clean file.
Built for the era of resource geopolitics.

This Dataset is used because Critical minerals are the flashpoint of 2020s geopolitics: EV batteries, wind turbines,
semiconductors, and defense systems all depend on a handful of elements — and a handful of
countries. China dominates rare-earth and graphite supply, the DRC dominates cobalt, Indonesia
dominates nickel, and since 2023 a wave of export controls has turned these supply chains
into strategic leverage. Yet most public data lives in scattered government PDFs. This dataset
packages the story as a clean analytical panel you can load and explore in one line.

The datased is 100% synthetic. No real production, reserve, price, or trade figures are reproduced. Every row is procedurally generated (fixed seed). What is calibrated to reality is the structure, so the
patterns match the real world:

* Production concentration reflects reported dominance — China in rare earths and graphite, DRC in cobalt, Indonesia in nickel, the Lithium Triangle in lithium — with the top-3 producer share around the mid-70s%, consistent with IEA Global Critical Minerals Outlook 2025 and USGS Mineral Commodity Summaries 2025/2026.
* Refining is modeled as more China-concentrated than mining, per the same sources.
* Price paths follow real dynamics (lithium's ~8× 2021–22 spike then >80% decline; cobalt/nickel/graphite softening in 2024).
* The export-control timeline mirrors the real wave of measures since 2023 (e.g. gallium/germanium and graphite from 2023, antimony from 2024, tungsten and several heavy rare earths in 2025, and a 2025 cobalt export pause), used here only to calibrate the synthetic export_control_active flag — not to assert any specific figure.

These sources informed the design of the simulator only; no data from them is reproduced. Use the
dataset for analysis, modeling, and education — not as a factual record of any country or market. The original dataset comes from ->  https://www.kaggle.com/datasets/sergionefedov/critical-minerals-and-rare-earths-20152026 

## Objectives

Analyze the evolution of global critical-mineral supply chains between 2015 and 2026 and identify the factors associated with supply disruptions, with the goal of predicting whether a disruption will occur in the following year.

In order to answer this question, The next points will be reviwed:
1. **Supply Concentration**
    * Which minerals have the most geographically concentrated production? <!-- Gotta look for the Coordinates of each contry and the scatter to see some groups-->

2. **Mining vs Refining**
    * Are some minerals relatively diversified in mining but highly concentrated in refining?
    * Which minerals have the greatest gap between mining and refining concentration?

3. **Reserves**
    * Which minerals have the greatest estimated years of remaining supply?
    * Are production increases reducing the apparent years of reserves? <!-- For this one, I should investigate a bit i think-->
    * Which minerals have high production but relatively low years of reserves?

4. **Price and Demand**
    * Does Demand growth correspond to increasing mineral prices?

5. **Export Controls and Suppy risk**
    * How strongly are export controls associated with supply disruptions?
    * What factors contribute most to a mineral's supply risk?
    * Is geographic concentration the main driver of supply risk, or do export controls and refining concentration contribute substantially?

6. **Risk Evolution**
    * Which minerals became increasingly risky between 2015 and 2026?

7. **Prediction**
    * Can we predict whether a supply disruption will occur next year based on current supply-chain conditions?