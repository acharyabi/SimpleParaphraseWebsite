from django.shortcuts import render
from transformers import AutoTokenizer
from joblib import load

# model= load('C:\\Users\\yoges\\Desktop\\py_projects\\DeployMajor\\md.joblib')

# def generate_paraphrase(question1):
#     tokenizer_name = "google/mt5-small"
#     tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
#     inputs_encoding =  tokenizer(
#             question1,
#             add_special_tokens=True,
#             max_length= 256,
#             padding = 'max_length',
#             truncation=True,
#             return_attention_mask=True,
#             return_tensors="pt"
#             )
#     generate_ids = model.generate(
#         input_ids = inputs_encoding["input_ids"],
#         attention_mask = inputs_encoding["attention_mask"],
#         do_sample=True,
#         max_length=64,
#         top_k=50,
#         top_p=0.95,
#         early_stopping=True,
#         num_return_sequences =1,
#         no_repeat_ngram_size=2,
#         )
#     preds = [
#         tokenizer.decode(gen_id,
#         skip_special_tokens=True, 
#         clean_up_tokenization_spaces=True)
#         for gen_id in generate_ids
#     ]

#     return "".join(preds)

# Create your views here.
def generate_text(request):
    if request.method == 'POST':
        input_text = request.POST.get('input-text')
        # TODO: Generate output text using Quillbot
        if input_text:
        # Do something with the input text to generate the output text
            output_text = "I am Abinash"
            # "generate_paraphrase(input_text)"
        else:
            output_text = None
        return render(request, 'paraphrasing/form.html', { 'output_text': output_text, 'input_text': input_text})
    else:
        return render(request, 'paraphrasing/form.html')