##docker images

# E-Commerce DB Dashboard

## Overview
This project provides a framework for preprocessing data from various e-commerce platforms and loading it into a MySQL database stored in a Docker container. The database schema ensures data integrity and accessibility for further analysis. Additionally, the project integrates Grafana for data visualization, enabling stakeholders to gain actionable insights into sales trends, customer behavior, and inventory management.

## Features
- **Data Preprocessing**: Extracts, cleans, and transforms data from different e-commerce platforms.
- **Database Management**: Loads processed data into a structured MySQL database.
- **Data Integrity**: Ensures consistency and accuracy of data.
- **Visualization with Grafana**: Provides dashboards for monitoring key business metrics.
- **Business Insights**: Facilitates informed decision-making through real-time analytics.

## Technologies Used
- **Python**: For data preprocessing and ETL pipeline.
- **MySQL (Docker)**: For structured data storage.
- **Grafana**: For interactive data visualization.
- **Docker**: For containerized deployment.

## Installation
### Prerequisites
Ensure you have the following installed on your system:
- Docker & Docker Compose
- Python 3.x
- Grafana

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/ArmenMadoyan/E-Commerce-DB-Dashboard.git
   cd E-Commerce-DB-Dashboard
   ```
2. Start the MySQL database using Docker Compose:
   ```sh
   docker-compose up -d

   ```
3. Create the database architecture with tables by running the SQL script:
   ```sh
   mysql -u root -p < coolina.sql
   ```
4. Preprocess the data and fill the database:
   - Run the Python script:
     ```sh
     python coolina1.py
     ```
   - Alternatively, run the Jupyter Notebook:
     ```sh
     jupyter notebook coolina.ipynb
     ```
5. Set up Grafana and configure data sources to connect to the MySQL database.
   docker pull grafana/grafana
   docker pull mysql/mysql-server

    ##change grafana-volume permissions

    chmod 777 grafana-volume
  open WEB
  http://{your_ip}:3000

  user- admin

  pass- admin

## Usage
- Once data is processed and loaded, Grafana dashboards can be accessed to visualize key metrics.
- The framework can be scheduled to run periodically to update the database with new data.

## Future Enhancements
- Automate data ingestion using Apache Airflow.
- Add support for additional e-commerce platforms.
- Implement machine learning models for predictive analytics.

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request with improvements or new features.

## Contact
For any inquiries or support, please reach out via [GitHub Issues](https://github.com/ArmenMadoyan/E-Commerce-DB-Dashboard/issues).

