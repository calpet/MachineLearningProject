# MachineLearningProject

This project was made for a research I did regarding AI in school. It's a prototype of an automoderator for a forum which filters out swearing words in any given forum post and censors it with '*'. Currently however, I've just hardcoded a Reddit post inside `main.py` and added some swearing words from the datasets at random places. 

## Installation

First off, download the [Bad words dataset from Kaggle](https://www.kaggle.com/datasets/nicapotato/bad-bad-words?resource=download) and put it inside the data folder. (the reason why it's not there already is because I feel awkward knowing I've put a dataset containing a thousand swearing words on my public repository)

Then, navigate to the root directory of the project & use the following command in your terminal:
```bash
$ pip install -r requirements.txt
```

Now we've installed everything we need.

## Usage
Run either:
```bash
$ python main.py
```
or
```bash
python3 main.py
```
to run it and watch the machine learning algorithm almost do what it's supposed to do!

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)