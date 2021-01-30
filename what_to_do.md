1. For now get the last 10 games. Eventually,Fetch games since the last time stamp
- Okay so the solution to the above is the use python-lichess for now. No idea what the fecking length 13 timetag is
- The issue with this is, whilst it gives a really nice dict return, it doesn't seen to give evals
2. For each game that isn't in the posted list, parse
3. Once parsed, post to twitter using the twitter post api
4. update the list of already post games and the timestamp to now



- Once this is working I"ll add a parser to find the worst move and generate two images of the position before and move after.
- Also store a pickled state of tweets so I can easily re-start
