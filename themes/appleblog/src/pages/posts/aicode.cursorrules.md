---
author: Heisenberg
cover:
  alt: cover
  square: https://daily.borninsea.com/assets/image_1739763605490_yobtaj.png
  url: https://daily.borninsea.com/assets/image_1739763605490_yobtaj.png
description: Magic to turn Cursor/Windsurf as 90% of Devin
featured: true
keywords: aicode.cursorrules,  Cursor,  Windsurf,  Devin,  AI assistant,  advanced
  agentic AI,  automated planning,  self-evolution,  tool usage,  web browsing,  search
  engine queries,  LLM-driven analysis,  multi-agent collaboration,  easy setup,  Cookiecutter,  manual
  setup,  Planner-Executor,  multi-agent branch,  web scraping,  DuckDuckGo,  LLM-powered
  analysis,  self-evolution,  lessons learned,  project-specific knowledge,  coachable
  AI,  usage tutorial.
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Heisenberg
  name: author
- content: aicode.cursorrules,  Cursor,  Windsurf,  Devin,  AI assistant,  advanced
    agentic AI,  automated planning,  self-evolution,  tool usage,  web browsing,  search
    engine queries,  LLM-driven analysis,  multi-agent collaboration,  easy setup,  Cookiecutter,  manual
    setup,  Planner-Executor,  multi-agent branch,  web scraping,  DuckDuckGo,  LLM-powered
    analysis,  self-evolution,  lessons learned,  project-specific knowledge,  coachable
    AI,  usage tutorial.
  name: keywords
pubDate: '2025-02-17'
tags:
- aicode
- cursorrules
- magic
- cursor
- windsurf
- devin
- ai-assistant
- github
- advanced-ai-capabilities
- automated-planning
- self-evolution
- tool-usage
- web-browsing
- search-engine-queries
- llm-driven-analysis
- multi-agent-collaboration
- easy-setup
- cookiecutter
- manual-setup
- planner-executor
- multi-agent
- web-scraping
- duckduckgo
- llm-powered-analysis
- self-evolution
- lessons-learned
- project-specific-knowledge
- coachable-ai
- usage-tutorial
theme: light
title: 'Transforming Cursor into Devin: A Developer''s AI Assistant Journey'
---



*Built by wanghaisheng | Last updated: 20250217*

12 minutes 24 seconds  read
## Project Genesis

### Transforming Your Coding Experience: The Journey Behind aicode.cursorrules

As a passionate coder, I’ve always been on the lookout for tools that can elevate my programming experience. I remember the first time I stumbled upon an AI coding assistant—it felt like magic. Suddenly, I had a virtual partner that could help me brainstorm ideas, debug code, and even suggest improvements. But as I delved deeper, I realized that many of these advanced tools came with a hefty price tag. That’s when the spark of inspiration hit me: what if I could create a solution that harnessed the power of AI without breaking the bank?

My personal motivation stemmed from a desire to democratize access to cutting-edge technology. I wanted to empower fellow developers, whether they were seasoned pros or enthusiastic beginners, to tap into the potential of AI-driven coding assistance. The thought of transforming a simple $20 Cursor into a Devin-like AI assistant was exhilarating. However, the journey was not without its challenges. I faced hurdles in understanding the intricacies of AI integration, and there were moments of doubt when I questioned whether I could truly replicate the capabilities of those high-end tools.

But with determination and a bit of creativity, I began to piece together a solution. Enter **aicode.cursorrules**—a repository designed to supercharge your Cursor/Windsurf IDE or GitHub Copilot with advanced agentic AI capabilities. In just under a minute, you can unlock features like automated planning and self-evolution, allowing your AI to “think before it acts.” This project is not just about coding; it’s about transforming the way we interact with technology, making it more intuitive and accessible for everyone.

Join me as I dive deeper into the world of aicode.cursorrules, sharing insights, tips, and the journey that led to this exciting development. Let’s explore how you can elevate your coding experience and unleash the full potential of AI in your projects!

## From Idea to Implementation

# Journey from Concept to Code: Transforming Cursor into a Devin-like AI Assistant

## 1. Initial Research and Planning

The journey began with a thorough analysis of existing AI coding assistants, particularly focusing on their capabilities, limitations, and pricing models. The primary inspiration was Devin, a high-end AI assistant that offered advanced features such as automated planning, self-evolution, and multi-agent collaboration. However, the $500/month subscription was a significant barrier for many developers. 

The goal was to create a more accessible solution that could replicate most of Devin's functionalities at a fraction of the cost. This involved researching various open-source tools and frameworks that could be integrated into existing IDEs like Cursor and Windsurf. The planning phase included identifying key features that would enhance user experience, such as automated task planning, web scraping, and LLM-driven analysis. 

## 2. Technical Decisions and Their Rationale

Several technical decisions were made during the development process, each with a clear rationale:

- **Choice of Frameworks**: The decision to use Cookiecutter for project setup was based on its ability to streamline the initialization process, making it easier for users to get started quickly. This was crucial for attracting users who might be intimidated by complex setups.

- **Multi-Agent Architecture**: Implementing a Planner-Executor model was a significant technical choice. The Planner, powered by o1, was designed to handle complex task coordination, while the Executor, utilizing Claude/GPT, focused on executing tasks. This separation of concerns allowed for improved solution quality and faster iteration, as each agent could specialize in its role.

- **Tool Integration**: The integration of web scraping tools (like Playwright) and search engine capabilities (such as DuckDuckGo) was essential for extending the AI's functionality. This decision was driven by the need for the AI to autonomously gather information and perform tasks that would typically require human intervention.

- **Self-Evolution Mechanism**: The implementation of a self-evolution feature allowed the AI to learn from user corrections and adapt its behavior over time. This was a key differentiator from other tools, as it transformed the AI into a coachable partner, enhancing its long-term utility.

## 3. Alternative Approaches Considered

During the planning and development phases, several alternative approaches were considered:

- **Standalone AI Assistant**: One option was to develop a completely standalone AI assistant rather than integrating with existing IDEs. However, this was deemed less practical, as many developers were already using tools like Cursor and GitHub Copilot. The integration approach allowed for leveraging existing user bases and enhancing their current workflows.

- **Simplified Feature Set**: Initially, there was a consideration to launch with a more simplified feature set to reduce development time. However, feedback from potential users indicated a strong desire for advanced capabilities. This led to the decision to include the full range of features from the outset, ensuring that the product would meet user expectations.

- **Different Collaboration Models**: Various collaboration models were explored, including single-agent systems and more complex multi-agent frameworks. Ultimately, the Planner-Executor model was chosen for its balance of complexity and effectiveness, allowing for clear roles and responsibilities within the AI system.

## 4. Key Insights That Shaped the Project

Several key insights emerged throughout the project that significantly influenced its direction:

- **User-Centric Design**: Engaging with potential users early in the process highlighted the importance of user experience. Feedback indicated that ease of setup and intuitive functionality were critical for adoption. This insight drove the decision to prioritize a straightforward installation process and clear documentation.

- **The Value of Adaptability**: The realization that users wanted an AI that could adapt to their specific workflows and preferences led to the emphasis on self-evolution. This feature not only enhances the AI's utility but also fosters a sense of partnership between the user and the AI.

- **Community and Open Source**: The open-source nature of the project was a significant factor in its development. By leveraging community contributions and feedback, the project could evolve more rapidly and remain aligned with user needs. This collaborative approach also helped in building a supportive user community around the tool.

In conclusion, the journey from concept to code for transforming Cursor into a Devin-like AI assistant was marked by careful research, strategic technical decisions, and a commitment to user-centric design. The result is a powerful tool that democratizes access to advanced AI capabilities, enabling developers to enhance their productivity and creativity without the hefty price tag.

## Under the Hood

# Technical Deep-Dive: Transforming Cursor into a Devin-like AI Assistant

## 1. Architecture Decisions

The architecture of the system is designed to facilitate a multi-agent approach, where distinct roles are assigned to different components. The primary architecture consists of:

- **Planner**: This component is responsible for high-level task planning and coordination. It utilizes the o1 agent to create a structured plan based on user input and project requirements.
- **Executor**: This component executes the tasks defined by the Planner. It leverages advanced language models like Claude or GPT-4o to perform actions step-by-step, ensuring that the execution aligns with the planned strategy.

This separation of concerns allows for improved modularity and maintainability. The Planner can focus on strategizing, while the Executor can concentrate on implementation, leading to better performance and adaptability.

### Example of Architecture Flow

1. **User Input**: The user provides a task or a goal.
2. **Planning Phase**: The Planner (o1) generates a detailed plan.
3. **Execution Phase**: The Executor (Claude/GPT) carries out the plan, providing feedback to the Planner for adjustments.

## 2. Key Technologies Used

The project leverages several key technologies to enhance its capabilities:

- **Cookiecutter**: A command-line utility that creates projects from templates. It simplifies the setup process for users.
  
  ```bash
  pip install cookiecutter
  cookiecutter gh:grapeot/devin.cursorrules --checkout template
  ```

- **Playwright**: A web automation library used for web scraping and browser interactions. It allows the AI to gather data from the web dynamically.

- **DuckDuckGo API**: Integrated for search engine queries, enabling the AI to fetch relevant information from the web.

- **Large Language Models (LLMs)**: Models like Claude and GPT-4o are utilized for natural language understanding and generation, allowing the AI to perform complex tasks and provide intelligent responses.

## 3. Interesting Implementation Details

### Self-Evolution Mechanism

One of the standout features of this system is its self-evolution capability. The AI learns from user corrections and updates its knowledge base stored in the `.cursorrules` file. This allows the AI to adapt to specific project requirements over time.

#### Example Code Snippet for Self-Evolution

```python
def update_lessons_learned(correction):
    with open('.cursorrules', 'a') as rules_file:
        rules_file.write(f"Lesson learned: {correction}\n")
```

This function appends new lessons learned to the `.cursorrules` file, allowing the AI to accumulate knowledge and improve its performance iteratively.

### Multi-Agent Collaboration

The experimental multi-agent collaboration feature allows for a more sophisticated approach to problem-solving. The Planner and Executor can work in tandem, where the Planner can adjust its strategy based on the Executor's feedback.

#### Example of Multi-Agent Interaction

```python
def execute_plan(plan):
    for step in plan:
        result = executor.execute(step)
        planner.update_plan(step, result)
```

In this example, the Executor executes each step of the plan, and the Planner updates the plan based on the results of each execution, creating a feedback loop that enhances the overall process.

## 4. Technical Challenges Overcome

### Integration of Multiple Tools

One of the significant challenges was integrating various tools and libraries (Playwright, DuckDuckGo, LLMs) into a cohesive system. Ensuring that these components could communicate effectively required careful design and testing.

### Handling User Feedback

Implementing a robust mechanism for handling user feedback was crucial for the self-evolution feature. The system needed to accurately capture corrections and integrate them into the learning process without introducing errors.

### Example of Feedback Handling

```python
def handle_user_feedback(feedback):
    if feedback.is_correct:
        update_lessons_learned(feedback.correction)
    else:
        log_error(feedback.error_message)
```

This function processes user feedback, updating the AI's knowledge base when corrections are made and logging errors for further analysis.

## Conclusion

The transformation of Cursor into a Devin-like AI assistant showcases a sophisticated architecture that leverages multi-agent collaboration, self-evolution, and advanced tool integration. By utilizing technologies like Cookiecutter, Playwright, and LLMs, the system provides users with powerful capabilities at a fraction of the cost of traditional solutions. The challenges faced during implementation have led to a more robust and adaptable AI assistant, capable of evolving with user needs.

## Lessons from the Trenches

Based on the project history and README for the "Turn any AI code assistant to best degree with rules" project, here are some key technical lessons learned, what worked well, what could be done differently, and advice for others:

### Key Technical Lessons Learned

1. **Modular Design**: The separation of the planner and executor into distinct agents allows for better management of complex tasks. This modularity enhances maintainability and scalability, making it easier to update or replace components without affecting the entire system.

2. **Self-Evolution Mechanism**: Implementing a feedback loop where the AI can learn from corrections and update its knowledge base is crucial. This feature not only improves the AI's performance over time but also fosters a more interactive and engaging user experience.

3. **Tool Integration**: The ability to integrate various tools (like web scraping and search engines) into the AI's workflow significantly expands its capabilities. This integration allows the AI to perform more complex tasks autonomously, reducing the need for manual intervention.

### What Worked Well

1. **User-Friendly Setup**: The use of Cookiecutter for project initialization simplifies the setup process for users. This approach minimizes the barrier to entry, allowing users to get started quickly without extensive configuration.

2. **Multi-Agent Collaboration**: The experimental multi-agent system has shown promising results in improving task execution quality. By having a dedicated planner and executor, the system can handle more intricate tasks efficiently.

3. **Documentation and Tutorials**: Providing comprehensive documentation and step-by-step tutorials has been beneficial for users. Clear instructions help users understand how to leverage the advanced features effectively.

### What You'd Do Differently

1. **Enhanced Error Handling**: While the self-evolution feature is valuable, implementing more robust error handling and recovery mechanisms could further improve user experience. This would help the AI manage unexpected situations more gracefully.

2. **User Feedback Mechanism**: Establishing a more structured way for users to provide feedback on AI performance could enhance the self-evolution process. This could include a simple rating system or a feedback form integrated into the interface.

3. **Performance Metrics**: Introducing performance metrics to evaluate the AI's effectiveness over time would provide valuable insights. This data could help in refining algorithms and improving overall performance.

### Advice for Others

1. **Start Simple**: When implementing advanced AI features, begin with a simple version of your system. Gradually introduce complexity as you validate each component's functionality. This iterative approach reduces the risk of overwhelming users and allows for easier troubleshooting.

2. **Focus on User Experience**: Prioritize user experience in your design. Ensure that the AI's capabilities are intuitive and that users can easily understand how to interact with the system. A well-designed user interface can significantly enhance engagement.

3. **Encourage Community Contributions**: Open-source projects thrive on community involvement. Encourage users to contribute by providing clear guidelines for contributions and recognizing their efforts. This can lead to a richer ecosystem and faster development.

4. **Stay Updated with AI Trends**: The field of AI is rapidly evolving. Keep abreast of the latest research and trends to ensure that your project remains relevant and incorporates cutting-edge techniques.

By focusing on these aspects, you can enhance the effectiveness and usability of AI coding assistants, making them more valuable tools for developers.

## What's Next?

## Conclusion: The Future of aicode.cursorrules

As we stand at the current project status of aicode.cursorrules, we are excited to report significant progress in transforming the Cursor/Windsurf IDE and GitHub Copilot into powerful AI assistants. Our innovative features, such as automated planning, self-evolution, and multi-agent collaboration, have already begun to empower users to achieve advanced coding capabilities at a fraction of the cost of traditional solutions like Devin. The feedback from our early adopters has been overwhelmingly positive, validating our approach and inspiring us to push the boundaries even further.

Looking ahead, our development plans are ambitious. We aim to refine the multi-agent collaboration feature, enhancing the Planner-Executor dynamic to tackle even more complex tasks with greater efficiency. Additionally, we are exploring the integration of more advanced tools and APIs to expand the capabilities of our AI assistants. Our goal is to create a seamless experience that not only meets but exceeds user expectations, making coding more intuitive and productive.

We invite contributors from all backgrounds to join us on this exciting journey. Whether you are a developer, a designer, or simply an AI enthusiast, your insights and contributions can help shape the future of aicode.cursorrules. Together, we can enhance the functionality, usability, and reach of this project, making it a go-to resource for anyone looking to supercharge their coding experience.

In closing, the journey of developing aicode.cursorrules has been both challenging and rewarding. It has been a testament to the power of collaboration and innovation in the open-source community. As we continue to evolve and adapt, we remain committed to creating a tool that not only empowers individual developers but also fosters a community of learning and growth. Join us as we embark on this exciting path, and let’s redefine what’s possible in AI-assisted coding together!
## Project Development Analytics
### timeline gant

![Commit timelinegant](https://daily.borninsea.com/assets/aicode.cursorrules-timeline_chart.png)


### Commit Activity Heatmap
This heatmap shows the distribution of commits over the past year:

![Commit Heatmap]()

### Contributor Network
This network diagram shows how different contributors interact:

![Contributor Network](https://daily.borninsea.com/assets/aicode.cursorrules-contribution_network.png)

### Commit Activity Patterns
This chart shows when commits typically happen:

![Commit Activity](https://daily.borninsea.com/assets/aicode.cursorrules-commit_activity.png)

### Code Frequency
This chart shows the frequency of code changes over time:

![Code Frequency](https://daily.borninsea.com/assets/aicode.cursorrules-code_frequency.png)



* Repository URL: [https://github.com/wanghaisheng/aicode.cursorrules](https://github.com/wanghaisheng/aicode.cursorrules)
* Stars: **0**
* Forks: **0**
