
# WORDLE AUTOMATOR
## ABOUT

Wordle is a famous online word game where we are supposed to guess a random 5 letter word within 6 tries.

In this project I have built an automator that can solve the game automatically without any human inputs.


## ANALYSIS

Out of the 2117 words given in the wordle website, the average score was around 4 and only 15 words took more than 6 guesses.

<img width="476" alt="analysis" src="https://user-images.githubusercontent.com/69286061/157077554-ffb43ad0-ae2a-416b-b68a-91223785537d.png">



## SCOPE OF IMPROVEMENT

The average score is above 4 and there are 15 words that it is not able to find. This can be further optimized by using the frequency of a word used in daily life so that those words are given a higher priority before other words.

### Issue in code

For example: answer = "shave".

The guesses were:

saner,
slate,
shake,
shade,
shame,
shape,
shave.

After guessing "SHAKE" in the third guess, the algorithm deems shade, shame, shade and shake to have equal probability and thus unluckily "shave" turns out to be the 7th guess.  
