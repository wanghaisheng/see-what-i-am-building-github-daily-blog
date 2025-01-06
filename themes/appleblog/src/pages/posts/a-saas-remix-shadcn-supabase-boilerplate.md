---
author: Heisenberg
cover:
  alt: cover
  square: https://daily.borninsea.com/assets/image_1736135953793_096dz.png
  url: https://daily.borninsea.com/assets/image_1736135953793_096dz.png
description: (Corpify) A starter application for SaaS projects built with a modern
  stack (Remix Shadcn and Supabase)
featured: true
keywords: SaaS,  application,  Remix,  Shadcn,  Supabase,  boilerplate,  Vite,  authentication,  signup,  login,  password,  logout,  protected
  routes,  dashboard,  documentation,  pricing,  Stripe,  integration,  clone,  install,  project,  email,  rate
  limits,  third-party service,  development,  seed,  database,  Stripe Account,  API
  Keys,  Webhook,  Stripe CLI,  Webhook Secret Key.
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Heisenberg
  name: author
- content: SaaS,  application,  Remix,  Shadcn,  Supabase,  boilerplate,  Vite,  authentication,  signup,  login,  password,  logout,  protected
    routes,  dashboard,  documentation,  pricing,  Stripe,  integration,  clone,  install,  project,  email,  rate
    limits,  third-party service,  development,  seed,  database,  Stripe Account,  API
    Keys,  Webhook,  Stripe CLI,  Webhook Secret Key.
  name: keywords
pubDate: '2025-01-06'
tags:
- saas
- remix
- shadcn
- supabase
- boilerplate
- fullstack
- authentication
- dashboard
- documentation
- pricing
- stripe
- email-service
- development
- webhook
- vite
- typescript
- github
- project-setup
theme: light
title: 'Building a SaaS Boilerplate: My Journey with Remix, Shadcn, and Supabase'
---



*Built by wanghaisheng | Last updated: 20250106*

12 minutes 20 seconds  read
## Project Genesis

### Building the Future: My Journey with the Remix + Vite + shadcn/ui + Supabase Boilerplate

As a developer, I’ve always been fascinated by the endless possibilities that modern web technologies offer. Recently, I found myself yearning for a streamlined way to build fullstack applications that not only look great but also function seamlessly. That’s when the spark of inspiration hit me: why not combine the power of Remix, Vite, shadcn/ui, and Supabase into a single boilerplate? This idea quickly transformed into a passion project that I couldn’t resist diving into.

My motivation for this project was twofold. First, I wanted to create a robust foundation that would allow me—and others—to kickstart new applications without getting bogged down in repetitive setup tasks. Second, I was eager to explore the capabilities of Supabase, a tool that promised to simplify backend development while providing a rich set of features. I envisioned a boilerplate that would not only serve as a practical resource but also inspire creativity and innovation in the developer community.

Of course, every journey has its challenges. As I began to piece together the components, I quickly realized that integrating these technologies was no small feat. I faced hurdles with authentication flows, managing protected routes, and ensuring that the user experience was smooth and intuitive. But with each obstacle, I learned something new, and my determination only grew stronger. I found myself immersed in documentation, experimenting with code, and reaching out to the community for support.

After countless hours of coding, debugging, and refining, I’m thrilled to share the result: a comprehensive boilerplate that combines the best of Remix, Vite, shadcn/ui, and Supabase. This project not only includes a complete authentication flow—allowing users to sign up and log in with email, Google, or GitHub—but also features protected routes and a user-friendly interface. It’s a solution designed to empower developers to build powerful applications quickly and efficiently.

Join me as I take you through the ins and outs of this boilerplate, sharing insights, tips, and the lessons I learned along the way. Whether you’re a seasoned developer or just starting out, I hope this journey inspires you to explore the exciting world of fullstack development!

## From Idea to Implementation

### 1. Initial Research and Planning

The journey of developing the boilerplate for a fullstack application using Remix, Vite, shadcn/ui, and Supabase began with thorough research into the current landscape of web development frameworks and tools. The goal was to create a robust, scalable, and user-friendly application that could serve as a foundation for various projects. 

During the initial phase, the team explored several frameworks and libraries, assessing their strengths and weaknesses. Remix was chosen for its focus on server-rendered applications and its ability to handle data fetching efficiently. Vite was selected for its fast development experience and modern build capabilities. Supabase emerged as a strong choice for backend services due to its ease of use and built-in authentication features. The team also recognized the need for a polished UI, leading to the integration of shadcn/ui, which provided a professional and customizable design.

### 2. Technical Decisions and Their Rationale

Several key technical decisions were made during the development process:

- **Framework Selection**: The combination of Remix and Vite was chosen to leverage Remix's powerful routing and data loading capabilities alongside Vite's fast hot module replacement and build speed. This combination aimed to enhance developer productivity and improve the user experience.

- **Authentication with Supabase**: Supabase was integrated for its comprehensive authentication features, including support for email, Google, and GitHub logins. This decision was driven by the need for a secure and straightforward authentication flow, which is critical for any modern web application.

- **UI Design with shadcn/ui**: The choice of shadcn/ui was influenced by its aesthetic appeal and flexibility. The team wanted to ensure that the application not only functioned well but also provided a visually pleasing experience for users.

- **Email Service Integration**: Given Supabase's limitations on email sending in the free tier, the decision to integrate a third-party email service like Resend was made to ensure reliable email delivery for authentication and notifications.

- **Stripe for Payments**: The integration of Stripe was essential for handling subscriptions and payments. The team recognized the importance of a seamless payment experience and chose Stripe for its robust API and extensive documentation.

### 3. Alternative Approaches Considered

During the planning phase, the team considered several alternative approaches:

- **Different Frameworks**: Other frameworks such as Next.js and Angular were evaluated. However, Remix's focus on server-rendering and data management aligned better with the project’s goals.

- **Backend Options**: While Firebase was considered as an alternative backend service, Supabase was ultimately chosen for its SQL-based database and open-source nature, which provided more flexibility and control.

- **UI Libraries**: The team looked into various UI libraries, including Material-UI and Ant Design. However, shadcn/ui was preferred for its modern design and ease of customization, which matched the project’s aesthetic goals.

### 4. Key Insights That Shaped the Project

Several insights emerged throughout the development process that significantly influenced the project:

- **User Experience is Paramount**: The team learned that a seamless user experience is crucial for user retention. This realization drove the focus on creating a polished UI and a smooth authentication flow.

- **Scalability and Flexibility**: The importance of building a scalable architecture became evident. The choice of technologies that allowed for easy customization and expansion was a key factor in the project’s design.

- **Community and Documentation**: The availability of community support and comprehensive documentation for the chosen technologies played a significant role in the decision-making process. This ensured that the team could quickly resolve issues and implement features effectively.

- **Iterative Development**: The team adopted an iterative approach to development, allowing for continuous feedback and improvements. This flexibility enabled the incorporation of new ideas and adjustments based on testing and user feedback.

In conclusion, the journey from concept to code for the Remix + Vite + shadcn/ui + Supabase boilerplate was marked by careful research, strategic technical decisions, and a commitment to user experience. The insights gained throughout the process not only shaped the project but also laid a strong foundation for future developments.

## Under the Hood

# Technical Deep-Dive: Boilerplate for Remix + Vite + shadcn/ui + Supabase

## 1. Architecture Decisions

The architecture of this boilerplate is designed to leverage modern web development practices, focusing on a full-stack application that is both scalable and maintainable. The key architectural decisions include:

- **Separation of Concerns**: The application is structured to separate the frontend and backend logic. Remix handles the routing and server-side rendering, while Supabase serves as the backend database and authentication provider.
  
- **Modular Design**: By using Vite as the build tool, the application benefits from fast hot module replacement (HMR) and a modular approach to development. This allows developers to work on individual components without affecting the entire application.

- **Responsive and Adaptive UI**: The use of `shadcn/ui` provides a professional and responsive UI layout, ensuring that the application is visually appealing and user-friendly across devices.

- **Integration with Third-Party Services**: The architecture incorporates third-party services like Stripe for payment processing and Resend for email services, allowing for a more robust feature set without reinventing the wheel.

## 2. Key Technologies Used

The boilerplate utilizes a combination of cutting-edge technologies:

- **Remix**: A framework for building web applications that focuses on performance and user experience. It allows for server-side rendering and data fetching at the route level.

- **Vite**: A build tool that provides a fast development environment with features like HMR, making it ideal for modern web applications.

- **shadcn/ui**: A UI component library that offers pre-built components for building responsive and aesthetically pleasing user interfaces.

- **Supabase**: An open-source Firebase alternative that provides a backend-as-a-service, including authentication, database, and real-time capabilities.

- **Stripe**: A payment processing platform that allows for easy integration of subscription and payment functionalities.

### Example of a Supabase Configuration in `.env`:

```plaintext
SUPABASE_URL=https://<your_supabase_url>.supabase.co
SUPABASE_ANON_KEY=<your_supabase_anon_key>
SUPABASE_SERVICE_ROLE_KEY=<your_supabase_service_role_key>
```

## 3. Interesting Implementation Details

Several interesting implementation details enhance the functionality and usability of the application:

- **Authentication Flow**: The boilerplate includes a complete authentication flow using Supabase, which supports multiple sign-in methods (email, Google, GitHub). This is implemented using Supabase's built-in authentication methods, making it easy to manage user sessions.

- **Dynamic Pricing Page**: The pricing page is customizable and integrates with Stripe for payment processing. This allows developers to easily modify pricing tiers and manage subscriptions.

- **Webhook Integration**: The application listens for Stripe events using webhooks, which are crucial for handling real-time updates related to payments and subscriptions. The setup requires the Stripe CLI to forward events to the local development server.

### Example of Setting Up a Stripe Webhook:

```sh
stripe listen --forward-to localhost:3000/api/webhook
```

## 4. Technical Challenges Overcome

While developing this boilerplate, several technical challenges were addressed:

- **Email Rate Limiting**: Supabase's free tier imposes strict rate limits on email sending. To overcome this, the boilerplate recommends using a third-party email service like Resend, which can handle email delivery more efficiently.

- **Database Seeding**: Ensuring that the database is populated with initial data for development can be challenging. The boilerplate includes a seed command that simplifies this process, allowing developers to quickly set up their environment.

### Example of Seeding the Database:

```sh
pnpm run seed
```

- **Environment Configuration**: Managing environment variables for different services (Supabase, Stripe) can be cumbersome. The boilerplate provides a clear structure for setting up the `.env` file, ensuring that developers can easily configure their environment without confusion.

## Conclusion

This boilerplate for Remix + Vite + shadcn/ui + Supabase provides a solid foundation for building modern web applications. By leveraging a modular architecture, integrating third-party services, and addressing common technical challenges, it enables developers to focus on building features rather than dealing with boilerplate code. The combination of these technologies not only enhances performance but also improves the overall developer experience.

## Lessons from the Trenches

Here’s a breakdown based on the project history and README for the Remix + Vite + shadcn/ui + Supabase boilerplate:

### 1. Key Technical Lessons Learned
- **Integration Complexity**: Integrating multiple technologies (Remix, Vite, Supabase, Stripe) can be complex. Each service has its own setup and configuration requirements, which can lead to confusion if not documented clearly.
- **Environment Management**: Managing environment variables is crucial, especially when dealing with services like Supabase and Stripe. Using a `.env` file helps keep sensitive information secure, but it’s important to ensure that all necessary keys are included and correctly configured.
- **Rate Limiting**: Understanding the limitations of services like Supabase on their free tier (e.g., email sending limits) is essential for planning. This necessitated the use of a third-party email service, which adds another layer of integration.
- **Webhook Handling**: Setting up webhooks for Stripe requires careful attention to detail. The need to run the Stripe CLI during development to listen for events is a key takeaway for managing real-time interactions.

### 2. What Worked Well
- **Modular Architecture**: The use of Remix and Vite allows for a modular and efficient development process. Remix’s routing and data fetching capabilities, combined with Vite’s fast build times, create a smooth development experience.
- **Authentication Flow**: The complete authentication flow with Supabase (including signup, login, and password recovery) was straightforward to implement and provided a solid foundation for user management.
- **UI Components**: Leveraging shadcn/ui for the dashboard layout provided a professional and visually appealing interface with minimal effort. The pre-built components saved time and improved the overall user experience.
- **Documentation**: The README provided clear instructions for setup, development, and deployment, which facilitated onboarding for new developers and reduced setup time.

### 3. What You'd Do Differently
- **Enhanced Error Handling**: Implementing more robust error handling and user feedback mechanisms, especially for authentication and payment processes, would improve the user experience and make debugging easier.
- **Testing Strategy**: Establishing a comprehensive testing strategy (unit tests, integration tests) from the beginning would help catch issues early and ensure the reliability of the application as it scales.
- **Email Service Alternatives**: Exploring multiple email service providers beyond Resend could provide more flexibility and potentially better pricing or features, especially as the user base grows.
- **State Management**: While Zustand is a great choice for state management, evaluating other options like React Query for data fetching and caching could enhance performance and simplify data handling.

### 4. Advice for Others
- **Thorough Documentation**: Always document your setup and configuration processes. This will save time for future developers and help avoid common pitfalls.
- **Start Small**: If you’re new to integrating multiple services, start with a minimal setup and gradually add features. This approach helps in understanding each component’s role and reduces complexity.
- **Monitor Service Limits**: Be aware of the limitations of the services you choose, especially regarding free tiers. Plan for potential upgrades or alternative solutions early in the development process.
- **Community Resources**: Leverage community resources and existing templates or boilerplates. They can provide valuable insights and save time on common tasks, allowing you to focus on unique features of your application.

By reflecting on these aspects, you can enhance your development process and create a more robust and user-friendly application.

## What's Next?

## Conclusion

As we reach the current milestone of the **Remix + Vite + shadcn/ui + Supabase Boilerplate**, we are excited to share that the project is fully functional and ready for use. The boilerplate provides a robust foundation for building fullstack applications, complete with authentication, a professional dashboard, and seamless integration with Supabase and Stripe. The live demo is available for exploration, showcasing the capabilities of this powerful stack.

Looking ahead, we have ambitious plans for future development. We aim to enhance the boilerplate by incorporating additional features such as advanced analytics, improved user management, and customizable themes. We also plan to refine the documentation to make it even more user-friendly, ensuring that developers can easily adapt the boilerplate to their specific needs. Your feedback and suggestions will be invaluable as we continue to evolve this project.

We invite contributors to join us on this journey! Whether you're a seasoned developer or just starting, your contributions—be it code, documentation, or ideas—are welcome. Together, we can make this boilerplate an even more powerful tool for the community. If you're interested in contributing, please check out our GitHub repository and feel free to open issues or submit pull requests.

In closing, this side project has been a rewarding journey of learning and collaboration. It has not only allowed us to explore new technologies but also to connect with like-minded individuals in the developer community. We hope that this boilerplate serves as a valuable resource for your projects and inspires you to embark on your own development adventures. Thank you for being a part of this journey, and we look forward to seeing what you create with it!
## Project Development Analytics
### timeline gant

![Commit timelinegant](https://daily.borninsea.com/assets/a-saas-remix-shadcn-supabase-boilerplate-timeline_chart.png)


### Commit Activity Heatmap
This heatmap shows the distribution of commits over the past year:

![Commit Heatmap]()

### Contributor Network
This network diagram shows how different contributors interact:

![Contributor Network](https://daily.borninsea.com/assets/a-saas-remix-shadcn-supabase-boilerplate-contribution_network.png)

### Commit Activity Patterns
This chart shows when commits typically happen:

![Commit Activity](https://daily.borninsea.com/assets/a-saas-remix-shadcn-supabase-boilerplate-commit_activity.png)

### Code Frequency
This chart shows the frequency of code changes over time:

![Code Frequency](https://daily.borninsea.com/assets/a-saas-remix-shadcn-supabase-boilerplate-code_frequency.png)



* Repository URL: [https://github.com/wanghaisheng/a-saas-remix-shadcn-supabase-boilerplate](https://github.com/wanghaisheng/a-saas-remix-shadcn-supabase-boilerplate)
* Stars: **0**
* Forks: **0**
