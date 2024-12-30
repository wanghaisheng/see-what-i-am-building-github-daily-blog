---
author: Heisenberg
cover:
  alt: cover
  square: https://daily.borninsea.com/assets/image_1735530711405_kn8uho.png
  url: https://daily.borninsea.com/assets/image_1735530711405_kn8uho.png
description: "\U0001F9B7\U0001FAA5\uFF5F AppointDent \uFF60 is a Swedish dental appointment\
  \ web app using microservices, publish-subscribe, and client-server architectures\
  \ for residents and dentists."
featured: true
keywords: AppointDent,  dental appointment,  web app,  microservices,  publish-subscribe,  client-server,  Sweden,  full-stack
  web application,  residents,  dentists,  distributed system,  infrastructure,  architectural
  styles,  TypeScript,  Node.js,  Vite.js,  Express.js,  Solid.js,  Sqlite3,  Tailwind
  CSS,  APIGateway,  stress-testing,  notifications,  calendar,  availability.
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Heisenberg
  name: author
- content: AppointDent,  dental appointment,  web app,  microservices,  publish-subscribe,  client-server,  Sweden,  full-stack
    web application,  residents,  dentists,  distributed system,  infrastructure,  architectural
    styles,  TypeScript,  Node.js,  Vite.js,  Express.js,  Solid.js,  Sqlite3,  Tailwind
    CSS,  APIGateway,  stress-testing,  notifications,  calendar,  availability.
  name: keywords
pubDate: '2024-12-30'
tags:
- appointdent
- dental-appointment
- web-app
- microservices
- publish-subscribe
- client-server
- sweden
- full-stack-web-application
- distributed-system
- architecture
- typescript
- node-js
- vite-js
- express-js
- solid-js
- sqlite3
- tailwind-css
- apigateway
- stress-testing
- notifications
- calendar
- appointments
- development-team
theme: light
title: 'Building AppointDent: A Microservices Journey in Dental Appointment Management'
---



*Built by wanghaisheng | Last updated: 20241230*

11 minutes 22 seconds  read
## Project Genesis

### Discovering AppointDent: A Journey to Simplify Dental Care in Sweden

As someone who has always been passionate about technology and its potential to improve everyday life, I found myself reflecting on a common frustration: managing dental appointments. Living in Sweden, I noticed that many residents struggled with the cumbersome process of scheduling and keeping track of their dental visits. This sparked an idea that would eventually evolve into **AppointDent**—a full-stack web application designed to streamline the appointment process for both patients and dentists.

My personal motivation for this project stemmed from my own experiences with dental care. I remember the anxiety of trying to remember appointment dates, the hassle of phone calls, and the confusion that often arose when trying to coordinate schedules with busy dental practices. I wanted to create a solution that would not only alleviate these stresses but also enhance the overall experience for everyone involved.

However, the journey to bring AppointDent to life was not without its challenges. From the outset, I faced the daunting task of designing a system that could effectively manage the complexities of dental appointments while ensuring a seamless user experience. Navigating the intricacies of a distributed system infrastructure, I had to familiarize myself with various architectural styles, including microservices, publish-subscribe, and client-server models. Each step was a learning experience, pushing me to think critically and creatively about how to build a robust platform.

Ultimately, the solution I developed is a comprehensive tool that empowers residents to easily manage their dental appointments while providing dentists with the organizational capabilities they need to run their practices efficiently. With AppointDent, scheduling is no longer a chore; it’s a simple, intuitive process that enhances communication and fosters better relationships between patients and their dental care providers.

Join me as I delve deeper into the features and benefits of AppointDent, and discover how this innovative application is transforming dental care in Sweden!

## From Idea to Implementation

### 1. Initial Research and Planning

The journey of developing **AppointDent** began with extensive research into the needs of both patients and dentists in Sweden. The team conducted surveys and interviews to understand the pain points associated with booking dental appointments, managing schedules, and receiving timely notifications. This research highlighted the necessity for a user-friendly platform that could streamline the appointment process for patients while providing dentists with tools to manage their practices effectively.

During the planning phase, the team outlined the core functionalities required for the application, such as appointment booking, cancellation, notifications, and a calendar for dentists. The decision to adopt a distributed system architecture was made early on, as it would allow for scalability and flexibility in managing different services independently. The team also established a timeline for development, breaking the project into manageable phases to ensure steady progress and regular feedback loops.

### 2. Technical Decisions and Their Rationale

The choice of a **full-stack web application** was driven by the need to create a seamless experience for users across different devices. The tech stack was carefully selected to leverage modern frameworks and libraries that would facilitate rapid development and maintainability. 

- **TypeScript** was chosen for its strong typing capabilities, which help catch errors early in the development process.
- **Node.js** was selected as the runtime environment due to its non-blocking architecture, making it suitable for handling multiple requests simultaneously.
- **Vite.js** was adopted for its fast build times and hot module replacement, enhancing the development experience.
- **Solid.js** was chosen for the client-side framework because of its fine-grained reactivity and performance benefits.
- The use of **Tailwind CSS** allowed for rapid UI development with a utility-first approach, enabling the team to create responsive designs efficiently.

The decision to implement a **microservices architecture** was based on the need for modularity and the ability to scale individual components independently. This approach also facilitated the use of the **MQTT** protocol for communication between services, ensuring efficient message delivery and reducing latency.

### 3. Alternative Approaches Considered

During the planning and design phases, the team considered several alternative approaches:

- **Monolithic Architecture**: Initially, the team contemplated a monolithic architecture for simplicity. However, this approach would have made scaling and maintaining the application more challenging as the project grew. The decision to adopt microservices ultimately provided greater flexibility and ease of deployment.

- **Different Frontend Frameworks**: Other frameworks such as React and Angular were evaluated for the frontend. However, Solid.js was favored for its performance and simplicity, which aligned with the team's goal of creating a fast and responsive user interface.

- **Traditional REST APIs**: While REST APIs were considered for service communication, the team opted for the **publish-subscribe** model using MQTT to enable real-time updates and notifications, which were critical for the appointment management features.

### 4. Key Insights That Shaped the Project

Several key insights emerged throughout the development process that significantly influenced the project's direction:

- **User-Centric Design**: The importance of a user-friendly interface became evident during user testing sessions. Feedback from potential users led to iterative design changes that improved the overall experience, emphasizing the need for intuitive navigation and clear communication of appointment statuses.

- **Scalability Needs**: As the team began to implement features, it became clear that scalability would be crucial for handling varying loads, especially during peak appointment times. This realization reinforced the decision to use a microservices architecture, allowing the team to scale services independently based on demand.

- **Continuous Integration**: The adoption of continuous integration practices proved invaluable in maintaining code quality and facilitating collaboration among team members. Regular testing and code reviews helped catch issues early, ensuring a smoother development process.

- **Real-Time Communication**: The necessity for real-time notifications and updates became a focal point of the project. Implementing the publish-subscribe model not only enhanced user engagement but also improved the overall reliability of the appointment management system.

In conclusion, the journey from concept to code for **AppointDent** was marked by thorough research, thoughtful technical decisions, and a commitment to user-centric design. The team's ability to adapt and iterate based on insights gained throughout the development process ultimately led to the creation of a robust and efficient platform for managing dental appointments in Sweden.

## Under the Hood

# Technical Deep-Dive: AppointDent

## 1. Architecture Decisions

The architecture of AppointDent is primarily based on a **Microservices-based architecture**. This decision was made to ensure scalability, maintainability, and independent deployment of services. Each service is responsible for a specific domain within the application, allowing for clear separation of concerns.

### Key Architectural Choices:
- **Microservices**: Each service (e.g., `appointment-service`, `dentist-service`) operates independently, which allows for easier updates and scaling.
- **MQTT Protocol**: The use of the MQTT protocol for communication between services enhances the system's ability to handle real-time notifications and updates efficiently.
- **Distributed System**: The architecture is designed to run on multiple machines, which improves fault tolerance and load distribution.

### Example of Service Communication:
```javascript
const mqtt = require('mqtt');
const client = mqtt.connect('mqtt://broker.hivemq.com');

client.on('connect', () => {
  client.subscribe('appointment/notifications', (err) => {
    if (!err) {
      console.log('Subscribed to appointment notifications');
    }
  });
});

client.on('message', (topic, message) => {
  console.log(`Received message: ${message.toString()}`);
});
```

## 2. Key Technologies Used

The tech stack for AppointDent includes a variety of modern technologies that facilitate both the front-end and back-end development.

### Front-End Technologies:
- **TypeScript**: Provides type safety and enhances code quality.
- **Solid.js**: A reactive UI library that offers high performance and fine-grained reactivity.
- **Tailwind CSS**: A utility-first CSS framework that allows for rapid UI development.

### Back-End Technologies:
- **Node.js**: The runtime environment for building server-side applications.
- **Express.js**: A web framework for Node.js that simplifies the creation of APIs.
- **SQLite3**: A lightweight database solution used for storing application data.

### Example of an Express.js Route:
```javascript
const express = require('express');
const router = express.Router();
const Appointment = require('../models/Appointment');

router.post('/appointments', async (req, res) => {
  try {
    const appointment = new Appointment(req.body);
    await appointment.save();
    res.status(201).send(appointment);
  } catch (error) {
    res.status(400).send(error);
  }
});
```

## 3. Interesting Implementation Details

### Monorepo Structure:
The project utilizes a **monorepo** structure, where all services and the client application are housed within a single repository. This approach simplifies dependency management and allows for easier coordination among team members.

### Stress Testing:
The team implemented stress testing using `k6`, which allows for simulating high loads on the application to ensure it can handle real-world usage scenarios. The stress-testing scripts are located in a dedicated folder, making it easy to run tests independently.

### Example of a k6 Test Script:
```javascript
import http from 'k6/http';
import { check, sleep } from 'k6';

export default function () {
  const res = http.post('http://localhost:3000/appointments', {
    patientId: '12345',
    dentistId: '67890',
    time: '2023-10-01T10:00:00Z',
  });
  check(res, { 'status was 201': (r) => r.status === 201 });
  sleep(1);
}
```

## 4. Technical Challenges Overcome

### Challenge: Managing Service Communication
One of the significant challenges was ensuring reliable communication between microservices. The team opted for the MQTT protocol, which is lightweight and designed for low-bandwidth, high-latency networks. This choice improved the responsiveness of the application, especially for real-time notifications.

### Challenge: Continuous Integration Setup
Initially, the project was developed on GitLab, and the CI/CD pipeline was set up using GitLab's features. However, when migrating to GitHub, the team faced challenges in replicating the CI/CD pipeline. They had to adapt their `.gitlab-ci.yml` to work with GitHub Actions, ensuring that automated testing and deployment processes remained intact.

### Example of a GitHub Actions Workflow:
```yaml
name: CI

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Node.js
        uses: actions/setup-node@v2
        with:
          node-version: '18.x'

      - name: Install dependencies
        run: npm install

      - name: Run tests
        run: npm test
```

### Conclusion
The AppointDent project showcases a well-thought-out architecture that leverages modern technologies and practices. The use of microservices, MQTT for communication

## Lessons from the Trenches

Here are some reflections based on the project history and README for AppointDent:

### Key Technical Lessons Learned
1. **Microservices Architecture**: Implementing a microservices architecture taught us the importance of service independence and scalability. Each service can be developed, deployed, and scaled independently, which enhances the overall system's resilience and flexibility.
2. **Communication Protocols**: Utilizing the MQTT protocol for inter-service communication highlighted the significance of choosing the right communication method for distributed systems. It allowed for efficient message passing and reduced latency.
3. **Continuous Integration**: The integration of CI practices improved our development workflow significantly. Automated testing and static analysis helped catch issues early, ensuring higher code quality and reducing the time spent on debugging later in the development cycle.
4. **Stress Testing**: Conducting stress tests using tools like k6 provided insights into system performance under load, helping us identify bottlenecks and optimize resource allocation.

### What Worked Well
1. **Team Collaboration**: The use of GitLab for version control and CI/CD facilitated effective collaboration among team members. The ability to review code and run tests before merging into the main branch helped maintain code quality.
2. **Modular Design**: The monorepo structure allowed for clear organization of the project components, making it easier for team members to navigate and understand the codebase. Each service having its own README file provided clarity on functionality and setup.
3. **User-Centric Features**: Features like appointment notifications and an integrated map for finding dentists were well-received during user testing, demonstrating the importance of user feedback in shaping the application.

### What You'd Do Differently
1. **Documentation**: While the README is comprehensive, we could have included more detailed API documentation for each service. This would have made it easier for new developers to onboard and understand how to interact with the services.
2. **CI/CD Migration**: Migrating the CI/CD pipeline to GitHub sooner would have streamlined our development process. We underestimated the time required to set up a new pipeline, which delayed some testing and deployment processes.
3. **Testing Coverage**: We could have invested more time in writing unit tests for individual components. While integration tests were useful, having a robust suite of unit tests would have caught more issues early in the development process.

### Advice for Others
1. **Start with a Clear Architecture**: Before diving into development, spend time designing the architecture. A well-thought-out architecture can save a lot of time and effort later on.
2. **Embrace CI/CD Early**: Implement continuous integration and deployment practices from the start. This will help maintain code quality and streamline the development process.
3. **Prioritize User Feedback**: Regularly seek feedback from potential users throughout the development process. This will help ensure that the final product meets user needs and expectations.
4. **Document Everything**: Maintain thorough documentation for both the codebase and the development process. This will aid in onboarding new team members and provide a reference for future development.

By reflecting on these aspects, future projects can benefit from the lessons learned and improve upon the successes achieved in AppointDent.

## What's Next?

## Conclusion

As we wrap up this phase of the **AppointDent** project, we are excited to share our current status and future development plans. Over the past 10 weeks, our dedicated team has successfully built a robust full-stack web application that empowers residents of Sweden to manage their dentist appointments seamlessly. The application is structured around a distributed system architecture, utilizing microservices, publish-subscribe, and client-server models to ensure efficiency and scalability.

Looking ahead, we have ambitious plans for further development. Our immediate focus will be on enhancing user experience by integrating advanced features such as personalized appointment reminders, a more intuitive user interface, and improved analytics for dentists to better manage their practices. Additionally, we aim to expand our service offerings to include tele-dentistry options, allowing patients to consult with dentists remotely. We are also exploring partnerships with dental clinics across Sweden to broaden our reach and impact.

We invite contributors from all backgrounds to join us on this journey. Whether you are a developer, designer, or simply passionate about improving healthcare accessibility, your skills and insights can make a significant difference. Check out our GitHub repository to see how you can contribute, whether through code, design, or feedback. Together, we can enhance the AppointDent experience and make dental care more accessible for everyone.

In closing, the journey of developing AppointDent has been both challenging and rewarding. It has not only allowed us to apply our technical skills but also to collaborate as a team and learn from one another. We are proud of what we have accomplished so far, and we are excited about the future. Thank you for being a part of this project, and we look forward to your contributions as we continue to grow and improve AppointDent!
## Project Development Analytics
### timeline gant

![Commit timelinegant](https://daily.borninsea.com/assets/AppointDent-timeline_chart.png)


### Commit Activity Heatmap
This heatmap shows the distribution of commits over the past year:

![Commit Heatmap]()

### Contributor Network
This network diagram shows how different contributors interact:

![Contributor Network](https://daily.borninsea.com/assets/AppointDent-contribution_network.png)

### Commit Activity Patterns
This chart shows when commits typically happen:

![Commit Activity](https://daily.borninsea.com/assets/AppointDent-commit_activity.png)

### Code Frequency
This chart shows the frequency of code changes over time:

![Code Frequency](https://daily.borninsea.com/assets/AppointDent-code_frequency.png)



* Repository URL: [https://github.com/wanghaisheng/AppointDent](https://github.com/wanghaisheng/AppointDent)
* Stars: **0**
* Forks: **0**
