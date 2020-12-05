Motion Recognition Project
By Xingyun Chang

Empathize:
The audience would be people being interested in how a person within an image in moving within a short video. When the user input a video, the algorithm can subtract the background and using heatmap-liked images to show the change in the person’s movement. 

Define:
I am exploring the extraction the human’s motion within a video. Specifically, the algorithm can transfer a short video into a sequence of images, and then extract the pixels of the image showing human motion. It would also research on the effect of using difference background subtracting threshold. 

Ideate:
First, we transfer the video dataset into a sequence of images. 
Second, we use a subtract_bg method to remove background, only keeping the pixels that are greater than the background threshold. Third, we use a diff_between_frames method to calculate the binary foreground difference between two images. 
Fourth, we calculate the motion history image value. 
I’m running the algorithm on a sample video. 
I’m also doing experiments to figure out what’s the best-fit background threshold for the given video. 

Prototype:
I plot 20 consequent images from the original video dataset. Those images directly show the change in person’s motion consecutively. Also, I’m running the algorithm on input with different background thresholds to find the best-fit range. 

Test:
The algorithm successfully extracted the motion of human’s motion. Also, the experiments are showing that as the threshold increases, there are more disturbing pixels in the output. The range between 38000-39000 gives the most optimized output. 

