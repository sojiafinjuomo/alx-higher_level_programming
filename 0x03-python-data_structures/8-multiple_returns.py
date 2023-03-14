#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return(0, None)
    else:
        Length = (len(sentence))
        first = sentence[0]
        return(Length, first)
