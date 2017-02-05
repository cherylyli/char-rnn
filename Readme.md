#ObamaBot
I used a recurrent neural net with 2 hidden layers, a dropout rate of 0.5, and rnn size of 521. A 1.5MB text file of Obama speeches to generate Obama-Style speeches. Then I used a Markov Twitter bot to read from the output of the Obama-Style speeches and generate short tweets with certain keywords that Donald Trump supporters tweet out.

Used a bunch of pre-existing libraries. 
Notably:
- char-rnn for the recurrent neural net
- using pseudoObama-Style text as input to respond to keywords extracted from Donald Trump's tweets
- indico to parse keywords and intent of tweets

Install a bunch of things, I recommed using a separate environment running python 2
- download torch / Lua 
- run this command, this will take a pretty long time to run though. 
```
$ th train.lua -data_dir data/Obama -rnn_size 512 -num_layers 2 -dropout 0.5
```
- get some output Obama gibberish: (you can add a length and primetext and temperature, these are fun things to play with)
```
$ th sample.lua cv/some_checkpoint.t7 -gpuid -1 
```
- you can redirect your ouput of Obama gibership into a text file and let the markov model read from it
- set up twitter app
-run 
```
python ObamaBot/app.py
```


## Used the following open source libraries:
- [char-rnn](https://github.com/karpathy/char-rnn)
- [MarvokBot](https://github.com/esdalmaijer/markovbot)

## License

MIT
