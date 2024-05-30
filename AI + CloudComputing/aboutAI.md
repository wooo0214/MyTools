The general problem of simulating (or creating) intelligence has been broken into sub-problems. These consist of particular traits or capabilities that researchers expect an intelligent system to display. The traits described below have received the most attention and cover the scope of AI research.

## Goals

- Reasoning and problem solving
- Knowledge representation
- Planning and decision making
- Machine Learning
- Natural language processing
- Perception
- Social intelligence
- General intelligence

## Techniques

AI research uses a wide variety of techniques to accomplish the goals above.
- Search and optimization: AI can solve many problems by intelligently searching through many possible solutions.
    - State space search
    - Local search
- Logic
- Probabilistic methods for uncertain reasoning
- Classifiers and statistical learning methods
- Artificial neural networks
- Deep learning
- Generative Pre-trained Transformers (GPT)

## Machine Learning

From perceptron, to convolution, and to neural network, and to convolutional neural network. 

> A perceptron and a support vector machine (SVM) are not the same, although they are both used for classification tasks in machine learning.

- Perceptron: This is a type of linear classifier, which makes its predictions based on a linear predictor function combining a set of weights with the feature vector. It is one of the simplest types of artificial neural networks and is used primarily for binary classification.

- Support Vector Machine (SVM): This is a more advanced classification algorithm that finds the hyperplane that best separates the data into different classes. SVMs can handle both linear and non-linear classification by using kernel functions to transform the data into higher dimensions.

    In summary, while both are used for classification, SVMs are generally more powerful and flexible compared to perceptrons.

### Logistic Regression

Logistic regression is a supervised machine learning algorithm that accomplishes binary classification tasks by predicting the probability of an outcome, event, or observation. 
The model delivers a binary or dichotomous outcome limited to two possible outcomes: yes/no, 0/1, or true/false.

### Loss functions

> human model, the model we want to figure out using ML. x<sub>i</sub> is the human predicts and it equals either 1 or 0.   
ML model. y<sub>i</sub> is the machine model predicts of the probability, which ranges from 0 ~ 1.

- Least square method   
    min of (x<sub>i</sub> - y<sub>i</sub>)<sup>2</sup>

- Max likelihood estimation   
    use log function to convert * to +
- Cross entropy   
    - use entropy (information entropy) to discribe the complexity of a model.
    - the smaller of difference between models entropies, the better for a machine model can be.


### Metrics

Accuracy, precision, recall, f1
ROC, AUC
business metrics