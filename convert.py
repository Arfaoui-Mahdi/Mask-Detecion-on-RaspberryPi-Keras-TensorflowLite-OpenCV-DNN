import os
import tempfile

from matplotlib import pyplot as plt
import numpy as np
import tensorflow as tf


converter = tf.lite.TFLiteConverter.from_saved_model('saved_model_updated')
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)