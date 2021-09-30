from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
from collections import defaultdict
import spacy
from spacy import displacy
import uvicorn
import numpy as np
import random
import json
import pandas as pd
import os
import zh_core_web_sm

pd.set_option("display.max_colwidth", None)
# os.system("python -m spacy download zh_core_web_sm") # this should be included in docker file

app = FastAPI()
nlp = spacy.load("zh_core_web_sm")

# define functions
def open_file_return_corpus(path):
    """Given a path, open a json file and return a list of dictionaries."""
    f = open(path, encoding="utf-8")
    corpus = json.load(f)
    f.close()
    return corpus


# paths for images
wordcloud_path = "../images/ted_talk_wordcloud.png"
token_char_path = "../images/token_character.png"

# load corpora
paths = [
    "../transcripts/en/final/final_annotations.json",
    "../transcripts/ko/filtered/filtered_annotated_ted_talks_ko.json",
    "../transcripts/zh-cn/filtered/filtered_annotated_ted_talks_cn.json",
]

en_corpus = open_file_return_corpus(paths[0])
ko_corpus = open_file_return_corpus(paths[1])
cn_corpus = open_file_return_corpus(paths[2])

# global variable
valid_labels = {"PERSON", "ORG", "EVENT", "PRODUCT", "LOC", "WORK_OF_ART"}

# find paragraphs with a keyword
def find_paragraphs(keyword, language="all"):
    """Given keyword and language, find paragraphs in parallel corpus.
    Returns a dataframe of parallel paragraphs with selected languages."""
    parallel_corpora = defaultdict(dict)
    df = None
    # find a paragraph in a corpus
    count = 0
    for i, talk in enumerate(en_corpus):
        for k, para in enumerate(talk["text"]):
            if keyword.lower() in para["text"].lower():
                parallel_corpora[count]["talk_id"] = i
                parallel_corpora[count]["title"] = " ".join(
                    talk["title"].split("_")
                ).title()
                parallel_corpora[count]["en"] = para["text"][:500] + "..."
                parallel_corpora[count]["para_id"] = k

                ents = set()
                for ent in para["ents"]:
                    if ent["label"] in valid_labels:
                        ents.add((ent["text"], ent["label"]))

                parallel_corpora[count]["entities"] = list(ents)

                count += 1

    # language option
    print(language)
    if language == "all":
        for key, para_dict in parallel_corpora.items():
            talk_id = para_dict["talk_id"]
            para_id = para_dict["para_id"]
            ko_para = ko_corpus[talk_id]["text"][para_id]
            cn_para = cn_corpus[talk_id]["text"][para_id]

            parallel_corpora[key]["ko"] = ko_para["text"][:500] + "..."
            parallel_corpora[key]["zh-cn"] = cn_para["text"][:500] + "..."
        df = pd.DataFrame(parallel_corpora).T[
            ["title", "en", "ko", "zh-cn", "entities", "para_id"]
        ]
    if language == "ko":
        for key, para_dict in parallel_corpora.items():
            talk_id = para_dict["talk_id"]
            para_id = para_dict["para_id"]
            ko_para = ko_corpus[talk_id]["text"][para_id]

            parallel_corpora[key]["ko"] = ko_para["text"][:500] + "..."
        df = pd.DataFrame(parallel_corpora).T[
            ["title", "en", "ko", "entities", "para_id"]
        ]
    if language == "cn":
        for key, para_dict in parallel_corpora.items():
            talk_id = para_dict["talk_id"]
            para_id = para_dict["para_id"]
            cn_para = cn_corpus[talk_id]["text"][para_id]

            parallel_corpora[key]["zh-cn"] = cn_para["text"][:500] + "..."
        df = pd.DataFrame(parallel_corpora).T[
            ["title", "en", "zh-cn", "entities", "para_id"]
        ]

    if language == "en_only":
        df = pd.DataFrame(parallel_corpora).T[["title", "en", "entities", "para_id"]]

    return df


# find sentences with an entity or a label
def find_entity_or_label(keyword, mode="entity"):
    """Given a keyword (entity, or a label) return a dataframe containing
    the entity (or the label) and its contextual sentences."""
    entity_dict = defaultdict(dict)
    df = None
    count = 0
    for i, talk in enumerate(en_corpus):
        for k, para in enumerate(talk["text"]):
            for j, ent in enumerate(para["ents"]):

                if mode == "entity":
                    search = ent["text"].lower()
                elif mode == "label":
                    if ent["label"] in valid_labels:
                        search = ent["label"].lower()

                if search == keyword.lower() and ent["label"] in valid_labels:
                    entity_dict[count]["talk_id"] = i
                    entity_dict[count]["title"] = " ".join(
                        talk["title"].split("_")
                    ).title()
                    entity_dict[count]["para_id"] = k
                    entity_dict[count]["entity"] = ent["text"]
                    entity_dict[count]["label"] = ent["label"]
                    entity_dict[count]["start_index"] = ent["start"]
                    entity_dict[count]["end_index"] = ent["end"]
                    try:
                        entity_dict[count]["text"] = " ".join(
                            [
                                para["text"][: ent["start"]].split(".")[-1],
                                ent["text"],
                                para["text"][ent["end"] :].split(".")[0],
                                ".",
                            ]
                        )
                    except IndexError:
                        entity_dict[count]["text"] = para["text"]
                    count += 1

    df = pd.DataFrame(entity_dict).T[["title", "entity", "label", "text"]]
    return df


def render_paragraph(keyword, index, render_language):
    """Given a keyword and index, it finds a paragraph where the keyword appears,
    and the given language option, return a displaCy rendered version of the paragraph.
    """
    if render_language == "en":
        df = find_paragraphs(keyword, "en_only")
        title = df.iloc[index]["title"].lower().replace(" ", "_")
        para_id = df.iloc[index]["para_id"]
        for talk in en_corpus:
            if talk["title"] == title:
                paragraph = talk["text"][para_id]
        return displacy.render(
            paragraph,
            style="ent",
            manual=True,
            options={"ents": list(valid_labels)},
        )
    elif render_language == "cn":
        df = find_paragraphs(keyword, "cn")
        title = df.iloc[index]["title"].lower().replace(" ", "_")
        para_id = df.iloc[index]["para_id"]
        for talk in cn_corpus:
            if talk["title"] == title:
                paragraph = talk["text"][para_id]
                paragraph = nlp(paragraph["text"])
        return displacy.render(
            paragraph,
            style="ent",
            options={"ents": list(valid_labels)},
        )


@app.get("/")
def start():
    return FileResponse("frontend.html")


@app.get("/{filename}")
def get_file(filename):
    return FileResponse(filename)


@app.get("/corpus/")
def display_corpus(keyword, mode, language, displacy_index, render_language):
    """Display the dataframe where the keyword appears on the frontend html page.
    keyword -- a keyword of user's choice. It can be a word, an entity, or a label.
    mode -- a mode of search. Depending on the mode, this function calls different functions.
    language -- a language of paragraphs that will be included in the dataframe.
    displacy_index -- an index of a paragraph to render with displaCy.
    render language -- a language of a paragraph to render with displaCy.py
    """
    print(keyword)
    if len(displacy_index) > 0:
        print(displacy_index)
        displacy_index = int(displacy_index)
        return HTMLResponse(render_paragraph(keyword, displacy_index, render_language))
    if mode == "text":
        df = find_paragraphs(keyword, language).drop(columns=["para_id"])
        html_df = df.to_html()
        return HTMLResponse(html_df)
    if mode == "entity":
        return HTMLResponse(find_entity_or_label(keyword, mode).to_html())
    if mode == "label":
        return HTMLResponse(find_entity_or_label(keyword, mode).to_html())


@app.get("/about/")
def display_text():
    """Display 'about' contents on the HTML page."""
    return FileResponse("about.html")


@app.get("/how-to-use/")
def display_how_to_use():
    """Display 'how to use' contents on the HTML page."""
    return FileResponse("how-to-use.html")


@app.get("/dataviz/")
def display_data_viz():
    """Display 'data visualization' contents on the HTML page."""
    return FileResponse("dataviz.html")

@app.get("/demo/")
def display_demo():
    """Display 'demo' contents on the HTML page."""
    return FileResponse("demo.html")



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9999, debug=True)
