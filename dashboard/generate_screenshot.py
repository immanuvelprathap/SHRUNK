from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1600, 900
bg = Image.new('RGB', (W, H), '#04070f')

# subtle pitch-deck-style radial gradient on the background
grad = Image.new('RGBA', (W, H), (0,0,0,0))
gdraw = ImageDraw.Draw(grad)
gdraw.ellipse([-W, -H//2, W, H*1.5], fill=(56,189,248,18))
gdraw.ellipse([W//2, H//2, W*2, H*2], fill=(45,212,191,16))
bg.paste(grad, (0,0), grad)

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
surface = '#0d1628'
text = '#f1f5f9'
muted = '#93a4bc'
primary = '#38bdf8'
accent = '#2dd4bf'
draw.rectangle([0, 0, sb_w, H], fill=surface)
draw.text((30, 30), 'SHRUNK', font=font_title, fill=text)
draw.text((30, 66), 'SOVEREIGN CLINICAL INTELLIGENCE', font=font_tiny, fill=muted)
nav = ['Overview', 'Clinical Intelligence', 'Patient Chat', 'XAI', 'CEAI', 'Federation']
y = 130
for item in nav:
    if item == 'Clinical Intelligence':
        draw.rounded_rectangle([20, y, sb_w-20, y+36], radius=10, fill=(148,163,184,18))
    draw.text((34, y+8), item, font=font_small, fill=text if item=='Clinical Intelligence' else muted)
    y += 46
draw.rounded_rectangle([20, H-110, sb_w-20, H-30], radius=12, fill=(45,212,191,20), outline=(45,212,191,64))
draw.text((30, H-90), 'PHI-sealed on-premise node.', font=font_tiny, fill=accent)
draw.text((30, H-68), 'Patient data never leaves', font=font_tiny, fill=accent)
draw.text((30, H-46), 'this clinic.', font=font_tiny, fill=accent)

# header
header_h = 80
draw.rectangle([sb_w, 0, W, header_h], fill=(4,7,15,230))
draw.text((sb_w+30, 22), 'Clinical Intelligence Dashboard', font=font_title, fill=text)
draw.text((sb_w+30, 54), 'Lena M. · PATIENT_000092', font=font_small, fill=muted)
draw.rounded_rectangle([W-260, 22, W-40, 58], radius=8, fill=primary)
draw.text((W-240, 30), 'Run Clinical Query', font=font_small, fill='#04121a')
draw.rounded_rectangle([W-430, 22, W-280, 58], radius=8, outline=(45,212,191,90))
draw.text((W-410, 30), 'Consent: granted', font=font_small, fill=accent)

# main content
mx, my = sb_w + 30, header_h + 30
mw = W - sb_w - 60
mh = H - header_h - 60

draw.text((mx, my), 'CLINICAL INTELLIGENCE DOCUMENT', font=font_kicker, fill=accent)
draw.text((mx, my+26), 'One question, one continuous answer', font=font_title, fill=text)

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
def draw_wrapped_text(cx, cy, body, max_w, start_y):
    ly = start_y
    paragraphs = body.split('\n')
    for para in paragraphs:
        words = para.split(' ')
        line = ''
        for word in words:
            test = line + ' ' + word if line else word
            if text_length(test, font_small) > max_w:
                if line:
                    draw.text((cx, ly), line, font=font_small, fill=muted)
                    ly += 20
                line = word
                if ly > cy + card_h - 20:
                    return
            else:
                line = test
        if line:
            draw.text((cx, ly), line, font=font_small, fill=muted)
            ly += 22
        if ly > cy + card_h - 20:
            return

for i, (title, body) in enumerate(blocks):
    cx = x + (i % cols) * (card_w + 10)
    cy = y + (i // cols) * (card_h + 10)
    # card surface with subtle shadow
    draw.rounded_rectangle([cx+2, cy+3, cx+card_w, cy+card_h], radius=18, fill=(0,0,0,80))
    draw.rounded_rectangle([cx, cy, cx+card_w, cy+card_h], radius=18, fill=surface, outline=(148,163,184,46))
    draw.text((cx+16, cy+14), title.upper(), font=font_tiny, fill=accent)
    draw_wrapped_text(cx+16, cy, body, card_w - 36, cy + 40)

# composite
bg.paste(img, (0,0), img)
out_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'screenshot_dashboard.png')
bg.save(out_path)
print('saved', out_path)
