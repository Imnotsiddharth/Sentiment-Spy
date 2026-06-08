from textblob import TextBlob
print("Welcome to the AI Mood Detector!")
name = input("What's your name? ")
print (f"Nice to meet you, {name}! Let's analyze the sentiment of your sentence!")
print ("Type 'exit' to quit.\n")

while True:
    sentence = input("Your sentence: ")
    if sentence.lower() == "exit":
        print(f"Goodbye, {name}")
        break
    blob = TextBlob(sentence)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        print("Positive sentiment detected.")
        print(sentiment)
    elif sentiment < 0:
        print("Negative sentiment detected.")
        print(sentiment)
    else:
        print("Neutral sentiment detected.")
        print(sentiment)
        