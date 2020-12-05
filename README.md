Motion Recognition Project
By Xingyun Chang

This project would combine the idea of Art + AI, extracting the human’s motion within the image. 
Specifically, the algorithm can transfer a short video into a sequence of images, and then extract the pixels of the image showing human motion. It would also research on the effect of using difference background subtracting threshold. 

This project is inspired by an extra credit homework of CS4476 at Gatech, also using the dataset provided by the course. 

Video Data:
https://gatech.box.com/shared/static/sw7dkza8drr2ouyko59haqyrczg3bbg0.zip

First, we transfer the video dataset into a sequence of images.
 
Second, we use a subtract_bg method to remove background, only keeping the pixels that are greater than the background threshold.
Third, we use a diff_between_frames method to calculate the binary foreground difference between two images.
Fourth, we calculate the motion history image value.

The algorithm successfully extracted the motion of human’s motion. Also, the experiments are showing that as the threshold increases, there are more disturbing pixels in the output. The range between 38000-39000 gives the most optimized output. 



