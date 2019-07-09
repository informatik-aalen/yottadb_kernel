from ipykernel.kernelapp import IPKernelApp
from .kernel import YottaDBKernel

IPKernelApp.launch_instance(kernel_class=YottaDBKernel)
