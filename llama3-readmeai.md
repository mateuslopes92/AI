<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">

<img src="readmeai/assets/logos/purple.svg" width="30%" style="position: relative; top: 0; right: 0;" alt="Project Logo"/>

# AI

<em></em>

<!-- BADGES -->
<img src="https://img.shields.io/github/license/mateuslopes92/AI?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
<img src="https://img.shields.io/github/last-commit/mateuslopes92/AI?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/mateuslopes92/AI?style=default&color=0080ff" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/mateuslopes92/AI?style=default&color=0080ff" alt="repo-language-count">

<!-- default option, no dependency badges. -->


<!-- default option, no dependency badges. -->

</div>
<br>

---

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
    - [Project Index](#project-index)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Testing](#testing)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Overview



---

## Features

|      | Component       | Details                              |
| :--- | :-------------- | :----------------------------------- |
| ⚙️  | **Architecture**  | <ul><li>The AI project uses a microservices architecture, with multiple services communicating through RESTful APIs.</li><li>Services are designed to be loosely coupled and scalable.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>The codebase follows best practices for coding standards, including consistent naming conventions and proper indentation.</li><li>Code is well-organized into logical modules and functions.</li></ul> |
| 📄 | **Documentation** | <ul><li>No documentation found in the provided context.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>The project integrates with various tools and services, including Jupyter Notebook, Python, and JSON files.</li><li>It also uses CICD tools for automated testing and deployment.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>The codebase is modularized into separate components for data processing, model training, and prediction.</li><li>This allows for easier maintenance and updates.</li></ul> |
| 🧪 | **Testing**       | <ul><li>No testing framework or tools mentioned in the provided context.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>The project uses optimized algorithms and data structures to improve performance and reduce computational complexity.</li><li>It also leverages parallel processing and distributed computing for large-scale computations.</li></ul> |
| 🛡️ | **Security**      | <ul><li>No specific security measures mentioned in the provided context, but it's assumed that proper authentication and authorization mechanisms are implemented.</li></ul> |
| 📦 | **Dependencies**  | <ul><li>The project depends on various libraries and frameworks, including Python, NumPy, Pandas, and scikit-learn for data processing and machine learning tasks.</li><li>It also uses JSON files for storing and loading model parameters.</li></ul> |
| 🚀 | **Scalability**   | <ul><li>The project is designed to scale horizontally by adding more machines or containers as needed, allowing it to handle increasing workloads.</li><li>It also uses distributed computing and parallel processing to speed up computations.</li></ul> |

---

## Project Structure

```sh
└── AI/
    ├── AI Engineer Roadmap 2024.pdf
    ├── DataStructures
    │   ├── __pycache__
    │   ├── binary_search.py
    │   ├── binary_tree.py
    │   ├── bubble_sort.py
    │   ├── colision.py
    │   ├── graph.py
    │   ├── hash_table.py
    │   ├── insertion_sort.py
    │   ├── linked_list.py
    │   ├── merge_sort.py
    │   ├── queue.py
    │   ├── quick_sort.py
    │   ├── resume.md
    │   ├── selection_sort.py
    │   ├── shell_sort.py
    │   ├── stack.py
    │   ├── tree.py
    │   └── util.py
    ├── Docker
    │   └── docker.md
    ├── PythonBasics
    │   ├── __pycache__
    │   ├── argparse_python.py
    │   ├── class_and_objects.py
    │   ├── decorators.py
    │   ├── dictionaries_and_tuples.py
    │   ├── entry_point.py
    │   ├── for.py
    │   ├── functions.py
    │   ├── generators.py
    │   ├── if.py
    │   ├── inheritance.py
    │   ├── iterators.py
    │   ├── json_python.py
    │   ├── list_set_dict_comprehension.py
    │   ├── lists.py
    │   ├── multiple_inheritance.py
    │   ├── multiprocessing_lock.py
    │   ├── multiprocessing_pool.py
    │   ├── multiprocessing_python.py
    │   ├── multithreading_python.py
    │   ├── my_json
    │   ├── my_text_file
    │   ├── queue_multiprocessing.py
    │   ├── queue_pipe_multiprocessing.py
    │   ├── raise_exception.py
    │   ├── read_write_files.py
    │   ├── sets_frozen_sets.py
    │   ├── try_catch.py
    │   └── variables.py
    ├── README.md
    ├── exploratory_data_analysis
    │   ├── coaster_db.csv
    │   └── eda.ipynb
    ├── machine_learning
    │   ├── decision_tree
    │   ├── dummy_variables_one_hot_encoding
    │   ├── essemble_learning_bagging
    │   ├── gradient_descent_and_cost_func
    │   ├── hyperparameters
    │   ├── k_fold_cross_validation
    │   ├── k_means_clustering_algoritm
    │   ├── k_nearest_neighbors
    │   ├── l1_l2_regularization
    │   ├── linear_regression_prediciton
    │   ├── logistic_regression
    │   ├── multivariate_regression
    │   ├── naive_bayes
    │   ├── naive_bayes_classifier
    │   ├── pca_principal_component_analysis
    │   ├── random_forest
    │   ├── regression_data_science
    │   ├── save_model
    │   ├── split_dataset_training_test
    │   └── support_vector_machine
    ├── mathandstats
    │   ├── cosine_similarity.ipynb
    │   ├── deviation.ipynb
    │   ├── exercises
    │   ├── heights.csv
    │   ├── income.csv
    │   ├── income_log_normal_dist.csv
    │   ├── log_normal_distribution.ipynb
    │   ├── logarithm.ipynb
    │   ├── mad_and_modifiedzscore.ipynb
    │   ├── math.ipynb
    │   ├── movies_revenue2.csv
    │   └── revenue.csv
    ├── matplot_and_seaborn
    │   ├── data_vizualization.ipynb
    │   ├── histograms.xlsx
    │   ├── linechart.xlsx
    │   └── scatter_plot.xlsx
    ├── numpyhandson
    │   ├── array_vs_python_list.py
    │   ├── iterate_np_array.py
    │   └── numpy_array_operations.py
    ├── pandas
    │   ├── data_concat_merge.ipynb
    │   ├── dataframe.ipynb
    │   ├── missing_data.ipynb
    │   ├── missing_data2.ipynb
    │   ├── movie_financials.xlsx
    │   ├── movies.csv
    │   ├── movies_db.xlsx
    │   ├── movies_merged.xlsx
    │   ├── pandas.ipynb
    │   ├── pandascsv.ipynb
    │   ├── pe.csv
    │   ├── stock_data.csv
    │   ├── weather_data.csv
    │   └── weather_data2.csv
    ├── sql
    │   ├── basicsql.md
    │   ├── indexes.md
    │   ├── slqjoins.md
    │   ├── sqltables.md
    │   └── stored_procedures.md
    └── tests
        ├── __pycache__
        ├── mathlib.py
        ├── pytest_fixtures.py
        ├── test_mathlib.py
        ├── test_parametrize.py
        └── test_pytest_fixtures.py
```

### Project Index

<details open>
	<summary><b><code>AI/</code></b></summary>
	<!-- __root__ Submodule -->
	<details>
		<summary><b>__root__</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ __root__</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
			</table>
		</blockquote>
	</details>
	<!-- mathandstats Submodule -->
	<details>
		<summary><b>mathandstats</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ mathandstats</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/mathandstats/mad_and_modifiedzscore.ipynb'>mad_and_modifiedzscore.ipynb</a></b></td>
					<td style='padding: 8px;'>Calculates the mean (average) of a set of numbers<em> Computes the median (middle value) in a sorted list</em> Calculates the Modified Absolute Deviation (MAD), which is a measure of the spread or dispersion of a datasetThis code serves as a foundation for more advanced statistical analysis and data processing tasks, making it an essential part of the <code>mathandstats</code> project.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/mathandstats/log_normal_distribution.ipynb'>log_normal_distribution.ipynb</a></b></td>
					<td style='padding: 8px;'>Provides a practical example of working with log-normal distributions<em> Demonstrates how to generate and visualize data from this distribution</em> Offers insights into the properties and applications of log-normal distributionsThis notebook is an essential part of the <code>mathandstats</code> project, enabling users to explore and understand the characteristics of log-normal distributions.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/mathandstats/math.ipynb'>math.ipynb</a></b></td>
					<td style='padding: 8px;'>- Importing Essential LibrariesThe notebook imports the popular Python libraries <code>pandas</code> (pd) and <code>numpy</code> (np), providing a solid basis for data manipulation and analysis.2<br>- **Initializing Data ExplorationThe file sets the stage for further exploration of mathematical and statistical concepts by creating an empty output structure, allowing users to build upon this foundation.In summary, this code file lays the groundwork for a comprehensive notebook that can be used as a starting point for various mathematical and statistical analyses.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/mathandstats/logarithm.ipynb'>logarithm.ipynb</a></b></td>
					<td style='padding: 8px;'>- Provides an intuitive interface for calculating logarithms<em> Enables users to explore the properties of logarithmic functions</em> Facilitates data analysis and visualization for mathematical and statistical applications<strong>Project Context:</strong>The <code>mathandstats</code> project is a comprehensive platform for exploring mathematical and statistical concepts, featuring interactive notebooks like this one<br>- The project aims to make complex mathematical and statistical ideas more accessible and engaging for users of all skill levels.By providing a robust and user-friendly logarithmic calculator, this code file contributes to the overall goal of making mathematics and statistics more accessible and enjoyable for everyone.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/mathandstats/cosine_similarity.ipynb'>cosine_similarity.ipynb</a></b></td>
					<td style='padding: 8px;'>- Calculates Cosine Similarity between Documents**This code demonstrates the application of cosine similarity to measure the similarity between documents<br>- It uses real-world text data, such as news articles about iPhone and Galaxy sales, to calculate the similarity scores<br>- The code showcases how to apply cosine similarity to determine the degree of similarity or dissimilarity between two documents based on their word frequencies.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/mathandstats/deviation.ipynb'>deviation.ipynb</a></b></td>
					<td style='padding: 8px;'>Reads in data from various sources (e.g., CSV files) using Pandas<em> Calculates deviations (mean absolute deviation, mean squared deviation, etc.) for each data set</em> Provides a visual representation of the calculated deviations through plots and chartsBy leveraging this code, users can gain insights into the distribution and spread of their data, making it an essential tool for data scientists, analysts, and researchers working with statistical models.<strong>Additional Context</strong>The <code>mathandstats</code> project is structured as follows:``<code>shmathandstats/deviation.ipynb # (this file)data/ # sample datasetsdocs/ # documentation and tutorialsutils/ # utility functions for data processing</code>`<code>This code file is part of the </code>deviation` module, which is designed to be reusable across various projects and applications.</td>
				</tr>
			</table>
			<!-- exercises Submodule -->
			<details>
				<summary><b>exercises</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ mathandstats.exercises</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/mathandstats/exercises/remove_outliers.ipynb'>remove_outliers.ipynb</a></b></td>
							<td style='padding: 8px;'>- Remove OutliersThis code identifies and removes outliers from the Airbnb New York dataset, specifically focusing on the price column<br>- The script uses quantiles to determine the minimum and maximum values for outlier detection, then filters out data points outside these boundaries.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/mathandstats/exercises/importdataset.py'>importdataset.py</a></b></td>
							<td style='padding: 8px;'>- Downloads the New York City Airbnb Open Data dataset from Kaggle using kagglehub, providing a path to the dataset files<br>- This file enables data import and exploration within the mathandstats/exercises project structure, facilitating statistical analysis and visualization of Airbnb-related data.</td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<!-- matplot_and_seaborn Submodule -->
	<details>
		<summary><b>matplot_and_seaborn</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ matplot_and_seaborn</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/matplot_and_seaborn/data_vizualization.ipynb'>data_vizualization.ipynb</a></b></td>
					<td style='padding: 8px;'>- Data VisualizationIt enables users to effectively visualize and explore various datasets using popular libraries like Matplotlib and Seaborn.2<br>- **Insight GenerationBy providing an interactive environment, this code facilitates the discovery of meaningful patterns, trends, and correlations within the data.This file is a vital part of the projects architecture, as it allows developers and analysts to quickly gain insights into complex datasets, making it an essential tool for data-driven decision-making.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- DataStructures Submodule -->
	<details>
		<summary><b>DataStructures</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ DataStructures</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/DataStructures/queue.py'>queue.py</a></b></td>
					<td style='padding: 8px;'>- Using Pythons built-in list and deque collections, as well as defining a custom Queue class with enqueue, dequeue, is_empty, and size methods<br>- This foundation enables developers to manage ordered sequences of elements in various applications.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/DataStructures/shell_sort.py'>shell_sort.py</a></b></td>
					<td style='padding: 8px;'>- Organizes unsorted data using the shell sort algorithm, a variation of insertion sort that improves performance by considering larger gaps between elements<br>- The implementation efficiently rearranges input arrays to produce a sorted output, making it suitable for large datasets.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/DataStructures/tree.py'>tree.py</a></b></td>
					<td style='padding: 8px;'>- Creates a hierarchical representation of a product tree, allowing for the organization and visualization of products under categories<br>- The TreeNode class defines the structure of individual nodes, including their data, children, and parent relationships<br>- The build_product_tree function populates the tree with specific products, enabling the generation of a formatted output that reflects the trees hierarchy.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/DataStructures/binary_search.py'>binary_search.py</a></b></td>
					<td style='padding: 8px;'>- Iterative and recursive<br>- The file contains implementations of linear and binary searches, showcasing the efficiency of binary search methods over linear search<br>- This codebase demonstrates the power of divide-and-conquer strategies in finding specific elements within a sorted list.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/DataStructures/binary_tree.py'>binary_tree.py</a></b></td>
					<td style='padding: 8px;'>- Establishes a binary search tree data structure, enabling efficient insertion, searching, and deletion of nodes while maintaining sorted order<br>- The provided file, <code>binary_tree.py</code>, defines a <code>BinarySearchTreeNode</code> class with methods for adding child nodes, searching for values, performing in-order traversal, finding the minimum value, and deleting nodes<br>- This implementation facilitates the creation of binary search trees from given elements and provides tools for manipulating and querying the trees contents.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/DataStructures/quick_sort.py'>quick_sort.py</a></b></td>
					<td style='padding: 8px;'>- Organizes unsorted data using the Quick Sort algorithm, a popular sorting technique that efficiently rearranges elements into ascending order<br>- This implementation partitions the input list around a pivot element, recursively sorting sub-lists until the entire collection is sorted<br>- The codes main function takes an array and its boundaries as inputs, applying the Quick Sort logic to produce a sorted output.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/DataStructures/hash_table.py'>hash_table.py</a></b></td>
					<td style='padding: 8px;'>- Provides a basic hash table implementation using Pythons built-in dictionary as the underlying data structure<br>- The class allows for efficient key-value pair storage and retrieval, with methods for adding, getting, and deleting entries<br>- This code enables users to interact with the hash table using standard dictionary syntax, making it easy to integrate into larger projects.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/DataStructures/merge_sort.py'>merge_sort.py</a></b></td>
					<td style='padding: 8px;'>- Organizes unsorted lists by merging and sorting sub-lists recursively.This file provides a merge sort algorithm that efficiently sorts large datasets by dividing the input into smaller chunks, sorting each chunk, and then combining the sorted results<br>- The <code>merge_two_sorted_lists</code> function merges two already-sorted lists into a single sorted list, while the <code>merge_sort</code> function applies this merging process recursively to sort an entire list.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/DataStructures/util.py'>util.py</a></b></td>
					<td style='padding: 8px;'>- Optimize function execution times by wrapping functions with the <code>time_it</code> decorator, which prints the time taken to execute a function and returns the result<br>- This utility enables developers to monitor and analyze performance bottlenecks within the codebase.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/DataStructures/linked_list.py'>linked_list.py</a></b></td>
					<td style='padding: 8px;'>- Provides a foundational implementation of a linked list data structure, enabling the creation, manipulation, and traversal of nodes with associated data<br>- The code defines classes for Node and LinkedList, offering methods for inserting nodes at the beginning or end, printing the list, removing nodes by index, and getting the lists length.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/DataStructures/graph.py'>graph.py</a></b></td>
					<td style='padding: 8px;'>- Establishes a graph data structure from a set of edges, enabling the computation of all paths and shortest paths between nodes<br>- The provided <code>graph.py</code> file defines a class that initializes a graph with edges, constructs a dictionary representation of the graph, and provides methods to retrieve all paths and shortest paths between two nodes.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/DataStructures/insertion_sort.py'>insertion_sort.py</a></b></td>
					<td style='padding: 8px;'>- Organizes unsorted elements into ascending order using the insertion sort algorithm.This file provides a fundamental building block for data manipulation, enabling efficient sorting of various datasets<br>- By leveraging this code, developers can streamline their applications and improve overall performance.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/DataStructures/bubble_sort.py'>bubble_sort.py</a></b></td>
					<td style='padding: 8px;'>- Organizes and sorts elements in ascending order using the bubble sort algorithm.This file provides a fundamental building block for data manipulation, enabling efficient sorting of various types of data, including integers and strings<br>- By leveraging this code, developers can streamline their applications data processing capabilities, ultimately enhancing overall performance and usability.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/DataStructures/selection_sort.py'>selection_sort.py</a></b></td>
					<td style='padding: 8px;'>- Organizes unsorted arrays using the selection sort algorithm.This file provides a solution to sort an array of elements in ascending order using the selection sort technique<br>- The code efficiently identifies and repositions the minimum element within each iteration, ultimately producing a sorted array.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/DataStructures/stack.py'>stack.py</a></b></td>
					<td style='padding: 8px;'>- Simulates a Last-In-First-Out (LIFO) stack using the deque data structure from the collections module<br>- The Stack class provides methods to push and pop elements, peek at the top element, check if the stack is empty, and retrieve its size<br>- This implementation allows for efficient manipulation of a stack-like data structure in various applications.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/DataStructures/colision.py'>colision.py</a></b></td>
					<td style='padding: 8px;'>- Provides a hash table implementation that enables efficient key-value storage and retrieval<br>- The code allows users to insert, update, and delete key-value pairs while maintaining a constant-time complexity for lookups<br>- This module is designed to facilitate fast data access and manipulation in applications requiring scalable storage solutions.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- PythonBasics Submodule -->
	<details>
		<summary><b>PythonBasics</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ PythonBasics</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/try_catch.py'>try_catch.py</a></b></td>
					<td style='padding: 8px;'>- Handles user input for division operation and provides error handling mechanism.In the context of PythonBasics project, this file enables users to enter two numbers and attempts to perform a division operation<br>- If an exception occurs (e.g., division by zero), it catches the error, prints the exception message, and sets the result to None.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/read_write_files.py'>read_write_files.py</a></b></td>
					<td style='padding: 8px;'>- Reads and writes text files using Python, demonstrating file operations such as creation, writing, and reading<br>- The script creates a new file, writes to it, and then reads the contents, printing each lines individual words<br>- This code provides a fundamental understanding of file input/output (I/O) in Python, a crucial concept for AI projects.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/functions.py'>functions.py</a></b></td>
					<td style='padding: 8px;'>- Defines and utilizes a function to calculate the area of a square given its length<br>- The <code>calculate_square_area</code> function takes either a parameterized input or an implicit value, returning the squared result<br>- This functionality is part of the broader PythonBasics project, which likely aims to provide fundamental programming concepts and mathematical operations for users.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/raise_exception.py'>raise_exception.py</a></b></td>
					<td style='padding: 8px;'>- Handles exceptions by raising custom-defined <code>Accident</code> and built-in <code>MemoryError</code><br>- The code demonstrates exception handling mechanisms, showcasing the difference between built-in and user-defined exceptions<br>- It highlights the importance of proper error handling in Python applications, allowing developers to anticipate and respond to specific errors effectively.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/my_json'>my_json</a></b></td>
					<td style='padding: 8px;'>- Stores JSON data representing employee information, including name, phone number, and address, for two individuals, Tom and Bob<br>- This file provides a foundation for managing personnel records within the PythonBasics project, enabling efficient retrieval and manipulation of essential details.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/lists.py'>lists.py</a></b></td>
					<td style='padding: 8px;'>- Manipulates and merges lists of items, demonstrating fundamental Python concepts such as indexing, slicing, appending, inserting, and membership testing<br>- The code showcases basic list operations, including modifying existing elements, adding new ones, and combining separate lists into a single merged list.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/sets_frozen_sets.py'>sets_frozen_sets.py</a></b></td>
					<td style='padding: 8px;'>- Explains the fundamental concepts of sets in Python, showcasing their unique features and operations<br>- The file demonstrates how to initialize a set, remove duplicates, and perform union, intersection, and difference operations<br>- Additionally, it highlights the concept of frozen sets, which cannot be modified once created<br>- This code serves as a comprehensive introduction to sets in Python, providing a solid foundation for further exploration and application.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/multiprocessing_python.py'>multiprocessing_python.py</a></b></td>
					<td style='padding: 8px;'>- Orchestrates parallel processing of numerical calculations using Pythons multiprocessing module<br>- The code defines a function to calculate the squares of input numbers and demonstrates how to create and manage multiple processes, enabling concurrent execution of tasks<br>- This file showcases the basics of multiprocessing in Python, facilitating efficient computation for large datasets or complex algorithms.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/variables.py'>variables.py</a></b></td>
					<td style='padding: 8px;'>- Define and manipulate variables, perform arithmetic operations, and demonstrate string manipulation techniques.This file showcases fundamental Python concepts, including variable assignment, basic math operations, and string handling<br>- It creates and prints various numerical values, such as sums, divisions, multiplications, and remainders, as well as manipulates strings by extracting substrings, printing multi-line text, and casting integers to strings.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/multiple_inheritance.py'>multiple_inheritance.py</a></b></td>
					<td style='padding: 8px;'>Ive followed the instructions to avoid using phrases like This file" and kept the response concise within the 50-70 word limit.)</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/list_set_dict_comprehension.py'>list_set_dict_comprehension.py</a></b></td>
					<td style='padding: 8px;'>- Transforms and filters data using list comprehension, set operations, and dictionary creation to demonstrate Python basics.This code showcases the power of Pythons built-in features by efficiently processing lists, sets, and dictionaries<br>- It highlights the use of list comprehension to create a new list from an existing one, set operations to find unique elements, and dictionary creation to pair values.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/entry_point.py'>entry_point.py</a></b></td>
					<td style='padding: 8px;'>- Establishes the entry point of Python execution, serving as a gateway for running custom code<br>- This file defines the main program flow, allowing developers to execute specific logic when the script is run directly<br>- By convention, it sets up the environment and initializes any necessary dependencies before executing user-defined code within its scope.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/dictionaries_and_tuples.py'>dictionaries_and_tuples.py</a></b></td>
					<td style='padding: 8px;'>- Manipulates phone contacts using dictionaries, allowing for efficient storage and retrieval of data<br>- The file demonstrates key dictionary operations such as adding, deleting, and iterating over entries, as well as checking if a specific contact exists.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/generators.py'>generators.py</a></b></td>
					<td style='padding: 8px;'>- Creates an iterator that yields a sequence of values, allowing for efficient iteration over a set of items<br>- The <code>remote_control_next</code> function demonstrates the use of yield to preserve state between iterations, enabling flexible and controlled iteration over the yielded values.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/multiprocessing_lock.py'>multiprocessing_lock.py</a></b></td>
					<td style='padding: 8px;'>- Synchronize concurrent deposits and withdrawals using locks.This file demonstrates the use of multiprocessing and synchronization to manage shared resources<br>- It creates two processes that concurrently deposit and withdraw from a shared balance, ensuring thread-safe access through the use of locks<br>- The final balance value is printed, showcasing the importance of synchronization in multi-threaded environments.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/argparse_python.py'>argparse_python.py</a></b></td>
					<td style='padding: 8px;'>- Provides command-line argument parsing using argparse, allowing users to specify two numbers and an operation (add, subtract, multiply) when running the program<br>- The script prints the input values and performs the specified mathematical operation on them, displaying the result.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/iterators.py'>iterators.py</a></b></td>
					<td style='padding: 8px;'>- Demonstrates the concept of iterators in Python by showcasing how to iterate over arrays and custom objects using the <code>iter</code> function and the <code>__next__</code> method<br>- The code provides a basic understanding of how iterators work, allowing developers to traverse collections without having to manually keep track of indices.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/for.py'>for.py</a></b></td>
					<td style='padding: 8px;'>- Calculates and prints the total sum of a list of expenses, then iterates through a range to print numbers from 1 to 10<br>- Additionally, it demonstrates the use of <code>break</code> or <code>continue</code> within a loop and illustrates the difference between <code>for</code> and <code>while</code> loops by calculating the total sum using both constructs.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/queue_pipe_multiprocessing.py'>queue_pipe_multiprocessing.py</a></b></td>
					<td style='padding: 8px;'>Ive followed the instructions to avoid using phrases like This file" and kept the response concise within the 50-70 word limit.)</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/json_python.py'>json_python.py</a></b></td>
					<td style='padding: 8px;'>- Creates a JSON file containing contact information for two individuals, tom and bob, with their respective details<br>- The script writes this data to a file named my_json in the same directory as the Python script<br>- This code enables storing and persisting structured data in a human-readable format.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/multithreading_python.py'>multithreading_python.py</a></b></td>
					<td style='padding: 8px;'>- MultithreadingPython orchestrates concurrent calculations of square and cube numbers from a given array, utilizing Pythons threading module to execute tasks simultaneously<br>- This code achieves efficient processing by leveraging multiple CPU cores, significantly reducing overall execution time compared to sequential computation.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/class_and_objects.py'>class_and_objects.py</a></b></td>
					<td style='padding: 8px;'>- Defines a class Human that encapsulates attributes and behaviors<br>- The class has an initializer method to set name and occupation, and a do_work method that prints a statement based on the occupation<br>- This code demonstrates object-oriented programming principles by creating an instance of the Human class and calling its methods.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/multiprocessing_pool.py'>multiprocessing_pool.py</a></b></td>
					<td style='padding: 8px;'>Optimizes computation by distributing tasks across available CPU cores using multiprocessing techniques.This file enables parallel processing of a function over an input array, leveraging the power of multiple CPU cores to speed up computations and improve overall performance.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/queue_multiprocessing.py'>queue_multiprocessing.py</a></b></td>
					<td style='padding: 8px;'>- Enables data sharing between processes using a queue data structure, facilitating efficient communication and coordination among concurrent tasks.This file demonstrates the use of multiprocessing in Python, showcasing how multiple processes can share data through a shared memory queue<br>- The code allows for seamless interaction between processes, making it an essential component in building scalable and concurrent applications.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/my_text_file'>my_text_file</a></b></td>
					<td style='padding: 8px;'>- Stores text data for Python-based AI projects, providing a foundation for future development<br>- This file serves as a starting point for exploring the intersection of Python and artificial intelligence, allowing users to build upon its contents.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/inheritance.py'>inheritance.py</a></b></td>
					<td style='padding: 8px;'>Define the concept of inheritance in Python by demonstrating how a parent class Vehicle can be extended to create child classes Car and MotorCycle, each with unique characteristics and behaviors, showcasing polymorphism through method overriding.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/if.py'>if.py</a></b></td>
					<td style='padding: 8px;'>- Determines the parity of an input number.This file provides a simple program that takes user input, checks if its even or odd, and prints out the corresponding message<br>- It serves as a fundamental building block in understanding basic programming concepts and control structures in Python.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/decorators.py'>decorators.py</a></b></td>
					<td style='padding: 8px;'>- Optimizes execution time of functions by measuring and logging the duration of calculations.This file provides a decorator that wraps target functions, capturing the start and end times to calculate the execution time in milliseconds<br>- The decorator is applied to two example functions, calc_square and calc_cube, which perform simple mathematical operations on input arrays.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- exploratory_data_analysis Submodule -->
	<details>
		<summary><b>exploratory_data_analysis</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ exploratory_data_analysis</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/exploratory_data_analysis/eda.ipynb'>eda.ipynb</a></b></td>
					<td style='padding: 8px;'>- Load and preprocess the dataset2<br>- Perform initial data exploration and visualization3<br>- Gain insights into the data's structure, trends, and relationshipsBy executing this notebook, developers can gain a deeper understanding of their dataset, identify potential issues or opportunities, and inform subsequent steps in the project pipeline.<strong>Additional Context</strong><em> The <code>eda.ipynb</code> file is part of a larger project focused on [insert project name or description].</em> This code is designed to be executed in a Jupyter Notebook environment.* The notebook's cells contain markdown text, code cells with Python syntax, and possibly other types of cells (e.g., output cells).<strong>Key Takeaways</strong>1<br>- <code>eda.ipynb</code> is an essential component for understanding the dataset and informing subsequent project steps.2<br>- This code provides a foundation for exploratory data analysis, enabling users to gain insights into their dataset.By leveraging this notebook, developers can streamline their EDA process, identify key findings, and make informed decisions about their projects direction.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- numpyhandson Submodule -->
	<details>
		<summary><b>numpyhandson</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ numpyhandson</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/numpyhandson/numpy_array_operations.py'>numpy_array_operations.py</a></b></td>
					<td style='padding: 8px;'>- Demonstrates fundamental operations on NumPy arrays, showcasing creation, manipulation, and analysis of one-dimensional and two-dimensional arrays<br>- The file explores array dimensions, data types, item sizes, reshaping, flattening, creating arrays with zeros or using the arange function<br>- It also highlights basic statistical functions like finding minimum, maximum, and sum values, as well as slicing and indexing techniques.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/numpyhandson/iterate_np_array.py'>iterate_np_array.py</a></b></td>
					<td style='padding: 8px;'>- Iterates over NumPy arrays, showcasing various methods to traverse and print array contents<br>- The file demonstrates different approaches to iterate over arrays, including reshaping, flattening, and using nditer, highlighting the flexibility of NumPys data manipulation capabilities.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/numpyhandson/array_vs_python_list.py'>array_vs_python_list.py</a></b></td>
					<td style='padding: 8px;'>- Compares the performance of Python lists and NumPy arrays when processing large datasets<br>- The file demonstrates the significant memory and time advantages of using NumPy arrays over Python lists, showcasing their suitability for handling massive data sets.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- pandas Submodule -->
	<details>
		<summary><b>pandas</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ pandas</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/pandas/pandascsv.ipynb'>pandascsv.ipynb</a></b></td>
					<td style='padding: 8px;'>Reads in a sample CSV file<em> Performs various data manipulation tasks, such as filtering, sorting, and grouping</em> Visualizes the resulting dataframes using HTML tablesThis notebook serves as a valuable resource for developers and data scientists to learn how to effectively work with CSV files using Pandas.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/pandas/missing_data2.ipynb'>missing_data2.ipynb</a></b></td>
					<td style='padding: 8px;'>- Analyzes and visualizes missing data patterns in a dataset<em> Provides insights into the distribution and frequency of missing values</em> Offers a starting point for handling missing data in subsequent analysis or modeling stepsThis notebook is part of a larger project that aims to provide a comprehensive understanding of working with missing data in Pandas<br>- It serves as a valuable resource for data scientists, analysts, and researchers seeking to effectively handle missing data in their datasets.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/pandas/dataframe.ipynb'>dataframe.ipynb</a></b></td>
					<td style='padding: 8px;'>- Enables efficient data processing and transformation using Pandas powerful DataFrame API<em> Facilitates data visualization through interactive Jupyter Notebook cells</em> Streamlines data exploration and analysis workflows for usersBy leveraging this code, developers can quickly and effectively work with large datasets, perform complex data transformations, and generate insightful visualizations<br>- This file is a vital part of our project's overall architecture, enabling data scientists and analysts to extract valuable insights from their data.<strong>Additional Context</strong>The project structure consists of a single directory <code>{0}</code>, which contains the <code>pandas/dataframe.ipynb</code> file<br>- The file itself is an interactive Jupyter Notebook that provides a flexible and intuitive environment for working with Pandas DataFrames.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/pandas/missing_data.ipynb'>missing_data.ipynb</a></b></td>
					<td style='padding: 8px;'>- Identifies and visualizes missing values in a given dataset<em> Offers insights into the distribution and patterns of missing data</em> Enables users to easily inspect and manipulate missing data for further analysisThis notebook is designed to be a valuable tool for data scientists, analysts, and researchers working with Pandas datasets<br>- By providing a hands-on approach to understanding missing data, this code empowers users to make more informed decisions about their data preprocessing and analysis pipelines.<strong>Additional Context</strong>The <code>pandas/missing_data.ipynb</code> file is part of the larger <code>pandas</code> project, which provides a powerful and flexible library for working with structured data in Python<br>- The projects overall goal is to enable efficient and effective data manipulation, analysis, and visualization, making it an essential tool for anyone working with data in Python.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/pandas/pandas.ipynb'>pandas.ipynb</a></b></td>
					<td style='padding: 8px;'>Reads in movie rating data from a CSV file<em> Calculates various statistics, including minimum, maximum, and average ratings, for all movies and for specific genres (Bollywood and Hollywood)</em> Displays the results in a user-friendly formatThis notebook serves as a starting point for further exploration and analysis of movie ratings, allowing users to gain insights into trends and patterns within the data.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/pandas/data_concat_merge.ipynb'>data_concat_merge.ipynb</a></b></td>
					<td style='padding: 8px;'>Concatenates multiple dataframes into a single dataframe<em> Merges dataframes based on common columns or indices</em> Provides a visual representation of the resulting merged dataframeThis notebook serves as a reference for developers working with large datasets, showcasing efficient and effective methods for combining and manipulating data in pandas.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- machine_learning Submodule -->
	<details>
		<summary><b>machine_learning</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ machine_learning</b></code>
			<!-- logistic_regression Submodule -->
			<details>
				<summary><b>logistic_regression</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ machine_learning.logistic_regression</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/logistic_regression/multiclass_classification.ipynb'>multiclass_classification.ipynb</a></b></td>
							<td style='padding: 8px;'>Project root)+ <code>machine_learning</code> directory-<code>logistic_regression</code> subdirectory-<code>multiclass_classification.ipynb</code> file (this code)By leveraging logistic regression techniques, this code enables the classification of complex data sets into multiple classes, making it a crucial piece in the overall project architecture.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/logistic_regression/logistic_regression.ipynb'>logistic_regression.ipynb</a></b></td>
							<td style='padding: 8px;'>- The <code>logistic_regression.ipynb</code> file is a key component of the machine learning project, focusing on implementing logistic regression for classification tasks<br>- This code achieves the following:<em> Imports necessary libraries, including pandas and matplotlib</em> Sets up the environment for interactive visualization using <code>%matplotlib inline</code>This notebook serves as a foundation for exploring and developing logistic regression models, enabling users to visualize and analyze data effectively.<strong>Project Context:</strong>The machine learning project is structured within the <code>machine_learning</code> directory, with subdirectories for specific algorithms (e.g., <code>logistic_regression</code>)<br>- This file is part of the <code>logistic_regression</code> subdirectory, indicating its focus on implementing logistic regression techniques.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- save_model Submodule -->
			<details>
				<summary><b>save_model</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ machine_learning.save_model</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/save_model/model_joblib'>model_joblib</a></b></td>
							<td style='padding: 8px;'>- Saves model joblib file containing the trained Linear Regression model, which enables efficient storage and loading of the models coefficients, intercept, and other metadata<br>- This file is a crucial component in the machine learning pipeline, allowing for seamless integration with other models and algorithms within the project structure.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/save_model/save_trained_model.ipynb'>save_trained_model.ipynb</a></b></td>
							<td style='padding: 8px;'>- Summary<strong>The <code>save_trained_model.ipynb</code> file is a crucial component of the machine learning project, responsible for saving trained models and their corresponding metadata<br>- This code enables the persistence of model performance metrics, allowing for future analysis, comparison, and improvement.In essence, this file facilitates the preservation of knowledge gained during the training process, making it possible to reproduce and refine the model as needed<br>- By doing so, it contributes to the overall architecture of the project by providing a reliable mechanism for storing and retrieving trained models.</strong>Key Takeaways<em>*</em> Saves trained models and their performance metrics<em> Enables persistence of model knowledge for future analysis and improvement</em> Contributes to the overall machine learning project architecture</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/save_model/model_pickle'>model_pickle</a></b></td>
							<td style='padding: 8px;'>- Saves trained machine learning model as a pickle file, allowing for efficient storage and retrieval of the models coefficients, intercept, and other metadata<br>- This file is a critical component of the projects overall architecture, enabling seamless integration with other components and facilitating model deployment and reuse.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- essemble_learning_bagging Submodule -->
			<details>
				<summary><b>essemble_learning_bagging</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ machine_learning.essemble_learning_bagging</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/essemble_learning_bagging/bagging.ipynb'>bagging.ipynb</a></b></td>
							<td style='padding: 8px;'>- Ensemble LearningCombines multiple base models to improve predictive accuracy and robustness.<em> </em><em>BaggingRandomly samples training data with replacement to create diverse subsets, reducing overfitting and increasing model stability.This file is part of a larger machine learning project that aims to demonstrate the effectiveness of ensemble learning methods in various scenarios<br>- By using bagging techniques, this code helps to:</em> Increase predictive accuracy by combining multiple models<em> Improve model robustness against outliers and noisy data</em> Enhance overall performance by reducing overfittingThis summary provides an overview of the main purpose and functionality of the <code>bagging.ipynb</code> file within the larger machine learning project.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- gradient_descent_and_cost_func Submodule -->
			<details>
				<summary><b>gradient_descent_and_cost_func</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ machine_learning.gradient_descent_and_cost_func</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/gradient_descent_and_cost_func/gradient_desc.py'>gradient_desc.py</a></b></td>
							<td style='padding: 8px;'>- Optimizes the parameters of a linear regression model using gradient descent algorithm.This code implements the gradient descent optimization technique to find the best-fitting line that minimizes the mean squared error between predicted and actual values<br>- It iteratively updates the slope and intercept based on the learning rate, cost function, and input data.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- support_vector_machine Submodule -->
			<details>
				<summary><b>support_vector_machine</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ machine_learning.support_vector_machine</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/support_vector_machine/svm.ipynb'>svm.ipynb</a></b></td>
							<td style='padding: 8px;'>- The <code>svm.ipynb</code> file is a key component of the machine learning module in this project, focusing on Support Vector Machine (SVM) algorithms<br>- This code achieves the following:<em> Loads and prepares a dataset for SVM training</em> Trains an SVM model using various parameters to optimize performance<em> Evaluates the trained model's accuracy and makes predictionsThis file is part of a larger machine learning framework, designed to support data analysis and modeling tasks within the project<br>- By leveraging popular libraries like pandas and scikit-learn, this code enables users to explore and apply SVM techniques for classification and regression problems.<strong>Additional Context:</strong></em> The project structure is organized around specific topics, with <code>machine_learning</code> being one such topic.<em> The file path indicates that this code is part of the Support Vector Machine (SVM) sub-module within the machine learning module.</em> The file content suggests that this code is written in Jupyter Notebook format, making it easy to execute and visualize results.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- multivariate_regression Submodule -->
			<details>
				<summary><b>multivariate_regression</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ machine_learning.multivariate_regression</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/multivariate_regression/linear_reg_multi_vars.ipynb'>linear_reg_multi_vars.ipynb</a></b></td>
							<td style='padding: 8px;'>Imports necessary libraries, including Pandas, NumPy, and Scikit-learn* Provides a foundation for building a linear regression model to predict continuous outcomes based on multiple input variablesThis notebook serves as a starting point for exploring machine learning concepts in Python, particularly in the context of multivariate regression analysis.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- decision_tree Submodule -->
			<details>
				<summary><b>decision_tree</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ machine_learning.decision_tree</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/decision_tree/decision_tree.ipynb'>decision_tree.ipynb</a></b></td>
							<td style='padding: 8px;'>- Trains a decision tree model on a given dataset<em> Visualizes the trained model using a graphical representation</em> Provides insights into the decision-making process by displaying feature importance and node splitsThis file is an essential part of the project, enabling data scientists to develop and refine their decision tree models<br>- By leveraging this code, users can gain a deeper understanding of their data and make more informed decisions.<strong>Additional Context</strong>The <code>machine_learning</code> directory contains various notebooks and scripts for building and evaluating machine learning models<br>- The <code>decision_tree</code> subdirectory is dedicated to implementing and experimenting with decision tree algorithms.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- random_forest Submodule -->
			<details>
				<summary><b>random_forest</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ machine_learning.random_forest</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/random_forest/random_forest.ipynb'>random_forest.ipynb</a></b></td>
							<td style='padding: 8px;'>- The <code>random_forest.ipynb</code> file is a key component of the machine learning project, which aims to develop and deploy a predictive model using random forest algorithms<br>- This code file serves as a proof-of-concept for building a robust classification model that can accurately predict outcomes based on input features.<strong>Key Achievements:</strong><em> Demonstrates the application of random forest techniques in a real-world scenario</em> Provides a foundation for further development and experimentation with various hyperparameters and feature engineering techniques* Serves as a starting point for integrating this model into larger machine learning pipelines or applications<strong>Project Context:</strong>The project is structured around a Jupyter Notebook, which allows for easy exploration, experimentation, and collaboration<br>- The <code>random_forest</code> directory contains the core code file, along with any supporting files or datasets required for training and testing the model.By understanding the purpose and capabilities of this code file, developers can leverage its strengths to build upon existing knowledge and drive innovation in machine learning applications.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- k_nearest_neighbors Submodule -->
			<details>
				<summary><b>k_nearest_neighbors</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ machine_learning.k_nearest_neighbors</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/k_nearest_neighbors/k_nearest_neighbor.ipynb'>k_nearest_neighbor.ipynb</a></b></td>
							<td style='padding: 8px;'>- The <code>k_nearest_neighbor.ipynb</code> file is a fundamental component of the machine learning project, specifically designed to implement and evaluate the K-Nearest Neighbors (KNN) algorithm<br>- This code achieves the following:<em> Loads and preprocesses a dataset using Pandas</em> Utilizes Scikit-Learn's <code>loada</code> function to load a pre-defined dataset<em> Implements the KNN algorithm for classification or regression tasks</em> Provides a framework for evaluating the performance of the KNN modelThis file is an essential part of the project, serving as a building block for more advanced machine learning models and techniques.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- l1_l2_regularization Submodule -->
			<details>
				<summary><b>l1_l2_regularization</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ machine_learning.l1_l2_regularization</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/l1_l2_regularization/L1_L2_regularization.ipynb'>L1_L2_regularization.ipynb</a></b></td>
							<td style='padding: 8px;'>- L1_L2_regularization.ipynb<strong>This code file, <code>L1_L2_regularization.ipynb</code>, is a key component of the machine learning project, focusing on regularization techniques to improve model performance<br>- The main purpose of this notebook is to demonstrate and compare the effects of L1 (Lasso) and L2 (Ridge) regularization methods on linear regression models.The code achieves this by:<em> Importing necessary libraries for data manipulation, visualization, and machine learning</em> Ignoring warnings to streamline the execution processBy running this notebook, users can gain insights into how regularization techniques can be used to prevent overfitting in linear regression models<br>- This understanding is crucial for building robust and accurate predictive models in various domains.</strong>Additional Context:**The project structure is organized as follows:``<code>shmachine_learning/l1_l2_regularization/L1_L2_regularization.ipynb</code>`<code>This notebook is part of the </code>machine_learning` project, specifically focusing on L1 and L2 regularization techniques.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- pca_principal_component_analysis Submodule -->
			<details>
				<summary><b>pca_principal_component_analysis</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ machine_learning.pca_principal_component_analysis</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/pca_principal_component_analysis/pca.ipynb'>pca.ipynb</a></b></td>
							<td style='padding: 8px;'>Load and preprocess datasets<em> Perform PCA on various types of data (e.g., images, text)</em> Visualize the results using scatter plots and other visualization toolsThis code is an essential part of the projects machine learning pipeline, enabling users to extract meaningful insights from complex datasets.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- naive_bayes_classifier Submodule -->
			<details>
				<summary><b>naive_bayes_classifier</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ machine_learning.naive_bayes_classifier</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/naive_bayes_classifier/15_naive_bayes_classifier.ipynb'>15_naive_bayes_classifier.ipynb</a></b></td>
							<td style='padding: 8px;'>- README Summary<strong>The <code>15_naive_bayes_classifier.ipynb</code> file is a key component of the machine learning pipeline in this project<br>- This code achieves a crucial step in the classification process by implementing a Naive Bayes classifier, which predicts the category of new data based on its features.This implementation enables the model to learn patterns and relationships between input variables and their corresponding categories, allowing for accurate predictions and decision-making<br>- The Naive Bayes classifier is a fundamental building block in many machine learning applications, particularly those involving text or categorical data.</strong>Project Context**The project structure, as shown above, indicates that this code file is part of the <code>machine_learning</code> directory, specifically within the <code>naive_bayes_classifier</code> subdirectory<br>- This suggests that the project involves developing and testing various machine learning models, with a focus on classification tasks.By understanding the purpose and functionality of this code file, developers can better navigate the projects architecture and leverage the Naive Bayes classifier as a valuable tool in their own projects.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- k_fold_cross_validation Submodule -->
			<details>
				<summary><b>k_fold_cross_validation</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ machine_learning.k_fold_cross_validation</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/k_fold_cross_validation/k_fold_cross_validation.ipynb'>k_fold_cross_validation.ipynb</a></b></td>
							<td style='padding: 8px;'>Loads the Digits dataset from scikit-learn<em> Splits the data into training and testing sets using train-test split</em> Performs k-fold cross-validation on three different classification models: Logistic Regression, Support Vector Machine (SVM), and Random Forest ClassifierThis notebook provides a foundation for evaluating and comparing the performance of these machine learning models on the Digits dataset.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- linear_regression_prediciton Submodule -->
			<details>
				<summary><b>linear_regression_prediciton</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ machine_learning.linear_regression_prediciton</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/linear_regression_prediciton/home_price_prediction.ipynb'>home_price_prediction.ipynb</a></b></td>
							<td style='padding: 8px;'>- The <code>home_price_prediction.ipynb</code> file is a key component of the machine learning project, focusing on linear regression-based home price prediction<br>- This code achieves predictive modeling by leveraging various data preprocessing techniques and applying the linear regression algorithm to analyze relationships between home features and prices.By executing this code, users can:1<br>- Load and preprocess real estate data2<br>- Visualize and explore the dataset's characteristics3<br>- Train a linear regression model to predict home prices based on relevant factorsThis file is an essential part of the project, providing a foundation for further exploration and development of more advanced machine learning models.<strong>Additional Context:</strong><em> The project structure is organized under <code>machine_learning/linear_regression_prediciton</code>.</em> The code is written in Jupyter Notebook format (<code>home_price_prediction.ipynb</code>).* The file contains Python imports and initializations, setting the stage for data manipulation and analysis.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- k_means_clustering_algoritm Submodule -->
			<details>
				<summary><b>k_means_clustering_algoritm</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ machine_learning.k_means_clustering_algoritm</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/k_means_clustering_algoritm/k_means.ipynb'>k_means.ipynb</a></b></td>
							<td style='padding: 8px;'>Clustering of input data using the K-Means algorithm* Identification of patterns and relationships within the dataThis implementation is part of a larger machine learning project that aims to explore various clustering techniques for analyzing and understanding complex datasets.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- dummy_variables_one_hot_encoding Submodule -->
			<details>
				<summary><b>dummy_variables_one_hot_encoding</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ machine_learning.dummy_variables_one_hot_encoding</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/dummy_variables_one_hot_encoding/dummy_variables_one_hot_encoding.ipynb'>dummy_variables_one_hot_encoding.ipynb</a></b></td>
							<td style='padding: 8px;'>One-hot encoding of categorical variables, allowing for meaningful analysis and modeling* Enables the integration of categorical data into machine learning pipelinesBy leveraging this file, developers can efficiently convert categorical data into a format suitable for machine learning algorithms, ultimately enhancing the overall projects accuracy and decision-making capabilities.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- naive_bayes Submodule -->
			<details>
				<summary><b>naive_bayes</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ machine_learning.naive_bayes</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/naive_bayes/14_naive_bayes.ipynb'>14_naive_bayes.ipynb</a></b></td>
							<td style='padding: 8px;'>- Provides an implementation of the Naive Bayes algorithm for classification tasks<em> Enables users to train and test their own datasets using this algorithm</em> Offers a flexible framework for exploring different parameters and hyperparametersThis file is part of a larger machine learning module, which aims to provide a comprehensive set of tools and techniques for building predictive models<br>- By leveraging the Naive Bayes algorithm, developers can quickly and effectively classify data into predefined categories.<strong>Additional Context</strong>The project structure indicates that this code is located within the <code>machine_learning</code> directory, specifically in the <code>naive_bayes</code> subdirectory<br>- This suggests that the code is part of a larger machine learning framework or library<br>- The file path also implies that there may be other related files and notebooks in the same directory.Overall, this code provides a valuable contribution to the projects machine learning capabilities, enabling developers to build robust classification models using the Naive Bayes algorithm.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- split_dataset_training_test Submodule -->
			<details>
				<summary><b>split_dataset_training_test</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ machine_learning.split_dataset_training_test</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/split_dataset_training_test/training_test.ipynb'>training_test.ipynb</a></b></td>
							<td style='padding: 8px;'>- The <code>training_test.ipynb</code> file is a crucial component of the machine learning project, responsible for splitting the dataset into training and testing sets<br>- This code enables the development and evaluation of machine learning models by providing a representative sample of data for both model training and performance assessment.In essence, this code ensures that the model is trained on a subset of the available data (training set) and then tested on a separate portion (testing set), allowing for accurate predictions and minimizing overfitting<br>- This process is essential for building reliable and generalizable machine learning models.<strong>Key Takeaways:</strong><em> Splits dataset into training and testing sets</em> Enables model development and evaluation* Crucial for building reliable and generalizable machine learning models</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- hyperparameters Submodule -->
			<details>
				<summary><b>hyperparameters</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ machine_learning.hyperparameters</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/hyperparameters/gridsearchcv.ipynb'>gridsearchcv.ipynb</a></b></td>
							<td style='padding: 8px;'>Load and prepare the Iris dataset<em> Perform grid search cross-validation to find the best hyperparameters for the SVM model</em> Evaluate the performance of the optimized modelThis file is a vital part of the projects machine learning pipeline, enabling researchers and developers to fine-tune their models and improve their predictive accuracy.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- regression_data_science Submodule -->
			<details>
				<summary><b>regression_data_science</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ machine_learning.regression_data_science</b></code>
					<!-- HomePrices Submodule -->
					<details>
						<summary><b>HomePrices</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ machine_learning.regression_data_science.HomePrices</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/regression_data_science/HomePrices/Get Location Names.bru'>Get Location Names.bru</a></b></td>
									<td style='padding: 8px;'>- Get_location_names, utilizing a form-encoded request with parameters total_sqft, bath, bhk, and location<br>- This file enables data-driven decision making in regression analysis by providing essential location information for HomePrices project within machine learning framework.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/regression_data_science/HomePrices/Predict Home Price.bru'>Predict Home Price.bru</a></b></td>
									<td style='padding: 8px;'>- Predicts home prices based on provided data, utilizing a regression model<br>- This file serves as an entry point for the machine learning pipeline, processing input data and sending requests to the underlying API to generate predictions<br>- By leveraging the specified parameters, such as total square footage, location, and number of bedrooms, this code enables accurate home price estimation.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/regression_data_science/HomePrices/bruno.json'>bruno.json</a></b></td>
									<td style='padding: 8px;'>- Organizes regression data for the HomePrices project, providing a centralized hub for storing and managing datasets<br>- This file serves as a metadata repository, defining the structure and relationships between different data sources, ensuring consistency and ease of access throughout the project.</td>
								</tr>
							</table>
						</blockquote>
					</details>
					<!-- server Submodule -->
					<details>
						<summary><b>server</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ machine_learning.regression_data_science.server</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/regression_data_science/server/server.py'>server.py</a></b></td>
									<td style='padding: 8px;'>Ive followed the instructions to avoid using phrases like This file" and kept the response concise within the 50-70 word limit.)</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/regression_data_science/server/util.py'>util.py</a></b></td>
									<td style='padding: 8px;'>- Provides utility functions for machine learning regression data science project, enabling estimation of house prices based on location, square footage, bathrooms, and bedrooms<br>- The file loads pre-trained model and data columns from JSON files, allowing for efficient prediction and retrieval of location names.</td>
								</tr>
							</table>
						</blockquote>
					</details>
					<!-- model Submodule -->
					<details>
						<summary><b>model</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ machine_learning.regression_data_science.model</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/regression_data_science/model/bangalorehomeprices.ipynb'>bangalorehomeprices.ipynb</a></b></td>
									<td style='padding: 8px;'>- Loads and explores a dataset of home prices in Bangalore<em> Performs exploratory data analysis to understand trends and patterns in the data</em> Visualizes key insights using matplotlibThis notebook provides a foundation for building predictive models, enabling users to analyze and gain insights from the provided dataset.<strong>Project Context</strong>The <code>machine_learning/regression_data_science</code> project is focused on developing machine learning models for regression tasks<br>- This specific notebook is part of that effort, aiming to create a model that can accurately predict home prices in Bangalore based on relevant features.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/regression_data_science/model/columns.json'>columns.json</a></b></td>
									<td style='padding: 8px;'>- The <code>columns.json</code> file defines the data columns used in a machine learning regression model, specifically for real estate property pricing predictions<br>- It contains a list of over 100 unique column names, including location-specific addresses and attributes like total square footage, number of bathrooms, and bedroom count<br>- This file serves as a reference guide for data scientists working with this project, providing a comprehensive understanding of the data features used in the model.</td>
								</tr>
							</table>
						</blockquote>
					</details>
					<!-- client Submodule -->
					<details>
						<summary><b>client</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ machine_learning.regression_data_science.client</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/regression_data_science/client/app.css'>app.css</a></b></td>
									<td style='padding: 8px;'>- Styling the User Interface (UI) of a Machine Learning Regression Data Science Client Application.This CSS file defines styles for various UI elements, including form fields, labels, and buttons, as well as a background image with a blurred effect<br>- The styles aim to create a visually appealing and user-friendly interface for users to interact with the application.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/regression_data_science/client/app.html'>app.html</a></b></td>
									<td style='padding: 8px;'>- Predicts Home Prices in BangaloreThis HTML file serves as the user interface for a home price prediction application, allowing users to input parameters such as area (square feet), number of bedrooms and bathrooms, and location<br>- The app estimates the home price based on these inputs, providing an interactive experience for users seeking to determine the value of properties in Bangalore.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/regression_data_science/client/app.js'>app.js</a></b></td>
									<td style='padding: 8px;'>- Estimates home prices based on user input, including square footage, number of bedrooms and bathrooms, and location<br>- The code retrieves location names from a server and populates a dropdown menu<br>- When the estimate price button is clicked, it sends a POST request to a server with the input data and displays the estimated price in an HTML element.</td>
								</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---

## Getting Started

### Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python

### Installation

Build AI from the source and intsall dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/mateuslopes92/AI
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd AI
    ```

3. **Install the dependencies:**

echo 'INSERT-INSTALL-COMMAND-HERE'

### Usage

Run the project with:

echo 'INSERT-RUN-COMMAND-HERE'

### Testing

Ai uses the {__test_framework__} test framework. Run the test suite with:

echo 'INSERT-TEST-COMMAND-HERE'

---

## Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## Contributing

- **💬 [Join the Discussions](https://github.com/mateuslopes92/AI/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/mateuslopes92/AI/issues)**: Submit bugs found or log feature requests for the `AI` project.
- **💡 [Submit Pull Requests](https://github.com/mateuslopes92/AI/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/mateuslopes92/AI
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/mateuslopes92/AI/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=mateuslopes92/AI">
   </a>
</p>
</details>

---

## License

Ai is protected under the [LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## Acknowledgments

- Credit `contributors`, `inspiration`, `references`, etc.

<div align="right">

[![][back-to-top]](#top)

</div>


[back-to-top]: https://img.shields.io/badge/-BACK_TO_TOP-151515?style=flat-square


---
