# SenatorsPR

Analysis of Puerto Rican Senate voting 2017-2020

## Motivation and Description

While studying the Singular Value Decomposition (SVD) and its appllications, I learned that it can be used to compare similarities of voters in a group, like the senate. Consequently, I decided to perform an analysis on Puerto Rican senators' voting by using the SVD.

This analysis takes all of the votes each senator participated in during the term. Then, it plots a point for each senator. Essentially, the closer two points are, the more similar those senators voted. Each point's color is based on that senator's political party. With this analysis, we can figure out if senators in the same party have similar voting patters. We performed this analysis for the whole term and for each year. Additionally, we analyzed a subset of controversial bills. An example error plot and analysis plot can be found in the repository. The others can be obtained by running SVD_Plot.py.

## Data

The data from the pdf's is readily available from http://votaciones.senado.pr.gov/. Each pdf contains data of bill numbers and how each senator voted in them. Additionally, each pdf is for a three month period of the term.

The pdf's were converted into 16 txt files. Then, in PR_Senators.py a txt file can be converted into a matrix where the SVD can be performed. The matrix has one row for each senator and a column for each bill. The entries are all 1, 0, or -1. These correspond to the votes "A favor", "Ausente"/"Abstenido", and "En contra". In English, "Yes", "Absent"/"Abstain", and "No" respectively.

## Controversial Bills

Since many bills had most, or all, of the senators vote the same way, the senators' votes are all correlated. So, to more precisely achieve the goal of finding which senators have simimlar voting patterns it is necessary to look at a subset of bills where senators voted differently. We define a controversial bill as one that had 5-25 out of 30 senators vote yes. This means a controversial bill has at least 15% disagreement. The same SVD analysis was performed on this subset of bills.

We also did the same for non controversial bills which simply all of the bills that were not controversial. That is, 25 or more senators agreed on the bill.

## What's Next

For now, the analysis only shows the political party of a senator. It would be useful to know which senators have the closest voting patterns. So, next, we will make a plot where the senator represented by each point is displayed. Also, this analysis would be performed every year of the upcoming 2021-2024 term, which has more political parties represented. Furthermore, if more information is needed, this analysis can be performed on other subsets of bills.
