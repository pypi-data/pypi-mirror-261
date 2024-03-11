# torch-cfu

This project is for adding custom function unit to accelerate AI algorithm. 

## How to install

You can install it by pip for the latest version. And assume that you have installed torch before.

``` bash
pip install torch-cfu
```

## How to use 

First you need to 'import torch', then 'import torch_cfu'. And you are able to rename default device name to whatever you want.

``` bash
$ python
Python 3.8.18 (default, Sep 11 2023, 13:40:15) 
[GCC 11.2.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> import torch_cfu
>>> torch_cfu.custom_device(0)
device(type='privateuseone', index=0)
>>> torch.utils.rename_privateuse1_backend("cfu")
>>> torch_cfu.custom_device(0)
device(type='cfu', index=0)
>>>
>>> x = torch.ones(4, 4, device='cfu:0')
Custom aten::empty.memory_format() called!
Custom allocator's allocate() called!
>>> x.device
device(type='cfu', index=0)
>>> x.is_cpu
False
>>> exit()
Custom allocator's delete() called!
```

x = torch.randn(3, 3)
y = torch.randn(3, 3)

# Assuming the custom operation is registered in a library called 'myops'
result = myops.myadd(x, y)
print(result)

## How to add new custom kernels in C++

1. Writing custom kernels in C++, and registering them to the PyTorch dispatcher
2. Providing a user API for your custom device, so users can invoke the custom code using `torch.foo(..., device="custom_device")`
3. Registering a custom memory allocator
4. Registering a custom device guard

## Defining schema and backend implementations

``` bash
TORCH_LIBRARY_IMPL(myops, CPU, m) {
  m.impl("myadd", myadd_cpu);
}
```

## Reference

``` bash
python setup.py sdist bdist_wheel
twine upload dist/*
```
