
# COLX Project Group2

Building a named entity annotated parallel corpus across multiple languages based on TED transcripts

## Project Goal

In this project, we are going to build a Multilingual TED corpus with the named entity annotation. The corpus will be a collection of transcripts from TED videos including TEDx talks and TED-Ed across all genres, aiming to collect the transcripts in three different languages (English, Korean, and Chinese (simplified)), with the possibility of extending to French and Spanish. The final corpus will have named entity annotation for each language data. The details of the project can be found here: [project proposal](https://github.ubc.ca/iameleve/COLX_523_Group2/blob/master/Milestone_1/Group2_Project_Proposal.md)

## Annotated English Corpus
- The final version of English corpus after annotations from spaCy and correction with AMT workers can be found [here](https://github.ubc.ca/iameleve/COLX_523_Group2/tree/master/transcripts/en/final).
- The Korean and Chinese parallel corpora corresponding to the English corpus can be found here: [Korean corpus](https://github.ubc.ca/iameleve/COLX_523_Group2/blob/master/transcripts/ko/filtered/filtered_annotated_ted_talks_ko.json) [Chinese corpus](https://github.ubc.ca/iameleve/COLX_523_Group2/blob/master/transcripts/zh-cn/filtered/filtered_annotated_ted_talks_cn.json)

## Folders

```
.
├── Milestone_1
├── Milestone_2
├── Milestone_3
├── annotation
│   └── intermediate_files
├── images
├── src
└── transcripts
    ├── en
    │   ├── annotated
    │   ├── filtered
    │   └── final
    ├── ko
    │   ├── annotated
    │   └── filtered
    └── zh-cn
        ├── annotated
        └── filtered
```

1. Milestone_1
    - All documents related to milestone 1 will be in this folder such as Team Agreement, Project Proposal.
2. Milestone_2
    - All documents related to milestone 2 will be found in this folder: Corpus readme, Annotation materials, Annotation plan.
3. Milestone_3
    - All documents related to milestone 3 will be found in this folder: Annotation process, Interannotator agreement study, and Interface plan.
4. annotation
    - Materials for Amazon Mechanical Turk can be found here.
5. images
    - This folder contains all image files of the repo. 
6. src
    - All python scripts / ipython notebooks will be in this folder.
7. transcripts
    - All outputs from scraping will be stored in this folder, under individual language folders.
    - Each subfolder `annotated` contains the annotated version of the original corpus.
    - The English corpus with the final annotaiton can be found [here](https://github.ubc.ca/iameleve/COLX_523_Group2/tree/master/transcripts/en/final).

## Corpus Collection

**NOTE**: All codes for collecting the corpus are in [TranscriptScrape.ipynb](https://github.ubc.ca/iameleve/COLX_523_Group2/blob/master/src/TranscriptScrape.ipynb). There is no separated file for milestone1 and milestone2. 

To scrape transcripts from the scratch, 

1. Make sure there is no `todo.txt` under `/src/` and no transcripts under `/transcripts/`. As the code for scraping is tested a few times, `todo.txt` and all transcripts are stored in those folders. If you don't erase those files, you will be **continuing from the stage where we stopped**.
2. Follow the instructions below and run all cells in `/src/TranscriptScrap.ipynb` to scrape transcripts. 
3. After finishing scraping, all outputs will be stored in `/transcripts/{language}/` folders, and it will create / append `todo.txt` under `/src/`.


### Instruction for running `/src/TranscriptScrap.ipynb`

1. Import required libraries and packages
2. Define functions
3. Define variables and seeds. 
    - You can change the `languages` variable to collect parallel transcripts in languages of your interest. By default, the code collects parallel transcripts of English, Korean, and Chinese (simplified). 
    - You can increase the value of `NUM_DOCUMENTS` to increase the number of documents that you will collect (by default, it is 10).
    - The current seed has two talks from TED.
4. Run the cells to scrape the transcripts until you have collected a brown-size (or desired-size) corpus. 
5. All transcripts will be in `/transcripts/{language}/` folders.


## Contributors
- Yundong Yao (@Yundong Yao)
- Ladan Jafari Naimi (@Ladan)
- Gurpreet Bedi (@Gurpreet Bedi)
- Jin Cho (@Jin)
