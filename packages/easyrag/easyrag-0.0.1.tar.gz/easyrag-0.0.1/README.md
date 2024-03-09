# easyrag: Retrieval-Augmented Generation Uncovered

"easyrag: Retrieval-Augmented Generation Uncovered" is a multi-chapter project focused on exploring Retrieval-Augmented Generation (RAG) from simple implementations to advanced techniques. Utilizing open Large Language Models (LLMs) hosted on Hugging Face, this project aims to provide a comprehensive guide through the RAG landscape, demonstrating the power of combining retrieval mechanisms with generative models. Each part includes evaluation metrics allowing is to compare the performance of different techniques and models.

* [Part 1: Simple RAG](./chapters/part1_simple_rag.ipynb)

Retrieval-Augmented Generation (RAG) combines the retrieval of informational content with generative deep learning models. This approach enhances the model's ability to produce relevant and contextually rich responses by leveraging external knowledge sources. Building RAG applications always follows some kind of "flow" or "pipeline". Therefore i started to represent RAG applications through Graphs, which allows us to create understandable visuals for our RAG applications, which can include the cycles or conditional statements that are present in the application. We are going to use [Langgraph](https://python.langchain.com/docs/langgraph#when-to-use) to represent the RAG applications as graphs.

## What is easyrag?

easyrag is also a library that provides helpful methods and classes to work with RAG applications. It is designed to be a lightweight and easy-to-use library that can be used to build and evaluate RAG applications. It is easy to hack and extend. It doesn't provide complex abstractions or extensive features.

### Evaluation Metrics

easyrag implements a set of evaluation metrics to compare the performance of different RAG models. Those metrics are inspired and adopted from [ragas](https://docs.ragas.io/en/latest/index.html), [llamaindex](https://docs.llamaindex.ai/en/latest/index.html) and are adapted to work with Open LLMs, by adjusting the prompts and extending the examples. 

Supported metrics include:
* **Answer Correctness**: Evaluates the `answer` with the `ground truth` and returns 0 INCORRECT or 1 CORRECT.
* **Answer Faithfulness**: Evaluates if `answer` is "faithfull" based on the provided `context` and returns a 0 UNFAITHFUL or 1 FAITHFUL, e.g. I cannot answer since no information is given in the context.
* **Context Precision**: Evaluates how many of the retrieved documents are relevant to answer the question, uses `question`, `context` and `ground truth` answer.
* **Context Recall**: Evaluates how many sentences in the `answer` can be attributed to retrieved documents, uses `context` and `answer`. 

### Why those 4 metrics? 

Those 4 metrics allow us to evaluate the performance of the whole RAG application. We can evaluate the performance of the retriever/ranking by using the `Context Precision` and `Context Recall` metrics. We can evaluate the performance of the generator by using the `Answer Correctness` and `Answer Faithfulness` metrics. 


### Datasets

To build and evaluate RAG applications, we need to have access to datasets. easyrag provides a set of datasets that can be used to build and evaluate RAG applications. The datasets are stored on Hugging Face and can be easily accessed using the `datasets` library. 

Supported datasets include:
* [philschmid/easyrag-mini-wikipedia](https://huggingface.co/datasets/philschmid/easyrag-mini-wikipedia): Wikipedia based dataset with ~900 questions and ground truth answers + 3,200 documents for retrieval.


## Installation and Setup

- Python 3.10 or later
- Access to Hugging Face Inference API


Clone the repository and install the required dependencies:
```bash
pip install git+https://github.com/philschmid/easyrag.git
```

Open the chapter you want to run. 

## Contributing
We welcome contributions to "easyrag"! If you have suggestions for improvements, please open an issue or submit a pull request.

* Fork the repository
* Create a new branch for your feature (git checkout -b feature/amazing-feature)
* Commit your changes (git commit -am 'Add some amazing feature')
* Push to the branch (git push origin feature/amazing-feature)
* Open a pull request

## License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## Acknowledgments

A special thank you to Hugging Face and Langchain for providing the platforms and tools that made this project possible. Also, big acknowledgment to [ragas](https://docs.ragas.io/en/latest/index.html) and [llamaindex](https://docs.llamaindex.ai/en/latest/index.html) for providing the evaluation metrics and inspiration for this project.


## Todos: 

* [ ] semantic chunking
* [ ] replace all " with \" to fix json parsing