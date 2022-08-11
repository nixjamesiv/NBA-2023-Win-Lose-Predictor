# NBA-2023-Win-Lose-Predictor
## Overview 
This project centered around a model that predicts the outcome of the NBA's next season. 205 Sports Solutions was founded in order to help NBA teams have a better idea of their future by the numbers in order to know what to expect with their future and thus set out the correct long term plan for success. In order to create our model we use data based on ESPN and Basketball-Reference.com from the 2001 to the 2022 NBA seasons and analyzed 1,821 games during that span.

## Business Problem
We were hired by __ to create a model that can predict future outcomes of NBA games in regards to winning or losing. By doing so we can aid our stakeholders in accumulating more money through betting on NBA games.

## Data Understanding 
The data sets we used to create our models came from two ESPN databases and data from Basketball-Reference.com. The data included 1,821 games from seasons between 2011-2022. We then combined the 3 data sets by player ranking, team, and game data which combined the player and team data sets which then allowed for the player rank to be next to each player and then we found each team in the game data sets and added in the player rankings.  

## Methods


### Data Prep
We began by turning all of the string nulls into the mean. We chose the mean because the ranking contained nulls, an upper and lower bound, and was continuous so there were no gaps in the rankings. 

### Modeling
Our decision tree was overfit and not 100% accurate. Decision trees can be 100% accurate but not if there isn't enough data. From this we can gather that we need to gather and implement more data if we want our score to improve from 9.4. Our max error was 45.5 on our train set and 39.5 on our test set which are both high. As we continue to try and improve this we can do this by decreasing mean squared error which as a result will also improve our max error. We have an explained variance of 0.28 which indicates that r=there is data that is not taken into account in this model. 

Our XGBoost model was an improvement overall upon our previous decision tree model as our mean square error was reduced by 0.5 points and as a result our max error dropped by 1 point. This is a desirable outcome, especially because our explained variance did not change. 

## Results

## Conclusion




