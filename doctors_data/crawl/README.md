# Doctors Data Crawling and Preprocessing

This project crawls, processes, and analyzes doctors' data from a healthcare platform. It consists of three main stages:

   - Crawling doctors' information from an API.
   - Preprocessing and selecting key features from the raw data.
   - Crawling and extracting the "About Me" section for doctors with available information.

## Prerequisites

To run the scripts, ensure you have the following Python packages installed:

bash

pip install requests beautifulsoup4 pandas numpy tqdm

 1. Crawling Doctors' Information from API

The first script (main_crawl.py) collects data on doctors from various cities and specialties by querying an API.
How it Works:

    Expertise and City Data: Expertise areas are scraped from the website, while a list of cities is predefined.
    API Requests: For each city and expertise combination, data is retrieved across multiple pages (up to 25 pages per combination).
    Data Storage: The data is saved in new_doctors.json under the ../data/raw/ directory.

### Usage:

bash

python main_crawl.py

Output:

    Crawled data is stored in ../data/raw/new_doctors.json.

2. Preprocessing and Feature Selection

The second script (preprocess.py) cleans the raw data, selects relevant features, and extracts additional information such as clinics, gender, and symptoms.
Key Steps:

    Data Cleaning: Removes duplicates and fills in missing names based on the title field.
    Gender Assignment: Uses a separate names.csv file to assign genders (M/F) based on doctors' first names.
    Complex Field Extraction: Processes fields like centers (clinics), rate_info (ratings), and expertise to extract structured information.
    Feature Selection: Key features such as doctor ratings, experience, and online booking status are selected.

### Usage:

bash

python preprocess.py

Output:

    Processed data is saved in ../data/processed/new_dataset.csv.

3. Crawling the "About Me" Section

The third script (crawl_about_me.py) crawls the "About Me" section for doctors who have this field available on the website.
Key Steps:

    API Requests: Sends API requests to retrieve the "About Me" sections based on doctors' medical_code.
    Partitioning: Processes the dataset in 40 partitions to manage API limits and performance.
    Data Cleaning: Removes HTML tags from the "About Me" sections.

### Usage:

bash

python crawl_about_me.py

Output:

    The crawled data is saved in partitioned files (about_dataset_0.csv, about_dataset_1.csv, etc.), and finally combined into about_dataset.csv in the ../data/processed/ directory.

Directory Structure

    ../data/raw/: Contains raw data files (new_doctors.json, names.csv).
    ../data/processed/: Contains processed and partitioned data files (new_dataset.csv, about_dataset.csv).
    ../elastic/symptomes.json: Contains symptom mapping data for expertise.

### License

This project is open-source. Contributions are welcome!