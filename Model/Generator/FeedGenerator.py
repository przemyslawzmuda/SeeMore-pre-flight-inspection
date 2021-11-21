class FeedDataGenerator:
    def __init__(self, path_to_data, target_image_sample_size, batch_size, output_class_mode, **kwargs):
        self.path_to_data = path_to_data
        self.target_image_sample_size = target_image_sample_size
        self.batch_size = batch_size
        self.output_class_mode = output_class_mode
        self.bool_shuffle = kwargs.get('shuffle')

    def injectDataIntoGenerator(self, data_generator: object) -> object:
        if self.bool_shuffle:
            configured_batch_of_data = data_generator.flow_from_directory(
                self.path_to_data,
                target_size=(self.target_image_sample_size, self.target_image_sample_size),
                batch_size=self.batch_size,
                class_mode=self.output_class_mode
            )
            return configured_batch_of_data
        else:
            configured_batch_of_data = data_generator.flow_from_directory(
                self.path_to_data,
                target_size=(self.target_image_sample_size, self.target_image_sample_size),
                batch_size=self.batch_size,
                class_mode=self.output_class_mode
            )
            return configured_batch_of_data
