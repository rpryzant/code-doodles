# Description

This is a lighthearted QC hackathon project by Noah Grumman, Jonah Eisen, and Reid Pryzant.

We set up a webcam outside the company fridge, and used it to automatically predict how well stocked each drink, snack, etc. was. We then streamed all the results online so that our teammates would be more informed the next time they left their desks for a coconut water. 

# My Role

Within the project, my role was to invent and implement the algorithm that, given a picture of a fridge, estimates the quantity of each item. The result worked fairly well. It's in `detect_objs.py`. The algorithm executes the following steps:

1. Draw bounding boxes around each "section" of the fridge (i.e. where each different type of drink/snack is)
2. Count the number of pixels of a particular "indicator color" (i.e. the crimson in a coke can label, the deep blue in a water bottle cap) right after the fridge is stocked
3. Monitor those indicator pixel frequencies over the course of the day, and use their fluctuations to estimate item removal/addition
