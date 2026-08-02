# Retail Data Anonymizer

## Overview

This project anonymizes sensitive customer information from retail order data while preserving business metrics for analytics and dashboarding.

## Features

- Reads retail order data from Excel
- Masks customer phone numbers
- Replaces customer and shipping addresses with anonymized values
- Exports a clean anonymized dataset

## Technologies Used

- Python
- Pandas
- OpenPyXL

## Project Structure

Retail-Data-Anonymizer/
│── data/
│── output/
│── anonymize.py
│── requirements.txt
│── README.md

## How to Run

```bash
pip install -r requirements.txt
python anonymize.py
```

## Output

The script creates an anonymized Excel file inside the `output` folder.