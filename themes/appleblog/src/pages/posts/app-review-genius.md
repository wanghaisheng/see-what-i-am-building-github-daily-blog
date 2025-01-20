---
author: Heisenberg
cover:
  alt: cover
  square: https://daily.borninsea.com/assets/image_1737344844151_jujt6o.png
  url: https://daily.borninsea.com/assets/image_1737344844151_jujt6o.png
description: No description provided.
featured: true
keywords: app-review-genius,  capcut,  ios app,  daily top 100,  github action,  historical
  data,  medical industry,  game,  health,  app review dataset,  hunt apps,  waybackmachine,  google
  search,  sitemaps,  app basic info,  itune api,  release date,  developer id,  genres,  screenshot,  continuous
  search,  historical reviews,  app reviews,  keyword search,  app store,  developer
  profile,  category,  top 100 apps,  insight,  analysis,  related apps,  feedback
  types,  GPT-4,  app store scraper,  Candy Crush Saga
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Heisenberg
  name: author
- content: app-review-genius,  capcut,  ios app,  daily top 100,  github action,  historical
    data,  medical industry,  game,  health,  app review dataset,  hunt apps,  waybackmachine,  google
    search,  sitemaps,  app basic info,  itune api,  release date,  developer id,  genres,  screenshot,  continuous
    search,  historical reviews,  app reviews,  keyword search,  app store,  developer
    profile,  category,  top 100 apps,  insight,  analysis,  related apps,  feedback
    types,  GPT-4,  app store scraper,  Candy Crush Saga
  name: keywords
pubDate: '2025-01-20'
tags:
- app-review-genius
- capcut
- ios-app
- top100
- github-action
- health
- game
- medical
- app-review-dataset
- waybackmachine
- google-search
- sitemaps
- app-basic-info
- itune-api
- historical-reviews
- keyword-search
- app-store
- developer-profile
- category-tracking
- insight
- analysis
- related-apps
- feedback-types
- app-store-scraper
- candy-crush-saga
theme: light
title: 'Building App-Review-Genius: Automating iOS Insights with GitHub Actions'
---



*Built by wanghaisheng | Last updated: 20250120*

12 minutes 22 seconds  read
## Project Genesis

### How to Build an iOS App Review Dataset in 5 Minutes Without Coding

Two years ago, I embarked on a journey to scrape app reviews for CapCut, a project that ignited my passion for data analysis and app insights. You can check out my initial foray on GitHub [here](https://github.com/wanghaisheng/scrape-app-reviews-without-coding). Fast forward to today, and I find myself reflecting on the wisdom of a tech guru who once advised me to keep a close eye on app rankings. Life got busy, and I let that advice linger in the back of my mind—until now.

After dedicating a day to finally tackle the iOS app daily Top 100, I realized how much I had missed this world of data exploration. Thanks to GitHub Actions, I can now automate the process, allowing me to gather insights while I sleep. Imagine waking up to a neatly organized dataset, ready for review—it's like having a personal assistant who works tirelessly while you dream!

As someone with a background in the medical field, I’ve always been fascinated by the intersection of health and technology. My ultimate goal is to merge these two passions, focusing on health apps that can make a real difference. So, naturally, I prioritized the health category for this project. 

Of course, the journey wasn’t without its challenges. Initially, I struggled with how to efficiently gather historical data and keep it updated. But after some trial and error, I discovered a few clever techniques: using the Wayback Machine for historical snapshots, leveraging Google searches for continuous app tracking, and utilizing sitemaps for ongoing updates. 

In this blog post, I’ll share how you can build your own iOS app review dataset in just five minutes—no coding required! Join me as I dive into the tools and strategies that made this project not only possible but also incredibly rewarding. Let’s unlock the potential of app reviews together!

## From Idea to Implementation

### 1. Initial Research and Planning

The journey began with a keen interest in the intersection of gaming and healthcare, inspired by the potential of mobile applications to enhance user engagement in both fields. The initial research phase involved exploring existing tools and methodologies for scraping app reviews, particularly focusing on iOS applications. A notable reference was the repository by Wang Haisheng, which provided insights into scraping app reviews without coding. This laid the groundwork for understanding the landscape of app review data collection.

The planning phase included identifying the key objectives of the project: to build a comprehensive dataset of iOS app reviews, particularly in the health category, and to derive actionable insights from this data. The decision to focus on the health category stemmed from a personal background in the medical field, aiming to leverage gaming elements to improve health-related applications.

### 2. Technical Decisions and Their Rationale

Several technical decisions were made during the project, each with a specific rationale:

- **Use of GitHub Actions**: Automating the data collection process using GitHub Actions allowed for continuous scraping of app reviews without manual intervention. This was particularly beneficial for collecting daily updates while minimizing the workload.

- **Historical Data Collection**: The decision to utilize the Wayback Machine and Google search for historical data was driven by the need to gather a comprehensive dataset that included both current and past reviews. This approach ensured a richer context for analysis.

- **API Utilization**: Leveraging the iTunes API for app metadata (e.g., release date, developer ID, genres) was crucial for obtaining structured data efficiently. This decision was based on the need for reliable and consistent data sources.

- **Rate Limiting**: Implementing a rate limit for scraping reviews (e.g., 2 seconds sleep for every 20 reviews) was essential to avoid being blocked by the app store's servers. This decision balanced the need for data collection speed with the risk of being flagged for excessive requests.

### 3. Alternative Approaches Considered

During the planning and execution phases, several alternative approaches were considered:

- **Manual Data Collection**: Initially, manual collection of app reviews was contemplated. However, this approach was quickly deemed impractical due to the sheer volume of data and the time required for manual entry.

- **Using Third-Party Scraping Tools**: While there are several third-party tools available for scraping app reviews, the decision was made to build a custom solution. This allowed for greater flexibility in tailoring the scraping process to specific needs, such as focusing on the health category and integrating insights generation.

- **Focusing on a Broader App Category**: Although the health category was prioritized, there was consideration of expanding to other categories. Ultimately, the decision to focus on health was reinforced by the project's alignment with personal interests and expertise.

### 4. Key Insights that Shaped the Project

Several key insights emerged throughout the project that significantly influenced its direction:

- **Importance of Continuous Data Collection**: The realization that app reviews are dynamic and can change frequently underscored the need for a continuous data collection strategy. This insight led to the implementation of daily scraping routines to keep the dataset up-to-date.

- **Value of Historical Context**: Understanding that historical reviews provide valuable insights into user sentiment over time shaped the approach to data collection. This context is crucial for identifying trends and patterns in user feedback.

- **Leveraging AI for Analysis**: The potential of using AI, specifically GPT-4, to categorize and analyze reviews was a pivotal insight. This capability could transform raw data into actionable insights, enhancing the overall value of the dataset.

- **User-Centric Focus**: Throughout the project, maintaining a user-centric perspective was vital. The goal was not just to collect data but to derive insights that could inform the development of better health-related applications, ultimately benefiting users.

### Conclusion

The journey from concept to code involved a blend of research, technical decision-making, and iterative refinement. By focusing on the health category and leveraging automation, the project aimed to create a robust dataset of iOS app reviews that could drive meaningful insights and innovations at the intersection of gaming and healthcare. The insights gained throughout the process will continue to inform future developments and enhancements in this exciting domain.

## Under the Hood

## Technical Deep-Dive: iOS App Review Dataset Collection

### 1. Architecture Decisions

The architecture of the iOS app review dataset collection system is designed to be modular and efficient, leveraging automation to minimize manual effort. The key components include:

- **Data Collection**: The system is built to scrape app reviews and metadata from various sources, including the App Store, Google Search, and historical data from the Wayback Machine.
- **Automation**: GitHub Actions are utilized to automate the data collection process, allowing the system to run scripts at scheduled intervals (daily, hourly, or weekly) without manual intervention.
- **Data Storage**: Collected data can be stored in a structured format (e.g., JSON, CSV) for easy access and analysis.
- **Insight Generation**: The system incorporates GPT-4 for categorizing reviews and generating insights, enhancing the analysis of user feedback.

### 2. Key Technologies Used

- **GitHub Actions**: For automating the execution of scripts that collect app data and reviews.
- **Web Scraping Libraries**: Libraries such as `BeautifulSoup` or `Scrapy` (not explicitly mentioned but commonly used) for scraping data from web pages.
- **APIs**: Utilization of the iTunes API to fetch app metadata, including release dates, developer IDs, genres, and screenshots.
- **Natural Language Processing (NLP)**: GPT-4 is employed for categorizing reviews and generating insights based on user feedback.

### 3. Interesting Implementation Details

- **Historical Data Collection**: The system uses the Wayback Machine to gather historical app data, which is crucial for understanding trends over time. This is particularly useful for apps with a long history of user reviews.
  
- **Continuous App Tracking**: The system continuously monitors Google Search results for newly released or updated apps. This is achieved by checking the Google SERP (Search Engine Results Page) for the last 24 hours, ensuring that the dataset remains current.

- **Review Collection Strategy**: For apps with a large number of reviews (over 100,000), the system implements a strategy to collect a sample rather than the entire dataset. This is done to manage the load and time required for scraping, with a sleep interval of 2 seconds between requests to avoid being blocked.

- **Keyword-Based Search**: The system allows users to input keywords to find relevant apps and scrape their reviews. This is done through multiple channels, including direct searches in the App Store and Google, as well as checking the sitemap of the App Store.

### 4. Technical Challenges Overcome

- **Rate Limiting and Scraping Ethics**: One of the challenges faced during implementation is adhering to the rate limits imposed by the App Store and Google. The system incorporates sleep intervals and limits the number of reviews collected per app to avoid being flagged as abusive.

- **Data Consistency**: Ensuring that the data collected is consistent and accurate across different sources was a challenge. The implementation includes checks to validate the data retrieved from various APIs and scraping methods.

- **Scalability**: As the number of apps and reviews grows, the system needed to be scalable. By using GitHub Actions and modular scripts, the architecture allows for easy scaling of data collection processes without significant rework.

### Code Concepts

Here are some code snippets that illustrate key concepts from the implementation:

#### Example: Scraping App Metadata

```python
import requests
from bs4 import BeautifulSoup

def scrape_app_metadata(app_id):
    url = f"https://itunes.apple.com/us/app/id{app_id}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    app_data = {
        'title': soup.find('h1').text,
        'developer': soup.find('a', class_='link').text,
        'release_date': soup.find('time')['datetime'],
        'genres': [genre.text for genre in soup.find_all('a', class_='genre')]
    }
    
    return app_data
```

#### Example: Automating Data Collection with GitHub Actions

```yaml
name: Daily App Review Collection

on:
  schedule:
    - cron: '0 0 * * *'  # Runs daily at midnight

jobs:
  collect_reviews:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Run data collection script
        run: python get-top100-app-daily.py
```

#### Example: Categorizing Reviews with GPT-4

```python
import openai

def categorize_reviews(reviews):
    categorized_reviews = {}
    for review in reviews:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": f"Categorize this review: {review}"}
            ]
        )
        category = response['choices'][0]['message']['content']

## Lessons from the Trenches

Based on your project history and README, here are some key technical lessons learned, what worked well, what you might do differently, and advice for others:

### Key Technical Lessons Learned
1. **Automation is Key**: Utilizing GitHub Actions for automating the data collection process proved to be efficient. It allows for continuous data gathering without manual intervention, which is crucial for keeping the dataset up-to-date.
  
2. **Diverse Data Sources**: Leveraging multiple sources (Wayback Machine, Google Search, sitemaps) for app discovery and historical data collection is essential. This approach helps in building a comprehensive dataset.

3. **Rate Limiting and Throttling**: Implementing sleep intervals between requests (e.g., 2 seconds for collecting reviews) is vital to avoid being blocked by the app store or search engines. This ensures sustainable scraping practices.

4. **Data Structuring**: Structuring the collected data effectively (e.g., app details, reviews, developer info) is crucial for analysis. Using a consistent format makes it easier to perform insights and analytics later.

5. **Keyword Expansion**: Using keywords to discover related apps and reviews can significantly enhance the dataset. This method can lead to discovering niche apps that may not be in the top rankings but have valuable user feedback.

### What Worked Well
1. **Daily Tracking of Top Apps**: The implementation of a daily script to track the top 100 apps in the health category has been effective. This allows for timely insights into market trends and user preferences.

2. **Integration with GPT-4**: Utilizing GPT-4 for categorizing reviews into feedback types is a powerful way to analyze user sentiment and feature requests, although it’s still in the testing phase.

3. **Historical Data Collection**: The ability to collect historical reviews for apps with a large number of reviews has provided a rich dataset for analysis, allowing for trend identification over time.

### What You'd Do Differently
1. **Testing and Iteration**: Prioritize testing the historical data mining script and iterating based on the results. Early testing can help identify potential issues before scaling up the data collection.

2. **Error Handling**: Implement more robust error handling and logging mechanisms to track issues during scraping. This will help in diagnosing problems quickly and maintaining data integrity.

3. **User Feedback Loop**: Consider creating a feedback loop where users of the dataset can provide insights or request additional features. This could guide future development and enhancements.

### Advice for Others
1. **Start Small**: If you're new to data scraping, start with a small subset of apps or reviews. Gradually scale up as you become more comfortable with the tools and techniques.

2. **Respect Terms of Service**: Always review and respect the terms of service of the platforms you are scraping. This helps avoid legal issues and ensures ethical data collection practices.

3. **Documentation**: Maintain thorough documentation of your processes, scripts, and findings. This will be invaluable for future reference and for anyone else who may work on the project.

4. **Community Engagement**: Engage with the developer community on platforms like GitHub. Sharing your findings and learning from others can lead to valuable insights and collaborations.

5. **Focus on Insights**: While collecting data is important, focus on deriving actionable insights from the data. This will make your project more impactful and relevant to your goals in the health and gaming sectors.

By following these lessons and advice, you can enhance your project and make it more effective in achieving your goals in the intersection of gaming and healthcare.

## What's Next?

### Conclusion for App-Review-Genius

As we reflect on the journey of App-Review-Genius, we are excited to share our current project status and future development plans. Over the past two years, we have made significant strides in our app review scraping capabilities, particularly with our focus on the iOS app landscape. Our recent implementation of a daily tracking system for the top 100 health apps has streamlined our data collection process, allowing us to gather insights effortlessly while we sleep. The integration of GitHub Actions has minimized manual effort, enabling us to focus on analysis and insights.

Looking ahead, our development plans are ambitious. We aim to enhance our historical data mining capabilities and refine our insights generation using advanced AI techniques, including the categorization of reviews with GPT-4. We also plan to expand our focus beyond health apps to include other categories, thereby broadening our dataset and insights. Additionally, we are eager to test and improve the scripts we have developed, ensuring they are robust and effective in delivering valuable data.

We invite contributors to join us on this exciting journey. Whether you are a developer, data analyst, or simply passionate about app reviews, your insights and contributions can help us refine our tools and expand our reach. Together, we can create a comprehensive resource that benefits developers, marketers, and users alike.

In closing, the journey of App-Review-Genius has been both challenging and rewarding. It has been a side project fueled by passion and curiosity, and we are grateful for the progress we have made. As we continue to evolve and grow, we look forward to the collaborative efforts that will shape the future of this project. Let’s harness the power of app reviews to drive innovation and improve user experiences in the app ecosystem. Join us, and let’s make a difference together!
## Project Development Analytics
### timeline gant

![Commit timelinegant](https://daily.borninsea.com/assets/app-review-genius-timeline_chart.png)


### Commit Activity Heatmap
This heatmap shows the distribution of commits over the past year:

![Commit Heatmap]()

### Contributor Network
This network diagram shows how different contributors interact:

![Contributor Network](https://daily.borninsea.com/assets/app-review-genius-contribution_network.png)

### Commit Activity Patterns
This chart shows when commits typically happen:

![Commit Activity](https://daily.borninsea.com/assets/app-review-genius-commit_activity.png)

### Code Frequency
This chart shows the frequency of code changes over time:

![Code Frequency](https://daily.borninsea.com/assets/app-review-genius-code_frequency.png)



* Repository URL: [https://github.com/wanghaisheng/app-review-genius](https://github.com/wanghaisheng/app-review-genius)
* Stars: **0**
* Forks: **1**
