# AlifStores Gadgets Webscraping

This repository contains the code for scraping gadget types from AlifStores using Scrapy and Selenium. AlifStores website renders its contents with JavaScript, so we utilized Selenium along with Scrapy for scraping.

## Data Collected

The following data were collected from the website:

- Product Category
- Name
- Link
- Price
- Currency
- Slots Left

## Scraping Process

1. **Setup**: Installed necessary dependencies including Scrapy, Selenium, and the Chrome WebDriver.
2. **Spider Creation**: Developed a custom spider using Scrapy to navigate through the website's pages and extract relevant data.
3. **JavaScript Rendering**: Integrated Selenium with Scrapy to handle pages where content is rendered with JavaScript.
4. **Data Extraction**: Utilized XPath to locate and extract desired information such as product category, name, link, price, currency, and slots left.
5. **CSV Export**: Saved the scraped data into a CSV file for further analysis and processing.

## Running the Code

To run the code:

1. Ensure you have Python installed on your system.
2. Install Scrapy, Selenium, and Chrome WebDriver.
3. Clone this repository.
4. Navigate to the project directory.
5. Run the spider using the command `scrapy crawl iphone`.

## File Structure

- `scrapy.cfg`: Scrapy configuration file.
- `iphone.py`: Custom spider for scraping AlifStores.
- `items.py`: Defines the data structure for scraped items.
- `middlewares.py`: Custom middlewares for handling JavaScript rendering.
- `pipelines.py`: Pipeline for processing scraped items and exporting to CSV.
- `settings.py`: Scrapy settings including user agent and delay settings.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request with any improvements or additional features.


### website view

![image](https://github.com/FaeyO/webscrapping-alifstores-website./assets/118575325/85b24858-44f4-48a9-817c-d87ddc92d532)
