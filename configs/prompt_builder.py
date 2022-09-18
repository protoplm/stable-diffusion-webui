import yaml
import itertools  


with open('CLI-config.yaml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

# First word into every prompt
subject = 'fish'

# Values to be shuffled and repeated with every possible combinaton including blanks but no repeats of the same word
values = ['red','yellow','blue']


list_values = []

for i in range(0,len(values)+1):
    list_values.extend(list(itertools.permutations(values,i)))

new_list = []

for tup in list_values:
    new_list.append(list( (subject,) + tup ))
 
prompt_list = []
for i in new_list:
    prompt_list.append(', '.join(i))

print(len(prompt_list))

target = 'txt2img'
toggles = [1,2,3,4,5,7]

seed = 911
sampler_name = 'k_euler_a'
prompt = new_list
steps = 50
n_iter = 5
cfg_scale = 15

config['prompt'] = prompt_list
config['seed'] = seed
config['toggles'] = toggles

with open('python-config.yaml', 'w') as file:
    documents = yaml.dump(config, file)



# target: target
# prompt: prompt
# ddim_steps: steps
# sampler_name: sampler_name
# # Adding an int to toggles enables the corresponding feature.
#   # 0: Create prompt matrix (separate multiple prompts using |, and get all combinations of them)
#   # 1: Normalize Prompt Weights (ensure sum of weights add up to 1.0)
#   # 2: Save individual images
#   # 3: Save grid
#   # 4: Sort samples by prompt
#   # 5: Write sample info files
#   # 6: jpg samples
#   # 7: Fix faces using GFPGAN
#   # 8: Upscale images using Real-ESRGAN
# toggles: toggles
# ddim_eta: 0.0  # legacy name, applies to all algorithms.
# n_iter: n_iter
# batch_size: 1
# cfg_scale: cfg_scale
# # Leave blank for random seed:
# seed: seed
# height: 512
# width: 512
# fp:
# realesrgan_model_name: 'RealESRGAN_x4plus'
# variant_amount: 0