# Project: Weakly supervised learning-- label noise and correction


### [Full Project Description](doc/project3_desc.md)

Term: Spring 2024

+ Team 7
+ Team members
	+ Rui Chen
	+ Jiaqi Liu
	+ Fei Li
	+ Xiaoyu Mai

+ Project summary: In this project, we explored image classification on a noisy variant of the CIFAR-10 dataset, developing two models to tackle label noise. Model I was a straightforward CNN trained directly on noisy labels, offering a baseline performance. Model II advanced this by first refining labels through a label correction CNN trained on a clean subset, then applying the corrected labels to train the final classifier, which reduces the impact of noisy labels, potentially enhancing classification accuracy. This project highlighted the significance of label quality in machine learning and explored methods to improve model robustness against data imperfections.
	
**Contribution statement**: ([default](doc/a_note_on_contributions.md)) All team members contributed equally in all stages of this project. All team members approve our work presented in this GitHub repository including this contributions statement. 

Following [suggestions](http://nicercode.github.io/blog/2013-04-05-projects/) by [RICH FITZJOHN](http://nicercode.github.io/about/#Team) (@richfitz). This folder is orgarnized as follows.

```
proj/
├── lib/
├── data/
├── doc/
├── figs/
└── output/
```

Please see each subfolder for a README file.
