import time

tokenizer, model, image_processor, context_len = None, None, None, None

def image_prompt(image_file, prompt):
    from transformers import AutoModelForCausalLM, AutoTokenizer
    from PIL import Image

    model_id = "vikhyatk/moondream2"
    revision = "2024-03-05"
    model = AutoModelForCausalLM.from_pretrained(
        model_id, trust_remote_code=True, revision=revision
    )
    tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)

    t0 = time.time()
    image = Image.open(image_file)
    enc_image = model.encode_image(image)
    resp = model.answer_question(enc_image, prompt, tokenizer)
    t1 = time.time()
    print(t1-t0)
    return resp

def llava_image_prompt(image_file, prompt):
    from llava.model.builder import load_pretrained_model
    from llava.mm_utils import get_model_name_from_path
    from llava.eval.run_llava import eval_model

    global tokenizer
    global model
    global image_processor
    global context_len

    model_path = "liuhaotian/llava-v1.5-7b"
    ##model_path = "liuhaotian/llava-v1.5-13b"
    #model_path = "TheBloke/llava-v1.5-13B-AWQ"

    if tokenizer is None:
        tokenizer, model, image_processor, context_len = load_pretrained_model(
            model_path=model_path,
            model_base=None,
            model_name=get_model_name_from_path(model_path)
        )

    t0 = time.time()
    args = type('Args', (), {
        "model_path": model_path,
        "model_base": None,
        "model_name": get_model_name_from_path(model_path),
        "query": prompt,
        "conv_mode": None,
        "image_file": image_file,
        "sep": ",",
        "temperature": 0,
        "top_p": None,
        "num_beams": 1,
        "max_new_tokens": 512
    })()

    result = eval_model(args)
    t1 = time.time()
    print(t1-t0)
    return result
