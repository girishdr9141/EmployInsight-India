import os
import urllib.request
from PIL import Image, ImageDraw, ImageFont, ImageOps

def download_font(url, filename):
    # If file exists but is empty or invalid, remove it
    if os.path.exists(filename) and os.path.getsize(filename) == 0:
        os.remove(filename)
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        try:
            # Add user agent headers to prevent HTTP blocking
            req = urllib.request.Request(
                url, 
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            )
            with urllib.request.urlopen(req) as response, open(filename, 'wb') as out_file:
                out_file.write(response.read())
            print("Download successful.")
        except Exception as e:
            print(f"Failed to download font: {e}")

# Working direct download links for Montserrat from its official repository
FONT_BOLD_URL = "https://github.com/googlefonts/montserrat/raw/master/fonts/ttf/Montserrat-Bold.ttf"
FONT_MEDIUM_URL = "https://github.com/googlefonts/montserrat/raw/master/fonts/ttf/Montserrat-Medium.ttf"

download_font(FONT_BOLD_URL, "Montserrat-Bold.ttf")
download_font(FONT_MEDIUM_URL, "Montserrat-Medium.ttf")

# Use downloaded fonts or fallback to default
try:
    font_name = ImageFont.truetype("Montserrat-Bold.ttf", 64)
    font_role = ImageFont.truetype("Montserrat-Medium.ttf", 36)
    font_company = ImageFont.truetype("Montserrat-Bold.ttf", 36)
except IOError:
    print("Using default system fonts due to error loading TTF.")
    font_name = ImageFont.load_default()
    font_role = ImageFont.load_default()
    font_company = ImageFont.load_default()

# 1. Create a white canvas of size 1200 x 630 (Perfect LinkedIn Post Resolution)
canvas_width = 1200
canvas_height = 630
badge = Image.new("RGB", (canvas_width, canvas_height), "white")
draw = ImageDraw.Draw(badge)

# 2. Process profile image (circular crop)
profile_path = "profile.jpg"
if os.path.exists(profile_path):
    prof_img = Image.open(profile_path)
    
    # Crop to square from center
    w, h = prof_img.size
    min_dim = min(w, h)
    left = (w - min_dim) // 2
    top = (h - min_dim) // 2
    right = (w + min_dim) // 2
    bottom = (h + min_dim) // 2
    square_img = prof_img.crop((left, top, right, bottom))
    
    # Resize to 380x380
    size = (380, 380)
    square_img = square_img.resize(size, Image.Resampling.LANCZOS)
    
    # Create circular mask
    mask = Image.new("L", size, 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.ellipse((0, 0) + size, fill=255)
    
    # Apply mask
    circular_img = ImageOps.fit(square_img, size, centering=(0.5, 0.5))
    circular_img.putalpha(mask)
    
    # Paste circular image onto canvas
    # Position: X = 700, Y = 125 (Centered vertically)
    badge.paste(circular_img, (700, 125), circular_img)

# 3. Draw Text
text_color = (45, 55, 72) # #2d3748
accent_color = (51, 65, 85) # #334155

# Name text
name = "Girish D. R."
draw.text((100, 180), name, fill=text_color, font=font_name)

# Role text
role_y_start = 320
draw.text((100, role_y_start), "Data Science Intern", fill=text_color, font=font_role)

# Draw "at"
try:
    role_width = draw.textlength("Data Science Intern", font=font_role)
except AttributeError:
    role_width = draw.textsize("Data Science Intern", font=font_role)[0]

# Standardize alignment to match reference layout
draw.text((100, role_y_start + 45), "at", fill=text_color, font=font_role)

# Company text
company_name = "Oasis Infobyte"
company_x = 100
company_y = role_y_start + 90
draw.text((company_x, company_y), company_name, fill=text_color, font=font_company)

# Draw underline under company name
try:
    text_width = draw.textlength(company_name, font=font_company)
except AttributeError:
    text_width = draw.textsize(company_name, font=font_company)[0]

line_y = company_y + 45
draw.line((company_x, line_y, company_x + text_width, line_y), fill=text_color, width=3)

# Save the generated badge
output_path = "badge.png"
badge.save(output_path, "PNG")
print(f"Successfully generated badge saved at: {output_path}")
