# Transparent Shape Dataset
This is the dataset release of our paper [Through the Looking Glass: Neural 3D Reconstruction of Transparent Shapes, CVPR 2020](https://arxiv.org/abs/2004.10904). Please consider citing this paper if you find this dataset useful in your project. Please contact us if you have any questions or issues. 
![](http://cseweb.ucsd.edu/~viscomp/projects/CVPR20Transparent/github/TransShape.gif)

## Dataset Links
Followings are the links to our dataset, to understand the data structure of our dataset, please refer to the dataset creation repository from this [link](https://github.com/lzqsd/TransparentShapeDatasetCreation) and the network repository from this [link](https://github.com/lzqsd/TransparentShapeReconstruction), which will tell you how the data are created and how to load the data for training. We also provide our final reconstruction results of 10-view, 20-view and 5-view reconstruction so that future researchers can compare with our method easily. 
* [Shapes](http://cseweb.ucsd.edu/~viscomp/projects/CVPR20Transparent/dataset/Shapes.zip)
  * The geometry, camera position and scene configuration files used to create the dataset. 
* [Images5](http://cseweb.ucsd.edu/~viscomp/projects/CVPR20Transparent/dataset/Images5.zip)
  * The rendered images, two-bounce normal and the final reconstructed meshes of the 5-view reconstruction. 
* [Images10](http://cseweb.ucsd.edu/~viscomp/projects/CVPR20Transparent/dataset/Images10.zip)
  * The rendered images, two-bounce normal and the final reconstructed meshes of the 10-view reconstruction. 
* [Images20](http://cseweb.ucsd.edu/~viscomp/projects/CVPR20Transparent/dataset/Images20.zip)
  * The rendered images, two-bounce normal and the final reconstructed meshes of the 20-view reconstruction. 
* Envmap
  * We use the [Laval Indoor Lighting Dataset](http://indoor.hdrdb.com/) to render our data. Unfortunately, we are not supposed to redistribute the dataset. We have actually rescaled and renamed the environment maps when creating our data. The `infoList.dat` and `mapEnvmaps.py` can be used to map the original environment maps to our environment maps used for rendering.  

## Quantitative Comparisons
To reproduce the quantitative number of shape reconstruction in our paper, you can download the dataset and run `testMesh.py` from this [link](https://github.com/lzqsd/TransparentShapeReconstruction) with `--dataRoot` and `--camNum` set properly. Please let us know if you have any questions running the code. 
