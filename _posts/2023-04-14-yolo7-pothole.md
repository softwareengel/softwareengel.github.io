# Train Pothole 

https://learnopencv.com/fine-tuning-yolov7-on-custom-dataset/
https://blog.roboflow.com/yolov7-custom-dataset-training-tutorial/
https://www.youtube.com/watch?v=5nsmXLyDaU4
https://learnopencv.com/yolov7-object-detection-paper-explanation-and-inference/
https://github.com/WongKinYiu/yolov7
https://learnopencv.com/pothole-detection-using-yolov4-and-darknet/#The-Pothole-Dataset
https://learnopencv.s3.us-west-2.amazonaws.com/pothole-dataset.zip
https://learnopencv.com/fine-tuning-yolov7-on-custom-dataset/


# Dataset

https://public.roboflow.com/object-detection/pothole/1
https://public.roboflow.com/models/object-detection


# 

```ps
python train.py --epochs 100 --workers 4 --device 1 --batch-size 32 --data data/pothole.yaml --img 640 640 --cfg cfg/training/yolov7_pothole-tiny.yaml --weights 'yolov7-tiny.pt' --name yolov7_tiny_pothole_fixed_res --hyp data/hyp.scratch.tiny.yaml

# Batch size 16 
python train.py --epochs 100 --workers 4 --device 1 --batch-size 16 --data data/pothole.yaml --img 640 640 --cfg cfg/training/yolov7_pothole-tiny.yaml --weights 'yolov7-tiny.pt' --name yolov7_tiny_pothole_fixed_res --hyp data/hyp.scratch.tiny.yaml
```

# 
    Traceback (most recent call last):
    File "C:\data\2023-pothole\down\yolov7\train.py", line 595, in <module>
        device = select_device(opt.device, batch_size=opt.batch_size)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "C:\data\2023-pothole\down\yolov7\utils\torch_utils.py", line 71, in select_device
        assert torch.cuda.is_available(), f'CUDA unavailable, invalid device {device} requested'  # check availability
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError: CUDA unavailable, invalid device 1 requested
    (.venv) PS C:\data\2023-pothole\down\yolov7> python train.py --epochs 100 --workers 4 --device 1 --batch-size 32 --data data/pothole.yaml --img 640 640 --cfg cfg/training/yolov7_pothole-tiny.yaml --weights 'yolov7-tiny.pt' --name yolov7_tiny_pothole_fixed_res --hyp data/hyp.scratch.tiny.yaml
# 

    Starting training for 100 epochs...

        Epoch   gpu_mem       box       obj       cls     total    labels  img_size
    0%|                                                                                                                                                                           | 0/40 [00:03<?, ?it/s] 
    Traceback (most recent call last):
    File "C:\data\2023-pothole\down\yolov7\train.py", line 616, in <module>
        train(hyp, opt, device, tb_writer)
    File "C:\data\2023-pothole\down\yolov7\train.py", line 361, in train
        pred = model(imgs)  # forward
    File "C:\ProgramData\anaconda3\lib\site-packages\torch\nn\modules\module.py", line 1130, in _call_impl
        return forward_call(*input, **kwargs)
    File "C:\data\2023-pothole\down\yolov7\models\yolo.py", line 599, in forward
        return self.forward_once(x, profile)  # single-scale inference, train
    File "C:\data\2023-pothole\down\yolov7\models\yolo.py", line 625, in forward_once
        x = m(x)  # run
    File "C:\ProgramData\anaconda3\lib\site-packages\torch\nn\modules\module.py", line 1130, in _call_impl
        return forward_call(*input, **kwargs)
    File "C:\data\2023-pothole\down\yolov7\models\common.py", line 108, in forward
        return self.act(self.bn(self.conv(x)))
    File "C:\ProgramData\anaconda3\lib\site-packages\torch\nn\modules\module.py", line 1130, in _call_impl
        return forward_call(*input, **kwargs)
    File "C:\ProgramData\anaconda3\lib\site-packages\torch\nn\modules\batchnorm.py", line 168, in forward
        return F.batch_norm(
    File "C:\ProgramData\anaconda3\lib\site-packages\torch\nn\functional.py", line 2438, in batch_norm
        return torch.batch_norm(
    RuntimeError: CUDA out of memory. Tried to allocate 20.00 MiB (GPU 0; 4.00 GiB total capacity; 3.40 GiB already allocated; 0 bytes free; 3.46 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF

#

```ps
(.venv) PS C:\data\2023-pothole\down\yolov7> python 
Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch 
>>> print(torch.cuda.is_available())
False
>>>  

>>> import  torch
>>> torch.cuda.get_arch_list()
```
# cuda conda pytorch 

https://pytorch.org/get-started/locally/

https://stackoverflow.com/questions/75505217/unable-to-run-pytorch-using-gpu-windows-10

    conda uninstall pytorch
    conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cudatoolkit=11.3 -c pytorch

# labeling tools 

## labelme 

https://github.com/wkentaro/labelme#installation
