---
author: Heisenberg
cover:
  alt: cover
  square: https://daily.borninsea.com/assets/image_1735530102662_ulh1q6d.png
  url: https://daily.borninsea.com/assets/image_1735530102662_ulh1q6d.png
description: 'AniProject: Watch Animes, Read Mangas and make Comments on this website
  made with Next.js, TypeScript, Firebase, Anilist, Consumet and Aniwatch API. AD
  FREE.'
featured: true
keywords: anime,  website,  hub,  AniProject,  watch,  animes,  read,  mangas,  comments,  Next.js,  TypeScript,  Firebase,  AniList,  Consumet,  Aniwatch
  API,  ad free,  project,  cast,  navigation,  features,  quick deploy,  under development,  technologies
  used,  Firebase database,  authentication,  collections,  documents,  users,  notifications,  search,  watch
  episodes,  read manga,  log in,  Anilist integration,  keep watching,  notifications,  mark
  favorites,  news feed,  quick deploy,  environment variables.
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Heisenberg
  name: author
- content: anime,  website,  hub,  AniProject,  watch,  animes,  read,  mangas,  comments,  Next.js,  TypeScript,  Firebase,  AniList,  Consumet,  Aniwatch
    API,  ad free,  project,  cast,  navigation,  features,  quick deploy,  under
    development,  technologies used,  Firebase database,  authentication,  collections,  documents,  users,  notifications,  search,  watch
    episodes,  read manga,  log in,  Anilist integration,  keep watching,  notifications,  mark
    favorites,  news feed,  quick deploy,  environment variables.
  name: keywords
pubDate: '2024-12-30'
tags:
- anime
- website
- hub
- aniproject
- watch
- animes
- read
- mangas
- comments
- next-js
- typescript
- firebase
- anilist
- consumet
- aniwatch-api
- ad-free
- project
- navigation
- features
- quick-deploy
- under-development
- technologies-used
- authentication
- collections
- documents
- users
- notifications
- previews
- screenshots
- search
- watch
- read
- log-in
- anilist-integration
- keep-watching
- be-notified
- mark-favorite
- news-feed
- comment
- deploy
theme: light
title: 'Building AniProject: Crafting an Ad-Free Anime Hub with Next.js & Firebase'
---



*Built by wanghaisheng | Last updated: 20241230*

12 minutes 12 seconds  read
## Project Genesis

# Welcome to AniProject: Your Ultimate Anime and Manga Hub!

As a lifelong anime and manga enthusiast, I’ve always found myself diving deep into the vibrant worlds created by talented artists and storytellers. However, I often faced a common challenge: finding a single, reliable source that could provide comprehensive information about my favorite series, characters, and upcoming releases. This frustration sparked the idea for AniProject—a one-stop hub for all things anime and manga.

My personal motivation for creating AniProject stems from my passion for sharing the joy of anime with others. I wanted to build a platform that not only serves as a resource for fans like myself but also fosters a community where we can discuss, discover, and celebrate our favorite titles together. The thought of connecting with fellow enthusiasts and helping newcomers navigate the vast landscape of anime and manga was incredibly inspiring.

Of course, the journey wasn’t without its challenges. As I embarked on this project, I quickly realized the complexities of integrating multiple APIs, such as AniList, Consumet, and Aniwatch. Each API had its own quirks and requirements, and I often found myself wrestling with data formats and compatibility issues. But with determination and a bit of trial and error, I was able to overcome these hurdles and create a seamless user experience.

The solution? AniProject! By harnessing the power of these APIs, I’ve built a website that offers a wealth of information about anime and manga releases, detailed cast data, and much more—all in one place. Whether you’re a seasoned otaku or just starting your journey into the world of anime, AniProject is designed to be your go-to resource.

I invite you to explore AniProject and join me in celebrating the incredible universe of anime and manga. Together, let’s dive into the stories that captivate our hearts and imaginations! You can check out the website [here](https://aniproject-dev.vercel.app/). Happy exploring!

## From Idea to Implementation

### 1. Initial Research and Planning

The journey of developing AniProject began with extensive research into the anime and manga landscape, identifying the needs of potential users and the existing solutions available in the market. The primary goal was to create a comprehensive platform that aggregates information from various sources, allowing users to search, watch, and read content seamlessly. 

During the planning phase, we analyzed popular anime and manga websites, noting their strengths and weaknesses. This analysis highlighted the demand for features such as personalized user experiences, notifications for new episodes, and integration with existing platforms like AniList. We also explored the APIs available, specifically the AniList, Consumet, and Aniwatch APIs, which provided the necessary data to build our application.

The planning phase culminated in a feature list that prioritized user engagement and ease of use. We aimed to create a non-commercial platform that would serve as a community hub for anime and manga enthusiasts, ensuring that the project adhered to legal guidelines regarding intellectual property.

### 2. Technical Decisions and Their Rationale

The technical stack for AniProject was chosen based on the need for a responsive, dynamic web application that could handle real-time data and user interactions. We opted for **Next.js** as the framework due to its server-side rendering capabilities, which enhance performance and SEO. **TypeScript** was selected for its type safety, making the codebase more maintainable and reducing runtime errors.

For state management, we chose **Redux** to manage the application's state efficiently, especially as user interactions increased. **Firebase** was integrated for authentication and database management, allowing us to leverage its real-time capabilities and ease of use for user data storage.

The decision to use **GraphQL** was driven by the need for efficient data fetching. GraphQL allows us to request only the data we need, reducing the amount of data transferred and improving performance. This was particularly important given the diverse data sources we were aggregating.

### 3. Alternative Approaches Considered

During the planning and development phases, we considered several alternative approaches. One option was to build the application using a traditional REST API instead of GraphQL. However, we ultimately decided on GraphQL for its flexibility and efficiency in handling complex queries, which was essential for our feature set.

Another alternative was to use a different front-end framework, such as Angular or Vue.js. However, Next.js's built-in features for server-side rendering and static site generation aligned better with our performance goals and user experience requirements.

We also explored the possibility of using a different database solution, such as MongoDB or PostgreSQL. However, Firebase's real-time capabilities and ease of integration with our chosen tech stack made it the most suitable option for our needs.

### 4. Key Insights That Shaped the Project

Several key insights emerged throughout the development of AniProject that significantly shaped the project:

- **User-Centric Design**: The importance of a user-friendly interface became evident early on. We prioritized features that enhance user engagement, such as personalized watchlists, notifications for new episodes, and the ability to mark favorite content. This focus on user experience guided our design and development decisions.

- **Community Engagement**: Understanding the community aspect of anime and manga consumption was crucial. We recognized that users often seek recommendations and discussions about their favorite shows. This insight led to the inclusion of features like a news feed and the ability to track and share progress on watched episodes.

- **Scalability and Flexibility**: As we built the application, we realized the need for a scalable architecture that could accommodate future features and user growth. This understanding influenced our choice of technologies, ensuring that the application could evolve without significant overhauls.

- **Legal Considerations**: The non-commercial nature of the project necessitated a careful approach to content usage. We ensured that our implementation adhered to legal guidelines, which shaped our decisions regarding API usage and data handling.

In conclusion, the journey from concept to code for AniProject was marked by thorough research, thoughtful technical decisions, and a commitment to user experience. The insights gained throughout the process not only shaped the project but also laid a strong foundation for future enhancements and community engagement.

## Under the Hood

# Technical Deep-Dive: AniProject

## 1. Architecture Decisions

AniProject is designed as a web application that serves as a platform for users to explore, watch, and read content related to anime and manga. The architecture is primarily based on a client-server model, utilizing a combination of front-end and back-end technologies to deliver a seamless user experience.

### Client-Side Architecture
- **Framework**: The front-end is built using **Next.js**, a React framework that enables server-side rendering and static site generation. This choice enhances performance and SEO, making the application more accessible.
- **State Management**: **Redux** is employed for state management, allowing for a centralized store to manage the application's state, which is particularly useful for handling user authentication and media data.
- **API Integration**: The application integrates with multiple APIs (AniList, Consumet, and Aniwatch) to fetch data about anime and manga. This modular approach allows for easy updates and maintenance of API connections.

### Server-Side Architecture
- **Back-End**: The back-end is powered by **Firebase**, which provides a Firestore database for data storage and Firebase Authentication for user management. This eliminates the need for a custom server, simplifying deployment and scaling.
- **Environment Configuration**: The application relies on environment variables to manage sensitive information and API keys, ensuring that configurations can be easily adjusted for different environments (development, staging, production).

## 2. Key Technologies Used

- **Next.js**: For building the front-end, enabling server-side rendering and static site generation.
- **TypeScript**: Provides type safety, improving code quality and maintainability.
- **Firebase**: Used for authentication and as a NoSQL database, allowing for real-time data synchronization.
- **Axios**: For making HTTP requests to external APIs.
- **GraphQL**: Utilized for querying data from APIs, providing a flexible and efficient way to retrieve only the data needed.
- **Framer Motion**: For animations, enhancing the user experience with smooth transitions and interactions.

## 3. Interesting Implementation Details

### User Authentication
The application supports multiple authentication methods, including Google, Anilist, and anonymous login. The implementation leverages Firebase Authentication, which simplifies the process of managing user sessions.

```javascript
import firebase from 'firebase/app';
import 'firebase/auth';

const signInWithGoogle = async () => {
  const provider = new firebase.auth.GoogleAuthProvider();
  const result = await firebase.auth().signInWithPopup(provider);
  // Handle result
};
```

### Data Fetching
Data fetching is handled through Axios, with a focus on modularity. Each API call is encapsulated in a service file, making it easy to manage and update.

```javascript
import axios from 'axios';

const fetchAnimeData = async (animeId) => {
  const response = await axios.get(`https://api.example.com/anime/${animeId}`);
  return response.data;
};
```

### Firestore Database Structure
The Firestore database is organized into collections for users, comments, and notifications. This structure allows for efficient querying and data retrieval.

```javascript
const userRef = firebase.firestore().collection('users').doc(userId);
const userData = await userRef.get();
```

## 4. Technical Challenges Overcome

### API Rate Limiting
One of the challenges faced was managing API rate limits imposed by external services. To mitigate this, the application implements caching strategies to store frequently accessed data, reducing the number of API calls.

### Cold Start Issues
When deploying on platforms like Vercel, cold start issues can lead to slow initial load times. To address this, the application uses server-side rendering for critical pages, ensuring that users receive content quickly.

### Handling User Preferences
Managing user preferences for media sources and content types required careful consideration of data structure and user experience. The application allows users to customize their experience, which is stored in the Firestore database.

```javascript
const updateUserPreferences = async (userId, preferences) => {
  await firebase.firestore().collection('users').doc(userId).update({
    preferences: preferences,
  });
};
```

### Conclusion
AniProject showcases a well-structured architecture that leverages modern web technologies to create a dynamic and user-friendly platform for anime and manga enthusiasts. The combination of Next.js, Firebase, and various APIs allows for a scalable and maintainable application, while the challenges faced during development have led to robust solutions that enhance the overall user experience.

## Lessons from the Trenches

### Key Technical Lessons Learned

1. **API Integration**: Successfully integrating multiple APIs (AniList, Consumet, and Aniwatch) taught me the importance of understanding each API's documentation and capabilities. I learned how to handle asynchronous requests and manage data flow between the front-end and back-end effectively.

2. **State Management**: Utilizing Redux for state management helped me understand the importance of maintaining a predictable state in a complex application. It allowed for easier debugging and improved performance by minimizing unnecessary re-renders.

3. **Firebase Authentication**: Implementing Firebase for user authentication provided insights into secure user management. I learned how to configure authentication methods and manage user sessions effectively.

4. **Environment Variables**: Managing environment variables for different deployment environments (development, staging, production) was crucial. It reinforced the need for security and flexibility in handling sensitive information.

5. **Responsive Design**: Building a responsive UI using CSS frameworks and custom styles taught me the importance of user experience across different devices. I learned to use media queries and flexible layouts to ensure accessibility.

### What Worked Well

1. **Modular Architecture**: The project’s modular structure allowed for easy maintenance and scalability. Each component was designed to be reusable, which simplified the development process.

2. **User Experience Features**: Features like "Keep Watching" and notifications for new episodes significantly enhanced user engagement. These features were well-received during testing and contributed to a positive user experience.

3. **Deployment Process**: The deployment process on platforms like Vercel and Render was straightforward. The integration of CI/CD practices allowed for quick updates and rollbacks, which streamlined the development workflow.

4. **Community Feedback**: Engaging with the anime community for feedback on features and design helped refine the application. User input was invaluable in prioritizing development tasks and improving overall functionality.

### What You'd Do Differently

1. **Documentation**: While the README provided a good overview, I would invest more time in creating comprehensive documentation for developers. This would include detailed API usage examples, component structure, and troubleshooting tips.

2. **Testing**: Implementing a more robust testing strategy (unit tests, integration tests) would have been beneficial. Automated testing could help catch bugs early and ensure that new features do not break existing functionality.

3. **Performance Optimization**: I would focus more on performance optimization techniques, such as code splitting and lazy loading, to improve the initial load time of the application.

4. **User Analytics**: Integrating user analytics from the start would provide insights into user behavior and help prioritize features based on actual usage patterns.

### Advice for Others

1. **Plan Before You Code**: Spend time planning the architecture and features of your project before diving into coding. A clear roadmap can save time and effort in the long run.

2. **Leverage Open Source**: Utilize existing open-source libraries and frameworks to speed up development. Don’t reinvent the wheel; instead, build upon the work of others.

3. **Engage with Users Early**: Involve potential users in the development process early on. Their feedback can guide feature development and help create a product that meets their needs.

4. **Stay Updated**: Technology evolves rapidly, so keep learning and stay updated with the latest trends and best practices in web development. This will help you make informed decisions and improve your skills continuously.

5. **Focus on Security**: Always prioritize security, especially when handling user data. Implement best practices for authentication, data storage, and API usage to protect your application and its users.

## What's Next?

## Conclusion

As we wrap up this phase of the AniProject journey, we are excited to share our current project status and future development plans. The AniProject website is live and operational, providing users with a comprehensive platform to explore and enjoy their favorite animes and mangas. With features like search filters, episode tracking, and notifications for new releases, we have laid a solid foundation for an engaging user experience.

Looking ahead, we have ambitious plans for further development. Our roadmap includes essential bug fixes, the introduction of new media sources, enhanced video player features, and the creation of a personalized profile page. We are also working on exciting features like hiding next episode images to avoid spoilers and a schedule section to keep users informed about upcoming releases. These enhancements will not only improve functionality but also enrich the overall user experience.

We invite all contributors, whether you are a developer, designer, or anime enthusiast, to join us in this exciting venture. Your insights, skills, and creativity can help shape the future of AniProject. Whether you want to contribute code, design elements, or even share your thoughts on potential features, your involvement is invaluable. Together, we can build a vibrant community around this project.

Reflecting on this side project journey, we are grateful for the support and enthusiasm from our contributors and users alike. The development of AniProject has been a labor of love, driven by our passion for anime and manga. As we continue to grow and evolve, we remain committed to creating a platform that celebrates the rich world of anime and manga, fostering connections among fans and providing a space for discovery and enjoyment.

Thank you for being a part of AniProject. We look forward to what the future holds and hope to see you contributing to our shared vision!
## Project Development Analytics
### timeline gant

![Commit timelinegant](https://daily.borninsea.com/assets/anime-website-hub-timeline_chart.png)


### Commit Activity Heatmap
This heatmap shows the distribution of commits over the past year:

![Commit Heatmap]()

### Contributor Network
This network diagram shows how different contributors interact:

![Contributor Network](https://daily.borninsea.com/assets/anime-website-hub-contribution_network.png)

### Commit Activity Patterns
This chart shows when commits typically happen:

![Commit Activity](https://daily.borninsea.com/assets/anime-website-hub-commit_activity.png)

### Code Frequency
This chart shows the frequency of code changes over time:

![Code Frequency](https://daily.borninsea.com/assets/anime-website-hub-code_frequency.png)



* Repository URL: [https://github.com/wanghaisheng/anime-website-hub](https://github.com/wanghaisheng/anime-website-hub)
* Stars: **0**
* Forks: **0**
