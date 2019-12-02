import numpy as np
import sklearn
import librosa
from sklearn import svm
from sklearn.externals import joblib
from sklearn import decomposition
from sklearn import neighbors
import preprocessing
import classify
#from tkinter import filedialog

def feature_extract(audio_filename):

    sr = 44100
    window_size = 2048
    hop_size = window_size/2

    music, sr= librosa.load(audio_filename, sr = sr)
    start_trim = preprocessing.detect_leading_silence(music)
    end_trim = preprocessing.detect_leading_silence(np.flipud(music))

    duration = len(music)
    trimmed_sound = music[start_trim:duration-end_trim]

    mfccs = librosa.feature.mfcc(y=trimmed_sound, sr=sr)
    aver = np.mean(mfccs, axis = 1)
    audio_feature = aver.reshape(20)
    return audio_feature


def result(pre):
    if pre == 1:
        print "The prediction of this instrument is cello."
    elif pre == 2:
        print "The prediction of this instrument is clarinet."
    elif pre == 3:
        print "The prediction of this instrument is flut."
    elif pre == 4:
        print "The prediction of this instrument is violin."
    elif pre == 5:
        print "The prediction of this instrument is piano."

def predictor(audio_filename):
    #audio_filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("mp3 files","*.mp3"),("all files","*.*")))
    #input("Please choose an audio file(test/1-10.mp3): ")
    print audio_filename
    demo_data = feature_extract(audio_filename)
    print 'processed data.'
    model_params = {
        'pca_n': 10,
        'knn_k': 5,
        'knn_metric': 'minkowski'
    }
    #  train_and_test(data, [model_params, 'svc'])
    model = classify.load_model(model_params)
    pre = classify.predict(model, demo_data, [model_params, 'svc'])
    result(pre)
    return pre

if __name__ == '__main__':
    main()
