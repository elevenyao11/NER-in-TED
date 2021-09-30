
## Corpus Explanation

### 1 General explanation about the corpus
    
We are going to build a Multilingual TED corpus with the named entity annotation. The corpus will be a collection of transcripts from TED video transcripts including all talks across all genres. We will preprocess the transcripts and extract named entities and get human annotation for the English data. An automatic projection method will be applied across multiple language data to build the parallel corpus. With this purpose, we have collected a number of transcripts in three different languages in this milestone including English, Korean, and Chinese.
       
### 2 The source

The main source of the corpus is transcripts from TED: [LINK](https://www.ted.com/talks)

We chose TED talks as the source of data as it is rich in transcripts that are available in different languages. Although we focus on English, Korean, and Chinese, there is an opportunity to construct a multilingual corpus of more than twenty languages. 
     
### 3 Links to scraped corpora

The three scraped parallel corpora can be found in these links:
- [English Corpus](https://github.ubc.ca/iameleve/COLX_523_Group2/blob/master/transcripts/en/ted_talks_en.json)
- [Korean Corpus](https://github.ubc.ca/iameleve/COLX_523_Group2/blob/master/transcripts/ko/ted_talks_ko.json)
- [Chinese Corpus](https://github.ubc.ca/iameleve/COLX_523_Group2/blob/master/transcripts/zh-cn/ted_talks_zh-cn.json)


### 4 Corpus format

The format of the data we have collected is in Json files. It is a list of dictionaries; each dictionary contains one example of the data collected for one talk. You may find one example of a transcript as follow:

```
[
    {
        "title":"anita_collins_how_playing_an_instrument_benefits_your_brain",
        "talker":"Anita Collins",
        "text_length":4515,
        "views":"10,175,572",
        "language":"en",
        "text":" text
        "url":"https://www.ted.com/talks/anita_collins_how_playing_an_instrument_benefits_your_brain/transcript?language=en"
    },
    { ...
```
The data collected for each transcript is a dictionary consisting of the keys and explanations as follows:

- title: The title of the talk in words separated with under scores.
- talker: The name of the presenter; first name and last name capitalized and space separated. It helps to find information about the presenters.
- text_length: The number of the words in the talk. It shows how elaborate the talk is on the specific topic.
- views: The number of views the talk receives across its online present. It shows the popularity of the talk among viewers.
- language: The language of the talk. It will help to separate talks from different languages.
- text: The specific talk transcript.
- url: The link to the talk. It will help to find the talk online.


### 5 Corpus Details

Each document in the corpus is one transcript of one talk from TED in either English, Chinese, or Korean. The transcript is collected only when it was available in all three languages. 

#### 5.1 Total number of documents, tokens, characters
	
| Language    | No. of Documents | No. of tokens | No. of Character | No. of Paragraphs |
|-------------|-------------------|---------------|------------------|-------------------|
| **English** | 780               | 1,581,957     | 8,747,004        | 21,927            |
| **Korean**  | 771               | 1,076,770     | 4,542,943        | 19,637            |
| **Chinese** | 524               | -             | 2,084,021        | 12,760            |


#### 5.2 A summarized analysis on the English transcripts
- Analysis on the TED Talk corpus showed that:
	- Average number of words per talk is: 2027.29
	- Average number of words per paragraph is: 72.12
	- Average number of paragraphs per talks is: 28.11

#### 5.3 A more detailed analysis
- For the detailed corpus analysis, please refer to this link: [Corpus Analysis](https://github.ubc.ca/iameleve/COLX_523_Group2/blob/master/Milestone_2/corpus_analysis.md)

### 6 Automatic Annotation

After scraping data from TED, we applied spaCy to each document in order to extract named entities in the English corpus. 

#### 6.1 Code for creating annotated corpus

The whole process for creating annotated corpus can be found [here](https://github.ubc.ca/iameleve/COLX_523_Group2/blob/master/src/process_corpus.ipynb). To summarize, we first removed irrelevant characters such as `"\n"` or empty space. Then we split those texts into paragraphs (which was distinguished by `"[PARAGRAPH]"`). After applying spaCy, we collected all information related to entities for each paragraph: the start index of the entity, the end index of the entity, the label of the entity, as well as the text of the paragraph. 

Since we are going to correct errors only in the English corpus, we left the entities in the Korean corpus and the Chinese corpus empty, splitting texts into paragraphs. 

#### 6.2 Links to annotated corpus

The annotated English corpus and the structured corpora of Korean and Chinese from the process 6.1 can be found here:
- [English annotated corpus](https://github.ubc.ca/iameleve/COLX_523_Group2/blob/master/transcripts/en/annotated/annotated_ted_talks_en.json)
- [Korean structured corpus](https://github.ubc.ca/iameleve/COLX_523_Group2/blob/master/transcripts/ko/annotated/annotated_ted_talks_ko.json)
- [Chinese structured corpus](https://github.ubc.ca/iameleve/COLX_523_Group2/blob/master/transcripts/zh-cn/annotated/annotated_ted_talks_cn.json)

#### 6.3 Final structure of the corpus

The final structure of the corpus after applying automatic named entity extraction is as below.

```
[
 {
        "title": "TITLE_CONTENT"
        "talker":"TALKER",
        "text_length":TEXT_LENGTH,
        "views": VIEWS,
        "language": "LANGUAGE",
        "text":[
            {
                "text":"PARAGRAPH1",
                "ents":[
		                {	
			                "start": START_INDEX
			                "end": END_INDEX
			                "text": "ENTITY"
			                "label": "LABEL"
		                },
		                ...
		                ]
            },
            ...
 },
 ...
 ]
```

### 7 Problems with the corpus

#### 7.1 Different number of transcripts on different languages

There are mismatches between the number of transcripts in different languages. This is because when we collect the corpus, there were some issues such as connection failures. Therefore, certain transcripts of a language have been missed. However, we still get 519 aligned transcripts in all English, Korean and Chinese after preprocessing.

#### 7.2 Paragraph content misalignment of the three languages

The collected transcripts of the three languages of English, Chinese, and Korean showed that paragraph boundaries for each language were not aligned based on the content they were conveying. For example, the content conveyed in one and a half paragraph of a transcript in English text was aligned with the content conveyed in one paragraph of the same talk in the Korean transcript, or vice versa. One of the aims of this project is to create a parallel corpus of the three languages. As paragraphs were considered as a basic unit for creating the parallel corpus, the misalignment between paragraphs might be a problem. Therefore, we will filter the transcripts where the number of paragraphs is identical for each language. 

#### 7.3 Preprocessing steps for Chinese and Korean transcripts

For the purpose of analysis, we might need to do more steps of preprocessing to prepare the corpus of Chinese and Korean such as:

- For Chinese corpus, word segmentation is needed to preprocess the transcripts.
- For Korean corpus morphological analysis needs to be done in order to distinguish between morphemes (especially for empty/grammatical morphemes and full morphemes) that are often combined in each word chunk.

