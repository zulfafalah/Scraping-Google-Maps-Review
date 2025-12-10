# Google Maps Review Scraper

A Python-based web scraper designed to extract reviews from Google Maps locations. This tool uses Selenium WebDriver to automatically scroll through and collect review data including reviewer names, ratings, dates, and review text.

## 📋 Description

This scraper automates the process of collecting Google Maps reviews by:
- Emulating a mobile browser to access the mobile version of Google Maps
- Automatically scrolling through all available reviews
- Extracting review details using BeautifulSoup and regular expressions
- Exporting the scraped data to a CSV file

## ✨ Features

- **Automatic Scrolling**: Infinitely scrolls through reviews to load all available data
- **Mobile Emulation**: Uses mobile user agent for better compatibility
- **Data Extraction**: Collects reviewer name, date, rating, and review text
- **CSV Export**: Saves all reviews to a structured CSV file
- **Headless Mode Option**: Can run with or without visible browser window

## 🔧 Requirements

- Python 3.7+
- Chrome Browser
- ChromeDriver (automatically managed by webdriver-manager)

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/zulfafalah/Scraping-Google-Maps-Review.git
   cd Scraping-Google-Maps-Review
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

1. **Edit the URL in main.py**
   
   Open `main.py` and replace the `url_map` variable with your desired Google Maps location URL:
   ```python
   url_map = "YOUR_GOOGLE_MAPS_URL_HERE"
   ```

2. **Run the scraper**
   ```bash
   python main.py
   ```

3. **View the results**
   
   The scraped reviews will be saved to `output.csv` in the project directory.

## 📊 Output Format

The generated CSV file contains the following columns:
- **nama**: Reviewer's name
- **waktu**: Review date/time
- **rating**: Star rating (e.g., "5 bintang" = 5 stars)
- **ulasan**: Review text content

## ⚙️ Configuration

### Headless Mode

To run the scraper without opening a visible browser window, uncomment the headless option in `main.py`:

```python
options.add_argument("--headless")
```

### Mobile Emulation

The scraper uses mobile emulation by default. You can modify the user agent in the `mobile_emulation` configuration if needed.

## 📁 Project Structure

```
Scraping-Google-Maps-Review/
├── main.py              # Main scraper script (updated version)
├── requirements.txt     # Python dependencies
├── output.csv          # Generated output file
├── Scraping_gmaps/     # Alternative version
│   ├── main.py
│   ├── Read me.txt
│   └── requirements.txt
└── README.md           # This file
```

## 🛠️ Dependencies

Key libraries used:
- `selenium` - Browser automation
- `beautifulsoup4` - HTML parsing
- `lxml` - XML/HTML parser
- `webdriver-manager` - Automatic ChromeDriver management
- `requests` - HTTP library

See `requirements.txt` for the complete list.

## ⚠️ Important Notes

- **Rate Limiting**: Be mindful of Google's rate limits. Excessive scraping may result in temporary blocks.
- **Terms of Service**: Ensure compliance with Google Maps Terms of Service when using this tool.
- **Reliability**: Google Maps structure may change, which could break the scraper. Regular expression patterns may need updates.
- **Internet Connection**: Stable internet connection is required for proper operation.

## 🐛 Troubleshooting

### Common Issues

1. **ChromeDriver not found**: The webdriver-manager should handle this automatically, but ensure Chrome browser is installed.

2. **Timeout errors**: Increase the `time.sleep()` duration if pages are loading slowly.

3. **No data scraped**: Google Maps may have changed its HTML structure. Check and update the regular expressions in the code.

4. **SSL errors**: If you encounter SSL certificate errors, ensure your system certificates are up to date.

## 📝 Example

```python
# Example URL format
url_map = "https://www.google.com/maps/place/[Place+Name]/@[coordinates]/data=..."

# Run the scraper
main(url_map)

# Output will be saved to output.csv
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📄 License

This project is for educational purposes. Please use responsibly and in accordance with Google's Terms of Service.

## 👤 Author

**Zulfa Falah**
- GitHub: [@zulfafalah](https://github.com/zulfafalah)

## 🙏 Acknowledgments

- Thanks to the Selenium and BeautifulSoup communities for their excellent documentation
- webdriver-manager for simplifying ChromeDriver management

---

**Disclaimer**: This tool is for educational and research purposes only. Users are responsible for ensuring their use complies with Google Maps Terms of Service and applicable laws.
