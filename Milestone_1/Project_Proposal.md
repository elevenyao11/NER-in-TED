<h1><p align="center">Project Proposal </p></h1>


<h1><p align="center">Named Entity Annotated Multilingual Parallel Corpus<br>over<br>TED Transcripts</p></h1>

## Overview

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In this project, we are going to build a Multilingual TED corpus with
the named entity annotation. The corpus will be a collection of
transcripts from TED videos including TEDx talks and TED-Ed across all
genres, aiming to collect the transcripts in three different languages
(English, Korean, and Chinese (simplified)), with the possibility of
extending to French and Spanish. After we collect the transcripts, we
will preprocess to extract named entities and get human annotation for
the English data, and then apply automatic projection methods across
multiple language data to build the parallel corpus.

## TED Transcripts as a Source of the Corpus

We chose TED as the source of the corpus for three reasons.

-   TED is a diverse global community that spreads world-changing ideas
    in concise but powerful talks. There are a wide variety of such
    videos across all genres by world-renowned speakers. Transcripts
    Vocabulary would be highly diverse, and this characteristic of the
    corpus will be well suitable for our annotation work (i.e., Named
    Entity annotation), because correctly recognizing those entities
    plays an important role in many different natural language
    processing tasks such as machine translation.

-   TED offers 100,000+ videos, each with a duration of approximately 15
    minutes. The transcripts of each video have around 1,000+ tokens.
    Generally speaking, on TED, videos often have 15+ translations,
    with a total mixture of 100+ languages (Salesky et al., 2021).
    This means that there are enough resources to construct a corpus
    with around 1M tokens, as well as a multilingual corpus.

-   The transcripts of different languages are often aligned in
    paragraphs along with timestamps. It is not perfect as they are
    not parallelly aligned (sentence by sentence), however, with the
    extra effort of multilingual projection, this is good enough to
    easily build a multi-parallel corpus.

## Data Source

The corpus will be a collection of transcripts from [TED
videos](https://www.ted.com/talks?sort=newest) including TED-Ed and TEDx
talks.

**Note:**<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;There will be some limitations in terms of the availability of
translations for some videos (English, Korean, Chinese, (we might extend to Spanish and
French)). We will scrape the videos which have all the five translations available.

## Project Specifications

|  Feature              |            Value                            |
| :---        |    :----   |   
| **Data Source**       | Transcripts from TEDx talks and TED-Ed      |
| **Data Source URL**   | [https://www.ted.com/talks?sort=newest](https://www.ted.com/talks?sort=newest)     |
| **Text Type**         | Public speech transcripts across all genres by world-renowned speakers (TEDx Talks)|
|                       | Short video lessons by experts across all genres (TED-Ed)  |
| **Document Length**   | Roughly 1,000+ tokens per document          |
| **Target**            | Speech text and translations across all genres    |
| **Languages**         | -   English, Korean, and Chinese (simplified)<br>-   Potentially extend to French and Spanish           
| **Data availability** | There is enough data to construct a "brown-size" corpus. (over 150,000 videos with English transcripts | |                       |   and translations in 100+ languages)       |
| **Structure**         | Final Data would be stored in a (.csv/.txt) file  |
| **Metadata**          | It would include:<br> -   `Video URL`<br> -   `Speaker name`<br> -   `Language`<br> -   `Topic`<br> -   `Title`<br> -   `Date (Month & Year)`<br> -   `Related tags`<br> -   `Views`<br> -   `Length of tokens in each transcript`<br>
| **Pre-processing**    | Pre-processing techniques might include:<br> -   `Removing punctuations`<br> -   `Removing stop words`<br> -   `Tokenization`<br> -   `Lemmatization`<br> -   `Sentence segmentation`<br> -   `Morphological analysis`<br> -   `Automated named entity recognition`      |
| **Annotation**        | Named entity annotation                     |
| **Other**             | Translations of each transcript are aligned in paragraph-wise |

## Possible Challenges

There are possible challenges that might come up during this project.

-   First, to make a parallel corpus, we need to collect nicely aligned
    transcripts across multiple languages. There are some transcripts
    that are already aligned in paragraphs, but not all videos nor all
    translations are as such. Before we scrape the entire text data,
    we need to decide on how to deal with "not perfectly aligned"
    transcripts/translations.

-   Secondly, preprocessing will be a must for extracting named entities
    especially in Korean and Chinese. In order to process the Chinese
    text data, applying sentence segmentation tools will be necessary,
    and to deal with the Korean text data, we need to use
    morphological analyzers to extract nouns that are attached to
    postpositional particles.

-   Lastly, once we have obtained the aligned transcripts (either in
    paragraphs or in sentences), as well as the human annotated named
    entity English corpus, we need to align the named entities over
    multiple language transcripts in order to get a named
    entity-annotated parallel corpus. In order to reduce the amount of
    work for annotation, we will adapt automatic tools for recognizing
    named entities in English, as well as word alignment tools such as
    MUSE instead of manually annotating all named entities in all
    transcripts/translations.

## Potential Application Usage

The multilingual named entity annotated corpus could be much of interest
in many different natural language processing tasks such as:

*   Named entity annotated corpora have been a crucial role for building named 
    entity recognition systems to conduct a variety of NLP applications. 
    Therefore, there has been a constant need for annotated corpora, especially 
    for non-English languages as there is a shortage of annotated data for most 
    of the world's languages other than English (Ehrmann et al., 2011).

*   Named entity annotated corpora is very useful, as when you are able
    to pick intent and custom named entities from your multilingual
    sentences with more features, then it helps you to solve real
    business problems (like picking entities from Electronic Medical
    Records, etc.). This could be further applied to low resource
    languages like Swahili as well.

*   The development of generalizable speech translation models requires
    large, diverse, and easily extensible multilingual corpora
    (Salesky et al., 2021). As all transcripts from TED talk are
    provided with audio data, there will be possibilities of
    application of this corpus to the speech processing tasks.

-   The use of multilingual parallel corpora has the benefit of ensuring
    the comparability of NER system results across different
    languages. Moreover, as named entity recognition systems are
    domain sensitive, it could be relevant to evaluate multilingual
    NER systems on equivalent tasks.

-   Furthermore, multilingual annotated corpora also constitute a
    crucial resource to acquire or infer linguistic knowledge about
    how each language is being used. It is widely accepted that
    linguistically annotated corpora are very useful resources for
    computational and linguistic analysis of languages.

-   Other potential applications of this corpus will include text
    summarization and information retrieval (Chen et al., 2021).

## References

-   Ehrmann, M., Turchi, M., & Steinberger, R. (2011). Building a
    multilingual named entity-annotated corpus using annotation
    projection. In Proceedings of the International Conference Recent
    Advances in Natural Language Processing 2011 (pp. 118-124).

-   Salesky, E., Wiesner, M., Bremerman, J., Cattoni, R., Negri, M.,
    Turchi, M., \... & Post, M. (2021). The Multilingual TEDx Corpus
    for Speech Recognition and Translation. arXiv preprint
    arXiv:2102.01757.

-   Chen, Y., Lim, K., Park, J. (2021). Korean Named Entity Recognition
    Based on Language-Specific Features. ACM Trans. Asian Low-Resour.
    Lang. Inf. Process. 1, 1, Article 1 (February 2021), 17 pages.
    <https://doi.org/0000001.0000001>
