# Global
'''
DATASET_PATH = '/home/david/Desktop/data/lung/data'
ANNOTATIONS_PATH = '/home/david/Desktop/data/lung/csv'
#ANNOTATIONS_PATH = '/input/Tianchi/dataset/csv'
PREPROCESS_PATH = '/home/david/Desktop/data/lung/preprocess'
#PREPROCESS_PATH = '/input/Tianchi/preprocess2'
LOG_BASE_PATH = './output/training_logs'
#LOG_BASE_PATH = '/output/training_logs'
'''

DATASET_PATH = 'D:\\韩霖借用-19大创\\temp\\lung'
ANNOTATIONS_PATH = 'D:\\韩霖借用-19大创\\temp\\lung\\csv'
#ANNOTATIONS_PATH = '/input/Tianchi/dataset/csv'
PREPROCESS_PATH = 'D:\\韩霖借用-19大创\\temp\\preprocess'
#PREPROCESS_PATH = '/input/Tianchi/preprocess2'
LOG_BASE_PATH = './output/training_logs'
#LOG_BASE_PATH = '/output/training_logs'

MSG_LOG_FILE = '{}/log.log'.format(LOG_BASE_PATH)
TRAIN_VAL_RATIO = 0.7


# Debug
DEBUG_PLOT_WHEN_PREPROCESSING = False
DEBUG_PLOT_WHEN_GETTING_SEG_BATCH = False
DEBUG_PLOT_WHEN_EVALUATING_SEG = True
# DEBUG_IMAGE_STD = 2000.0
DEBUG_ONLY_TRAIN_FINE_CUT_BIG_TUMOR_SWITCHER = False
DEBUG_ONLY_TRAIN_COVER_RATIO_BIGGER_THAN = 0.1
DEBUG_ONLY_TRAIN_TUMOR_DIAMETER_LARGER_THAN = 12.0

# Preprocessing
BINARY_THRESHOLD = -550
PROCESS_DONE = False
MIN_BOUND = -1000.0
MAX_BOUND = 400.0

# switcher, distinguish 2 training
TRAIN_CLASSIFY_NOT_SEGMENTATION = True
RESAMPLE_DATA_LESS_10_RATIO = 4
RESAMPLE_DATA_LESS_30_RATIO = 3

# Segmentation Model
INPUT_WIDTH, INPUT_HEIGHT, INPUT_DEPTH, INPUT_CHANNEL, OUTPUT_CHANNEL = 64, 64, 64, 1, 1
DIAMETER_SPACING_EXPAND = True
RANDOMIZE_RECORDS = True
TRAIN_SEG_LEARNING_RATE = 3e-5
USE_SIMPLIFIED_UNET = True
SEG_LOG_DIR = LOG_BASE_PATH + '/seg-run-{}'
DIAMETER_BUFFER = 0
TRAIN_SEG_ENABLE_DATA_AUGUMENTATION = True
TRAIN_SEG_SAMPLE_RANDOM_OFFSET = 20
TRAIN_SEG_POSITIVE_SAMPLE_RATIO = 0.7
TRAIN_SEG_EPOCHS = 100000000
TRAIN_SEG_EARLY_STOPPING_PATIENCE = 10
TRAIN_SEG_TRAIN_BATCH_SIZE = 16
TRAIN_SEG_STEPS_PER_EPOCH = 20
TRAIN_SEG_VALID_BATCH_SIZE = 16
TRAIN_SEG_VALID_STEPS = 5
TRAIN_SEG_EVALUATE_FREQ = 2

# Classification Model
TRAIN_CLASSIFY_MODEL = 'VGG' # VGG, DenseNet, Inception, ResNet
TRAIN_CLASSIFY_LEARNING_RATE = 1e-4
USE_SIMPLIFIED_VGG = True
TRAIN_CLASSIFY_USE_BN = False
CLASSIFY_INPUT_WIDTH, CLASSIFY_INPUT_HEIGHT, CLASSIFY_INPUT_DEPTH, CLASSIFY_INPUT_CHANNEL = 32, 32, 32, 1
CLASSIFY_LOG_DIR = LOG_BASE_PATH + '/classify-run-{}'
TRAIN_CLASSIFY_EPOCHS = 100000000
TRAIN_CLASSIFY_EARLY_STOPPING_PATIENCE = 10
TRAIN_CLASSIFY_TRAIN_BATCH_SIZE = 16
TRAIN_CLASSIFY_STEPS_PER_EPOCH = 10
TRAIN_CLASSIFY_VALID_BATCH_SIZE = 16
TRAIN_CLASSIFY_VALID_STEPS = 2

TRAIN_CLASSIFY_ENABLE_DATA_AUGUMENTATION = True
TRAIN_CLASSIFY_POSITIVE_SAMPLE_RATIO = 0.5
TRAIN_CLASSIFY_SAMPLE_RANDOM_OFFSET = 2

# Inception
INCEPTION_BLOCKS = 6
INCEPTION_REDUCTION_STEPS = 2
INCEPTION_KEEP_FILTERS = 128
INCEPTION_ENABLE_DEPTHWISE_SEPARABLE_CONV_SHRINKAGE = 0.333
INCEPTION_ENABLE_SPATIAL_SEPARABLE_CONV = True
INCEPTION_DROPOUT = 0.5

# ResNet
RESNET_BLOCKS = 16
RESNET_SHRINKAGE_STEPS = 4
RESNET_INITIAL_FILTERS = 16

# DenseNet
DENSE_NET_BLOCKS = 3
DENSE_NET_BLOCK_LAYERS = 5
DENSE_NET_INITIAL_CONV_DIM = 16
DENSE_NET_GROWTH_RATE = DENSE_NET_INITIAL_CONV_DIM // 2
# called DenseNet-BC if ENABLE_BOTTLENETCK and COMPRESSION < 1 in paper
DENSE_NET_ENABLE_BOTTLENETCK = False
DENSE_NET_TRANSITION_COMPRESSION = 1.0
DENSE_NET_ENABLE_DROPOUT = True
DENSE_NET_DROPOUT = 0.5
