from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1600, 900
bg = Image.new('RGB', (W, H), '#04070f')
img = Image.new('RGBA', (W, H), (0,0,0,0))
draw = ImageDraw.Draw(img)

# fonts
font_path = "C:/Windows/Fonts/segoeui.ttf"
if not os.path.exists(font_path):
    font_path = None

def get_font(size):
    try:
        return ImageFont.truetype(font_path, size)
    except Exception:
        return ImageFont.load_default()

font_title = get_font(26)
font_kicker = get_font(16)
font_body = get_font(18)
font_small = get_font(14)
font_tiny = get_font(12)

def text_length(t, font):
    try:
        return draw.textlength(t, font=font)
    except Exception:
        return len(t) * font.size * 0.55

# sidebar
sb_w = 240
draw.rectangle([0, 0, sb_w, H], fill='#0d1628')
draw.text((30, 30), 'SHRUNK', font=font_title, fill='#f1f5f9')
draw.text((30, 66), 'SOVEREIGN CLINICAL INTELLIGENCE', font=font_tiny, fill='#93a4bc')
nav = ['Overview', 'Clinical Intelligence', 'Patient Chat', 'XAI', 'CEAI', 'Federation']
y = 130
for item in nav:
    if item == 'Clinical Intelligence':
        draw.rounded_rectangle([20, y, sb_w-20, y+36], radius=10, fill=(148,163,184,20))
    draw.text((34, y+8), item, font=font_small, fill='#f1f5f9' if item=='Clinical Intelligence' else '#93a4bc')
    y += 46
draw.rounded_rectangle([20, H-110, sb_w-20, H-30], radius=12, fill=(45,212,191,20), outline=(45,212,191,64))
draw.text((30, H-90), 'PHI-sealed on-premise node.', font=font_tiny, fill='#2dd4bf')
draw.text((30, H-68), 'Patient data never leaves', font=font_tiny, fill='#2dd4bf')
draw.text((30, H-46), 'this clinic.', font=font_tiny, fill='#2dd4bf')

# header
header_h = 80
draw.rectangle([sb_w, 0, W, header_h], fill=(4,7,15,255))
draw.text((sb_w+30, 22), 'Clinical Intelligence Dashboard', font=font_title, fill='#f1f5f9')
draw.text((sb_w+30, 54), 'Lena M. · PATIENT_000092', font=font_small, fill='#93a4bc')
draw.rounded_rectangle([W-260, 22, W-40, 58], radius=8, fill='#2dd4bf')
draw.text((W-240, 30), 'Run Clinical Query', font=font_small, fill='#04121a')
draw.rounded_rectangle([W-430, 22, W-280, 58], radius=8, outline=(148,163,184,72))
draw.text((W-410, 30), 'Consent: granted', font=font_small, fill='#2dd4bf')

# main content
mx, my = sb_w + 30, header_h + 30
mw = W - sb_w - 60
mh = H - header_h - 60

draw.text((mx, my), 'CLINICAL INTELLIGENCE DOCUMENT', font=font_kicker, fill='#2dd4bf')
draw.text((mx, my+26), 'One question, one continuous answer', font=font_title, fill='#f1f5f9')

# grid of 10 mini cards
cols = 2
rows = 5
card_w = (mw - 20) // cols
card_h = (mh - 100 - 20) // rows
x = mx
y = my + 80
blocks = [
    ('Clinical Question', 'What is the overall clinical picture and what should I do next?'),
    ('Retrieved Evidence', '• NOTE_000092_002: passive SI, sleep 4.5h\n• NOTE_000092_007: stopped Sertraline\n• CHAT_000092_014: worse on Tuesdays'),
    ('Patient-Specific Summary', 'Lena has recurrent MDD with moderate current risk. Medication non-adherence and sleep deterioration.'),
    ('Clinical Interpretation', 'Relapse precipitated by work stress and medication non-adherence. Prior Bupropion response is protective.'),
    ('Clinical Evaluation', 'Triage: moderate · Diagnosis: MDD recurrent · Plan: consider Bupropion XL + sleep hygiene.'),
    ('Uncertainty / Missing', 'No recent labs; Zurich medication history pending consent.'),
    ('Safety Considerations', 'Passive SI without plan. Sleep <5h warning. Follow-up within 48–72h.'),
    ('Recommended Review', '1) Discuss Bupropion switch  2) Request Zurich consent  3) Sleep/stress check-in'),
    ('Clinical Workflow', 'Onboarded 2025-11 · 14 notes · 23 chat entries · 1 pending consent.'),
    ('Sources', 'NOTE_000092_002, NOTE_000092_007, CHAT_000092_014, EPD_SUMMARY_000092')
]
for i, (title, body) in enumerate(blocks):
    cx = x + (i % cols) * (card_w + 10)
    cy = y + (i // cols) * (card_h + 10)
    draw.rounded_rectangle([cx, cy, cx+card_w, cy+card_h], radius=14, fill='#0d1628', outline=(148,163,184,46))
    draw.text((cx+16, cy+14), title.upper(), font=font_tiny, fill='#2dd4bf')
    words = body.split(' ')
    line = ''
    ly = cy + 38
    for word in words:
        test = line + ' ' + word if line else word
        if text_length(test, font_small) > card_w - 36:
            draw.text((cx+16, ly), line, font=font_small, fill='#93a4bc')
            line = word
            ly += 20
            if ly > cy + card_h - 20:
                break
        else:
            line = test
    if line and ly <= cy + card_h - 20:
        draw.text((cx+16, ly), line, font=font_small, fill='#93a4bc')

# composite
bg.paste(img, (0,0), img)
bg.save('screenshot.png')
print('saved screenshot.png')
