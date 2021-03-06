from imgaug import augmenters as iaa

from mnist.preprocess import PreProcesser

if __name__ == '__main__':
	dataset = PreProcesser.load_files(folder='./Fashion-MNIST/')
	augmenter = iaa.OneOf([

	])
	aug_dataset = PreProcesser.augment_mnist_data(dataset, augmenter=augmenter, augmented_ratio=1)
	PreProcesser.save(aug_dataset, 'Fashion-MNIST/dataset_ratio_1_no_augmentation.pkl')