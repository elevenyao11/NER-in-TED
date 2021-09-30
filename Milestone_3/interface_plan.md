## Plan for the Interface
### 1. Overview of this Interface

The components of the interface will include two major parts: 1) a search function where users can search through our named entity-annotated parallel corpus using a keyword and one of the labels of named entities 2) a brief document about the project including information about the corpus, a summary of the basic statistics, and some word cloud images. 

The categories of named entities in the corpus are listed in the following table:

| Label    |Description                               |Examples|
| :----    | :-----                                   | :----- |
| PERSON   | People, including fictional              | Harry Potter, Emma Watson, John |
| ORG      | Companies, agencies, institutions, etc.  | Google, Apple |
|LOC       | Non-GRE locations, mountain ranges, bodies of water |   North America, Mont-blanc |
|PRODUCT   | Objects, vehicles, foods, etc. (Not services.)| MacBook, Tesla model x |
| EVENT    | Named hurricanes, battles, wars, sports events, etc. |  WW2, battle of waterloo  |
| WORK_OF_ART| Title of books, songs, etc.|The diary of Anne Frank, Pride and Prejudice |

### 2. Main functionality

#### 2.1 Text search
- We will create:
	- A text search box which uses a keyword as an input to find paragraphs in our corpus. 
	- By default, the result will display five paragraphs, with English, Korean, and Chinese versions of each paragraph being displayed on the first page, with additional result on the following pages. Results in a specific language can be filtered using the language option. 
	- The paragraphs will be ranked according to the result from Elastic Search. 

#### 2.2 Label search
- Next to the text search box, a dropdown list of labels can be used to highlight specific entities within the displayed paragraphs. 
- If used with a keyword, the five paragraphs will contain highlighted entities according to the selection from the dropdown list. 
- If used individually without a keyword, the selection from the dropdown list will result in five random paragraphs from the corpora displayed on the page, which will contain highlighted entities according to the selection made.


### 3. Additional Functionality
- There will be two buttons to display additional information regarding the project:
	- Introduction to the project
	- Visualizations of the corpus: bar charts for the basic stats, wordcloud, etc.

### 4. Backend.py Components
- The backend.py script will include these components:
	1. Create an interface including a text box for the user to input the specific keyword. The interface also should include a list of possible named entity options (a dropdown list).
	2. Read the corpus file.
	3. Write a function that receives a user's selection (keyword, label, language) and returns:
	   - a. paragraphs based on the user's selection, ranked by Elastic Search.
	   - b. total counts of results corresponding to the user's selection. 
	4. Display the results in a table.
	5. Create a page where the introduction to the project, bar chart for basic stats of the corpus and the Wordcloud visualization will be displayed.