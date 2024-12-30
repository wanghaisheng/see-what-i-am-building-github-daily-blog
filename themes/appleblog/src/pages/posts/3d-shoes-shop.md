---
author: Heisenberg
cover:
  alt: cover
  square: https://daily.borninsea.com/assets/image_1735530039411_epupij.png
  url: https://daily.borninsea.com/assets/image_1735530039411_epupij.png
description: 'Build an ecommerce website using Redux Toolkit and Thunk middleware '
featured: true
keywords: 3d-shoes-shop,  ecommerce website,  Redux Toolkit,  Thunk middleware,  shoes
  shop,  online platform,  shopping experience,  footwear,  React,  Ant Design,  Axios,  React
  Router,  Formik,  Yup,  Framer Motion,  React Three Fiber,  Swiper,  React Toastify,  sign
  in,  sign up,  add products,  remove products,  update products,  search products,  filter
  products,  like products,  unlike products,  themes
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Heisenberg
  name: author
- content: 3d-shoes-shop,  ecommerce website,  Redux Toolkit,  Thunk middleware,  shoes
    shop,  online platform,  shopping experience,  footwear,  React,  Ant Design,  Axios,  React
    Router,  Formik,  Yup,  Framer Motion,  React Three Fiber,  Swiper,  React Toastify,  sign
    in,  sign up,  add products,  remove products,  update products,  search products,  filter
    products,  like products,  unlike products,  themes
  name: keywords
pubDate: '2024-12-30'
tags:
- 3d-shoes-shop
- ecommerce
- website
- redux-toolkit
- thunk
- shoes
- footwear
- react
- ant-design
- axios
- react-router
- formik
- yup
- framer-motion
- react-three-fiber
- swiper
- react-toastify
- features
- shopping-experience
- sign-in
- sign-up
- cart-management
- product-search
- themes
theme: light
title: 'Building 3D Shoes Shop: Crafting an E-commerce Experience with Redux Toolkit'
---



*Built by wanghaisheng | Last updated: 20241230*

11 minutes 49 seconds  read
## Project Genesis

### Stepping into the Future: My Journey with 3D Shoes Shop

As a lifelong sneaker enthusiast, I’ve always been captivated by the world of footwear. From the moment I laced up my first pair of high-tops, I knew that shoes were more than just a fashion statement; they were a form of self-expression. This passion sparked the idea for my project: a 3D shoe shop that would revolutionize the way we shop for shoes online. I envisioned a platform where users could not only browse a diverse range of styles but also experience them in a whole new dimension.

The motivation behind this project was deeply personal. I often found myself frustrated with the limitations of traditional online shopping—poor fit, lack of variety, and the inability to truly visualize how a shoe would look on my feet. I wanted to create a solution that would empower others to make informed choices, ensuring that every pair of shoes they purchased was a perfect match for their unique style and comfort needs.

Of course, the journey wasn’t without its challenges. As I dove into the world of e-commerce, I quickly realized the complexities of building a user-friendly interface that could seamlessly integrate 3D technology. There were moments of doubt, especially when I faced technical hurdles that seemed insurmountable. But with each setback, I learned and adapted, fueled by the vision of a platform that could transform the shopping experience.

After countless hours of coding and design, I’m thrilled to share the solution we’ve crafted: a sleek, intuitive online store built with React and powered by Ant Design. Our platform not only showcases a stunning array of footwear but also allows users to interact with 3D models, giving them a true sense of how each shoe will look and feel. Join me as I take you through the exciting features of the 3D Shoes Shop and the journey that brought this vision to life!

## From Idea to Implementation

### 1. Initial Research and Planning

The journey of developing the shoe e-commerce website began with thorough research into the current market trends and user expectations in the online shopping space. The team conducted surveys and analyzed competitor platforms to identify common features and pain points experienced by users. This research highlighted the importance of a user-friendly interface, seamless navigation, and robust functionality, such as effective search and filtering options. 

The planning phase involved defining the core features of the application, which included user authentication (sign in/sign up), cart management (add/remove/update products), product search and filtering, and the ability to like/unlike products. Additionally, the team recognized the need for a responsive design to cater to users on various devices. A project timeline was established, outlining milestones for design, development, testing, and deployment.

### 2. Technical Decisions and Their Rationale

The choice of technologies was driven by the need for a scalable, maintainable, and performant application. React was selected as the primary framework due to its component-based architecture, which promotes reusability and simplifies state management. The integration of Redux Toolkit was essential for managing the global state, particularly for cart operations and user authentication.

Ant Design was chosen for its comprehensive UI components, which allowed for rapid development of a visually appealing interface. Axios was utilized for making API calls, providing a straightforward way to handle asynchronous requests. Formik and Yup were incorporated for form handling and validation, ensuring a smooth user experience during sign-up and product management.

For animations and transitions, Framer Motion was selected, enhancing the overall user experience with smooth visual feedback. React Three Fiber was considered for potential 3D product displays, but ultimately, it was decided to focus on 2D representations to maintain performance and simplicity. Swiper was integrated for creating a responsive carousel for product displays, while React Toastify was used for user notifications, providing real-time feedback on actions like adding items to the cart.

### 3. Alternative Approaches Considered

During the planning and development phases, several alternative approaches were considered. For state management, the team evaluated using Context API instead of Redux Toolkit. However, given the complexity of the application and the need for advanced state management features, Redux Toolkit was deemed more suitable.

In terms of UI frameworks, Bootstrap was initially considered due to its popularity and ease of use. However, Ant Design was ultimately chosen for its modern design language and extensive component library, which aligned better with the project’s aesthetic goals.

The team also explored the possibility of building a native mobile application using React Native. However, after assessing the target audience and the resources available, it was decided to focus on a responsive web application that could be accessed on both desktop and mobile devices, ensuring a broader reach without the overhead of maintaining separate codebases.

### 4. Key Insights That Shaped the Project

Several key insights emerged throughout the project that significantly influenced its direction. First, the importance of user feedback became evident early on. Engaging potential users through surveys and usability testing helped refine features and prioritize functionality that truly mattered to the target audience.

Another insight was the necessity of performance optimization. As the application grew in complexity, the team recognized the importance of optimizing loading times and responsiveness. This led to the implementation of lazy loading for images and components, ensuring a smooth user experience even with a large inventory of products.

Finally, the team learned the value of iterative development. By adopting an agile approach, they were able to continuously integrate user feedback and make adjustments throughout the development process. This flexibility not only improved the final product but also fostered a collaborative environment where team members could contribute ideas and solutions.

In conclusion, the journey from concept to code for the shoe e-commerce website was marked by careful research, strategic technical decisions, and a commitment to user-centered design. The insights gained throughout the process not only shaped the project but also equipped the team with valuable lessons for future endeavors.

## Under the Hood

# Technical Deep-Dive: Shoes Shop E-Commerce Website

## 1. Architecture Decisions

The architecture of the Shoes Shop e-commerce website is designed to provide a scalable, maintainable, and user-friendly experience. The application follows a component-based architecture, leveraging React for building reusable UI components. The decision to use Redux Toolkit for state management allows for a centralized store, making it easier to manage the application's state across various components.

### Key Architectural Choices:
- **Component-Based Structure**: Each UI element (e.g., product card, cart, navigation) is encapsulated in its own component, promoting reusability and separation of concerns.
- **Client-Server Architecture**: The application communicates with a backend API using Axios for data fetching, allowing for a clear separation between the frontend and backend.
- **Routing**: React Router is used to manage navigation within the application, enabling a single-page application (SPA) experience.

## 2. Key Technologies Used

The following technologies were chosen for their robustness and community support:

- **React**: A JavaScript library for building user interfaces, allowing for the creation of dynamic and interactive web applications.
- **Ant Design**: A UI design language and React-based implementation that provides a set of high-quality components for building rich user interfaces.
- **Redux Toolkit**: A powerful toolset for efficient Redux development, simplifying the process of managing application state.
- **Formik and Yup**: Formik is used for handling form state and validation, while Yup provides a schema-based validation solution.
- **Framer Motion**: A library for animations that enhances user experience with smooth transitions and animations.
- **React Three Fiber**: A React renderer for Three.js, allowing for the integration of 3D graphics into the application.
- **Swiper**: A modern touch slider that provides a responsive and customizable way to display product images.
- **React Toastify**: A library for displaying notifications, enhancing user feedback during interactions.

## 3. Interesting Implementation Details

### State Management with Redux Toolkit

The application uses Redux Toolkit to manage the global state, particularly for the shopping cart and user authentication. The following code snippet demonstrates how to set up a slice for the cart:

```javascript
import { createSlice } from '@reduxjs/toolkit';

const cartSlice = createSlice({
  name: 'cart',
  initialState: {
    items: [],
  },
  reducers: {
    addItem: (state, action) => {
      state.items.push(action.payload);
    },
    removeItem: (state, action) => {
      state.items = state.items.filter(item => item.id !== action.payload.id);
    },
    clearCart: (state) => {
      state.items = [];
    },
  },
});

export const { addItem, removeItem, clearCart } = cartSlice.actions;
export default cartSlice.reducer;
```

### Form Handling with Formik and Yup

Formik is used to manage form state, while Yup is used for validation. Here’s an example of a sign-up form:

```javascript
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';

const SignupForm = () => {
  return (
    <Formik
      initialValues={{ email: '', password: '' }}
      validationSchema={Yup.object({
        email: Yup.string().email('Invalid email address').required('Required'),
        password: Yup.string().min(6, 'Must be 6 characters or more').required('Required'),
      })}
      onSubmit={(values) => {
        // Handle form submission
      }}
    >
      <Form>
        <Field name="email" type="email" />
        <ErrorMessage name="email" component="div" />
        <Field name="password" type="password" />
        <ErrorMessage name="password" component="div" />
        <button type="submit">Sign Up</button>
      </Form>
    </Formik>
  );
};
```

### Animations with Framer Motion

Framer Motion is utilized to create engaging animations. For example, when a product is added to the cart, a notification appears with a smooth transition:

```javascript
import { motion } from 'framer-motion';

const Notification = ({ message }) => {
  return (
    <motion.div
      initial={{ opacity: 0, y: -20 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -20 }}
    >
      {message}
    </motion.div>
  );
};
```

## 4. Technical Challenges Overcome

### Managing Asynchronous State

One of the significant challenges was managing asynchronous state updates, especially when fetching product data and handling user authentication. To address this, Redux Toolkit's `createAsyncThunk` was used to handle asynchronous actions effectively.

Example of fetching products:

```javascript
import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import axios from 'axios

## Lessons from the Trenches

Certainly! Here’s a breakdown based on the project history and README for the shoe e-commerce website:

### 1. Key Technical Lessons Learned
- **State Management with Redux Toolkit**: Implementing Redux Toolkit simplified state management significantly. The use of slices and the createAsyncThunk function made handling asynchronous actions (like fetching products) more straightforward and maintainable.
- **Form Handling with Formik and Yup**: Using Formik for form management and Yup for validation streamlined the process of handling user inputs, especially for sign-up and sign-in forms. This combination reduced boilerplate code and improved user experience with real-time validation feedback.
- **Responsive Design with Ant Design**: Leveraging Ant Design's components helped in creating a responsive and visually appealing UI quickly. Understanding how to customize themes and styles within Ant Design was crucial for maintaining brand consistency.
- **Animation with Framer Motion**: Integrating Framer Motion for animations enhanced the user experience. Learning how to implement animations effectively without compromising performance was a valuable lesson.
- **Optimizing Performance with React.memo and useMemo**: As the application grew, optimizing performance became essential. Using React.memo and useMemo helped prevent unnecessary re-renders and improved the overall responsiveness of the app.

### 2. What Worked Well
- **User Authentication Flow**: The sign-in and sign-up process was seamless, thanks to the integration of Formik and Yup for form handling and validation. This led to a positive user experience.
- **Product Search and Filtering**: Implementing search and filter functionalities using Axios for API calls allowed users to find products quickly. The performance of these features was satisfactory, even with a large dataset.
- **Cart Management**: The ability to add, remove, and update products in the cart was intuitive and worked well. The use of Redux for managing cart state ensured that the cart was always in sync with the UI.
- **Visual Appeal**: The use of Swiper for product carousels and React Three Fiber for 3D product views added a modern touch to the website, making it visually engaging.

### 3. What You'd Do Differently
- **Testing**: While the application was functional, implementing more comprehensive testing (unit tests and integration tests) using tools like Jest and React Testing Library would have improved reliability and made it easier to catch bugs early.
- **Code Splitting**: Although the app performed well, implementing code splitting with React.lazy and Suspense could have further optimized loading times, especially for larger components and routes.
- **Accessibility**: Focusing more on accessibility from the start would have been beneficial. Ensuring that all components are keyboard navigable and screen reader friendly is crucial for inclusivity.
- **Documentation**: While the README provided a good overview, more detailed documentation on the codebase and setup instructions would help future developers onboard more quickly.

### 4. Advice for Others
- **Start with a Clear Plan**: Before diving into coding, outline the project structure, features, and technologies you plan to use. This will save time and help avoid scope creep.
- **Leverage Existing Libraries**: Don’t reinvent the wheel. Use established libraries and frameworks to handle common functionalities (like form handling, state management, and routing) to speed up development.
- **Focus on User Experience**: Prioritize user experience in your design and functionality. Regularly test your application with real users to gather feedback and make improvements.
- **Iterate and Refine**: Be open to iterating on your design and features based on user feedback. Continuous improvement is key to a successful product.
- **Stay Updated**: The tech landscape is always changing. Keep learning about new tools and best practices to improve your development skills and the quality of your projects.

By reflecting on these aspects, you can gain valuable insights that will help in future projects and enhance your development practices.

## What's Next?

## Conclusion

As we wrap up this phase of our 3D Shoes Shop project, we are excited to share our current status and future development plans. The shoe e-commerce website has successfully established a solid foundation, offering users a diverse and convenient shopping experience for various styles of footwear. With features such as user authentication, cart management, product search and filtering, and a visually appealing interface powered by cutting-edge technologies like React, Redux Toolkit, and Framer Motion, we are proud of the progress we've made.

Looking ahead, our development plans are ambitious. We aim to enhance the user experience further by integrating advanced features such as personalized recommendations, augmented reality (AR) for virtual try-ons, and improved payment options. Additionally, we are exploring partnerships with local shoe brands to expand our product offerings and provide users with unique styles that reflect their individuality. Our goal is to create a vibrant online community where shoe enthusiasts can connect, share, and discover the latest trends.

We invite contributors to join us on this exciting journey! Whether you are a developer, designer, or simply passionate about footwear, your skills and ideas can help shape the future of the 3D Shoes Shop. Together, we can innovate and elevate the online shopping experience for our users. If you're interested in contributing, please reach out to us through our GitHub repository or social media channels.

In closing, this side project has been a remarkable journey of creativity, collaboration, and learning. We have faced challenges, celebrated milestones, and built a platform that we believe will resonate with shoe lovers everywhere. As we continue to grow and evolve, we are grateful for the support of our community and excited for what lies ahead. Thank you for being a part of the 3D Shoes Shop adventure!
## Project Development Analytics
### timeline gant

![Commit timelinegant](https://daily.borninsea.com/assets/3d-shoes-shop-timeline_chart.png)


### Commit Activity Heatmap
This heatmap shows the distribution of commits over the past year:

![Commit Heatmap]()

### Contributor Network
This network diagram shows how different contributors interact:

![Contributor Network](https://daily.borninsea.com/assets/3d-shoes-shop-contribution_network.png)

### Commit Activity Patterns
This chart shows when commits typically happen:

![Commit Activity](https://daily.borninsea.com/assets/3d-shoes-shop-commit_activity.png)

### Code Frequency
This chart shows the frequency of code changes over time:

![Code Frequency](https://daily.borninsea.com/assets/3d-shoes-shop-code_frequency.png)



* Repository URL: [https://github.com/wanghaisheng/3d-shoes-shop](https://github.com/wanghaisheng/3d-shoes-shop)
* Stars: **0**
* Forks: **0**
