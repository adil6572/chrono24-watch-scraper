# Scrapy Chrono24 Watch Scraper

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
  - [Changing the Start URL](#changing-the-start-url)
  - [Changing the Output Filename](#changing-the-output-filename)
  - [Output Format](#output-format)
- [Contributing](#contributing)
- [License](#license)
![The Infatuation](https://github.com/adil6572/chrono24-watch-scraper/blob/main/chrono24.png)
## Introduction

Welcome to the **Scrapy Chrono24 Watch Scraper** project. This repository contains a Scrapy spider that extracts watch details from the website [chrono24.com](https://chrono24.com) and saves the data in JSON format. Chrono24 is a popular platform for buying and selling watches, and this scraper enables you to collect watch information for various purposes.

## Installation

Follow these steps to get started with the Chrono24 Watch Scraper:

### Prerequisites

- Python 3.6 or higher
- Scrapy (install using `pip install scrapy`)

### Instructions

1. Clone this repository to your local machine using Git:

   ```bash
   git clone https://github.com/adil6572/chrono24-watch-scraper.git
   cd chrono24-watch-scraper
   ```

2. Install the required Python packages:

   ```bash
   pip install scrapy
   ```

## Usage

To use the Chrono24 Watch Scraper, follow these steps:

1. Open the Scrapy spider configuration file (`watch.py`) and customize it as needed.

2. Run the scraper:

   ```bash
   scrapy crawl watch_detail_scraper
   ```

3. The scraped data will be saved in JSON format in the specified output file.

You can now use this data for various purposes, such as analysis, building your watch collection database, or any other creative project you have in mind.

## Customization

### Changing the Start URL

To scrape a different page on Chrono24 or another website, open the spider's configuration file (`my_spider.py`) and change the `start_urls` list. Replace the default URL with the one you want to scrape.

```python
start_urls = ['https://www.chrono24.com/patekphilippe/index.htm']  # Replace with your target URL
```

### Changing the Output Filename

You can change the name of the output JSON file in the `FEEDS` setting. Open the spider's configuration file and update the `FEEDS` dictionary with your desired filename:

```python
 custom_settings = {
        'FEEDS': {
            'ouput.json': {
                'format': 'json',
                'overwrite': True,
            },
        },
    },
```

Replace `'output.json'` with your preferred filename.

## Output Format

The scraped data will be saved in a JSON file with items structured as follows:

```json
{
  "watch_id": "29315694",
  "watch_title": "A. Lange & Söhne Lange 1",
  "watch_price": "29950",
  "watch_details": {
    "Basic Info": {
      "Listing code": "HGC4U1",
      "Dealer product code": "4813572",
      "Movement": "Manual winding",
      "Case material": "Yellow gold",
      "Year of production": "Unknown",
      "Gender": "Men's watch/Unisex",
      "Location": "United States of America, Pennsylvania",
      "Price": "$29,950",
      "Availability": "Item is in stock"
    },
    "Caliber": {
      "Movement": "Manual winding",
      "Power reserve": "72 h"
    },
    "Case": {
      "Case material": "Yellow gold",
      "Water resistance": "3 ATM",
      "Crystal": "Sapphire crystal",
      "Dial": "Silver",
      "Dial numerals": "Roman numerals"
    },
    "Bracelet/strap": {
      "Bracelet color": "Brown",
      "Clasp": "Buckle"
    }
  }
}
```

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository to your own GitHub account.

2. Clone the forked repository to your local machine.

3. Create a new branch with a descriptive name for your feature or bug fix.

4. Make your changes and commit them.

5. Push your branch to your GitHub repository.

6. Create a pull request to the main repository, explaining your changes and improvements.

We welcome your contributions and ideas to make this project even better!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Thank you for using the Chrono24 Watch Scraper! Happy web scraping and data analysis! If you have any questions or need assistance, feel free to open an issue or contact the maintainers.
