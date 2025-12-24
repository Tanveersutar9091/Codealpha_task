**🕸️ Web Scraping & Custom Dataset Creation**

This project demonstrates the ability to programmatically extract unstructured data from the web and transform it into a structured, analysis-ready format. Using **Python**, **BeautifulSoup**, and **Requests**, I developed a scraper to navigate a multi-page web environment and build a custom dataset.

**🎯 Project Objectives**

- **Automated Extraction:** Use Python libraries to extract data from public web pages.
- **Data Navigation:** Handle HTML structure and multi-page pagination to gather comprehensive data.
- **Data Cleaning:** Process raw HTML strings into clean numerical and categorical formats.
- **Dataset Customization:** Create a tailored CSV dataset specifically designed for future analysis (EDA).

**🛠️ The Technical Workflow**

- **Request & Response:** Mimicked a real browser using headers (User-Agent) to securely access the target server.
- **Parsing HTML:** Used the html.parser to navigate the DOM tree and identify specific tags like &lt;article class="product_pod"&gt;.
- **Data Extraction:** Targeted specific attributes, such as:
  - **Titles:** From the title attribute of the anchor tags.
  - **Prices:** Extracted and cleaned of currency artifacts using string manipulation.
  - **Ratings:** Derived from the class attributes of the star-rating paragraph tags.
- **Pagination:** Implemented a for loop to dynamically generate URLs and scrape multiple pages automatically.

**📊 Comparison of Approaches**

While this repository focuses on Python-based scraping, I also recognize the value of automated tools for different use cases:

| **Feature** | **BeautifulSoup (My Code)** | **No-Code Tools (Octoparse/ParseHub)** |
| --- | --- | --- |
| **Logic** | Custom Python Script | Visual Point-and-Click |
| **Speed** | Highly efficient for static pages | Slower due to browser emulation |
| **Cleaning** | Dynamic cleaning via code | Visual filters/GUI options |
| **Best For** | Scaling and Integration | Rapid prototyping/Non-coders |
