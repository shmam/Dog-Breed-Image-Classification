import split_folders

SOURCE_PATH = "images/"
DEST_PATH = "train_dataset/"

# Split folder of test-data in desired ratio (train,val,test)
split_folders.ratio(SOURCE_PATH, output=DEST_PATH, seed=1337, ratio=(.7, .2, .1)) # default values
