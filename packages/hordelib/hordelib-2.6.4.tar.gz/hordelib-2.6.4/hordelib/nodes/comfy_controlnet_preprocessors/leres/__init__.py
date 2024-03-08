import cv2
import numpy as np
import torch
import os

# from modules import devices, shared
from torchvision.transforms import transforms

# AdelaiDepth/LeReS imports
from .leres.depthmap import estimateleres, estimateboost
from .leres.multi_depth_model_woauxi import RelDepthModel
from .leres.net_tools import strip_prefix_if_present

# pix2pix/merge net imports
# from .pix2pix.options.test_options import TestOptions
# from .pix2pix.models.pix2pix4depth_model import Pix2Pix4DepthModel

import builtins

old_modeldir = os.path.dirname(os.path.realpath(__file__))
import model_management

# remote_model_path_leres = "https://cloudstor.aarnet.edu.au/plus/s/lTIJF4vrvHCAI31/download"
remote_model_path_leres = (
    "https://huggingface.co/lllyasviel/Annotators/resolve/1e70a29f5d06c27d37988d2c6c43f6fd21fdb2d1/res101.pth"
)
remote_model_path_pix2pix = "https://sfu.ca/~yagiz/CVPR21/latest_net_G.pth"

model = None
pix2pixmodel = None


def unload_leres_model():
    global model, pix2pixmodel
    if model is not None:
        model = model.cpu()
    if pix2pixmodel is not None:
        pix2pixmodel = pix2pixmodel.unload_network("G")


def download_model_if_not_existed():
    model_path = os.path.join(builtins.annotator_ckpts_path, "res101.pth")
    # old_model_path = os.path.join(old_modeldir, "res101.pth")

    # if os.path.exists(old_model_path):
    #    model_path = old_model_path
    if not os.path.exists(model_path):
        from hordelib.nodes.comfy_controlnet_preprocessors.util import load_file_from_url

        load_file_from_url(remote_model_path_leres, model_dir=builtins.annotator_ckpts_path)
        os.rename(os.path.join(builtins.annotator_ckpts_path, "res101.pth"), model_path)
    return model_path


def apply_leres(input_image, thr_a, thr_b):
    global model, pix2pixmodel
    # boost = shared.opts.data.get("control_net_monocular_depth_optim", False)
    boost = False  # Too lazy to implement this to ComfyUI
    if model is None:
        model_path = download_model_if_not_existed()
        checkpoint = torch.load(model_path, map_location=torch.device(model_management.get_torch_device()))
        model = RelDepthModel(backbone="resnext101").to(model_management.get_torch_device())
        model.load_state_dict(strip_prefix_if_present(checkpoint["depth_model"], "module."), strict=True)
        del checkpoint

    """ if boost and pix2pixmodel is None:
        pix2pixmodel_path = os.path.join(builtins.annotator_ckpts_path, "latest_net_G.pth")
        if not os.path.exists(pix2pixmodel_path):
            from hordelib.nodes.comfy_controlnet_preprocessors.util import load_file_from_url
            load_file_from_url(remote_model_path_pix2pix, model_dir=builtins.annotator_ckpts_path)

        opt = TestOptions().parse()
        if not torch.cuda.is_available():
            opt.gpu_ids = [] # cpu mode
        pix2pixmodel = Pix2Pix4DepthModel(opt)
        pix2pixmodel.save_dir = builtins.annotator_ckpts_path
        pix2pixmodel.load_networks('latest')
        pix2pixmodel.eval() """

    # if devices.get_device_for("controlnet").type != 'mps':
    # model = model.to(devices.get_device_for("controlnet"))

    assert input_image.ndim == 3
    height, width, dim = input_image.shape

    with torch.no_grad():
        if boost:
            depth = estimateboost(input_image, model, 0, pix2pixmodel, max(width, height))
        else:
            depth = estimateleres(input_image, model, width, height)

        numbytes = 2
        depth_min = depth.min()
        depth_max = depth.max()
        max_val = (2 ** (8 * numbytes)) - 1

        # check output before normalizing and mapping to 16 bit
        if depth_max - depth_min > np.finfo("float").eps:
            out = max_val * (depth - depth_min) / (depth_max - depth_min)
        else:
            out = np.zeros(depth.shape)

        # single channel, 16 bit image
        depth_image = out.astype("uint16")

        # convert to uint8
        depth_image = cv2.convertScaleAbs(depth_image, alpha=(255.0 / 65535.0))

        # remove near
        if thr_a != 0:
            thr_a = thr_a * 255
            depth_image = cv2.threshold(depth_image, thr_a, 255, cv2.THRESH_TOZERO)[1]

        # invert image
        depth_image = cv2.bitwise_not(depth_image)

        # remove bg
        if thr_b != 0:
            thr_b = thr_b * 255
            depth_image = cv2.threshold(depth_image, thr_b, 255, cv2.THRESH_TOZERO)[1]

        return depth_image
