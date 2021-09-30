# Annotation process
## Milestone 3
- This is the document regarding how the annotation is processed. 

### 1. Automatic annotation with spaCy
In the last milestone, we extracted named entities with spaCy. As we had a lot of named entities in our corpus, we set our strategy to extract those automatically first, and then correct some labels with human annotators. 
- [Annotated corpus after applying spaCy](https://github.ubc.ca/iameleve/COLX_523_Group2/blob/master/transcripts/en/annotated/annotated_ted_talks_en.json)
- [Code for combining annotated corpus with the originally extracted corpus](https://github.ubc.ca/iameleve/COLX_523_Group2/blob/master/src/process_corpus.ipynb)

### 2. Filter, align corpora paragraph-wise
Before we create a CSV file for publishing to AMT, we filtered the English, Korean, and Chinese corpora to align paragraph-wise. We set the number of paragraphs for each talk as a criteria for the alignment of each corpus.  After the filtration, we had 330 documents (talks), 7,660 paragraphs, and 689,614 tokens / 478,551 tokens / 1,264,013 characters in the English, Korean, and Chinese corpora, respectively. 

- [Filtered English corpus](https://github.ubc.ca/iameleve/COLX_523_Group2/blob/master/transcripts/en/filtered/filtered_annotated_ted_talks_en.json)
- [Code for filtering corpora and basic statistics](https://github.ubc.ca/iameleve/COLX_523_Group2/blob/master/src/filter_corpus.ipynb)


### 3. Prepare CSV file
When we created the CSV file, we decided to extract only the unique combinations of entity-label. We extracted not only entities and labels, but also the contexts associated with each entity as well as the indices of documents, paragraphs, and entities. 
Furthermore, we reduced the number of labels to 6, which include PERSON, ORG, LOC, PRODUCT, EVENT, and WORK_OF_ART. The label FAC was combined with ORG, and the label GPE was combined with LOC to avoid confusion due to their similarities. 

We originally extracted around 1,500 unique entity-label pairs, but because of the financial limitation of our project, we had to truncate some labels from the original CSV file. As a result, we were able to publish 790 unique entity-label pairs. 

All processes for creating the CSV file are stored in [this notebook](https://github.ubc.ca/iameleve/COLX_523_Group2/blob/master/src/NE_Annotation_for_MTurk.ipynb). 

- [Initial CSV file](https://github.ubc.ca/iameleve/COLX_523_Group2/blob/master/annotation/Annotation.csv)
- [First batch for AMT](https://github.ubc.ca/iameleve/COLX_523_Group2/blob/master/annotation/intermediate_files/truncated_unique_AMT.csv)
- [Second batch for AMT](https://github.ubc.ca/iameleve/COLX_523_Group2/blob/haejin_w3/annotation/intermediate_files/truncated_unique_AMT_2.csv)
- [Code for truncating the initial CSV file](https://github.ubc.ca/iameleve/COLX_523_Group2/blob/master/annotation/intermediate_files/truncate.ipynb)


### 4. AMT annotations
With the first and second batches above, we published our assignments to AMT. The error corrections were done in an hour. Unlike the pilot study, we changed our layout to display the label descriptions on the main page, and we added an additional qualification for workers: HIT approval rate % for all requesters’ HITs greater than 85. 

However, even with the modified settings above, we faced some issues during the annotation process. First, sometimes workers did not click “YES”, instead they clicked “NO” with the correct label (which was already given to workers) for that entity. Second, we had to pay the extra 0.01 dollar to Amazon (not for workers), so the final cost was doubled. Therefore, we had to truncate our assignments as we discussed above. Lastly, there were some workers who had 0% of HIT approval rate even though we set the additional qualification. To avoid this situation, we should have added another criterion for the number of HITs approved. 

In the end, we obtained 2,370 annotations from three workers, with the 790 unique entity-label combinations. 

- The final csv file from AMT workers is [here](https://github.ubc.ca/iameleve/COLX_523_Group2/blob/master/annotation/batch_result_final.csv).
- The interannotation study associated with this result is [here](https://github.ubc.ca/iameleve/COLX_523_Group2/blob/master/Milestone_3/Interannotator%20agreement%20study.md)


### 4-1. Experimenting with annotation options

All experiments that we conducted to increase the quality of annotations are summarized in [this notebook](https://github.ubc.ca/iameleve/COLX_523_Group2/blob/master/Milestone_3/Experimenting%20with%20annotation%20options.md).

### 5. Select the best labels and update new labels to the corpus
The last step for creating our annotated corpus was to select the “best” labels from AMT workers and update those in the original corpus. 

The best labels were selected by the principle of majority vote from the three workers. In case of a tie (i.e. all three labels are different), we used the system label from spaCy. Also, when updating the labels, we updated new labels to all instances of entities in the corpus, not just the unique entities that we used for AMT annotations. If there were more than two annotations for one entity, we applied the corrected labels only if we had talk_id, para_id, ent_id. Other than that, we skipped correcting those cases. 

All processes can be found here:

- [Code for creating final corpus](https://github.ubc.ca/iameleve/COLX_523_Group2/blob/master/src/create_final_corpus.ipynb)
- [Final annotated corpus](https://github.ubc.ca/iameleve/COLX_523_Group2/blob/master/transcripts/en/final/final_annotations.json)


