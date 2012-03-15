# -*- coding: utf-8 -*-


import theano
import theano.tensor as T


def tanh(inpt):
    return T.tanh(inpt)


def tanhplus(inpt):
    return T.tanh(inpt) + inpt


def sigmoid(inpt):
    return T.nnet.sigmoid(inpt)


def rectified_linear(inpt):
    return T.clip(inpt, 0, 1E20)


def soft_rectified_linear(inpt):
    return T.log(1 + T.exp(inpt))


def identity(inpt):
    return inpt
