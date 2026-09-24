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

font_title = get_font(24)
font_kicker = get_font(15)
font_body = get_font(16)
font_small = get_font(13)
font_tiny = get_font(11)

def text_length(t, font):
    try:
        return draw.textlength(t, font=font)
    except Exception:
        return len(t) * font.size * 0.55

# palette
surface = '#0d1628'
surface_soft = 'rgba(148,163,184,0.08)'
text = '#f1f5f9'
muted = '#93a4bc'
primary = '#38bdf8'
accent = '#2dd4bf'
gold = '#f5b15c'
risk = '#f87171'
line = (148,163,184,46)

# sidebar
sb_w = 250
draw.rectangle([0, 0, sb_w, H], fill=surface)
draw.text((28, 28), 'SHRUNK', font=font_title, fill=text)
draw.text((28, 62), 'SOVEREIGN CLINICAL INTELLIGENCE', font=font_tiny, fill=muted)

nav_items = [
    ('Dashboard', True),
    ('Patients', False),
    ('Clinical Query', False),
    ('Patient Chat Bot', False),
    ('Doctor Chat Bot', False),
    ('Sovereign LLM', False),
    ('Teacher & Student', False),
    ('XAI', False),
    ('CEAI', False),
    ('Federated Metrics', False),
    ('Multi-User Chat', False),
    ('Architecture', False),
    ('Settings', False),
    ('Clear Database', False)
]
y = 115
for item, active in nav_items:
    if active:
        draw.rounded_rectangle([16, y, sb_w-16, y+32], radius=10, fill=(148,163,184,18))
        draw.text((34, y+7), item, font=font_small, fill=text)
    else:
        draw.text((34, y+7), item, font=font_small, fill=muted)
    y += 38

draw.rounded_rectangle([16, H-100, sb_w-16, H-30], radius=12, fill=(45,212,191,20), outline=(45,212,191,64))
draw.text((26, H-82), 'PHI-sealed on-premise node.', font=font_tiny, fill=accent)
draw.text((26, H-62), 'Patient data never leaves', font=font_tiny, fill=accent)
draw.text((26, H-42), 'this clinic.', font=font_tiny, fill=accent)

# header
header_h = 78
draw.rectangle([sb_w, 0, W, header_h], fill=(4,7,15,230))
draw.text((sb_w+28, 20), 'Clinical Intelligence Dashboard', font=font_title, fill=text)
draw.text((sb_w+28, 50), 'Lena M. · PATIENT_000092', font=font_small, fill=muted)
draw.rounded_rectangle([W-270, 20, W-40, 56], radius=8, fill=primary)
draw.text((W-250, 29), 'Run Clinical Query', font=font_small, fill='#04121a')
draw.rounded_rectangle([W-440, 20, W-290, 56], radius=8, outline=(45,212,191,90))
draw.text((W-420, 29), 'Consent: granted', font=font_small, fill=accent)

# main content
mx, my = sb_w + 28, header_h + 28
mw = W - sb_w - 56
mh = H - header_h - 56

draw.text((mx, my), 'CLINICAL INTELLIGENCE DOCUMENT', font=font_kicker, fill=accent)
draw.text((mx, my+24), 'One question, one continuous answer', font=font_title, fill=text)

# stats row
stats = [('Patients','1'),('Clinical Notes','23'),('Queries','13'),('Responses','13'),('Clinics','3'),('Logs','147')]
stat_w = (mw - (len(stats)-1)*14) // len(stats)
for i, (label, val) in enumerate(stats):
    sx = mx + i*(stat_w+14)
    sy = my + 72
    draw.rounded_rectangle([sx, sy, sx+stat_w, sy+62], radius=14, fill=surface, outline=line)
    draw.text((sx+12, sy+10), val, font=font_title, fill=primary)
    draw.text((sx+12, sy+42), label.upper(), font=font_tiny, fill=muted)

# grid of 10 mini cards
cols = 2
rows = 5
card_w = (mw - 16) // cols
card_h = (mh - 90 - 16 - 78) // rows
x = mx
y = my + 148
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
                    ly += 18
                line = word
                if ly > cy + card_h - 18:
                    return
            else:
                line = test
        if line:
            draw.text((cx, ly), line, font=font_small, fill=muted)
            ly += 20
        if ly > cy + card_h - 18:
            return

for i, (title, body) in enumerate(blocks):
    cx = x + (i % cols) * (card_w + 8)
    cy = y + (i // cols) * (card_h + 8)
    # card surface with subtle shadow
    draw.rounded_rectangle([cx+2, cy+3, cx+card_w, cy+card_h], radius=16, fill=(0,0,0,80))
    draw.rounded_rectangle([cx, cy, cx+card_w, cy+card_h], radius=16, fill=surface, outline=line)
    draw.text((cx+14, cy+12), title.upper(), font=font_tiny, fill=accent)
    draw_wrapped_text(cx+14, cy, body, card_w - 32, cy + 36)

# composite
bg.paste(img, (0,0), img)
out_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'screenshot_dashboard.png')
bg.save(out_path)
print('saved', out_path)
