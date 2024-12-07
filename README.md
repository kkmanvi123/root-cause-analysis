# Root Cause Analysis for Cadence Design Systems

## Project Overview

This project aims to develop a machine learning (ML) model to identify the root causes of software program failures (bugs). By analyzing historical failure data, the model uncovers patterns and correlations, enabling faster and more effective debugging processes. This work is critical for software development organizations like Cadence Design Systems, where debugging is both time-sensitive and resource-intensive. Engineers currently spend up to 70% of their time debugging, and team-developed software often requires years of expertise for mastery.

The goal is to create a solution that not only classifies bug failure types but also identifies the most effective ML algorithm to solve the problem. Additionally, the project incorporates this model into a user-friendly terminal-based tool to streamline its integration into developers' workflows. By significantly reducing debugging time, the project empowers engineers to focus more on innovative development tasks, enhancing productivity and customer satisfaction.

## Objectives
1. **Understand and define the problem**: Clearly identify the goals and scope of root cause analysis.
2. **Develop a machine learning model**: Create and optimize an ML model capable of accurately classifying bug types.
3. **Select the best methodology**: Explore and compare various ML algorithms to identify the most effective approach.
4. **Integrate with developer tools**: Build a model terminal for real-world usability and integration into debugging workflows.

## Methodology

### Data Understanding and Preparation
- Initially, team-generated buggy and fixed code served as training data. However, scalability challenges led to adopting publicly available datasets,  such as the [Microsoft Inferred Bugs Dataset](https://github.com/microsoft/InferredBugs/tree/main).
- Key steps included:
  - Filtering buggy code for relevant features.
  - Leveraging feature engineering to improve model performance.

### Modeling and Evaluation
- Models evaluated: Logistic Regression (baseline) and Random Forest (chosen model).
- Random Forest excelled due to its ability to handle high-dimensional data and provide feature importance insights.
- Evaluation metrics included accuracy, ROC-AUC, and confusion matrices.
- Cross-validation (GridSearch and RandomSearch) helped refine hyperparameters for optimal performance.

## Results
- **Model Performance**: 
  - Random Forest achieved an ROC-AUC of 92%, outperforming Logistic Regression at 71%.
  - High true positive and true negative rates with a balanced error rate.
- **Insights**:
  - Features like resource allocation and mutable object usage were critical in predicting memory leaks and null dereference bugs.
  - Precision-focused evaluation ensured high-confidence predictions, reducing developer time waste.

## Potential Next Steps
1. **Expand Bug Types**: Introduce more categories to enhance the model's versatility.
2. **Increase Dataset Size**: Collect additional data for better generalizability and reduced misclassification.
3. **Refine Feature Engineering**: Explore new features to differentiate bug types more effectively.
4. **Specificity Improvements**: Add details like the line number or range where errors occur.
5. **Process Iteration**: Continue refining data collection, feature selection, and terminal integration.

## Business Impact
This project addresses a critical pain point in software development: debugging. By reducing the time and effort needed for bug fixes, this model can significantly improve productivity for software engineers and enhance customer satisfaction.

## Running the program.

### Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Git**: [Download Git](https://git-scm.com/downloads)
- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **Pip**: Comes bundled with Python 3.x

### Installation Steps

#### 1. Clone the Repository

Start by cloning the repository to your local machine using Git. Open your terminal and execute:

```bash
git clone https://github.com/kkmanvi123/root-cause-analysis.git
```

#### 2. Navigate to the Project Directory

Change your current directory to the cloned repository:

```bash
cd root-cause-analysis
```

#### 3. Install Python Dependencies

Ensure you have all the required Python packages installed. Run the following command:

```bash
pip3 install -r requirements.txt
```

#### 4. Run the Debugger
   
To execute the debugger, navigate to the bttai-debugger directory and run the debugger script. Replace <buggy-file.java> with the path to your actual Java file

```bash
cd bttai-debugger
python3 debugger.py <buggy-file.java>
```

## Contributing

### Reproducing the Project

To successfully reproduce and extend this project, follow these guidelines:

1. **Use the `.ipynb` file in the GitHub repository** to generate the model. After making your desired edits, download the model as a `.pkl` file. Follow the outlined steps to test the updated model.

2. **Do not modify the original `.ipynb` Google Colab file.** Instead, create a copy of the file to make your changes. Use this copy to:
   - Improve the existing functionality.
   - Add new features.
   - Refine the project further.

3. **Testing the new model**:
   - Follow the documented steps carefully.
   - To customize test scenarios, modify the `.java` file with the code snippets of your choice.

4. **Handling the `.py` file**:
   - The `.py` file should remain unchanged unless you:
     - Add new features.
     - Include more bugs.
     - Change the name of your `.pkl` file.
   - If you make changes, ensure the `.py` file contains the correct information. The testing steps will not work as expected if the necessary information is missing or incorrect.

By adhering to these instructions, you can reproduce and extend the project while maintaining compatibility with the existing workflow.


### License
Purpose: State the licensing under which the project is released.
Suggested Content: A short statement about the license, typically linking to the full license file.
Credits and Acknowledgments


## Resources Leveraged
- Github Repository for data: Microsoft Inferred Bugs
- Google Colab: To train and develop the model
- Scikit learn, Pandas, numpy
- Jira: Project management
- Google Drive: File documentation management

## Acknowledgements

We have gained invaluable knowledge and experience throughout this project, and we are deeply thankful to everyone who contributed to our journey. 

A special thank you to **Cadence Design Systems** for sharing their expertise and providing exceptional guidance. We extend our heartfelt gratitude to our incredible Challenge Advisors, **Francoise Martinolle** and **Yosinori Watanabe**, for their unwavering support and insightful advice.

We also want to thank **Break Through Tech AI** and the **Cornell Tech AI Program** team for giving us this remarkable opportunity. A huge shoutout to our AI Studio TA, **Kailey Bridgeman**, for her encouragement, assistance, and dedication.

Finally, we’re grateful for the collaboration and camaraderie of our fellow Studio Project Team members. This journey wouldn’t have been the same without:

- **Sarah Goldman**
- **Manvi Kottakota**
- **Lee Mabhena**
- **Hema Motiani**
- **Alison Ramirez**

To everyone who has been part of this experience—thank you for making it unforgettable!

**Project README File**: [Team AI Project README](https://docs.google.com/document/d/1X5YY3s5BmaMiMwrdpNidn6r5Yt225q2N7V7UnbMHvIY/edit?usp=sharing)

