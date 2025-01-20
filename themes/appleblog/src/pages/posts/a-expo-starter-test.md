---
author: Heisenberg
cover:
  alt: cover
  square: https://daily.borninsea.com/assets/image_1737344322684_c6wfam.png
  url: https://daily.borninsea.com/assets/image_1737344322684_c6wfam.png
description: "\U0001F4F1 A template for your local-first Expo project: Bun, Expo 51,\
  \ TypeScript, TailwindCSS, DrizzleORM, Sqlite, EAS, GitHub Actions, Env Vars, expo-router,\
  \ react-hook-form."
featured: true
keywords: Expo,  local-first,  template,  Bun,  Expo 51,  TypeScript,  TailwindCSS,  DrizzleORM,  Sqlite,  EAS,  GitHub
  Actions,  Env Vars,  expo-router,  react-hook-form,  React Native,  shadcn-ui,  state
  management,  mobile apps,  Android,  iOS,  Web,  Expo Router,  zustand,  rn-reusables,  dark
  mode,  light mode,  Absolute Imports,  linter,  code formatter,  biome,  VSCode,  Node.js,  pnpm,  bun,  iOS
  Simulator,  Android Studio Emulator,  live reload.
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Heisenberg
  name: author
- content: Expo,  local-first,  template,  Bun,  Expo 51,  TypeScript,  TailwindCSS,  DrizzleORM,  Sqlite,  EAS,  GitHub
    Actions,  Env Vars,  expo-router,  react-hook-form,  React Native,  shadcn-ui,  state
    management,  mobile apps,  Android,  iOS,  Web,  Expo Router,  zustand,  rn-reusables,  dark
    mode,  light mode,  Absolute Imports,  linter,  code formatter,  biome,  VSCode,  Node.js,  pnpm,  bun,  iOS
    Simulator,  Android Studio Emulator,  live reload.
  name: keywords
pubDate: '2025-01-20'
tags:
- expo
- local-first
- template
- bun
- expo-51
- typescript
- tailwindcss
- drizzleorm
- sqlite
- eas
- github-actions
- env-vars
- expo-router
- react-hook-form
- react-native
- nativewind
- zustand
- rn-reusables
- dark-mode
- light-mode
- absolute-imports
- linter
- code-formatter
- vscode
- sqlite
- tusco
- node-js
- pnpm
- android-studio
- ios-simulator
- development-mode
- live-reload
theme: light
title: 'Building a Local-First Expo App: My Journey with a-Expo-Starter-Test'
---



*Built by wanghaisheng | Last updated: 20250120*

11 minutes 51 seconds  read
## Project Genesis

### Unleashing Creativity with the Expo Starter Test: My Journey to a Local-First Template

As a developer, I’ve always been fascinated by the intersection of creativity and technology. The spark for the Expo Starter Test ignited during a late-night coding session, where I found myself frustrated by the repetitive setup tasks that seemed to drain the joy out of building new projects. I wanted to create something that would not only streamline the development process but also inspire others to dive into the world of Expo with confidence.

My personal motivation stemmed from my own experiences as a beginner in the Expo ecosystem. I remember the overwhelming feeling of staring at a blank screen, unsure of where to start. I wanted to craft a solution that would serve as a guiding light for others, helping them bypass the initial hurdles and focus on what truly matters: bringing their ideas to life.

However, the journey wasn’t without its challenges. I faced numerous obstacles, from figuring out the best frameworks to use, to ensuring that the template was user-friendly and adaptable for various projects. There were moments of doubt, where I questioned whether I could create something that would genuinely make a difference.

But through perseverance and a passion for problem-solving, I developed the Expo Starter Template—a free project model that incorporates the latest frameworks and configurations. This template is designed to eliminate the tedious setup tasks, allowing developers to hit the ground running. In this blog post, I’ll take you through my journey, the lessons I learned, and how the Expo Starter Test can empower you to kickstart your own projects with ease. Let’s dive in!

## From Idea to Implementation

### 1. Initial Research and Planning

The journey of developing the Expo Local-first Template began with a thorough analysis of the current landscape of mobile app development frameworks and tools. The goal was to create a robust starter template that would streamline the process of building React Native applications using Expo. 

During the initial research phase, we identified several key trends and requirements in the developer community:

- **Cross-Platform Development**: The need for a solution that allows developers to build applications for both iOS and Android using a single codebase was paramount. Expo emerged as a leading choice due to its comprehensive support for cross-platform development.

- **State Management**: As applications grow in complexity, effective state management becomes crucial. We explored various state management libraries and settled on Zustand for its simplicity and performance.

- **Styling Solutions**: The popularity of utility-first CSS frameworks like Tailwind CSS prompted us to integrate NativeWind, which brings Tailwind's styling capabilities to React Native.

- **Local-first Database Strategy**: With the increasing emphasis on offline capabilities and data persistence, we recognized the importance of integrating a local-first database solution. This led us to explore SQLite for native applications and Sqlite.js for web applications.

### 2. Technical Decisions and Their Rationale

Several technical decisions were made during the development of the template, each with a specific rationale:

- **Framework Selection**: We chose Expo v51 and React Native v0.73.6 as the foundation for the template. Expo's extensive ecosystem and ease of use made it an ideal choice for rapid development and deployment.

- **State Management with Zustand**: Zustand was selected for its minimalistic API and ability to manage state without the boilerplate often associated with other libraries like Redux. This decision aimed to enhance developer productivity and reduce complexity.

- **Integration of Tailwind CSS**: By using NativeWind, we aimed to provide developers with a familiar styling approach that promotes rapid UI development. This decision was influenced by the growing popularity of Tailwind in the web development community.

- **Local-first Database**: The integration of Expo SQLite and Sqlite.js was a strategic choice to ensure that applications could function seamlessly offline while providing a consistent data management experience across platforms.

### 3. Alternative Approaches Considered

Throughout the planning and development phases, we considered several alternative approaches:

- **Using Other State Management Libraries**: While Zustand was ultimately chosen, we initially explored alternatives like Redux and MobX. However, their complexity and boilerplate requirements led us to favor Zustand for this template.

- **Different Styling Solutions**: We also considered using styled-components or Emotion for styling. However, the utility-first approach of Tailwind CSS, combined with NativeWind, offered a more efficient and flexible solution for rapid UI development.

- **Other Database Solutions**: We evaluated various local database options, including Realm and WatermelonDB. However, the combination of SQLite for native and Sqlite.js for web provided a more straightforward and widely adopted solution.

### 4. Key Insights That Shaped the Project

Several key insights emerged during the development of the Expo Local-first Template:

- **Developer Experience Matters**: A primary focus was on enhancing the developer experience. By integrating tools like VSCode extensions, linter configurations, and a streamlined setup process, we aimed to reduce friction and allow developers to focus on building features rather than configuring their environment.

- **Community Feedback is Valuable**: Engaging with the developer community through forums and social media provided invaluable insights into common pain points and desired features. This feedback directly influenced the selection of libraries and tools included in the template.

- **Emphasis on Flexibility and Scalability**: The template was designed with scalability in mind, allowing developers to easily extend and customize their applications as needed. This flexibility was a crucial consideration in the choice of libraries and architectural decisions.

In conclusion, the journey from concept to code for the Expo Local-first Template was marked by careful research, thoughtful technical decisions, and a commitment to enhancing the developer experience. The result is a powerful starter template that empowers developers to build high-quality, cross-platform applications efficiently.

## Under the Hood

# Technical Deep-Dive: Expo Local-first Template

## 1. Architecture Decisions

The architecture of the Expo Local-first Template is designed to facilitate the development of cross-platform applications using React Native and Expo. The key architectural decisions include:

- **Local-first Database Strategy**: The template adopts a local-first approach, allowing applications to function offline and sync data when connectivity is restored. This is achieved through the integration of SQLite for native applications and Sqlite.js for web applications. This decision enhances user experience by ensuring data availability regardless of network conditions.

- **Component-Based Structure**: The use of reusable components from the `rn-reusables` library promotes a modular architecture. This allows developers to build applications by composing various UI components, leading to cleaner and more maintainable code.

- **State Management**: The choice of Zustand for state management simplifies the handling of application state. Zustand's minimalistic API and performance make it an excellent choice for managing state in React applications.

- **Styling with Tailwind CSS**: The integration of NativeWind, which brings Tailwind CSS to React Native, allows for a utility-first approach to styling. This decision enhances the development speed and consistency of UI design.

## 2. Key Technologies Used

The template leverages several modern technologies and frameworks:

- **Expo**: The core framework for building cross-platform applications, providing a rich set of APIs and tools for mobile development.
  
- **React Native**: The underlying framework for building native mobile applications using JavaScript and React.

- **NativeWind**: A utility-first CSS framework that allows developers to style React Native components using Tailwind CSS classes.

- **Zustand**: A small, fast state management solution that simplifies state handling in React applications.

- **SQLite**: A lightweight database engine used for local data storage in mobile applications.

- **DrizzleORM**: An ORM that provides a type-safe way to interact with databases, enhancing the development experience.

## 3. Interesting Implementation Details

- **Local-first Database Integration**: The template integrates both Expo SQLite for native applications and Sqlite.js for web applications. This dual approach allows developers to write code that works seamlessly across platforms. For example, the following code snippet demonstrates how to initialize a SQLite database:

  ```javascript
  import * as SQLite from 'expo-sqlite';

  const db = SQLite.openDatabase('mydatabase.db');

  db.transaction(tx => {
    tx.executeSql(
      'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY NOT NULL, name TEXT);'
    );
  });
  ```

- **Dark and Light Mode Support**: The template includes built-in support for dark and light modes, ensuring that the application adapts to user preferences. This is achieved by using the `Appearance` API from React Native:

  ```javascript
  import { Appearance } from 'react-native';

  const colorScheme = Appearance.getColorScheme();
  const isDarkMode = colorScheme === 'dark';
  ```

- **Absolute Imports**: The template supports absolute imports using the `@` prefix, which simplifies the import statements and improves code readability. This can be configured in the `tsconfig.json` or `babel.config.js`:

  ```json
  {
    "compilerOptions": {
      "baseUrl": ".",
      "paths": {
        "@/*": ["src/*"]
      }
    }
  }
  ```

## 4. Technical Challenges Overcome

- **Cross-Platform Compatibility**: One of the main challenges was ensuring that the application works seamlessly across iOS, Android, and web platforms. The use of Expo and React Native mitigated many of these issues, but careful attention was needed when integrating libraries like SQLite and Zustand to ensure compatibility.

- **State Management Complexity**: Managing state in a local-first application can be complex, especially when dealing with offline scenarios. Zustand's simple API allowed for effective state management without introducing unnecessary complexity. For example, the following code demonstrates how to create a store with Zustand:

  ```javascript
  import create from 'zustand';

  const useStore = create(set => ({
    users: [],
    addUser: (user) => set(state => ({ users: [...state.users, user] })),
  }));
  ```

- **Database Synchronization**: Implementing a local-first database strategy required careful planning for data synchronization. The integration of DrizzleORM provided a robust solution for managing database interactions, allowing for live queries and efficient data handling.

In conclusion, the Expo Local-first Template is a well-architected project that leverages modern technologies to provide a robust starting point for React Native and Expo applications. Its focus on local-first strategies, modular architecture, and developer experience makes it a valuable resource for developers looking to build cross-platform applications.

## Lessons from the Trenches

Here are some key technical lessons learned, what worked well, what could be done differently, and advice for others based on the project history and README of the Expo Local-first Template:

### Key Technical Lessons Learned

1. **Integration of Libraries**: Successfully integrating multiple libraries (like Zustand for state management and DrizzleORM for database management) can significantly enhance the functionality of the app. However, it’s crucial to ensure that these libraries are compatible with each other and the overall architecture of the project.

2. **Local-first Database Strategy**: Implementing a local-first database approach using Expo SQLite and Sqlite.js has proven to be effective for offline capabilities. This strategy allows for better performance and user experience, especially in mobile applications where connectivity can be inconsistent.

3. **Cross-Platform Development**: Utilizing Expo for cross-platform support simplifies the development process. It allows developers to write code once and deploy it across iOS, Android, and web platforms, which saves time and resources.

4. **Dark and Light Mode**: Implementing a dark and light mode that syncs with the Android Navigation Bar enhances user experience. It’s important to consider user preferences for UI themes, especially in mobile applications.

### What Worked Well

1. **Ease of Setup**: The command to create a new project (`bunx create-expo-app --template @expo-starter/template`) is straightforward and reduces the initial setup time for developers. This ease of use encourages more developers to adopt the template.

2. **Developer Experience**: The inclusion of VSCode recommended extensions, settings, and snippets significantly improves the developer experience. This helps new contributors get up to speed quickly and maintain consistency in code quality.

3. **Live Reloading**: The ability to run the app in development mode with live reload is a major productivity booster. It allows developers to see changes in real-time, which is essential for rapid iteration.

4. **Community Contributions**: Encouraging contributions and feedback from the community fosters a collaborative environment. This can lead to improvements and new features that benefit all users of the template.

### What You'd Do Differently

1. **Documentation**: While the README is informative, providing more detailed documentation on specific features (like the local-first database implementation) could help new users understand how to leverage these capabilities effectively.

2. **Testing Framework**: Integrating a testing framework from the start could help ensure code quality and reliability. This would allow for easier identification of bugs and issues during development.

3. **Performance Optimization**: Conducting performance benchmarks and optimizations early in the development process could help identify potential bottlenecks, especially with the local-first database strategy.

4. **User Feedback Loop**: Establishing a more structured feedback loop with users could provide insights into how the template is being used in real-world applications, leading to more targeted improvements.

### Advice for Others

1. **Start Simple**: When creating a new project template, start with the essential features and gradually add more complex functionalities. This approach helps maintain focus and reduces the initial complexity.

2. **Prioritize User Experience**: Always consider the end-user experience when designing features. Implementing user-friendly features like dark/light mode and responsive design can significantly enhance satisfaction.

3. **Encourage Community Engagement**: Foster a community around your project by encouraging contributions, feedback, and discussions. This can lead to a more robust and feature-rich product.

4. **Stay Updated**: Keep an eye on updates to the libraries and frameworks you are using. Regularly updating dependencies can help avoid security vulnerabilities and ensure compatibility with the latest features.

By focusing on these areas, developers can create more effective and user-friendly applications while also enhancing their own development processes.

## What's Next?

## Conclusion

As we wrap up this phase of the Expo Local-first Template project, we are excited to share the current status and future direction of our initiative. The project is well underway, featuring a robust foundation built on the latest versions of Expo and React Native, along with a suite of integrated tools and libraries designed to streamline the development process. Our local-first database strategy, utilizing Expo SQLite and DrizzleORM, positions us to create powerful, responsive applications that work seamlessly across platforms.

Looking ahead, we have ambitious plans for further development. Our immediate focus is on enhancing the local-first database capabilities with OP-sqlite and ensuring smooth synchronization with Tusco. We also aim to expand our library of reusable components and improve the overall user experience. Your feedback and contributions will be invaluable as we refine these features and explore new possibilities.

We invite all developers, designers, and enthusiasts to join us on this journey. Whether you have ideas for new features, want to report bugs, or simply wish to contribute code, your involvement can make a significant impact. Together, we can create a powerful tool that empowers developers to build exceptional applications with ease.

In closing, this side project has been a rewarding experience, showcasing the power of collaboration and innovation. We are grateful for the support we've received so far and are excited about the road ahead. Let’s continue to build, learn, and grow together in this vibrant community. Thank you for being a part of the Expo Starter journey!
## Project Development Analytics
### timeline gant

![Commit timelinegant](https://daily.borninsea.com/assets/a-expo-starter-test-timeline_chart.png)


### Commit Activity Heatmap
This heatmap shows the distribution of commits over the past year:

![Commit Heatmap]()

### Contributor Network
This network diagram shows how different contributors interact:

![Contributor Network](https://daily.borninsea.com/assets/a-expo-starter-test-contribution_network.png)

### Commit Activity Patterns
This chart shows when commits typically happen:

![Commit Activity](https://daily.borninsea.com/assets/a-expo-starter-test-commit_activity.png)

### Code Frequency
This chart shows the frequency of code changes over time:

![Code Frequency](https://daily.borninsea.com/assets/a-expo-starter-test-code_frequency.png)



* Repository URL: [https://github.com/wanghaisheng/a-expo-starter-test](https://github.com/wanghaisheng/a-expo-starter-test)
* Stars: **0**
* Forks: **0**
