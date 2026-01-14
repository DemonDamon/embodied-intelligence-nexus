import torch
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import torchvision.transforms as transforms
import os

def linear_beta_schedule(timesteps):
    beta_start = 0.0001
    beta_end = 0.02
    return torch.linspace(beta_start, beta_end, timesteps)

T = 1000
betas = linear_beta_schedule(timesteps=T)
alphas = 1. - betas
alphas_cumprod = torch.cumprod(alphas, axis=0)
sqrt_alphas_cumprod = torch.sqrt(alphas_cumprod)
sqrt_one_minus_alphas_cumprod = torch.sqrt(1. - alphas_cumprod)

def q_sample(x_start, t, noise=None):
    if noise is None:
        noise = torch.randn_like(x_start)
    sqrt_alpha_bar_t = sqrt_alphas_cumprod[t]
    sqrt_one_minus_alpha_bar_t = sqrt_one_minus_alphas_cumprod[t]
    return sqrt_alpha_bar_t * x_start + sqrt_one_minus_alpha_bar_t * noise

def load_image(path, size=128):
    if not os.path.exists(path):
        raise FileNotFoundError(f"找不到文件：{path}，请检查路径是否正确。")
    img = Image.open(path).convert("RGB")   # (Height, Width, Channel)
    transform = transforms.Compose([
        transforms.Resize((size, size)),
        transforms.ToTensor(),   # Normalization + Permutation ([0.0, 1.0], (C, H, W))
        transforms.Lambda(lambda t: (t * 2) - 1)   # [-1, 1]
    ])
    return transform(img)

local_path = "demo.jpg"
try:
    x_0 = load_image(local_path)
    print("图片加载成功！")
except Exception as e:
    print(f"出错啦：{e}")

def show_tensor_image(image_tensor):
    reverse_transform = transforms.Compose([
        transforms.Lambda(lambda t: (t + 1) / 2),
        transforms.Lambda(lambda t: t.permute(1, 2, 0)),
        transforms.Lambda(lambda t: t * 255.),
        transforms.Lambda(lambda t: t.numpy().astype(np.uint8)),
    ])
    return reverse_transform(image_tensor)

time_steps_to_show = [0, 50, 100, 200, 500, 999]
plt.figure(figsize=(15, 3))

noise = torch.randn_like(x_0)

for i, t in enumerate(time_steps_to_show):
    if t == 0:
        noisy_img = x_0
    else:
        noisy_img = q_sample(x_0, t = torch.tensor(t), noise=noise)
    ax = plt.subplot(1, len(time_steps_to_show), i + 1)
    plt.imshow(show_tensor_image(noisy_img))
    plt.title(f"t = {t}")
    plt.axis("off")

plt.tight_layout()
plt.show()