## Interannotator agreement study

### 1. The choice of Interannotator agreement measure

We choose Krippendorf's Alpha as our Interannotator agreement measure based on the reasons below:

- Alpha and K are more appropriate to abstract away from the bias of specific coders.
- We have different annotatorts (annotators in three coder group are not the same person)
- Because some pairs of entites might be more like each other, so the scale of metric alpha is useful.
- The "N/A" correction from Mechanical Turk workers might be scaled down campared to different entities correction.

### 2. Calculate interannotator agreement

We got alpha score: 0.7348 after scaling. The code of interannotator agreement calculation can be found here: [interannotator agreement calculation](https://github.ubc.ca/iameleve/COLX_523_Group2/blob/master/src/agreement.ipynb)

### 3. The discussion on the reliability of annotation.

From [Inter-Coder Agreement for Computational Linguistics](https://ict.usc.edu/pubs/Inter-Coder%20Agreement%20for%20Computational%20Linguistics.pdf) Krippendorff’s recommendations were developed for the field of content analysis, where coding is used to draw conclusions from the texts. A coded corpus is thus akin to the result of a scientific experiment, and it can only be considered valid if it is reproducible—that is, if the same coded results can be replicated in an independent coding exercise. Krippendorff therefore argues that any study using observed agreement as a measure of reproducibility must satisfy the following requirements:

- It must employ an exhaustively formulated, clear, and usable coding scheme together with step-by-step instructions on how to use it.
- It must use clearly specified criteria concerning the choice of coders (so that others may use such criteria to reproduce the data).
- It must ensure that the coders that generate the data used to measure reproducibility work independently of each other.

Because of our annotation process on Amazon Mechnical Turk with a clear step-by-step instructions, and different workers work independently, the annotations have a good reliabity. 

### 4. Possible improvement 

- Consider the scale of different entites which have done and got a 0.05 improvement.
- Add more groups of workers and raise the requirement of workers such as approval rates.
- Increase more data for the annotations.
- Try different machine annoation tools.
