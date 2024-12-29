---
author: Heisenberg
cover:
  alt: cover
  square: https://daily.borninsea.com/assets/image_1735514225495_7syyws.png
  url: https://daily.borninsea.com/assets/image_1735514225495_7syyws.png
description: 'Code associated with the EMNLP 2024 Main paper: "Image, tell me your
  story!" Predicting the original meta-context of visual misinformation.'
featured: true
keywords: 5Pils,  EMNLP 2024,  visual misinformation,  meta-context,  dataset,  Apache
  2.0,  CC-BY-SA-4.0,  fact-checkers,  automated approaches,  veracity scores,  inconsistencies,  forgeries,  image
  contextualization,  question-answer pairs,  5 Pillars framework,  retrieval,  reasoning,  Iryna
  Gurevych,  TU Darmstadt,  UKP Lab,  Miami.
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Heisenberg
  name: author
- content: 5Pils,  EMNLP 2024,  visual misinformation,  meta-context,  dataset,  Apache
    2.0,  CC-BY-SA-4.0,  fact-checkers,  automated approaches,  veracity scores,  inconsistencies,  forgeries,  image
    contextualization,  question-answer pairs,  5 Pillars framework,  retrieval,  reasoning,  Iryna
    Gurevych,  TU Darmstadt,  UKP Lab,  Miami.
  name: keywords
pubDate: '2024-12-30'
tags:
- 5pils
- emnlp-2024
- visual-misinformation
- dataset
- apache-2-0
- cc-by-sa-4-0
- fact-checking
- automated-image-contextualization
- 5-pillars-framework
- iryna-gurevych
- miami
- tu-darmstadt
- ukp-lab
- image-captioning
- veracity-scores
- misinformation-detection
- question-answer-pairs
- retrieval
- reasoning
theme: light
title: 'From Idea to Reality: Building 5pils to Combat Visual Misinformation'
---



*Built by wanghaisheng | Last updated: 20241230*

12 minutes 41 seconds  read
## Project Genesis

### Unveiling the Truth Behind Visual Misinformation: My Journey with 5Pils

In a world where images can be manipulated and misrepresented at the click of a button, the need for clarity and truth has never been more pressing. My journey into the realm of visual misinformation began with a simple yet profound question: How can we discern the original context of an image? This curiosity sparked the creation of the 5Pils dataset, a project that has not only challenged my understanding of visual narratives but has also ignited a passion for uncovering the stories behind the pixels.

As I delved deeper into this project, I found myself motivated by a personal mission: to empower individuals with the tools to critically analyze the images they encounter daily. The rise of misinformation in our digital age is alarming, and I felt compelled to contribute to a solution that could help restore trust in visual media. However, the path was not without its hurdles. I faced initial challenges in curating a comprehensive dataset that accurately represented the complexities of visual storytelling. The task of predicting the original meta-context of images was daunting, but it was this very challenge that fueled my determination to push forward.

Through countless hours of research, collaboration, and experimentation, I developed a framework that not only addresses these challenges but also provides a robust solution for predicting the original context of images. The 5Pils dataset, introduced in our EMNLP 2024 paper, is a testament to the power of perseverance and innovation. In this blog post, I invite you to join me on this journey as we explore the intricacies of visual misinformation, the inspiration behind 5Pils, and the potential it holds for fostering a more informed society. Together, let’s uncover the stories that images tell and the truths they may conceal.

## From Idea to Implementation

### 1. Initial Research and Planning

The journey of developing the 5Pils dataset began with a thorough investigation into the existing methodologies for visual misinformation detection. Researchers recognized that while many automated systems focused on identifying inconsistencies between images and their captions or detecting forgeries, they often overlooked a critical aspect of the fact-checking process: understanding the original meta-context of an image. This gap in the literature prompted the team to explore how automated image contextualization could enhance the effectiveness of fact-checkers.

The planning phase involved defining the scope of the project, which included the creation of a dataset that would not only provide images but also detailed annotations based on the 5 Pillars fact-checking framework. The team aimed to compile a diverse set of 1,676 fact-checked images, ensuring that the dataset would be representative of real-world misinformation scenarios. This phase also included discussions on ethical considerations, particularly regarding the inclusion of graphic content, which was deemed necessary to reflect the true nature of misinformation that fact-checkers encounter.

### 2. Technical Decisions and Their Rationale

Several key technical decisions were made during the development of the 5Pils dataset. One of the primary choices was the selection of the 5 Pillars framework as the basis for annotations. This framework provided a structured approach to categorizing the meta-context of images, allowing for a comprehensive understanding of the factors surrounding each piece of misinformation.

The decision to release the dataset under a **CC-BY-SA-4.0** license was also significant, as it aimed to promote collaboration and further research in the field of misinformation detection. Additionally, the team opted to implement a baseline model that utilized both image content and textual evidence retrieved from the open web. This multimodal approach was chosen to enhance the model's ability to ground images in their original context, leveraging the strengths of both visual and textual data.

### 3. Alternative Approaches Considered

During the planning and development phases, the team considered several alternative approaches to the dataset's creation and the model's implementation. One alternative was to focus solely on image manipulation detection without incorporating the broader context of the images. However, this approach was quickly dismissed as it would not address the core objective of understanding the original meta-context of the images.

Another alternative was to filter out images containing graphic content to create a more sanitized dataset. However, the team recognized that this would not accurately represent the types of images that professional fact-checkers encounter in their work. Ultimately, the decision was made to include such images while providing appropriate content warnings, ensuring that the dataset remained relevant and useful for its intended audience.

### 4. Key Insights That Shaped the Project

Several key insights emerged throughout the project's development that significantly shaped its direction. One of the most important was the realization that effective misinformation detection requires a holistic understanding of the context surrounding an image, rather than merely focusing on its content. This insight underscored the importance of the 5 Pillars framework and informed the design of the dataset and the baseline model.

Another critical insight was the necessity of collaboration between different modalities—specifically, the integration of visual and textual evidence. This realization led to the development of a multimodal approach that would allow the model to leverage diverse sources of information, ultimately improving its performance in contextualizing images.

Finally, the team recognized the importance of community engagement and feedback. By releasing the dataset and code under open licenses and encouraging collaboration, the researchers aimed to foster a community of practitioners and researchers who could contribute to the ongoing development of tools for combating visual misinformation.

In summary, the journey from concept to code for the 5Pils project involved extensive research, thoughtful technical decisions, consideration of alternative approaches, and the incorporation of key insights that ultimately shaped the project's goals and outcomes. The result is a dataset and framework that not only addresses a critical gap in the field of misinformation detection but also serves as a valuable resource for future research and development.

## Under the Hood

# Technical Deep-Dive: "Image, Tell me your story!" Predicting the Original Meta-Context of Visual Misinformation

## 1. Architecture Decisions

The architecture of the 5Pils project is designed to facilitate the automated contextualization of images in the realm of visual misinformation. The key architectural decisions include:

- **Modular Design**: The codebase is structured into distinct modules for data collection, processing, evaluation, and model inference. This modularity allows for easier maintenance and scalability. For example, the dataset is processed in separate scripts, such as `build_dataset_from_url.py` for downloading images and `evaluate_answer_generation.py` for evaluating model performance.

- **Baseline Model**: The project implements a baseline model that combines visual and textual evidence to ground images in their original meta-context. This model leverages a Vision Transformer (ViT) for image classification and a multimodal approach for generating answers based on the 5 Pillars framework.

- **Data-Driven Approach**: The architecture emphasizes the importance of data quality and relevance. The 5Pils dataset is curated with 1,676 fact-checked images, ensuring that the model is trained on high-quality, relevant data.

## 2. Key Technologies Used

The project employs several key technologies that enhance its functionality:

- **Python**: The primary programming language used for implementing the project. The code is compatible with Python 3.9, ensuring a stable environment for development.

- **SpaCy**: A natural language processing library used for various text processing tasks, including downloading language models. The command `python -m spacy download en_core_web_lg` is used to download the large English language model.

- **Google Vision API**: This API is utilized for reverse image search, allowing the model to collect evidence based on image URLs. The integration of this API is crucial for the model's ability to retrieve relevant textual evidence.

- **Azure OpenAI Service**: For advanced answer generation, the project can leverage GPT-4 (Vision) through the Azure OpenAI service, providing a powerful tool for generating contextual answers based on the retrieved evidence.

## 3. Interesting Implementation Details

Several implementation details stand out in the 5Pils project:

- **Dataset Structure**: The dataset is organized into JSON files (`train.json`, `val.json`, `test.json`), which contain annotated question-answer pairs. This structure allows for easy access and manipulation of the data during training and evaluation.

- **Image Downloading**: The project provides a script (`build_dataset_from_url.py`) to automate the downloading of images based on the URLs provided in the dataset. This script simplifies the process of dataset preparation.

    ```python
    # Example of downloading images
    $ python scripts/build_dataset_from_url.py
    ```

- **Evaluation Framework**: The evaluation process is designed to be flexible, allowing users to evaluate model performance on specific pillars. For instance, to evaluate the model's performance on the "Date" pillar, the following command is used:

    ```python
    $ python scripts/evaluate_answer_generation.py --results_file output/results_date.json --task date
    ```

- **Embedding Computation**: The project includes functionality to compute embeddings for evidence ranking and few-shot demonstration selection, which is essential for improving the model's performance in contextualization tasks.

    ```python
    # Compute embeddings for evidence ranking
    $ python scripts/get_embeddings.py
    ```

## 4. Technical Challenges Overcome

The development of the 5Pils project faced several technical challenges, which were addressed through innovative solutions:

- **Handling Misinformation**: One of the primary challenges was the inherent complexity of visual misinformation. The project addresses this by focusing on the original meta-context of images, which is often overlooked in traditional misinformation detection methods. The introduction of the 5 Pillars framework provides a structured approach to contextualization.

- **Data Collection and Annotation**: Collecting and annotating a dataset of 1,676 fact-checked images required significant effort. The team opted not to filter out images with violent content to maintain the dataset's relevance for professional fact-checkers. This decision necessitated careful handling of sensitive content, leading to the release of URLs instead of direct image files.

- **Integration of Multiple Data Sources**: The project successfully integrates various data sources, including images, textual evidence, and external APIs (Google Vision API). This integration required careful design to ensure that the data flows seamlessly through the system.

- **Model Performance Evaluation**: Evaluating the model's performance on specific tasks (e.g., date and location verification) posed challenges in terms of defining metrics and ensuring that the evaluation process was robust. The project provides clear guidelines and scripts for conducting evaluations, which helps mitigate these challenges.

In conclusion, the 5Pils project represents a significant advancement in the field of visual misinformation detection by focusing on the original meta-context of images. Through thoughtful architectural decisions, the use of key technologies, and the overcoming of technical challenges,

## Lessons from the Trenches

Here are some key technical lessons learned, what worked well, what could be done differently, and advice for others based on the project "Image, Tell me your story! Predicting the original meta-context of visual misinformation":

### 1. Key Technical Lessons Learned
- **Data Annotation Complexity**: Annotating images with their original meta-context is a complex task that requires a deep understanding of both the visual content and the associated textual information. The 5 Pillars framework provided a structured approach, but ensuring high-quality annotations was challenging.
- **Model Performance Variability**: The performance of models in detecting misinformation can vary significantly based on the quality of the training data and the chosen architecture. Experimenting with different models (e.g., ViT, multimodal models) helped identify the best fit for the task.
- **Importance of Contextual Evidence**: The retrieval of contextual evidence from the web is crucial for grounding the image in its original context. The integration of reverse image search and evidence collection tools proved essential for improving model accuracy.

### 2. What Worked Well
- **Structured Dataset**: The creation of the 5Pils dataset with clear annotations based on the 5 Pillars framework facilitated focused research and experimentation. The dataset's structure allowed for straightforward evaluation and comparison of different models.
- **Baseline Implementation**: The implementation of a baseline model that combined image content with textual evidence retrieval was effective in demonstrating the feasibility of the approach. This provided a solid foundation for further improvements and refinements.
- **Community Engagement**: Presenting the work at conferences and engaging with the research community helped gather valuable feedback and foster collaborations, which enriched the project.

### 3. What You'd Do Differently
- **Enhanced Data Filtering**: While the decision to include graphic content was made to reflect real-world scenarios, a more nuanced approach to filtering could be considered to balance the dataset's representativeness with ethical considerations.
- **Broader Model Testing**: Expanding the range of models tested, including more recent architectures and techniques, could yield better performance. Future work could involve experimenting with ensemble methods or hybrid models that leverage both visual and textual data more effectively.
- **User-Centric Evaluation**: Incorporating feedback from actual fact-checkers during the evaluation phase could provide insights into the practical utility of the model outputs, leading to more user-friendly solutions.

### 4. Advice for Others
- **Invest in Quality Annotations**: Ensure that the annotation process is rigorous and involves domain experts. High-quality annotations are critical for training effective models, especially in complex tasks like misinformation detection.
- **Iterate on Model Development**: Be prepared to iterate on model designs and experiment with various architectures. The landscape of machine learning is rapidly evolving, and staying updated with the latest advancements can lead to significant improvements.
- **Engage with the Community**: Actively seek feedback from peers and practitioners in the field. Presenting your work at conferences and workshops can provide valuable insights and foster collaborations that enhance the research.
- **Consider Ethical Implications**: Always consider the ethical implications of your work, especially when dealing with sensitive content. Strive to balance the need for comprehensive datasets with the responsibility to avoid causing harm or distress.

By reflecting on these aspects, future projects can be better positioned to tackle the challenges of visual misinformation and contribute meaningfully to the field.

## What's Next?

## Conclusion: Looking Ahead with 5Pils

As we reflect on the current status of the 5Pils project, we are excited to share that our dataset has been successfully introduced and accepted for presentation at the EMNLP 2024 conference. The 5Pils dataset, comprising 1,676 meticulously fact-checked images annotated with question-answer pairs, is now available for researchers and practitioners interested in tackling the critical issue of visual misinformation. Our initial baseline model has shown promising results, yet we recognize that there are still significant challenges to address in the realms of retrieval and reasoning.

Looking to the future, we have ambitious plans for the continued development of 5Pils. We aim to enhance our baseline model by incorporating advanced machine learning techniques and expanding our dataset to include a broader range of visual misinformation scenarios. Additionally, we are exploring collaborations with fact-checking organizations to refine our annotations and ensure that our dataset remains relevant and impactful. We envision 5Pils becoming a cornerstone resource for researchers and developers working on automated image contextualization and misinformation detection.

We invite contributors from diverse backgrounds—be it researchers, developers, or fact-checkers—to join us on this journey. Your insights, expertise, and contributions can help us improve the dataset, develop more robust models, and ultimately make strides in the fight against misinformation. Whether you have ideas for new features, wish to collaborate on research, or simply want to provide feedback, we encourage you to reach out and get involved.

In closing, the journey of developing 5Pils has been both challenging and rewarding. We have witnessed the power of collaboration and innovation in addressing a pressing societal issue. As we move forward, we remain committed to our mission of empowering fact-checkers and researchers with the tools they need to combat visual misinformation effectively. Together, we can make a meaningful impact in this critical area. Thank you for your support, and we look forward to your contributions!
## Project Development Analytics
### timeline gant

![Commit timelinegant](https://daily.borninsea.com/assets/5pils-timeline_chart.png)


### Commit Activity Heatmap
This heatmap shows the distribution of commits over the past year:

![Commit Heatmap]()

### Contributor Network
This network diagram shows how different contributors interact:

![Contributor Network](https://daily.borninsea.com/assets/5pils-contribution_network.png)

### Commit Activity Patterns
This chart shows when commits typically happen:

![Commit Activity](https://daily.borninsea.com/assets/5pils-commit_activity.png)

### Code Frequency
This chart shows the frequency of code changes over time:

![Code Frequency](https://daily.borninsea.com/assets/5pils-code_frequency.png)



* Repository URL: [https://github.com/wanghaisheng/5pils](https://github.com/wanghaisheng/5pils)
* Stars: **0**
* Forks: **0**
