# Music Instrument Classifier

This is a simple classifier that is able to detect single-note sounds of various musical instruments.

Currently supported types are cello, clarinet, flute, violin and piano. The audios are supposed to be single-note sounds within the 4th octave.

A user interface is included for ease of usage.

Created by Ivy Zheng, Weiyuan Deng and Yuchen Rao from Northwestern University.


## Dataset

The dataset used to train this classifier was collected from London Philharmonic Orchestra Dataset (http://www.philharmonia.co.uk/explore/sound_samples). Each audio file records one note from one of the five instruments, and has a length from 0.25 seconds to 6 seconds. In total, over 600 audio pieces were used to train the classifier, and the distribution of each class was roughly the same. 

For copyright reasons, the original data is not included in this repository. 


## Dependencies

 - Python 2
 - NumPy
 - Scikit-Learn (sklearn)
 - Librosa
 - glob


### Preprocessing

The music pieces have their leading and ending silence trimmed. The threshold of trimming is 0.001 - if the intensity of the sound in the frame is below 0.1% of the highest sound intensity in the audio file, then the frame is trimmed out. 

### Feature Extraction

The Mel Frequency Cepstral Coefficents (MFCCs) of each music piece was extracted using Librosa. For each audio file, its MFCCs are averaged to produce the final, length-20 feature vector. 

### Classification

An SVM classifier is trained from the feature vectors to determine the instrument it belongs to. The SVM classifier worked in a one-vs-rest fashion, in which it trained 5 classifiers for each intrument class against all audios that are not in that class. The kernel of the SVM classifiers is linear. 


### Accuracy

With the given dataset and under 10-fold cross-validation, we achived a 95% accuracy on the instrument label prediction.

## Try it Out

In addition to the code for training, this repository also includes a pre-trained model that you can play with. Try to run the following code in your terminal:

    python ui.py

After that, choose the audio file path that you want to classify. It will output the musical instrument that it recognized in the audio.
