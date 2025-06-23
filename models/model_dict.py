from models.segment_anything.build_sam import sam_model_registry
from models.segment_anything_samus.build_sam_us import samus_model_registry
from models.segment_anything_samus_autoprompt.build_samus import autosamus_model_registry
# from models.samed.build_samed import sam_model_registry
# import models.samed.sam_lora_image_encoder as lora 


def get_model(modelname="SAM", input_size=256, ckpt=None, opt=None, lora_cpt=None):
    if modelname == "SAM":
        model = sam_model_registry['vit_b'](checkpoint=ckpt)
    elif modelname == "SAMUS":
        model = samus_model_registry['vit_b'](input_size, checkpoint=ckpt)
    # elif modelname == "SAMed":
    #     sam, _ = sam_model_registry['vit_h'](input_size, num_classes=8, 
    #                                           checkpoint=ckpt, pixel_mean=[0, 0, 0],
    #                                           pixel_std=[1, 1, 1])
    #     model = lora.LoRA_Sam(sam, 4).cuda()
    #     model.load_lora_parameters(lora_cpt)
    elif modelname == "AutoSAMUS":
        model = autosamus_model_registry['vit_b'](input_size, checkpoint=opt.load_path)
    else:
        raise RuntimeError("Could not find the model:", modelname)
    return model
