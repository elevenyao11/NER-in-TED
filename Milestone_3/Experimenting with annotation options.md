## Experimenting with annotation options

### Option 1: Raise the levels of annotation workers such as approval rates.
We have changed the lifetime approval rates of annotators from 0% to 85% in the final Mechanical Turk annotations which have given us a better quality of annotations.

### Option 2: Reject and require again the annotations manually which have obvious errors.
In the pilot annotations we have rejected and required again the annotations manually which have obvious errors. And we had quite improved our agreement scores after the update. However, we don't have enough budget and time to do that in the final annotations, we think it would be useful in the future works.

### Option 3: Scale the NA annotations.
In the agreement calculation, we use alpha and scaled down the distance of N/A annotations which annotators think the entity is not included in our provided choices. It gave us 0.05 improvement.

### Option 4: Change the layout of sandbox.
We found several errors while doing the pilot study, and we found the reason for these errors in the position of detailed label descriptions. That is, people do not tend to click "more instructions" to read the detailed information about the assignment. Therefore, we summarized the most important information and put the information right above the task on the main page.

### Option 5: Limit the number of labels that human annotators can choose.
At first, we chose 9 categories of labels for this annotation. However, we found that `FAC` (facility) and `ORG` (organization), and `GPE` (countries, cities) and `LOC` (non-gpe locations) can be very confusing due to their similarities. Therefore, we merged all `FAC` labels to `ORG`, and `GPE` labels to `LOC`. Also, we omitted the `LANGUAGE` category after discussion. This seemed to have a good impact on the quality of annotations, especially when we compared the quality of annotation of the pilot study with that of the final annotation result.


### Other options:
- Different amounts of renumeration.
- Add more groups of workers.
- Increase more data for the annotations.
- Try different machine annoation tools.
