from katiag_image_processing.utils import io, plot
from katiag_image_processing.processing import combination, transformation

image1 = io.read_image('https://github.com/kriskacg/katiag-image-processing-package/sample_images/cachoeira.jpg')
image2 = io.read_image('https://github.com/kriskacg/katiag-image-processing-package/sample_images/ponte-madeira.jpg')

plot.plot_image(image1)
plot.plot_image(image2)

result_image = combination.transfer_histogram(image1,image2)

plot.plot_result(image1,image2, result_image)