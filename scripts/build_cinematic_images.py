import os
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageFont

brain_dir = '/Users/Mc/.gemini/antigravity/brain/ab458402-a66c-4673-a778-82cd347f2c88'
og_path = os.path.join(brain_dir, 'cinematic_og_banner_1790415826954.jpg')
stadium_path = os.path.join(brain_dir, 'cinematic_sports_stadium_1790415899805.jpg')
device_path = os.path.join(brain_dir, 'cinematic_firestick_setup_1790415918149.jpg')

out_guides = 'public/images/guides'
out_images = 'public/images'

os.makedirs(out_guides, exist_ok=True)
os.makedirs(out_images, exist_ok=True)

TARGET_W, TARGET_H = 1200, 630

def crop_and_resize(img, target_w=1200, target_h=630, focus_y=0.5):
    """Crop image to target aspect ratio and resize smoothly."""
    w, h = img.size
    target_ratio = target_w / target_h
    current_ratio = w / h
    
    if current_ratio > target_ratio:
        # Too wide, crop sides
        new_w = int(h * target_ratio)
        left = (w - new_w) // 2
        img_cropped = img.crop((left, 0, left + new_w, h))
    else:
        # Too tall, crop top/bottom with focus_y
        new_h = int(w / target_ratio)
        top = int((h - new_h) * focus_y)
        img_cropped = img.crop((0, top, w, top + new_h))
        
    return img_cropped.resize((target_w, target_h), Image.Resampling.LANCZOS)

def apply_vignette(img, intensity=0.4):
    """Apply a subtle dark cinematic vignette around the edges."""
    w, h = img.size
    overlay = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Outer dark border
    border = 60
    for i in range(border):
        alpha = int((1.0 - (i / border)) * intensity * 255)
        draw.rectangle([i, i, w - i - 1, h - i - 1], outline=(0, 0, 0, alpha))
        
    img_rgba = img.convert('RGBA')
    combined = Image.alpha_composite(img_rgba, overlay)
    return combined.convert('RGB')

def add_glass_badge(img, text, category="AUSTRALIA 4K", x=50, y=500):
    """Add a sleek glassmorphic badge with subtle glow for cinematic tech aesthetic."""
    img_rgba = img.convert('RGBA')
    overlay = Image.new('RGBA', img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    pad_x, pad_y = 24, 14
    box_w = 460
    box_h = 68
    
    # Frosted glass background
    draw.rounded_rectangle(
        [x, y, x + box_w, y + box_h],
        radius=14,
        fill=(10, 15, 25, 190),
        outline=(0, 240, 255, 100),
        width=2
    )
    
    # Category tag
    draw.text((x + pad_x, y + 10), category.upper(), fill=(0, 240, 255, 255))
    draw.text((x + pad_x, y + 32), text, fill=(255, 255, 255, 240))
    
    combined = Image.alpha_composite(img_rgba, overlay)
    return combined.convert('RGB')

print("Generating 1. og-banner.webp...")
base_og = Image.open(og_path)
og_banner = crop_and_resize(base_og, TARGET_W, TARGET_H, focus_y=0.45)
og_banner = apply_vignette(og_banner, 0.35)
og_banner.save(os.path.join(out_images, 'og-banner.webp'), 'WEBP', quality=92)

print("Generating 2. watch-nrl-afl-australia.webp...")
base_stadium = Image.open(stadium_path)
stadium_img = crop_and_resize(base_stadium, TARGET_W, TARGET_H, focus_y=0.5)
stadium_img = apply_vignette(stadium_img, 0.4)
stadium_img = add_glass_badge(stadium_img, "Live NRL & AFL Fixtures in Uncompressed 4K 60FPS", "LIVE SPORTS BROADCAST")
stadium_img.save(os.path.join(out_guides, 'watch-nrl-afl-australia.webp'), 'WEBP', quality=92)

print("Generating 3. aussie-sports-crisis.webp...")
# Contrast grade for sports crisis
crisis_img = crop_and_resize(base_stadium, TARGET_W, TARGET_H, focus_y=0.4)
enhancer = ImageEnhance.Color(crisis_img)
crisis_img = enhancer.enhance(1.15)
crisis_img = apply_vignette(crisis_img, 0.5)
crisis_img = add_glass_badge(crisis_img, "Overcoming Paywall Fragmentation in Australian Sports", "MARKET ANALYSIS")
crisis_img.save(os.path.join(out_guides, 'aussie-sports-crisis.webp'), 'WEBP', quality=92)

print("Generating 4. best-iptv-fire-stick-australia.webp...")
base_device = Image.open(device_path)
device_img = crop_and_resize(base_device, TARGET_W, TARGET_H, focus_y=0.45)
device_img = apply_vignette(device_img, 0.35)
device_img = add_glass_badge(device_img, "Optimized FireStick 4K Setup & Player Configuration", "HARDWARE BENCHMARK")
device_img.save(os.path.join(out_guides, 'best-iptv-fire-stick-australia.webp'), 'WEBP', quality=92)

print("Generating 5. firestick-australia-setup.webp...")
fire_setup = crop_and_resize(base_device, TARGET_W, TARGET_H, focus_y=0.35)
fire_setup = apply_vignette(fire_setup, 0.4)
fire_setup = add_glass_badge(fire_setup, "Complete Fire TV Stick Sideloading & Buffer Tuning", "STEP-BY-STEP SETUP")
fire_setup.save(os.path.join(out_guides, 'firestick-australia-setup.webp'), 'WEBP', quality=92)

print("Generating 6. downloader-firestick-steps.webp...")
dl_steps = crop_and_resize(base_device, TARGET_W, TARGET_H, focus_y=0.55)
dl_steps = apply_vignette(dl_steps, 0.4)
dl_steps = add_glass_badge(dl_steps, "Direct APK Installation via Downloader Code", "APPLICATION INSTALL")
dl_steps.save(os.path.join(out_guides, 'downloader-firestick-steps.webp'), 'WEBP', quality=92)

print("Generating 7. iptv-legal-australia.webp...")
# Legal tech grading: cool deep sapphire cyber tone
legal_img = crop_and_resize(base_og, TARGET_W, TARGET_H, focus_y=0.5)
# Tint cooler
r, g, b = legal_img.split()
r = r.point(lambda p: int(p * 0.82))
g = g.point(lambda p: int(p * 0.94))
b = b.point(lambda p: min(255, int(p * 1.15)))
legal_cool = Image.merge('RGB', (r, g, b))
legal_cool = apply_vignette(legal_cool, 0.45)
legal_cool = add_glass_badge(legal_cool, "Australian Copyright Act & Section 115A Legal Clarity", "LEGAL & COMPLIANCE")
legal_cool.save(os.path.join(out_guides, 'iptv-legal-australia.webp'), 'WEBP', quality=92)

print("Generating 8. iptv-architecture-australia.webp...")
arch_img = crop_and_resize(base_og, TARGET_W, TARGET_H, focus_y=0.35)
arch_img = apply_vignette(arch_img, 0.4)
arch_img = add_glass_badge(arch_img, "Low-Latency Edge CDN Architecture across Sydney & Melbourne", "INFRASTRUCTURE & CDN")
arch_img.save(os.path.join(out_guides, 'iptv-architecture-australia.webp'), 'WEBP', quality=92)

print("Generating 9. iptv-isp-blocking-australia.webp...")
isp_img = crop_and_resize(base_og, TARGET_W, TARGET_H, focus_y=0.6)
r, g, b = isp_img.split()
r = r.point(lambda p: int(p * 0.78))
g = g.point(lambda p: int(p * 0.92))
b = b.point(lambda p: min(255, int(p * 1.20)))
isp_cool = Image.merge('RGB', (r, g, b))
isp_cool = apply_vignette(isp_cool, 0.5)
isp_cool = add_glass_badge(isp_cool, "DNS Encryption & Australian ISP Throttling Bypass Guide", "NETWORK DEFENSE")
isp_cool.save(os.path.join(out_guides, 'iptv-isp-blocking-australia.webp'), 'WEBP', quality=92)

print("Generating 10. nbn-poi-streaming.webp...")
nbn_img = crop_and_resize(base_og, TARGET_W, TARGET_H, focus_y=0.4)
nbn_img = apply_vignette(nbn_img, 0.45)
nbn_img = add_glass_badge(nbn_img, "Direct NBN Point of Interconnect (POI) Peering Analysis", "AUSTRALIAN NBN TELEMETRY")
nbn_img.save(os.path.join(out_guides, 'nbn-poi-streaming.webp'), 'WEBP', quality=92)

print("Generating 11. iptv-setup-steps.webp...")
steps_img = crop_and_resize(base_device, TARGET_W, TARGET_H, focus_y=0.4)
steps_img = apply_vignette(steps_img, 0.4)
steps_img = add_glass_badge(steps_img, "Step 1: Choose Plan -> Step 2: Install App -> Step 3: Stream 4K", "QUICK ACTIVATION")
steps_img.save(os.path.join(out_guides, 'iptv-setup-steps.webp'), 'WEBP', quality=92)

print("ALL CINEMATIC IMAGES CREATED SUCCESSFULLY!")
