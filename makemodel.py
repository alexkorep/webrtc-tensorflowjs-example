from keras.applications.mobilenet import MobileNet
INPUT_SHAPE = (128, 128, 3)
model = MobileNet(weights='imagenet', include_top=True, input_shape=INPUT_SHAPE)
model.save('model.h5')