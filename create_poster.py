import qrcode
from PIL import Image, ImageDraw, ImageFont

def create_poster(url):
    """Create a QR code poster for the student app"""
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    # Create poster
    poster_width = 800
    poster_height = 1000
    poster = Image.new('RGB', (poster_width, poster_height), 'white')
    draw = ImageDraw.Draw(poster)
    
    # Add title
    title_text = "IEEE NEXUS 2026"
    subtitle_text = "Lunch Token Generator"
    instruction_text = "Scan QR Code to Get Your Lunch Token"
    
    # Resize QR code
    qr_size = 500
    qr_img = qr_img.resize((qr_size, qr_size))
    
    # Paste QR code in center
    qr_position = ((poster_width - qr_size) // 2, 250)
    poster.paste(qr_img, qr_position)
    
    # Add text (using default font)
    try:
        title_font = ImageFont.truetype("arial.ttf", 60)
        subtitle_font = ImageFont.truetype("arial.ttf", 40)
        instruction_font = ImageFont.truetype("arial.ttf", 30)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        instruction_font = ImageFont.load_default()
    
    # Draw title
    title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    draw.text(((poster_width - title_width) // 2, 50), title_text, fill='black', font=title_font)
    
    # Draw subtitle
    subtitle_bbox = draw.textbbox((0, 0), subtitle_text, font=subtitle_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    draw.text(((poster_width - subtitle_width) // 2, 130), subtitle_text, fill='#0066cc', font=subtitle_font)
    
    # Draw instruction
    instruction_bbox = draw.textbbox((0, 0), instruction_text, font=instruction_font)
    instruction_width = instruction_bbox[2] - instruction_bbox[0]
    draw.text(((poster_width - instruction_width) // 2, 800), instruction_text, fill='black', font=instruction_font)
    
    # Add URL at bottom
    url_text = f"Or visit: {url}"
    url_bbox = draw.textbbox((0, 0), url_text, font=instruction_font)
    url_width = url_bbox[2] - url_bbox[0]
    draw.text(((poster_width - url_width) // 2, 900), url_text, fill='gray', font=instruction_font)
    
    # Save
    poster.save('lunch_poster.png')
    print("✅ Poster created: lunch_poster.png")
    print(f"📱 Student App URL: {url}")

if __name__ == "__main__":
    # Change this to your deployed URL or local IP
    app_url = "http://localhost:8501"  # Change after deployment
    
    print("🎨 Creating QR Code Poster...")
    print(f"URL: {app_url}")
    print()
    
    create_poster(app_url)
    
    print()
    print("📋 Next Steps:")
    print("1. Deploy student_app.py to Streamlit Cloud")
    print("2. Update app_url in this script with your deployed URL")
    print("3. Run this script again to generate final poster")
    print("4. Print lunch_poster.png and place near canteen")
