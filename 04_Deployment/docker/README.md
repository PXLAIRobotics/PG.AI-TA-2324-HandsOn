# PXL Postgraduate AI Technical Architect
!!! Note: Do not clone this repository into a path containing a space !!!*

## Docker Container Specifications

### Base Environment

- Ubuntu: 22.04
- Python: 3.11
- CUDA: 11.5

### Libraries

#### Neural Network Libraries

- Tensorflow / Keras: 2.14

#### Deployment Libraries

- flask: 3.0.0
- onnx: 1.14.1

## Prerequisites
* A UNIX-like operating system, preferably Linux. (Ubuntu 20.04+ is recommended.) **or** Windows with Docker Desktop installed.
* xB free space
* An operational docker daemon.
* Standard Bash knowledge.

### GPU
You can run the container without GPU support, but your performance (with Deep Learning frameworks) will be low.

**Nvidia**

If you have an Nvidia graphics card capable of running hardware accelerated graphics, follow the instructions in the guide [here](CUDA%20Installation) to install all the necessary drivers, CUDA and the Nvidia docker toolkit. 

You can test GPU support by executing the following steps (after having built the container, see [How to build the container](https://github.com/PXLAIRobotics/PXL_ML_Docker_v2.0/tree/main#how-to-build-the-container)):

```
003_start_pxl_pgta_tf_deployment_container.sh
```

```
nvidia-smi
```

```
start_jupyter
```

Open the TestGPU.ipynb notebook and exectute the different steps.
 
## How to build the container
A bash script is provided to build the container, it can be executed by entering
the following command:

```
./001_build_images.sh
```

## How to start the container
To start the container execute the script below:

```
003_start_pxl_pgta_tf_deployment_container.sh
```
This script will check the available GPU and start the container accordingly.

To use multiple bash shells in the container, It's advised to either work with
`tmux` or execute the script with prefix `004` from the host:

```
./004_attach_bash_to_container.sh
```

## Start jupyter
To start jupyter notebooks, you can use the command
```
start_jupyter
```
inside the container.

## Prebuilt image
TBD
