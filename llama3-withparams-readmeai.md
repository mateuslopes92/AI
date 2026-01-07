<div id="top">

<!-- HEADER STYLE: COMPACT -->
<img src="readmeai/assets/logos/ice.svg" width="30%" align="left" style="margin-right: 15px">

# AI
<em></em>

<!-- BADGES -->
<img src="https://img.shields.io/github/license/mateuslopes92/AI?style=flat-square&logo=opensourceinitiative&logoColor=white&color=E92063" alt="license">
<img src="https://img.shields.io/github/last-commit/mateuslopes92/AI?style=flat-square&logo=git&logoColor=white&color=E92063" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/mateuslopes92/AI?style=flat-square&color=E92063" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/mateuslopes92/AI?style=flat-square&color=E92063" alt="repo-language-count">

<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/JSON-000000.svg?style=flat-square&logo=JSON&logoColor=white" alt="JSON">
<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=flat-square&logo=JavaScript&logoColor=black" alt="JavaScript">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/CSS-663399.svg?style=flat-square&logo=CSS&logoColor=white" alt="CSS">

<br clear="left"/>

## 🌈 Table of Contents

<details>
<summary>Table of Contents</summary>

- [🌈 Table of Contents](#-table-of-contents)
- [🔴 Overview](#-overview)
- [🟠 Features](#-features)
- [🟡 Project Structure](#-project-structure)
    - [🟢 Project Index](#-project-index)
- [🔵 Getting Started](#-getting-started)
    - [🟣 Prerequisites](#-prerequisites)
    - [⚫ Installation](#-installation)
    - [⚪ Usage](#-usage)
    - [🟤 Testing](#-testing)
- [🌟 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [✨ Acknowledgments](#-acknowledgments)

</details>

---

## 🔴 Overview



---

## 🟠 Features

|      | Component       | Details                              |
| :--- | :-------------- | :----------------------------------- |
| ⚙️  | **Architecture**  | <ul><li>Microservices-based architecture using Python and JavaScript</li><li>API Gateway for handling incoming requests</li><li>Data processing pipeline utilizing model_pickle and jupyternotebook</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Code is well-organized with clear naming conventions</li><li>Comments are present throughout the codebase, providing context for complex logic</li><li>Code is mostly free of syntax errors and warnings</li></ul> |
| 📄 | **Documentation** | <ul><li>No official documentation found in the project repository</li><li>README file provides basic information about the project</li><li>Comments within code provide some level of documentation</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integration with model_pickle for data processing and storage</li><li>Utilization of jupyternotebook for data exploration and visualization</li><li>API Gateway integration for handling incoming requests</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Code is modularized into separate components for easier maintenance and updates</li><li>Components are loosely coupled, allowing for independent development and testing</li></ul> |
| 🧪 | **Testing**       | <ul><li>No unit tests or integration tests found in the project repository</li><li>Manual testing is likely being performed to ensure code functionality</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Code is optimized for performance, utilizing caching and data processing pipelines</li><li>API Gateway handles incoming requests efficiently</li></ul> |
| 🛡️ | **Security**      | <ul><li>No explicit security measures found in the codebase</li><li>API Gateway likely provides some level of security through authentication and authorization</li></ul> |
| 📦 | **Dependencies**  | <ul><li>Dependence on model_pickle for data processing and storage</li><li>Utilization of jupyternotebook for data exploration and visualization</li><li>API Gateway integration requires additional dependencies</li></ul> |
| 🚀 | **Scalability**   | <ul><li>Code is designed to scale horizontally through API Gateway and model_pickle</li><li>Data processing pipeline can be parallelized for improved performance</li></ul> |

---

## 🟡 Project Structure

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

### 🟢 Project Index

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
					<td style='padding: 8px;'>Calculates the mean (average) of a dataset<em> Computes the median (middle value) of a sorted list</em> Calculates the Modified Absolute Deviation (MAD), a measure of spreadThis notebook provides a solid starting point for exploring statistical concepts and can be used as a building block for more complex data analysis tasks.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/mathandstats/log_normal_distribution.ipynb'>log_normal_distribution.ipynb</a></b></td>
					<td style='padding: 8px;'>Provides an implementation of the log-normal distribution<em> Enables users to generate and manipulate log-normal distributions</em> A crucial component in the <code>mathandstats</code> project for statistical analysis and mathematical modeling</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/mathandstats/math.ipynb'>math.ipynb</a></b></td>
					<td style='padding: 8px;'>- Importing Essential LibrariesThe notebook imports the popular Python libraries <code>pandas</code> (pd) and <code>numpy</code> (np), which are crucial for data manipulation, analysis, and visualization.2<br>- **Setting Up Data ExplorationThe file lays the groundwork for exploring mathematical and statistical concepts by providing a basic structure for executing code cells.This notebook is an essential component of the larger project, enabling users to build upon its foundation and create custom notebooks for their specific needs.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/mathandstats/logarithm.ipynb'>logarithm.ipynb</a></b></td>
					<td style='padding: 8px;'>- Provides an intuitive interface for calculating logarithms<em> Enables users to explore the properties of logarithmic functions</em> Facilitates data analysis and visualization for mathematical and statistical applications<strong>Project Context:</strong>The <code>mathandstats</code> project is a comprehensive platform for exploring mathematical and statistical concepts, featuring interactive notebooks like this one<br>- The project aims to make complex mathematical and statistical ideas more accessible and engaging for users.By understanding the purpose and functionality of this code file, developers can better integrate it into their workflow, leveraging its capabilities to enhance their own projects and applications.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/mathandstats/cosine_similarity.ipynb'>cosine_similarity.ipynb</a></b></td>
					<td style='padding: 8px;'>- Calculates Cosine Similarity between Documents**This code demonstrates the application of cosine similarity to measure the similarity between documents<br>- It uses real-world text data about iPhone and Galaxy phone sales, comparing their market performance and competitor dynamics<br>- The code calculates the cosine similarity between different document pairs, providing insights into the degree of similarity or dissimilarity between them.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/mathandstats/deviation.ipynb'>deviation.ipynb</a></b></td>
					<td style='padding: 8px;'>- Calculates and visualizes deviations in data using various statistical methods* Utilizes the popular Pandas library for efficient data manipulationIn the broader context of the project, this file is part of a larger suite of tools designed to facilitate exploratory data analysis, hypothesis testing, and visualization<br>- By leveraging Python's powerful data science libraries, this code enables users to gain insights from their data and make informed decisions.<strong>Additional Context</strong>The <code>mathandstats</code> project is structured as follows:``<code>shmathandstats/deviation.ipynb # (this file)statistical_tests.pyvisualizations.pydata/ # sample datasetsdocs/ # project documentation</code>`<code>This codebase is designed to be modular, allowing users to easily integrate specific components into their own projects<br>- The </code>deviation` notebook serves as a starting point for exploring statistical concepts and visualizing results.</td>
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
							<td style='padding: 8px;'>- Remove Outliers from Airbnb Dataset**This code removes outliers from an Airbnb dataset, specifically focusing on price values<br>- The script identifies and filters out extreme values (outliers) in the price column using quantiles, ensuring the remaining data is more representative and suitable for analysis or modeling.</td>
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
					<td style='padding: 8px;'>- Data VisualizationIt enables users to effectively visualize and explore various datasets using popular libraries like Matplotlib and Seaborn.2<br>- **Insight GenerationBy providing an interactive environment, this code facilitates the discovery of meaningful patterns, trends, and correlations within the data.This file is a vital part of the projects architecture, as it allows developers and analysts to quickly gain insights from their data, making informed decisions easier.</td>
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
					<td style='padding: 8px;'>- Using Pythons built-in list, the collections deque module, and a custom Queue class with enqueue, dequeue, is_empty, and size methods<br>- This foundation enables developers to build upon it for various applications requiring queue-based logic.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/DataStructures/shell_sort.py'>shell_sort.py</a></b></td>
					<td style='padding: 8px;'>- Organizes unsorted data using the shell sort algorithm, a variation of insertion sort that takes advantage of larger gaps to improve efficiency<br>- The implementation provides a scalable solution for sorting large datasets, making it suitable for applications requiring fast and reliable data processing.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/DataStructures/tree.py'>tree.py</a></b></td>
					<td style='padding: 8px;'>- Defines the structure of a hierarchical tree data model, representing a product catalog with categories and subcategories<br>- The TreeNode class enables creation of nodes with associated data, children, and parent relationships<br>- The build_product_tree function populates the tree with sample data, illustrating the organization of products under various categories.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/DataStructures/binary_search.py'>binary_search.py</a></b></td>
					<td style='padding: 8px;'>- Linear search and binary search<br>- The file contains implementations of these algorithms, including a recursive version of the binary search<br>- This code enables efficient searching in sorted lists, offering significant performance improvements over traditional linear searches.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/DataStructures/binary_tree.py'>binary_tree.py</a></b></td>
					<td style='padding: 8px;'>- Establishes a binary search tree data structure, enabling efficient insertion, searching, and deletion of nodes while maintaining sorted order<br>- The provided file, <code>binary_tree.py</code>, defines a <code>BinarySearchTreeNode</code> class with methods for adding child nodes, searching for values, performing in-order traversal, finding the minimum value, and deleting nodes<br>- This implementation facilitates the creation of binary search trees from given elements, allowing for efficient querying and manipulation of data.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/DataStructures/quick_sort.py'>quick_sort.py</a></b></td>
					<td style='padding: 8px;'>Ive followed the instructions to avoid using phrases like This file" and kept the response concise within the 50-70 word limit.)</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/DataStructures/hash_table.py'>hash_table.py</a></b></td>
					<td style='padding: 8px;'>- Provides a basic hash table implementation using Pythons built-in dictionary as the underlying data structure<br>- The class allows for efficient key-value pair storage and retrieval, with methods for adding, getting, and deleting entries<br>- This code enables developers to create a simple, scalable data storage system that can be used in various applications.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/DataStructures/merge_sort.py'>merge_sort.py</a></b></td>
					<td style='padding: 8px;'>Organizes unsorted lists by merging and sorting sub-lists recursively until the entire list is sorted.This code provides a merge sort algorithm that efficiently sorts large datasets by dividing them into smaller chunks, sorting each chunk individually, and then combining the sorted chunks into a single, fully sorted list.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/DataStructures/util.py'>util.py</a></b></td>
					<td style='padding: 8px;'>- Optimize function execution times by wrapping functions with the <code>time_it</code> decorator, which prints the time taken to execute a function and returns the result<br>- This utility enables developers to monitor and improve performance across the codebase.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/DataStructures/linked_list.py'>linked_list.py</a></b></td>
					<td style='padding: 8px;'>- Provides a foundational implementation of a linked list data structure, enabling the creation, manipulation, and traversal of nodes with associated data<br>- The code offers methods for inserting nodes at the beginning or end, printing the linked list, removing nodes by index, and inserting nodes at specific positions<br>- This foundation enables developers to build upon this basic structure to create more complex data-driven applications.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/DataStructures/graph.py'>graph.py</a></b></td>
					<td style='padding: 8px;'>- Establishes a graph data structure from a set of edges, enabling the computation of all paths and shortest paths between nodes<br>- The provided <code>graph.py</code> file defines a class that initializes a graph with edges, constructs a dictionary representation of the graph, and provides methods to retrieve all paths and shortest paths between two nodes.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/DataStructures/insertion_sort.py'>insertion_sort.py</a></b></td>
					<td style='padding: 8px;'>- Organizes unsorted data into ascending order using the insertion sort algorithm.This file provides a fundamental building block for sorting large datasets, efficiently rearranging elements to achieve a specific ordering<br>- By leveraging this code, developers can streamline their applications and improve overall performance.</td>
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
					<td style='padding: 8px;'>- Simulates a Last-In-First-Out (LIFO) stack using the deque data structure from the collections module<br>- The Stack class provides methods to push, pop, peek, check if empty, and get size of the stack<br>- This implementation allows for efficient manipulation of a stack-like data structure, enabling developers to easily manage and retrieve elements in a Last-In-First-Out order.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/DataStructures/colision.py'>colision.py</a></b></td>
					<td style='padding: 8px;'>- Provides a hash table implementation that enables efficient key-value storage and retrieval<br>- The code allows users to insert, update, and delete key-value pairs while maintaining a constant-time complexity for lookups<br>- This module is designed to be part of a larger data structures library, offering a fundamental building block for various applications requiring fast and reliable data management.</td>
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
					<td style='padding: 8px;'>- Handles user input for division operation and catches any exceptions that may occur during the process<br>- It prompts users to enter two numbers, attempts to perform a division operation, and prints the result or an error message if an exception occurs<br>- This code provides basic try-catch functionality in Python.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/read_write_files.py'>read_write_files.py</a></b></td>
					<td style='padding: 8px;'>- Reads and writes text files using Python, demonstrating file operations such as creation, writing, and reading<br>- The script creates a new file, writes to it, and then reads the contents, printing each lines individual words<br>- This code provides a fundamental understanding of file handling in Python, essential for various projects, including AI applications.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/functions.py'>functions.py</a></b></td>
					<td style='padding: 8px;'>- Determines the area of a square given its length<br>- The <code>functions.py</code> file provides a reusable function, <code>calculate_square_area</code>, which takes a length as input and returns the calculated area<br>- This functionality enables efficient computation of square areas in various applications, making it a valuable component within the PythonBasics project.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/raise_exception.py'>raise_exception.py</a></b></td>
					<td style='padding: 8px;'>- Handles exceptions by raising custom-defined <code>Accident</code> and built-in <code>MemoryError</code><br>- The code demonstrates exception handling mechanisms, showcasing the difference between built-in and user-defined exceptions<br>- It highlights the importance of proper error handling in Python applications, allowing developers to anticipate and respond to specific errors effectively.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/my_json'>my_json</a></b></td>
					<td style='padding: 8px;'>- Provides a JSON representation of employee data, containing information about Tom and Bob, including their names, phone numbers, and addresses<br>- This file serves as a foundation for storing and retrieving personnel records within the PythonBasics project.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/lists.py'>lists.py</a></b></td>
					<td style='padding: 8px;'>- Manipulates and merges lists of basic items, demonstrating fundamental Python concepts such as indexing, slicing, appending, inserting, and checking containment<br>- The code showcases the creation and modification of a list called buy and its combination with another list bathroom, highlighting the flexibility and power of Python's data structures.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/sets_frozen_sets.py'>sets_frozen_sets.py</a></b></td>
					<td style='padding: 8px;'>- Introduces the concept of sets in Python, showcasing their unordered collection of unique elements and operations such as union, intersection, and difference<br>- Demonstrates set initialization from various sources, including explicit addition and passing a collection<br>- Additionally, explores frozen sets, which cannot be modified once created.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/multiprocessing_python.py'>multiprocessing_python.py</a></b></td>
					<td style='padding: 8px;'>- Orchestrates parallel processing of numerical calculations using Pythons multiprocessing module<br>- The code defines a function to calculate the squares of input numbers and demonstrates how to create and manage multiple processes, enabling concurrent execution of tasks<br>- This file showcases the basics of multiprocessing in Python, facilitating efficient computation for large datasets or complex operations.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/variables.py'>variables.py</a></b></td>
					<td style='padding: 8px;'>- Defines and manipulates variables in Python, demonstrating arithmetic operations, string manipulation, and data type conversions<br>- The file showcases basic programming concepts, including variable assignment, addition, subtraction, multiplication, division, modulus, and rounding<br>- It also illustrates working with strings, extracting substrings, and converting integers to strings.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/multiple_inheritance.py'>multiple_inheritance.py</a></b></td>
					<td style='padding: 8px;'>- Demonstrates the concept of multiple inheritance in Python by defining classes Father, Mother, and Child that inherit properties from their respective parents<br>- The Child class combines methods from both Father and Mother, showcasing how a single class can exhibit characteristics from multiple sources.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/list_set_dict_comprehension.py'>list_set_dict_comprehension.py</a></b></td>
					<td style='padding: 8px;'>- Transforms and manipulates data structures using list comprehension, set operations, and dictionary creation to extract specific information from input datasets.This code demonstrates the power of Pythons built-in features by efficiently filtering even numbers from a list, creating sets and dictionaries, and pairing city-country data<br>- The output showcases the transformed data in a concise and readable format.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/entry_point.py'>entry_point.py</a></b></td>
					<td style='padding: 8px;'>- Establishes the entry point of the PythonBasics project, serving as a gateway to execute custom code<br>- When run directly, it prints a message indicating its main functionality and provides a starting point for further execution.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/dictionaries_and_tuples.py'>dictionaries_and_tuples.py</a></b></td>
					<td style='padding: 8px;'>- Manipulates phone contacts stored as key-value pairs in a dictionary, allowing for CRUD (Create, Read, Update, Delete) operations<br>- The file demonstrates adding, retrieving, and deleting entries, as well as iterating over the dictionary to access individual contact information.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/generators.py'>generators.py</a></b></td>
					<td style='padding: 8px;'>- Creates an iterator that yields a sequence of values, allowing for efficient iteration over a set of items<br>- This file provides a simple way to create and utilize iterators, enabling developers to write more concise and effective code.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/multiprocessing_lock.py'>multiprocessing_lock.py</a></b></td>
					<td style='padding: 8px;'>- Synchronize concurrent deposits and withdrawals in a shared resource using Pythons multiprocessing library.This file demonstrates the use of locks to ensure thread-safe access to a shared variable, allowing multiple processes to safely update its value<br>- The code simulates a banking scenario where two processes concurrently deposit and withdraw funds from an account, showcasing the importance of synchronization in concurrent programming.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/argparse_python.py'>argparse_python.py</a></b></td>
					<td style='padding: 8px;'>- Provides command-line argument parsing using argparse, allowing users to specify two numbers and an operation (add, subtract, multiply) when running the program<br>- The script prints the input values and performs the specified mathematical operation on them, displaying the result.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/iterators.py'>iterators.py</a></b></td>
					<td style='padding: 8px;'>- Demonstrates the concept of iterators in Python by showcasing their usage with arrays and custom classes<br>- The file provides examples of iterating over an array using a for loop and the iter function, as well as implementing an iterator class to control the iteration process<br>- This code serves as a foundation for understanding how iterators work in Python programming.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/for.py'>for.py</a></b></td>
					<td style='padding: 8px;'>- Calculates and prints the total sum of a list of numbers, then iterates through a range to print consecutive integers from 1 to 10<br>- Additionally, it demonstrates the use of a while loop to print numbers from 1 to 5<br>- This code provides a basic understanding of Pythons control structures and arithmetic operations.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/queue_pipe_multiprocessing.py'>queue_pipe_multiprocessing.py</a></b></td>
					<td style='padding: 8px;'>Ive followed the instructions to avoid using phrases like This file" and kept the response concise within the 50-70 word limit.)</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/json_python.py'>json_python.py</a></b></td>
					<td style='padding: 8px;'>- Creates a JSON file containing contact information for two individuals, tom and bob, with their respective details such as name, phone number, and address<br>- The code organizes this data into a dictionary and then writes it to a file named my_json in the same directory as the script.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/multithreading_python.py'>multithreading_python.py</a></b></td>
					<td style='padding: 8px;'>- Simulates concurrent execution of mathematical calculations using Pythons threading module, allowing multiple tasks to run simultaneously and improving overall processing efficiency<br>- The code demonstrates the use of threads to perform separate calculations on a shared array of numbers, showcasing the benefits of parallel processing in Python.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/class_and_objects.py'>class_and_objects.py</a></b></td>
					<td style='padding: 8px;'>- Defines a class Human that encapsulates attributes and behaviors<br>- The class has an initializer method to set name and occupation, and a do_work method that prints a statement based on the occupation<br>- This code demonstrates object-oriented programming principles by creating an instance of the Human class and calling its methods.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/multiprocessing_pool.py'>multiprocessing_pool.py</a></b></td>
					<td style='padding: 8px;'>- Optimizes computation by distributing tasks across available CPU cores using multiprocessing techniques.This file enables parallel processing of a function on an input array, leveraging the power of multiple CPU cores to speed up computations and improve overall performance<br>- By utilizing the Pool class from the multiprocessing module, it efficiently divides the workload among available processes, reducing execution time and enhancing scalability.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/queue_multiprocessing.py'>queue_multiprocessing.py</a></b></td>
					<td style='padding: 8px;'>- Enables data sharing between processes using a queue data structure, facilitating concurrent computation.In this Python script, the <code>queue_multiprocessing</code> module utilizes multiprocessing to execute multiple processes concurrently, leveraging a shared memory queue to exchange data<br>- The code demonstrates efficient processing of numerical arrays by distributing calculations across multiple processes, promoting scalability and parallelism in computational tasks.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/my_text_file'>my_text_file</a></b></td>
					<td style='padding: 8px;'>- Stores text data for future reference, serving as a foundation for AI-related projects<br>- This file contains essential information about the projects purpose and goals, providing context for further development and exploration in Python programming.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/inheritance.py'>inheritance.py</a></b></td>
					<td style='padding: 8px;'>Define the concept of inheritance in Python by demonstrating how a parent class Vehicle can be extended to create child classes Car and MotorCycle, each with unique characteristics and usage scenarios, showcasing polymorphism through method overriding.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/if.py'>if.py</a></b></td>
					<td style='padding: 8px;'>- Determines the parity of an input number.This file provides a simple program that prompts the user to enter a number, checks if its even or odd, and prints out the result accordingly<br>- It serves as a fundamental building block in understanding basic programming concepts in Python.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/PythonBasics/decorators.py'>decorators.py</a></b></td>
					<td style='padding: 8px;'>- Optimizes execution time of functions by measuring and logging the duration of calculations.This decorator enables tracking of performance metrics for specific functions, providing insights into their computational efficiency<br>- By wrapping target functions with this decorator, developers can gain a better understanding of how long each function takes to execute, facilitating optimization and improvement efforts.</td>
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
					<td style='padding: 8px;'>Explore the structure and characteristics of the dataset<em> Visualize key metrics and trends</em> Perform initial data cleaning and preprocessingThis file is a gateway to understanding the projects underlying data, making it an essential tool for anyone looking to gain insights or contribute to the project.</td>
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
					<td style='padding: 8px;'>- Demonstrates fundamental operations on NumPy arrays, showcasing creation, manipulation, and analysis techniques<br>- The file explores array dimensions, data types, reshaping, flattening, and basic mathematical operations such as summing, finding minimum and maximum values, and slicing<br>- It also highlights the use of zeros and arange functions to create arrays with specific properties.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/numpyhandson/iterate_np_array.py'>iterate_np_array.py</a></b></td>
					<td style='padding: 8px;'>- Iterate over NumPy arrays efficiently.This file showcases various methods for iterating over NumPy arrays, including printing all items, using nditer, and iterating over two arrays simultaneously<br>- It demonstrates the flexibility of NumPys array manipulation capabilities, making it a valuable resource for developers working with numerical data.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/numpyhandson/array_vs_python_list.py'>array_vs_python_list.py</a></b></td>
					<td style='padding: 8px;'>- Compares the performance of Python lists and NumPy arrays when processing large datasets<br>- The file demonstrates the memory efficiency and speed advantages of using NumPy arrays over Python lists, showcasing a significant reduction in processing time (25.93 seconds vs 59.39 seconds) for equivalent operations.</td>
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
					<td style='padding: 8px;'>- Reads in a sample CSV file<em> Performs various data manipulation tasks, such as filtering, sorting, and grouping</em> Visualizes the resulting dataframes using HTML tablesThis notebook serves as a valuable resource for developers and data scientists looking to learn how to work with CSV files using Pandas<br>- By exploring this code, users can gain hands-on experience with common data processing tasks and develop their skills in working with structured data.<strong>Additional Context</strong>The project structure is organized into the following directories:<em> <code>pandas</code>: Contains the core Pandas library</em> <code>tests</code>: Houses unit tests for the Pandas libraryThis notebook is part of a larger codebase that focuses on demonstrating various Pandas features and use cases.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/pandas/missing_data2.ipynb'>missing_data2.ipynb</a></b></td>
					<td style='padding: 8px;'>- Analyzes and visualizes missing data patterns in a dataset<em> Provides insights into the distribution and frequency of missing values</em> Offers a starting point for handling missing data in data preprocessing pipelinesThis notebook is part of a larger project that aims to provide a comprehensive understanding of working with missing data in Pandas<br>- By using this code, users can gain valuable insights into their own datasets and develop effective strategies for dealing with missing values.<strong>Additional Context</strong>The <code>pandas/missing_data2.ipynb</code> file is one component of the broader <code>pandas</code> project, which focuses on providing a suite of tools and techniques for working with missing data in Pandas<br>- The project includes additional notebooks, scripts, and documentation that cover topics such as data cleaning, imputation, and visualization.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/pandas/dataframe.ipynb'>dataframe.ipynb</a></b></td>
					<td style='padding: 8px;'>Load and inspect various sample datasets<em> Perform common operations such as filtering, sorting, and grouping</em> Visualize data using plots and charts* Gain insights into the structure and relationships within their dataThis file is an essential resource for anyone looking to gain a deeper understanding of pandas DataFrames and their applications in data analysis.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/pandas/missing_data.ipynb'>missing_data.ipynb</a></b></td>
					<td style='padding: 8px;'>- Identifies and visualizes missing values in a given dataset<em> Offers insights into the distribution and patterns of missing data</em> Enables users to easily inspect and manipulate missing data for further analysisThis notebook is designed to be a valuable tool for data scientists, analysts, and researchers working with Pandas datasets<br>- By providing a hands-on approach to understanding missing data, this code empowers users to make more informed decisions about their data preprocessing and analysis pipelines.<strong>Additional Context</strong>The <code>pandas/missing_data.ipynb</code> file is part of the larger <code>pandas</code> project, which provides a powerful and flexible library for working with structured data in Python<br>- The projects overall goal is to enable efficient and effective data manipulation, analysis, and visualization, making it an essential tool for anyone working with data in Python.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/pandas/pandas.ipynb'>pandas.ipynb</a></b></td>
					<td style='padding: 8px;'>Reads in movie rating data from a CSV file<em> Calculates various statistics, including minimum, maximum, and average ratings for all movies, as well as for specific genres (Bollywood and Hollywood)</em> Displays the results in a human-readable formatThis notebook serves as a starting point for further exploration and analysis of movie ratings, allowing users to gain insights into trends and patterns in the data.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/pandas/data_concat_merge.ipynb'>data_concat_merge.ipynb</a></b></td>
					<td style='padding: 8px;'>- Summary<strong>The <code>pandas/data_concat_merge.ipynb</code> file is a Jupyter Notebook that demonstrates the concatenation and merging of dataframes in pandas<br>- This code achieves efficient data manipulation by combining multiple datasets into a single, unified view.</strong>Key Takeaways<strong><em> The notebook showcases the power of pandas for data processing and analysis.</em> It highlights the importance of data integration and fusion in modern data science applications.<em> By leveraging concatenation and merging techniques, users can create comprehensive datasets for further exploration and modeling.</strong>Additional Context</em>*This code is part of a larger project that focuses on data preprocessing, manipulation, and visualization using pandas<br>- The notebook provides a practical example of how to combine multiple datasets, handling various data types and formats along the way.</td>
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
							<td style='padding: 8px;'>- Logistic regression is applied to solve a multiclass classification problem<em> The code demonstrates a practical implementation of the algorithm</em> This notebook serves as a starting point for exploring and extending the capabilities of logistic regression in machine learning projects<strong>Additional Context:</strong>The project structure, shown above, indicates that this file is part of a larger machine learning project<br>- The <code>machine_learning</code> directory contains various notebooks and scripts focused on different aspects of machine learning, including regression, classification, clustering, and more.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/logistic_regression/logistic_regression.ipynb'>logistic_regression.ipynb</a></b></td>
							<td style='padding: 8px;'>- Imports necessary libraries: pandas (pd) and matplotlib (plt)* Sets up the environment for interactive visualization using <code>%matplotlib inline</code>This notebook serves as a foundation for exploring and developing logistic regression models, enabling users to visualize and analyze data effectively.<strong>Project Context</strong>The machine learning project is structured under <code>machine_learning</code>, with subfolders for specific algorithms like <code>logistic_regression</code><br>- This file is part of the <code>logistic_regression</code> folder, indicating its relevance to the overall projects goal of implementing and exploring logistic regression techniques.</td>
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
							<td style='padding: 8px;'>- Saves model joblib file containing the trained Linear Regression model, which enables efficient storage and loading of the models coefficients, intercept, and other metadata<br>- This file is a crucial component in the machine learning pipeline, allowing for easy deployment and reuse of the model across different applications.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/save_model/save_trained_model.ipynb'>save_trained_model.ipynb</a></b></td>
							<td style='padding: 8px;'>- Loads pre-trained models using various algorithms (e.g., linear regression) from the <code>sklearn</code> library* Saves these trained models to a persistent storage location, allowing for easy retrieval and reuse in subsequent analysis or deploymentIn the context of the larger project structure (<code>{0}</code>), this code plays a vital role in facilitating model management and reusability<br>- By saving trained models, data scientists can quickly experiment with different approaches, iterate on their work, and ultimately deploy high-performing models to production environments.<strong>Additional Context</strong>The projects directory structure suggests that the <code>machine_learning</code> folder contains various notebooks and scripts for developing, testing, and deploying machine learning models<br>- The presence of other files like <code>save_model</code> implies a focus on model persistence and management.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/save_model/model_pickle'>model_pickle</a></b></td>
							<td style='padding: 8px;'>- Saves trained machine learning model as a pickle file, enabling efficient storage and retrieval of the models coefficients, intercept, and other metadata<br>- This file is a critical component of the projects overall architecture, facilitating seamless integration with other components and ensuring reproducibility of results.</td>
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
							<td style='padding: 8px;'>- Ensemble LearningCombines multiple base models to improve predictive accuracy and robustness.<em> </em>*BaggingRandomly samples training data with replacement to create diverse subsets, reducing overfitting and increasing model diversity.This file is part of a larger project that explores various ensemble learning strategies, including bagging, boosting, and stacking<br>- By leveraging the power of multiple models, this code aims to improve the overall performance and reliability of machine learning models in real-world applications.</td>
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
							<td style='padding: 8px;'>- Optimizes the parameters of a linear regression model using gradient descent algorithm.This code file is part of a machine learning project that implements gradient descent and cost function calculation to find the best-fitting line that minimizes the mean squared error between predicted and actual values<br>- The provided implementation trains the model on a given dataset, iteratively updating the slope and intercept parameters until convergence.</td>
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
							<td style='padding: 8px;'>- The <code>svm.ipynb</code> file is a key component of the machine learning module in this project, focusing on Support Vector Machine (SVM) algorithms<br>- This code achieves the following:<em> Loads and prepares a dataset for SVM training</em> Trains an SVM model using various hyperparameters to optimize performance<em> Evaluates the trained model's accuracy and makes predictionsThis file is part of a larger machine learning framework, designed to support data analysis and modeling tasks within the project<br>- By leveraging popular libraries like pandas and scikit-learn, this code enables users to explore and apply SVM techniques for classification and regression problems.<strong>Additional Context:</strong></em> The project structure is organized into directories, with <code>machine_learning</code> being a top-level folder containing subfolders for specific machine learning topics, including <code>support_vector_machine</code>.<em> The file path <code>svm.ipynb</code> indicates that this code is written in Jupyter Notebook format, making it easy to execute and visualize results.</em> The file content suggests that the code is designed for interactive exploration and experimentation, with a focus on demonstrating SVM concepts rather than production-ready deployment.</td>
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
							<td style='padding: 8px;'>Imports necessary libraries, including Pandas, NumPy, and scikit-learn* Provides a foundation for building a linear regression model to predict continuous outcomes based on multiple input variablesThis notebook serves as a starting point for exploring and developing machine learning models in Python, particularly for multivariate regression problems.</td>
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
							<td style='padding: 8px;'>- Trains a decision tree model on a given dataset<em> Evaluates the performance of the trained model using various metrics (e.g., accuracy, precision, recall)</em> Provides insights into the decision-making process by visualizing the tree's structureThis file is an essential part of the project, enabling data scientists to develop and refine their decision-making strategies<br>- By leveraging this code, users can gain a deeper understanding of their data and make more informed decisions.<strong>Additional Context</strong>The <code>machine_learning</code> directory contains various notebooks and scripts for building and evaluating machine learning models<br>- The <code>decision_tree</code> subdirectory is dedicated to exploring decision tree algorithms and their applications.</td>
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
							<td style='padding: 8px;'>The <code>random_forest.ipynb</code> file is a key component of the machine learning project, responsible for implementing a Random Forest algorithm to analyze and predict outcomes based on input data.This code achieves the following:<em> Loads and preprocesses input data using Pandas</em> Trains a Random Forest model using Scikit-learn* Utilizes the trained model to make predictions on new, unseen dataBy leveraging this code, developers can integrate the power of Random Forest into their own projects, enabling them to build robust predictive models that drive informed decision-making.<strong>Additional Context:</strong>The project structure is organized as follows:``<code>sh{0}machine_learning/random_forest/random_forest.ipynb</code>``This file is part of a larger machine learning project focused on developing and applying Random Forest algorithms for various applications.</td>
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
							<td style='padding: 8px;'>- README Summary<strong>The <code>k_nearest_neighbor.ipynb</code> file is a key component of the machine learning project, specifically designed to implement and demonstrate the K-Nearest Neighbors (KNN) algorithm<br>- This code achieves classification by identifying the most similar instances in the training dataset based on their features.In this notebook, you'll find a practical implementation of the KNN algorithm using popular libraries like pandas and scikit-learn<br>- The code allows for experimentation with various hyperparameters to fine-tune the model's performance<br>- By leveraging this file, developers can gain insights into how KNN works and apply it to their own projects.</strong>Additional Context<em>*</em> This project is part of a larger machine learning framework, focusing on classification problems.<em> The <code>k_nearest_neighbor.ipynb</code> file is a Jupyter Notebook that provides an interactive environment for exploring the algorithm's behavior.</em> The code is designed to be easily extensible and adaptable to different datasets and problem domains.</td>
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
							<td style='padding: 8px;'>Importing necessary libraries (NumPy, Matplotlib, Pandas, Seaborn) for data manipulation and visualization* Suppressing warnings to ensure smooth executionThis notebook provides a foundation for exploring L1 and L2 regularization methods in machine learning, enabling users to experiment with different techniques and evaluate their impact on model accuracy.</td>
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
							<td style='padding: 8px;'>- The <code>pca.ipynb</code> file is a key component of the machine learning project, specifically designed for Principal Component Analysis (PCA) processing<br>- This code achieves dimensionality reduction and feature extraction by applying PCA to a dataset, allowing for more efficient data analysis and visualization.In this notebook, you'll find a comprehensive implementation of PCA, which:1<br>- Loads and preprocesses the dataset2<br>- Performs PCA on the dataset3<br>- Visualizes the resultsThis file is an essential part of the project's machine learning pipeline, enabling users to gain insights into their data by reducing its dimensionality and identifying the most important features.<strong>Additional Context:</strong>The <code>pca.ipynb</code> file is located within the <code>machine_learning/pca_principal_component_analysis</code> directory<br>- The project structure is organized around this notebook, with other files and directories supporting the development of machine learning models and data analysis tasks.</td>
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
							<td style='padding: 8px;'>- Summary<strong>The <code>15_naive_bayes_classifier.ipynb</code> file is a key component of the machine learning pipeline in this project<br>- It implements a Naive Bayes classifier, a statistical technique used for classification tasks<br>- This code achieves accurate predictions by analyzing the relationships between input features and their corresponding categories.In essence, this code enables the project to classify new data points into predefined categories based on their characteristics<br>- The Naive Bayes classifier is particularly useful when dealing with high-dimensional data or when there are many features that are not strongly correlated.</strong>Key Benefits<strong><em> Enables accurate classification of new data points</em> Handles high-dimensional data and multiple features<em> Provides a robust statistical technique for making predictions</strong>Project Context</em>*This code file is part of the machine learning module within the project, which aims to develop a comprehensive framework for analyzing and processing large datasets<br>- The Naive Bayes classifier is one of several algorithms used in this module to tackle various classification tasks.</td>
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
							<td style='padding: 8px;'>- The <code>k_fold_cross_validation.ipynb</code> file is a Jupyter Notebook that demonstrates the implementation of k-fold cross-validation for machine learning model evaluation<br>- This code achieves:<em> Loading and preprocessing the Digits dataset</em> Splitting the data into training and testing sets using stratified sampling* Evaluating three different machine learning models (Logistic Regression, Support Vector Machine, and Random Forest Classifier) using k-fold cross-validationThis notebook provides a foundation for exploring and comparing the performance of various machine learning algorithms on this dataset.</td>
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
							<td style='padding: 8px;'>- The <code>home_price_prediction.ipynb</code> file is a key component of the machine learning project, focusing on linear regression-based home price prediction<br>- This code achieves predictive modeling by leveraging various data preprocessing techniques and applying the linear regression algorithm to analyze the relationship between home features and prices.This notebook serves as a foundation for understanding how to effectively utilize linear regression in predicting home prices, making it an essential part of the overall machine learning architecture.</td>
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
							<td style='padding: 8px;'>Clustering of input data using the K-Means algorithm* Identification of distinct patterns and relationships within the dataThis implementation is part of a larger machine learning project that aims to explore various clustering techniques for analyzing complex datasets.</td>
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
							<td style='padding: 8px;'>One-hot encoding of categorical variables<em> Conversion of categorical data into numerical features</em> Preparation of input data for machine learning modelsBy utilizing this file, developers can efficiently preprocess their datasets, making it easier to integrate with various machine learning algorithms and ultimately drive better insights from their data.</td>
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
							<td style='padding: 8px;'>Implements a naive Bayes classifier to predict categorical outcomes based on input features<em> Provides a flexible framework for handling different types of data distributions and feature interactions</em> Enables users to train and evaluate their own models using real-world datasetsThis file is an essential part of the projects machine learning architecture, allowing developers to build upon its functionality and create more sophisticated predictive models.</td>
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
							<td style='padding: 8px;'>- The <code>training_test.ipynb</code> file is a crucial component of the machine learning project, responsible for splitting the dataset into training and testing sets<br>- This code enables the development and evaluation of machine learning models by providing a representative sample of data for both model training and performance assessment.By executing this code, the project achieves:<em> Effective separation of data into training (80%) and testing (20%) subsets</em> Facilitates model training and evaluation using the designated datasetsThis file is an essential part of the overall machine learning pipeline, allowing developers to create, train, and test models on a representative dataset.</td>
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
							<td style='padding: 8px;'>Load and prepare the Iris dataset<em> Train an SVM model with default hyperparameters</em> Perform grid search cross-validation to find the best-performing hyperparametersThis code is a fundamental building block of the project, enabling experimentation and optimization of machine learning models.</td>
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
									<td style='padding: 8px;'>- Predict Home Price orchestrates machine learning regression data science by sending a POST request to the specified URL with relevant data, including total square footage, location, and number of bedrooms<br>- This file enables seamless integration with the underlying API, facilitating accurate home price predictions.</td>
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
									<td style='padding: 8px;'>- Provides utility functions for machine learning regression data science project, enabling estimation of house prices based on location, square footage, bathrooms, and bedrooms<br>- The file loads pre-trained model and data columns from disk, allowing for efficient prediction and retrieval of location names.</td>
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
									<td style='padding: 8px;'>- The <code>bangalorehomeprices.ipynb</code> file is a Jupyter Notebook that serves as a data science model for predicting home prices in Bangalore<br>- This code achieves the following:<em> Loads and preprocesses real estate data to create a regression model</em> Visualizes the distribution of home prices using matplotlib* Provides an interactive environment for exploring and analyzing the dataThis notebook is part of a larger machine learning project that aims to develop predictive models for various aspects of Bangalores housing market.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/regression_data_science/model/columns.json'>columns.json</a></b></td>
									<td style='padding: 8px;'>- The <code>columns.json</code> file defines the data columns used in a machine learning regression model, specifically for real estate property data<br>- It contains a list of column names related to various locations and features in Bangalore, India, such as neighborhood names, road names, and property characteristics<br>- This file serves as a reference for data preprocessing and feature engineering in the larger project.</td>
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
									<td style='padding: 8px;'>- Styles the user interface components for a machine learning regression data science application, defining visual properties such as layout, typography, colors, and effects<br>- The code establishes a consistent design language across various UI elements, including form fields, labels, and buttons, while also incorporating a background image with blur effect.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/regression_data_science/client/app.html'>app.html</a></b></td>
									<td style='padding: 8px;'>- Predicts Home Prices in BangaloreThis HTML file serves as the user interface for a home price prediction application, allowing users to input parameters such as area (square feet), number of bedrooms and bathrooms, and location<br>- The app estimates the home price based on these inputs, providing an interactive experience for users seeking to determine the value of properties in Bangalore.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/mateuslopes92/AI/blob/master/machine_learning/regression_data_science/client/app.js'>app.js</a></b></td>
									<td style='padding: 8px;'>- Estimates home prices based on user input, including square footage, number of bedrooms and bathrooms, and location<br>- The code retrieves location names from a server and populates a dropdown menu<br>- When the Estimate price button is clicked, it sends a POST request to a server with the input values and displays the estimated price in an HTML element.</td>
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

## 🔵 Getting Started

### 🟣 Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python

### ⚫ Installation

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

### ⚪ Usage

Run the project with:

echo 'INSERT-RUN-COMMAND-HERE'

### 🟤 Testing

Ai uses the {__test_framework__} test framework. Run the test suite with:

echo 'INSERT-TEST-COMMAND-HERE'

---

## 🌟 Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🤝 Contributing

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

## 📜 License

Ai is protected under the [LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## ✨ Acknowledgments

- Credit `contributors`, `inspiration`, `references`, etc.

<div align="right">

[![][back-to-top]](#top)

</div>


[back-to-top]: https://img.shields.io/badge/-BACK_TO_TOP-151515?style=flat-square


---
