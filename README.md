# AutoGPU

Tiny utility to get the torch.device with the most free memory. Built on [gpustat](https://github.com/wookayin/gpustat).

Install using 

```
pip install -e .
```

## Usage

```python
import autogpu

device = autogpu.freest()
```