from sklearn.linear_model import LogisticRegression

from src.utils.censorship_handler import censor
from src.utils.dataset_handler import get_dataset
from src.models.predictions_model import create_predictions_model
from src.models.training_model import train_model
from src.utils.token_handler import preprocess, tokenize

forum_post = '''
    Titanic (1997) remains a compelling film 25 years later. There are 90s movies and then there is Titanic. The look of that movie is at least a decade ahead of the rest. Even big movies released years later in the 90s like Phantom Menace, The Matrix etc don't look as good as Titanic. Of course, the technicals and art direction along with vfx aren't short of praises. They made Titanic a must watch spectacle back then.
    On a recent rewatch (my 3rd watch of Titanic), I focused on the script and story. What is noteworthy is that Titanic is perfectly split in two. No not the ship, the story. It's a story of two halves where the first half is about the romance that develops between Jack & Rose where Titanic and its majestic setting serves as a backdrop. The second half is about the Titanic sinking disaster where the above-mentioned romance takes a backseat. The roles are reversed but interestingly both aid one another. The disaster of Titanic we see through the eyes of Jack & Rose primarily. Their love story adding extra tension to the proceedings.
    Of course Titanic was a mega smash hit and perhaps the greatest box office story ever. But what about the script & direction? Was Jim Cameron successfully able to mesh the two halves together?
    My take is that the disaster portion of the film turned out to be the more fascinating picture and I would have liked to see more of that. The thoughts and ideas that went into the ship and what the voyage meant to people. The hubris of the owners and makers of the ship, the science of the ship etc.
    On the contrary, the Jack-Rose pairing is iconic in pop culture or culture even. Kind of a Rome-Juliet of its time. However, I am never convinced by short romances developed within hours or a couple of days. Jack and Rose meet each other 48-72 hours ago and by the end of the film are ready to die for each other, Rose ready to give up her mother, status and wealth too for a man who was a stranger a week ago. Rose has a chance to get on a boat earlier, and she does so too but then jumps ship to go back to Jack from the fear of separation. Young love I guess.
    Titanic does ultimately end up being a romance drama where disaster is the setting. Jim chooses to let the film continue for a good few minutes even after the sinking. The final shot is on the Titanic, but more than the sinking of Titanic, we are left feeling more sad at the sinking of Jack Dawson. Often termed as the greatest love story put to cinema, at least over the past few decades, it is hard to argue that Jim didn't make the right choice given its success and how well it seems to have aged.
    What are your thoughts on the movie in general? And was James Cameron right in merging epic romance with disaster?
    '''

def main():
    # Get necessary datasets and labels which we can use to train the AI:
    texts = get_dataset('./data/bad-words.csv')
    lRows = get_dataset('./data/labels.csv')
    labels = []
    temp = []

    # Convert each label row into int so the code doesn't spaghetti harder than it already does:
    for row in lRows:
        temp.extend(row)
    for value in temp:
        labels.append(int(value, base=10))
    
    # Train model, tokenize each word from the input (forum post), and preprocess it:
    model, vectorizer = train_model(model=LogisticRegression(), dataset=texts, labels=labels)
    tokens = tokenize(forum_post)
    preprocessed_tokens = [preprocess(token) for token in tokens]

    # Create predictions based on the preprocessed tokens & censor the text:
    predictions = create_predictions_model(preprocessed_tokens=preprocessed_tokens, vectorizer=vectorizer, model=model)
    censored_text = censor(tokens, predictions)
    print(censored_text)

if __name__ == '__main__':
    main()
