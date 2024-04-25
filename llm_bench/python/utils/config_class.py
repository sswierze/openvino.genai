# -*- coding: utf-8 -*-
# Copyright (C) 2023-2024 Intel Corporation
# SPDX-License-Identifier: Apache-2.0
from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM, T5ForConditionalGeneration, BlenderbotForConditionalGeneration, AutoModel
from diffusers.pipelines import DiffusionPipeline, LDMSuperResolutionPipeline
from optimum.intel.openvino import (
    OVModelForCausalLM,
    OVModelForSeq2SeqLM,
    OVStableDiffusionPipeline,
    OVLatentConsistencyModelPipeline,
    OVStableDiffusionXLPipeline
)
from utils.ov_model_classes import OVMPTModel, OVLDMSuperResolutionPipeline, OVChatGLMModel

TOKENIZE_CLASSES_MAPPING = {
    'decoder': AutoTokenizer,
    'mpt': AutoTokenizer,
    't5': AutoTokenizer,
    'blenderbot': AutoTokenizer,
    'falcon': AutoTokenizer,
}

OV_MODEL_CLASSES_MAPPING = {
    'decoder': OVModelForCausalLM,
    't5': OVModelForSeq2SeqLM,
    'blenderbot': OVModelForSeq2SeqLM,
    'falcon': OVModelForCausalLM,
    'mpt': OVMPTModel,
    'stable-diffusion-xl': OVStableDiffusionXLPipeline,
    'sdxl': OVStableDiffusionXLPipeline,
    'lcm-sdxl': OVStableDiffusionXLPipeline,
    'ssd-': OVStableDiffusionXLPipeline,
    'lcm-ssd-': OVStableDiffusionXLPipeline,
    'stable_diffusion': OVStableDiffusionPipeline,
    'lcm': OVLatentConsistencyModelPipeline,
    'replit': OVMPTModel,
    'codet5': OVModelForSeq2SeqLM,
    'codegen2': OVModelForCausalLM,
    'ldm_super_resolution': OVLDMSuperResolutionPipeline,
    'chatglm2': OVModelForCausalLM,
    'chatglm3': OVModelForCausalLM,
    'chatglm': OVChatGLMModel,
}

PT_MODEL_CLASSES_MAPPING = {
    'decoder': AutoModelForCausalLM,
    't5': T5ForConditionalGeneration,
    'blenderbot': BlenderbotForConditionalGeneration,
    'mpt': AutoModelForCausalLM,
    'falcon': AutoModelForCausalLM,
    'stable_diffusion': DiffusionPipeline,
    'ldm_super_resolution': LDMSuperResolutionPipeline,
    'chatglm': AutoModel,
}

USE_CASES = {
    'image_gen': ['stable-diffusion-', 'ssd-', 'deepfloyd-if', 'tiny-sd', 'small-sd', 'lcm-', 'sdxl'],
    'text2speech': ['whisper'],
    'image_cls': ['vit'],
    'code_gen': ['replit', 'codegen2', 'codegen', 'codet5', "stable-code"],
    'text_gen': [
        'decoder',
        't5',
        'falcon',
        'gpt-',
        'gpt2',
        'aquila',
        'mpt',
        'open-llama',
        'openchat',
        'neural-chat',
        'llama',
        'tiny-llama',
        'tinyllama',
        'opt-',
        'pythia-',
        'stablelm-',
        'stable-zephyr-',
        'rocket-',
        'blenderbot',
        'vicuna',
        'dolly',
        'bloom',
        'red-pajama',
        'chatglm',
        'xgen',
        'longchat',
        'jais',
        'orca-mini',
        'baichuan',
        'qwen',
        'zephyr',
        'mistral',
        'mixtral',
        'yi-',
        'phi-',
        'phi2-',
        'minicpm',
        'gemma',
        "deci",
        "internlm"
    ],
    'ldm_super_resolution': ['ldm-super-resolution'],
}

DEFAULT_MODEL_CLASSES = {
    'text_gen': 'decoder',
    'image_gen': 'stable_diffusion',
    'image_cls': 'vit',
    'speech2text': 'whisper',
    'code_gen': 'decoder',
    'ldm_super_resolution': 'ldm_super_resolution',
}
