COPY berlin_housing_data
FROM 'D:\DE_Project_HouseScrap\Housing-Scrap\data\Deutschland\Berlin_housing_data.csv'
(DELIMITER ',', FORMAT CSV, NULL '', ENCODING 'utf-8', HEADER true)