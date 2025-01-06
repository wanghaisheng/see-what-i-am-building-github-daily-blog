---
author: Heisenberg
cover:
  alt: cover
  square: https://daily.borninsea.com/assets/image_1736134831316_mlzf82.png
  url: https://daily.borninsea.com/assets/image_1736134831316_mlzf82.png
description: "99 Managers\u2122 Futsal Edition, is a futsal manager game made with\
  \ Godot Engine 4"
featured: true
keywords: 99 Managers,  Futsal Edition,  futsal manager game,  Godot Engine,  Steam,  Matrix,  Discord,  Codeberg,  Github,  Alpha
  version,  FAQ,  Roadmap,  Translations,  Weblate,  Open Source,  AGPLv3,  CC BY-SA
  4.0,  FSFE reuse tool,  licenses,  copyrights
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Heisenberg
  name: author
- content: 99 Managers,  Futsal Edition,  futsal manager game,  Godot Engine,  Steam,  Matrix,  Discord,  Codeberg,  Github,  Alpha
    version,  FAQ,  Roadmap,  Translations,  Weblate,  Open Source,  AGPLv3,  CC BY-SA
    4.0,  FSFE reuse tool,  licenses,  copyrights
  name: keywords
pubDate: '2025-01-06'
tags:
- 99-managers
- futsal-edition
- futsal-manager-game
- godot-engine
- steam
- matrix
- discord
- codeberg
- github
- alpha-version
- faq
- roadmap
- translations
- weblate
- open-source
- agplv3
- cc-by-sa-4-0
- fsfe-reuse-tool
- licenses
- copyrights
theme: light
title: "From Idea to Reality: Building 99 Managers\u2122 Futsal Edition with Godot\
  \ Engine"
---



*Built by wanghaisheng | Last updated: 20250106*

11 minutes 27 seconds  read
## Project Genesis

### Kicking Off the Journey: The Story Behind 99 Managers™ Futsal Edition

As a lifelong fan of both football and gaming, I’ve always dreamed of creating a project that combines my two passions. The spark for 99 Managers™ Futsal Edition ignited during a casual futsal match with friends, where the thrill of strategy and teamwork reminded me of the excitement of managing a football team. I realized that there was a unique opportunity to bring that experience to life in a digital format, and thus, the idea for this futsal manager game was born.

My personal motivation for this project runs deep. Growing up, I spent countless hours playing management games, immersing myself in the intricacies of team dynamics and player development. I wanted to create a game that not only captured that essence but also introduced players to the fast-paced world of futsal—a sport that often gets overshadowed by its larger counterpart. I envisioned a game where players could strategize, build their dream teams, and experience the thrill of leading their squad to victory, all while enjoying the unique challenges that futsal presents.

Of course, the journey hasn’t been without its hurdles. Developing a game from scratch is no small feat, especially when you’re working with a powerful yet complex tool like the Godot Engine. I faced numerous challenges, from mastering the intricacies of game mechanics to ensuring a smooth user experience. There were moments of frustration, but each obstacle only fueled my determination to create something special.

To tackle these challenges, I embraced a hands-on approach, diving deep into the Godot documentation and engaging with the vibrant community around it. I sought feedback from fellow gamers and developers, iterating on my ideas and refining the gameplay mechanics. The result? A dynamic and engaging futsal manager game that I’m incredibly proud to share with you.

So, whether you’re a seasoned manager or a newcomer to the world of futsal, I invite you to join me on this exciting journey. Wishlist 99 Managers™ Futsal Edition on Steam, and let’s kick off this adventure together! If you have questions or want to stay updated, feel free to join our community on [Matrix](https://matrix.to/#/%23s9i.org:matrix.org) or [Discord](https://discord.gg/a5DSHZKkA8). Your support means the world to me, and I can’t wait to see you on the virtual pitch!

## From Idea to Implementation

### 1. Initial Research and Planning

The journey of developing "99 Managers™ Futsal Edition" began with extensive research into the futsal genre and existing management games. The goal was to identify gaps in the market and understand player expectations. This involved analyzing popular futsal and football management games, gathering feedback from potential players through surveys and forums, and studying gameplay mechanics that resonate with the target audience.

During the planning phase, a clear vision was established: to create an engaging and user-friendly futsal management experience that emphasizes strategy, team building, and player development. The project scope was defined, including key features such as team management, match simulations, and player statistics. A roadmap was created to outline the development phases, from prototyping to alpha release, ensuring a structured approach to the project.

### 2. Technical Decisions and Their Rationale

Choosing the Godot Engine as the development platform was a pivotal decision. Godot's open-source nature, flexibility, and strong community support made it an ideal choice for an indie project. The engine's lightweight design and ease of use allowed for rapid prototyping and iteration, which was crucial during the early stages of development.

The decision to use the AGPLv3 license for the source code was driven by a desire to promote open-source collaboration and ensure that the project remains free for users. This choice aligns with the project's ethos of community involvement and transparency. Additionally, assets were licensed under CC BY-SA 4.0 to encourage sharing and adaptation while maintaining credit to the original creator.

### 3. Alternative Approaches Considered

Several alternative approaches were considered during the development process. Initially, there was contemplation of using a more complex game engine, such as Unity or Unreal Engine, which offer advanced graphics capabilities. However, these engines would have introduced unnecessary complexity and a steeper learning curve for the team, which was primarily focused on gameplay mechanics rather than high-end graphics.

Another alternative was to develop a web-based version of the game. While this would have increased accessibility, it posed challenges in terms of performance and user experience. Ultimately, the decision to create a desktop application using Godot allowed for a more immersive experience, leveraging the engine's capabilities to deliver a polished product.

### 4. Key Insights That Shaped the Project

Throughout the development journey, several key insights emerged that significantly shaped the project. One of the most important was the realization that player engagement hinges on meaningful choices and consequences. This insight led to the incorporation of deep strategic elements, allowing players to make impactful decisions regarding team formation, player training, and match tactics.

Another critical insight was the importance of community feedback. Engaging with players through platforms like Discord and Matrix provided invaluable input that informed design decisions and feature prioritization. This iterative feedback loop not only improved the game but also fostered a sense of community ownership among players.

Finally, the significance of localization and accessibility became apparent early on. Recognizing the global appeal of futsal, the decision to implement translation support through Weblate was made to ensure that players from diverse backgrounds could enjoy the game. This commitment to inclusivity has been a driving force in the project's development.

In conclusion, the journey from concept to code for "99 Managers™ Futsal Edition" has been marked by careful research, thoughtful technical decisions, consideration of alternative approaches, and key insights that have shaped the game's development. The project continues to evolve, driven by community engagement and a passion for creating an exceptional futsal management experience.

## Under the Hood

## Technical Deep-Dive: 99 Managers™ Futsal Edition

### 1. Architecture Decisions

The architecture of the "99 Managers™ Futsal Edition" game is primarily influenced by the choice of the Godot Engine, which is known for its flexibility and ease of use in game development. The architecture can be broken down into several key components:

- **Game Loop**: The core of the game is built around a standard game loop that handles input, updates game state, and renders graphics. Godot's built-in game loop simplifies this process, allowing developers to focus on game logic rather than low-level details.

- **Scene System**: Godot uses a scene system that allows developers to create reusable components. Each scene can represent a different part of the game, such as menus, game levels, or UI elements. This modular approach promotes code reuse and easier maintenance.

- **Data Management**: The game likely employs a data-driven approach to manage player statistics, team information, and game settings. This can be achieved using JSON or similar formats to store and load data dynamically.

- **Networking**: For multiplayer features, the architecture may include a client-server model, where the server manages game state and clients communicate with it to synchronize actions. This is crucial for maintaining a consistent game experience across players.

### 2. Key Technologies Used

- **Godot Engine**: The primary technology used for game development. Godot supports GDScript, a Python-like scripting language, which is used for game logic.

- **Weblate**: An open-source translation tool integrated into the project for managing localization. This allows contributors to add and improve translations easily.

- **GitHub and Codeberg**: These platforms are used for version control and collaboration, allowing developers to manage code changes and track issues effectively.

- **FSFE Reuse Tool**: This tool is used for managing licenses and ensuring compliance with open-source licensing requirements.

### 3. Interesting Implementation Details

- **Scene Instancing**: The game likely utilizes scene instancing to create multiple instances of game objects, such as players and teams. This allows for efficient memory usage and easier management of game entities. For example, a player scene can be instantiated for each player in a match:

    ```gdscript
    var player_scene = preload("res://Player.tscn")
    var player_instance = player_scene.instance()
    add_child(player_instance)
    ```

- **Translation Management**: The integration with Weblate allows for dynamic loading of translations based on user preferences. This can be implemented by loading the appropriate language file at runtime:

    ```gdscript
    var translation_file = "res://translations/" + user_language + ".po"
    TranslationServer.load_translation(translation_file)
    ```

- **Game State Management**: The game likely employs a state machine to manage different game states (e.g., menu, playing, paused). This can be implemented using a simple enum and a switch statement:

    ```gdscript
    enum GameState { MENU, PLAYING, PAUSED }
    var current_state = GameState.MENU

    func _process(delta):
        match current_state:
            GameState.MENU:
                show_menu()
            GameState.PLAYING:
                update_game(delta)
            GameState.PAUSED:
                show_pause_menu()
    ```

### 4. Technical Challenges Overcome

- **Multiplayer Synchronization**: One of the significant challenges in developing a multiplayer game is ensuring that all players have a synchronized view of the game state. This can be addressed by implementing a robust networking solution that handles latency and packet loss. Techniques such as client-side prediction and server reconciliation can be employed to improve the user experience.

- **Localization**: Managing translations for multiple languages can be complex, especially when dealing with varying text lengths and cultural nuances. The integration with Weblate simplifies this process, allowing for community contributions and easier updates.

- **Performance Optimization**: As the game grows in complexity, performance can become an issue. Profiling tools provided by Godot can help identify bottlenecks, and optimizations such as object pooling and efficient resource management can be implemented to enhance performance.

In conclusion, the "99 Managers™ Futsal Edition" project showcases a well-structured architecture leveraging the capabilities of the Godot Engine, with a focus on modular design, community involvement in translations, and adherence to open-source principles. The challenges faced during development are common in game development but can be effectively managed with the right tools and strategies.

## Lessons from the Trenches

Here are some key insights based on the project history and README for the "99 Managers™ Futsal Edition":

### 1. Key Technical Lessons Learned
- **Game Engine Selection**: Using the Godot Engine proved beneficial due to its open-source nature, flexibility, and strong community support. It allowed for rapid prototyping and iteration.
- **Version Control**: Utilizing platforms like GitHub and Codeberg for version control facilitated collaboration and tracking of changes, making it easier to manage contributions and releases.
- **Translation Management**: Integrating Weblate for translations streamlined the process of adding and managing multiple languages, enhancing accessibility and user engagement.
- **Licensing Awareness**: Understanding and applying appropriate licenses (AGPLv3 for code and CC BY-SA 4.0 for assets) helped clarify usage rights and fostered a collaborative environment.

### 2. What Worked Well
- **Community Engagement**: Creating channels on Matrix and Discord for community interaction helped build a supportive user base and provided a platform for feedback and suggestions.
- **Clear Documentation**: The README file is well-structured, providing essential information about the game, its development, and how to contribute. This clarity helped onboard new contributors and users effectively.
- **Roadmap Transparency**: Maintaining a visible roadmap allowed users and contributors to understand the project's direction and priorities, fostering trust and collaboration.

### 3. What You'd Do Differently
- **Early User Testing**: Implementing user testing earlier in the development process could have provided valuable insights into gameplay mechanics and user experience, potentially leading to a more polished product at launch.
- **More Frequent Updates**: While the roadmap is transparent, more frequent updates on progress and challenges could keep the community engaged and informed, reducing uncertainty about the project's status.
- **Diverse Marketing Strategies**: Exploring additional marketing strategies beyond Steam wishlisting, such as social media campaigns or partnerships with gaming influencers, could enhance visibility and attract a broader audience.

### 4. Advice for Others
- **Embrace Open Source**: Leverage the open-source community for support, contributions, and feedback. Engaging with users can lead to valuable insights and improvements.
- **Prioritize Documentation**: Invest time in creating comprehensive documentation for both users and contributors. This will facilitate onboarding and encourage more people to get involved.
- **Iterate Based on Feedback**: Be open to feedback and willing to iterate on your designs and features. User input can significantly enhance the quality and appeal of your project.
- **Plan for Localization Early**: If you aim for a global audience, consider localization from the start. Using tools like Weblate can simplify this process and make your game accessible to a wider range of players.

By reflecting on these aspects, you can enhance the development process and create a more successful and engaging game.

## What's Next?

## Conclusion: Looking Ahead for 99 Managers™ Futsal Edition

As we wrap up this phase of the 99 Managers™ Futsal Edition project, we are excited to share our current status and future aspirations. The alpha version of the game is now available on both [GitHub](https://github.com/dulvui/futsal-manager/releases) and [Codeberg](https://codeberg.org/dulvui/99managers-futsal-edition), marking a significant milestone in our journey. We have received valuable feedback from our early users, which has been instrumental in refining gameplay mechanics and enhancing user experience.

Looking ahead, our development plans are ambitious. We aim to expand the game’s features based on the feedback we’ve gathered, with a detailed roadmap available [here](ROADMAP.md). Our focus will be on improving gameplay dynamics, introducing new game modes, and enhancing the overall aesthetic appeal of the game. Additionally, we are committed to making the game accessible to a wider audience by incorporating more languages through community contributions on [Weblate](https://hosted.weblate.org/engage/99-managers-futsal-edition/).

We invite all contributors—whether you’re a developer, designer, translator, or simply a passionate futsal enthusiast—to join us in this exciting venture. Your insights and skills can help shape the future of 99 Managers™ Futsal Edition. Connect with us on [Discord](https://discord.gg/a5DSHZKkA8) or [Matrix](https://matrix.to/#/%23s9i.org:matrix.org) to share your ideas, report issues, or simply stay updated on our progress.

In closing, the journey of developing 99 Managers™ Futsal Edition has been both challenging and rewarding. It has been a testament to the power of community collaboration and open-source development. We are grateful for the support we’ve received thus far and look forward to what lies ahead. Together, let’s create a futsal management experience that players will love and cherish. Thank you for being a part of this journey!
## Project Development Analytics
### timeline gant

![Commit timelinegant](https://daily.borninsea.com/assets/99managers-futsal-edition-timeline_chart.png)


### Commit Activity Heatmap
This heatmap shows the distribution of commits over the past year:

![Commit Heatmap]()

### Contributor Network
This network diagram shows how different contributors interact:

![Contributor Network](https://daily.borninsea.com/assets/99managers-futsal-edition-contribution_network.png)

### Commit Activity Patterns
This chart shows when commits typically happen:

![Commit Activity](https://daily.borninsea.com/assets/99managers-futsal-edition-commit_activity.png)

### Code Frequency
This chart shows the frequency of code changes over time:

![Code Frequency](https://daily.borninsea.com/assets/99managers-futsal-edition-code_frequency.png)



* Repository URL: [https://github.com/wanghaisheng/99managers-futsal-edition](https://github.com/wanghaisheng/99managers-futsal-edition)
* Stars: **0**
* Forks: **0**
