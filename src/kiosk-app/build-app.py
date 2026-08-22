#!/usr/bin/env python3
"""Build the Concurrent 3280 docent-kiosk concept-review app as a single
self-contained index.html. The live screen is composited into the full cabinet
render (a thumbnail); clicking the screen opens it full-size and readable."""
import base64, mimetypes, pathlib

HERE = pathlib.Path(__file__).parent
A = HERE / "assets"

def uri(rel):
    p = A / rel
    mime = mimetypes.guess_type(p.name)[0] or "image/jpeg"
    b64 = base64.b64encode(p.read_bytes()).decode()
    return f"data:{mime};base64,{b64}"

IMG = {
    "__SHELL__":    uri("renders/shell.jpg"),
    "__MACHINE__":  uri("renders/machine.jpg"),
    "__INTERIOR__": uri("renders/interior-open.jpg"),
    "__KIOSK__":    uri("renders/kiosk-concept.jpg"),
    "__RADAR__":    uri("renders/radar.jpg"),
    "__NJPLANT__":  uri("renders/njplant.jpg"),
    "__YEAGER__":   uri("renders/yeager.jpg"),
    "__R10000__":   uri("renders/r10000.jpg"),
    "__M_WEATHER__":uri("mont/weather.jpg"),
    "__M_SPACE__":  uri("mont/space.jpg"),
    "__M_DEFENSE__":uri("mont/defense.jpg"),
    "__M_FINANCE__":uri("mont/finance.jpg"),
    "__LOGO__":     uri("renders/vcf-logo.png"),
}

HTML = r"""<title>3280 Docent Kiosk</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=Archivo:wght@500;600;700&family=Newsreader:ital,wght@0,400;0,500;0,600;1,400&family=Space+Mono:wght@400;700&display=swap">
<style>
:root{
  --bg:#ECE6DA; --bg2:#E3DBCB; --panel:#F7F3EA; --ink:#221F19; --muted:#6C6558;
  --line:#D8CFBE; --accent:#12305F; --accent2:#C0501C; --gold:#9C7529;
  --shadow:rgba(40,32,18,.24);
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --bg:#161513; --bg2:#0F0E0D; --panel:#201E1B; --ink:#ECE6D9; --muted:#9A9184;
    --line:#332F29; --accent:#7FA0DB; --accent2:#E2782F; --gold:#D7A94E;
    --shadow:rgba(0,0,0,.55);
  }
}
:root[data-theme="dark"]{
  --bg:#161513; --bg2:#0F0E0D; --panel:#201E1B; --ink:#ECE6D9; --muted:#9A9184;
  --line:#332F29; --accent:#7FA0DB; --accent2:#E2782F; --gold:#D7A94E;
  --shadow:rgba(0,0,0,.55);
}
/* live screen paper — matches render glass; constant in both themes */
:root{ --screen:#E9E2D0; --screen-ink:#282419; --screen-mut:#6f6753;
  --screen-accent:#123A6b; --screen-gold:#8f6413; --screen-line:#cdbf9f; }
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font-family:"Newsreader",Georgia,serif;
  line-height:1.55;background-image:radial-gradient(120% 80% at 50% -12%,var(--bg) 0%,var(--bg2) 100%);
  min-height:100vh}
.wrap{max-width:1060px;margin:0 auto;padding:clamp(22px,5vw,52px) clamp(16px,4vw,40px) 72px}

.eyebrow{font-family:"Oswald",sans-serif;text-transform:uppercase;letter-spacing:.28em;
  font-size:12px;font-weight:600;color:var(--accent)}
.mast{border-bottom:1px solid var(--line);padding-bottom:24px;margin-bottom:clamp(24px,4vw,38px)}
.mast h1{font-family:"Newsreader",serif;font-weight:600;font-size:clamp(28px,5.6vw,50px);
  line-height:1.03;letter-spacing:-.015em;margin:.28em 0 .18em;text-wrap:balance}
.mast p.dek{margin:0;max-width:46ch;color:var(--muted);font-size:clamp(15px,2.1vw,18px)}

/* ---- the installation (thumbnail) ---- */
.stage{display:flex;flex-direction:column;align-items:center;gap:14px}
.install{position:relative;width:min(88vw,470px);aspect-ratio:598/1268;
  background:url("__SHELL__") center/100% 100% no-repeat;border-radius:6px;
  box-shadow:0 34px 74px -30px var(--shadow),0 12px 26px -18px var(--shadow);
  -webkit-user-select:none;user-select:none}

/* CONCEPT marker — this is the guiding-light concept, not the built piece.
   Kept on the cabinet render and the enlarged view so no screenshot loses it. */
.cbadge{position:absolute;z-index:20;top:10px;left:10px;pointer-events:none;
  font-family:"Oswald",sans-serif;font-weight:600;font-size:12px;letter-spacing:.22em;
  text-transform:uppercase;color:#f6dc8c;background:rgba(20,16,9,.72);
  border:1px solid rgba(246,220,140,.55);border-radius:3px;padding:5px 10px 4px;
  box-shadow:0 2px 10px -4px rgba(0,0,0,.6)}

/* base screen surface — shared by the inline thumbnail and the enlarged modal */
.display{position:relative;container-type:inline-size;overflow:hidden;
  background:var(--screen);color:var(--screen-ink);border-radius:2px;
  font-family:"Archivo",-apple-system,BlinkMacSystemFont,sans-serif}
.install .display{position:absolute;left:30.9%;top:19.2%;width:38.5%;height:41.7%;
  cursor:zoom-in;box-shadow:0 0 0 1px rgba(0,0,0,.12) inset}
.zoomtag{position:absolute;top:3.2cqw;right:3.2cqw;z-index:8;width:8.4cqw;height:8.4cqw;
  border-radius:50%;background:rgba(20,16,9,.5);display:grid;place-items:center;pointer-events:none}
.zoomtag svg{width:5cqw;height:5cqw;stroke:#f2ecda;stroke-width:2.2;fill:none;stroke-linecap:round}
.counter{position:absolute;right:4.5cqw;bottom:3.4cqw;font-family:"Space Mono",monospace;
  font-size:clamp(8px,3.1cqw,11px);color:var(--screen-mut);letter-spacing:.04em;z-index:6}

.card{position:absolute;inset:0;padding:6cqw 5.5cqw;display:flex;flex-direction:column;
  opacity:0;transform:translateX(4cqw);pointer-events:none;
  transition:opacity .34s ease,transform .34s ease}
.card.on{opacity:1;transform:none;pointer-events:auto}
.card.prev{transform:translateX(-4cqw)}
.card.img,.card.contain{padding:0}
.card.img img{width:100%;height:100%;object-fit:cover;display:block}
.card.contain{background:#e7e0cd}
.card.contain img{width:100%;height:100%;object-fit:contain;display:block}
.imgcap{position:absolute;left:0;right:0;bottom:0;padding:16cqw 5cqw 5.5cqw;z-index:5;
  background:linear-gradient(to top,rgba(12,9,3,.95),rgba(12,9,3,.6) 46%,rgba(12,9,3,0));color:#f3ecda}
.imgcap .k{font-family:"Oswald",sans-serif;text-transform:uppercase;letter-spacing:.11em;
  font-size:clamp(13px,6.4cqw,26px);font-weight:700;color:#f6dc8c;display:block;margin-bottom:2.4cqw;
  text-shadow:0 2px 8px rgba(0,0,0,.9),0 0 2px rgba(0,0,0,.7);line-height:1.02}
.imgcap p{margin:0;font-size:clamp(8px,3.7cqw,12px);line-height:1.35;text-shadow:0 1px 4px rgba(0,0,0,.8)} .imgcap b{color:#fff}
.hl{position:absolute;left:5%;right:5%;border:2px solid #d7a94e;border-radius:3px;
  box-shadow:0 0 0 2000px rgba(16,12,6,.4);z-index:3}

/* paginated tall content (posters fill the display, stepped vertically) */
.card.ppage{padding:0;background-size:100% auto;background-repeat:no-repeat;background-color:#e7e0cd}
.plabel{position:absolute;top:0;left:0;right:0;z-index:5;display:flex;justify-content:space-between;
  align-items:center;gap:2cqw;padding:3.2cqw 4cqw 7cqw;
  background:linear-gradient(to bottom,rgba(18,14,7,.82),rgba(18,14,7,0))}
.plabel .pn{font-family:"Oswald",sans-serif;text-transform:uppercase;letter-spacing:.13em;
  font-size:clamp(7px,3.2cqw,11px);font-weight:600;color:var(--gold)}
.plabel .pp{font-family:"Space Mono",monospace;font-size:clamp(7px,2.9cqw,10px);color:#e7dcc0}
.pintro{position:absolute;left:0;right:0;bottom:0;z-index:5;text-align:center;padding:8cqw 4cqw 4cqw;
  background:linear-gradient(to top,rgba(18,14,7,.85),rgba(18,14,7,0));
  font-family:"Oswald",sans-serif;text-transform:uppercase;letter-spacing:.11em;
  font-size:clamp(8px,3.4cqw,12px);color:#f3ecda}

.card .kick{font-family:"Oswald",sans-serif;text-transform:uppercase;letter-spacing:.18em;
  font-size:clamp(7px,3.2cqw,11px);font-weight:600;color:var(--screen-accent);margin-bottom:3cqw}
.card h2{font-family:"Newsreader",serif;font-weight:600;font-size:clamp(15px,7.6cqw,27px);
  line-height:1.05;letter-spacing:-.01em;margin:0 0 3cqw;text-wrap:balance}
.card p{margin:0 0 2.6cqw;font-size:clamp(9px,4.55cqw,15px);line-height:1.42;color:var(--screen-ink)}
.card .lede{font-size:clamp(10px,5cqw,16px)} .card .sub{color:var(--screen-mut);font-size:clamp(8px,4.1cqw,13px)}
.hero-title{margin-top:6cqw} .home-img{margin:4cqw 0;border-radius:2px;overflow:hidden;background:#ddd6c4}
.home-img img{width:100%;display:block;aspect-ratio:16/10;object-fit:cover}
.prompt{margin-top:auto;font-family:"Oswald",sans-serif;text-transform:uppercase;letter-spacing:.12em;
  font-size:clamp(8px,3.7cqw,12px);font-weight:600;color:var(--screen-accent);display:flex;align-items:center;gap:2cqw}
.prompt .dot{width:2.4cqw;height:2.4cqw;border-radius:50%;background:var(--screen-gold);
  animation:blink 1.6s steps(2,jump-none) infinite}
@keyframes blink{50%{opacity:.25}}

.stats{display:flex;border-top:1px solid var(--screen-line);border-bottom:1px solid var(--screen-line);margin:1cqw 0 3.5cqw}
.stats div{flex:1;padding:2.6cqw 1cqw;text-align:center;border-left:1px solid var(--screen-line)}
.stats div:first-child{border-left:0}
.stats .n{font-family:"Space Mono",monospace;font-weight:700;font-size:clamp(11px,5cqw,17px);color:var(--screen-ink);display:block}
.stats .l{font-family:"Oswald",sans-serif;text-transform:uppercase;letter-spacing:.06em;
  font-size:clamp(6px,2.5cqw,9px);color:var(--screen-mut);margin-top:1cqw;display:block}
.chain{display:flex;flex-wrap:wrap;gap:1.4cqw 1.8cqw;align-items:center;margin:1cqw 0 3.5cqw}
.chain span{font-family:"Oswald",sans-serif;font-size:clamp(7px,3.4cqw,11px);letter-spacing:.01em;
  background:#ddd4bd;color:var(--screen-ink);padding:1.2cqw 2.4cqw;border-radius:2px}
.chain span.hot{background:var(--screen-accent);color:#f2ecda}
.chain i{color:var(--screen-gold);font-style:normal;font-weight:700;font-size:3.6cqw}

.roster{display:flex;flex-direction:column;gap:2.6cqw;margin:1cqw 0 2cqw;padding:0}
.roster li{list-style:none;display:block;font-size:clamp(8px,4.1cqw,13px);line-height:1.28}
.roster .nm{font-family:"Oswald",sans-serif;font-weight:600;color:var(--screen-ink)}
.roster .rl{color:var(--screen-mut)}
.roster .cr{display:block;font-style:italic;color:#877c60;font-size:clamp(8px,3.8cqw,12px)}
.roster .dt{display:block;color:var(--screen-accent);font-size:clamp(8px,3.8cqw,12px)}
.morep{font-size:clamp(8px,3.7cqw,12px);color:var(--screen-mut);font-style:italic;margin-top:auto}

/* Rick's format: headline + graphic + a few big bullets */
.card.ccard{padding:6.5cqw 6cqw;gap:0;justify-content:flex-start}
.ccard .ek{font-family:"Oswald",sans-serif;text-transform:uppercase;letter-spacing:.16em;
  font-size:clamp(8px,3.5cqw,13px);font-weight:600;color:var(--screen-gold);margin-bottom:2cqw}
.ccard h2{font-family:"Archivo",sans-serif;font-weight:700;font-size:clamp(19px,9.4cqw,38px);
  line-height:1.03;letter-spacing:-.02em;margin:0 0 4cqw;text-wrap:balance}
.ccard h2 .h2sub{display:block;font-size:.56em;font-weight:600;color:var(--screen-mut);margin-top:1.4cqw}
.cimg{width:100%;aspect-ratio:16/10;border-radius:3px;overflow:hidden;background:#d9d1bd;margin:0 0 4.5cqw;
  box-shadow:0 1px 4px rgba(0,0,0,.18)}
.cimg img{width:100%;height:100%;object-fit:cover;display:block}
/* four-panel montage (the poster hero) */
.mont4{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:.8cqw;width:100%;
  aspect-ratio:4/3;border-radius:3px;overflow:hidden;background:#cbc2ac;margin:0 0 4.5cqw;
  box-shadow:0 1px 4px rgba(0,0,0,.18)}
.mp{position:relative;background-size:cover;background-position:center}
.mp .tag{position:absolute;left:1.6cqw;bottom:1.4cqw;font-family:"Oswald",sans-serif;text-transform:uppercase;
  letter-spacing:.09em;font-size:clamp(6px,2.7cqw,10px);font-weight:600;color:#fff;
  background:rgba(16,12,6,.62);padding:.5cqw 1.4cqw;border-radius:2px}
.cimcap{font-family:"Oswald",sans-serif;text-transform:uppercase;letter-spacing:.1em;font-weight:600;
  font-size:clamp(7px,3.1cqw,12px);color:var(--screen-mut);margin:-3cqw 0 4.5cqw}
.blist{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:3.6cqw}
.blist li{position:relative;padding-left:6cqw;font-size:clamp(14px,6.7cqw,27px);line-height:1.22;
  font-family:"Archivo",sans-serif;font-weight:500;color:var(--screen-ink)}
.blist li::before{content:"";position:absolute;left:0;top:.5em;width:2.8cqw;height:2.8cqw;
  background:var(--screen-accent);border-radius:1px;transform:rotate(45deg)}
.blist b{color:var(--screen-accent)}

/* three real buttons — transparent hotspots over the drawn controls */
.hotbtn{position:absolute;width:9.8%;aspect-ratio:1;transform:translate(-50%,-50%);
  border:0;background:transparent;border-radius:50%;cursor:pointer;padding:0;z-index:7;
  -webkit-tap-highlight-color:transparent;transition:background .12s ease}
.hotbtn.back{left:36.1%;top:66.1%} .hotbtn.home{left:49.3%;top:66.1%} .hotbtn.next{left:62.4%;top:66.1%}
.hotbtn:active,.hotbtn.press{background:radial-gradient(circle at 50% 44%,rgba(255,255,255,.4),rgba(255,255,255,0) 66%)}
.hotbtn:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
.hotbtn[disabled]{cursor:default;background:radial-gradient(circle,rgba(28,24,16,.42),rgba(28,24,16,.30) 70%)}
.hint{font-family:"Oswald",sans-serif;text-transform:uppercase;letter-spacing:.11em;font-size:11px;
  color:var(--muted);text-align:center;margin:2px 0 0} .hint b{color:var(--accent);font-weight:600}

/* ---- enlarged screen (modal) ---- */
.modal{position:fixed;inset:0;z-index:60;display:none;place-items:center;overflow:auto;
  padding:20px;background:rgba(14,11,7,.86);-webkit-backdrop-filter:blur(3px);backdrop-filter:blur(3px)}
.modal.open{display:grid}
.mclose{position:fixed;top:14px;right:16px;width:44px;height:44px;border-radius:50%;border:0;cursor:pointer;
  background:rgba(255,255,255,.15);color:#fff;font-size:22px;line-height:1;z-index:62}
.mclose:hover{background:rgba(255,255,255,.26)}
.kbig{position:relative;display:flex;flex-direction:column;align-items:center;gap:18px;margin:auto}
.kbig-screen{background:#26262a;padding:12px;border-radius:12px;
  box-shadow:0 40px 90px -24px rgba(0,0,0,.75),0 0 0 1px rgba(0,0,0,.4)}
.display.big{width:min(86vw,410px);aspect-ratio:230/529;border-radius:3px}
.mbuttons{display:flex;gap:min(9vw,40px)}
.mbtn{display:flex;flex-direction:column;align-items:center;gap:8px;background:none;border:0;
  cursor:pointer;font-family:"Oswald",sans-serif;padding:0;-webkit-tap-highlight-color:transparent}
.mbtn .disc{width:58px;height:58px;border-radius:50%;display:grid;place-items:center;
  background:radial-gradient(circle at 38% 30%,#3d3d43,#2b2b2f 62%,#161618);
  box-shadow:0 3px 0 #0c0c0d,0 7px 14px -5px rgba(0,0,0,.55),0 1px 1px rgba(255,255,255,.22) inset;
  transition:transform .08s ease,box-shadow .08s ease}
.mbtn svg{width:25px;height:25px;stroke:#f0ece2;stroke-width:2.4;fill:none;stroke-linecap:round;stroke-linejoin:round}
.mbtn.home svg{fill:#f0ece2;stroke:none}
.mbtn .cap{text-transform:uppercase;letter-spacing:.14em;font-size:11px;font-weight:600;color:#d8ccb0}
.mbtn:active .disc{transform:translateY(3px);box-shadow:0 0 0 #0c0c0d,0 2px 6px rgba(0,0,0,.5),0 1px 1px rgba(255,255,255,.2) inset}
.mbtn:focus-visible .disc{outline:3px solid #7FA0DB;outline-offset:3px}
.mbtn[disabled]{cursor:default} .mbtn[disabled] .disc{opacity:.4} .mbtn[disabled] .cap{opacity:.5}

/* ---- physical concept ---- */
.concept{margin-top:clamp(46px,8vw,84px);border-top:1px solid var(--line);padding-top:clamp(30px,5vw,44px)}
.concept .eyebrow{color:var(--accent2)}
.concept h2{font-family:"Newsreader",serif;font-weight:600;font-size:clamp(23px,4vw,34px);
  letter-spacing:-.01em;margin:.3em 0 .2em;text-wrap:balance}
.concept .dek{color:var(--muted);max-width:54ch;margin:0 0 26px}
.specs{display:flex;flex-wrap:wrap;gap:10px;margin:0 0 30px}
.spec{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:12px 16px;flex:1;min-width:118px}
.spec .n{font-family:"Space Mono",monospace;font-weight:700;font-size:20px;color:var(--accent);display:block}
.spec .l{font-family:"Oswald",sans-serif;text-transform:uppercase;letter-spacing:.08em;font-size:10px;color:var(--muted);margin-top:4px;display:block}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:clamp(16px,3vw,26px)}
@media(max-width:720px){.grid2{grid-template-columns:1fr}}
figure{margin:0}
.shot{border-radius:10px;overflow:hidden;background:var(--panel);border:1px solid var(--line);box-shadow:0 18px 40px -26px var(--shadow)}
.shot img{width:100%;display:block}
figcaption{font-size:14px;color:var(--muted);margin-top:10px;line-height:1.45}
figcaption b{color:var(--ink);font-family:"Oswald",sans-serif;font-weight:600;text-transform:uppercase;letter-spacing:.06em;font-size:12px}
.feat{list-style:none;padding:0;margin:26px 0 0;display:grid;grid-template-columns:1fr 1fr;gap:2px 30px}
@media(max-width:620px){.feat{grid-template-columns:1fr}}
.feat li{padding:14px 0;border-top:1px solid var(--line);display:flex;gap:12px;align-items:baseline}
.feat .fn{font-family:"Space Mono",monospace;font-size:12px;color:var(--accent2);font-weight:700;flex:none}
.feat b{font-family:"Oswald",sans-serif;font-weight:600;text-transform:uppercase;letter-spacing:.05em;font-size:13px;display:block;margin-bottom:2px}
.feat p{margin:0;font-size:13.5px;color:var(--muted);line-height:1.45}

footer{margin-top:54px;border-top:1px solid var(--line);padding-top:22px;display:flex;gap:16px;
  align-items:center;justify-content:space-between;flex-wrap:wrap}
footer img{height:34px;width:auto;opacity:.9}
footer .note{font-size:12px;color:var(--muted);max-width:60ch;line-height:1.5}

@media (prefers-reduced-motion:reduce){.card{transition:none}.prompt .dot{animation:none}.hotbtn,.mbtn .disc{transition:none}}
</style>

<div class="wrap">
  <header class="mast">
    <div class="eyebrow">VCF Museum · Exhibit Concept Review</div>
    <h1>The 3280, told through its own front panel</h1>
    <p class="dek">The docent kiosk lives inside the Concurrent 3280 itself — one portrait screen where the
    door used to be, three real buttons, the card cage all around it. Tap the screen to read it full-size.</p>
  </header>

  <section class="stage" aria-label="Kiosk prototype in the 3280 cabinet">
    <div class="install">
      <div class="cbadge">Concept</div>
      <div class="display" id="display" role="button" tabindex="0" aria-label="Kiosk screen — activate to enlarge">
        <div class="zoomtag"><svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><line x1="16" y1="16" x2="21" y2="21"/><line x1="11" y1="8" x2="11" y2="14"/><line x1="8" y1="11" x2="14" y2="11"/></svg></div>
        <div class="counter" id="counter"></div>
      </div>
      <button class="hotbtn back" id="btnBack" aria-label="Back"></button>
      <button class="hotbtn home" id="btnHome" aria-label="Home"></button>
      <button class="hotbtn next" id="btnNext" aria-label="Next"></button>
    </div>
    <p class="hint">Tap the screen to enlarge · press <b>Back · Home · Next</b> · or use <b>← →</b> keys</p>
  </section>

  <section class="concept">
    <div class="eyebrow">The physical concept</div>
    <h2>A screen where the machine's door used to be</h2>
    <p class="dek">ChatGPT concept renders of the installed piece. A hinged, portrait display and three
    buttons; a docent swings it open to show the real card cage behind it.</p>

    <div class="specs">
      <div class="spec"><span class="n">23.0″</span><span class="l">Cabinet width</span></div>
      <div class="spec"><span class="n">69.5″</span><span class="l">Cabinet height</span></div>
      <div class="spec"><span class="n">9U + 9U</span><span class="l">Card cage bins</span></div>
      <div class="spec"><span class="n">3</span><span class="l">Buttons · no touch</span></div>
    </div>

    <div class="grid2">
      <figure>
        <div class="shot"><img src="__KIOSK__" alt="Concept render: the portrait kiosk door closed on the 3280 cabinet"></div>
        <figcaption><b>Door closed</b> — the kiosk screen sits in a hinged door, real boards framing it through the glass.</figcaption>
      </figure>
      <figure>
        <div class="shot"><img src="__INTERIOR__" alt="Concept render: the 3280 cabinet open, showing the 9U over 9U card cage"></div>
        <figcaption><b>Docent view</b> — swung open, the full 9U-over-9U card cage is exposed for a close look at the hand-wired boards.</figcaption>
      </figure>
    </div>

    <ul class="feat">
      <li><span class="fn">01</span><div><b>Hinged kiosk door</b><p>Swings open on left-side hinges so a docent can reveal the real boards behind it.</p></div></li>
      <li><span class="fn">02</span><div><b>Portrait display</b><p>Tall format suits placard text and the exhibit posters one screen at a time.</p></div></li>
      <li><span class="fn">03</span><div><b>Three buttons, no touch</b><p>Back · Home · Next only — nothing to smudge, nothing to explain, nothing to break.</p></div></li>
    </ul>
  </section>

  <footer>
    <img src="__LOGO__" alt="Vintage Computer Federation">
    <p class="note">Concept-review prototype. Cabinet imagery is AI concept art, not the final piece; on-screen
    copy uses the exhibit's verified facts. Screen content is an early draft — a few key points per screen, not the final wording.</p>
  </footer>
</div>

<!-- enlarged screen -->
<div class="modal" id="modal" aria-hidden="true">
  <button class="mclose" id="mclose" aria-label="Close">&times;</button>
  <div class="kbig" role="dialog" aria-modal="true" aria-label="Kiosk screen, enlarged">
    <div class="cbadge">Concept</div>
    <div class="kbig-screen"><div class="display big" id="mdisplay"><div class="counter" id="mcounter"></div></div></div>
    <div class="mbuttons">
      <button class="mbtn back" id="mBack" aria-label="Back">
        <span class="disc"><svg viewBox="0 0 24 24"><polyline points="15 5 8 12 15 19"/></svg></span><span class="cap">Back</span></button>
      <button class="mbtn home" id="mHome" aria-label="Home">
        <span class="disc"><svg viewBox="0 0 24 24"><path d="M3 11.5 12 4l9 7.5V21a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/></svg></span><span class="cap">Home</span></button>
      <button class="mbtn next" id="mNext" aria-label="Next">
        <span class="disc"><svg viewBox="0 0 24 24"><polyline points="9 5 16 12 9 19"/></svg></span><span class="cap">Next</span></button>
    </div>
  </div>
</div>

<script>
// Rick's format: each screen = one point, a graphic, 3–5 short bullets, big font.
const CARDS = [
  // HOME — the whole story in one screen
  {cls:"ccard", html:`<div class="ek">The Concurrent 3280</div>
    <h2>This computer was designed and built in New Jersey<span class="h2sub">Deployed everywhere &middot; 1981&ndash;1986</span></h2>
    <div class="mont4">
      <div class="mp" style="background-image:url('__M_WEATHER__')"><span class="tag">Weather</span></div>
      <div class="mp" style="background-image:url('__M_SPACE__');background-position:center 28%"><span class="tag">Space</span></div>
      <div class="mp" style="background-image:url('__M_DEFENSE__')"><span class="tag">Defense</span></div>
      <div class="mp" style="background-image:url('__M_FINANCE__');background-position:center 22%"><span class="tag">Finance</span></div>
    </div>
    <ul class="blist">
      <li>Designed in <b>Tinton Falls</b>, built in <b>Oceanport</b></li>
      <li>Ran <b>weather radar, spaceflight, defense &amp; Wall Street</b></li>
      <li>Its designers later shaped chips at <b>MIPS, IBM &amp; Sony</b></li>
    </ul>
    <div class="prompt"><span class="dot"></span> Press Next</div>`},

  // WHAT IT DID
  {cls:"ccard", html:`<div class="ek">What it did</div>
    <h2>One machine, many jobs</h2>
    <div class="cimg"><img src="__RADAR__" alt="Weather radar"></div>
    <ul class="blist">
      <li>Tracked storms on the <b>national weather radar</b></li>
      <li>Trained <b>NASA astronauts</b> for the Space Shuttle</li>
      <li>Ran the computers on <b>Wall Street</b></li>
    </ul>`},

  // POWER
  {cls:"ccard", html:`<div class="ek">Under the hood</div>
    <h2>Big iron, built by hand</h2>
    <div class="cimg"><img src="__INTERIOR__" alt="The 3280 circuit boards"></div>
    <ul class="blist">
      <li>Built for jobs <b>too big for any desktop</b></li>
      <li>Grew to <b>12 processors</b> working as one</li>
      <li>Every circuit board <b>wired by hand</b></li>
    </ul>`},

  // NEW JERSEY
  {cls:"ccard", html:`<div class="ek">Where it was born</div>
    <h2>Made in Monmouth County</h2>
    <div class="cimg"><img src="__NJPLANT__" alt="Concurrent's New Jersey plant"></div>
    <ul class="blist">
      <li><b>Designed</b> in Tinton Falls</li>
      <li><b>Built</b> in Oceanport</li>
      <li><b>A few miles from this museum</b></li>
    </ul>`},

  // THE PEOPLE
  {cls:"ccard", html:`<div class="ek">Who built it</div>
    <h2>Built by a small team</h2>
    <div class="cimg"><img src="__YEAGER__" alt="Ken Yeager"></div>
    <div class="cimcap">Ken Yeager · lead architect</div>
    <ul class="blist">
      <li>About <b>15 engineers</b>, in one New Jersey lab</li>
      <li>One later designed the chip inside the <b>PlayStation 3 &amp; Xbox 360</b></li>
      <li>Its lead architect went on to <b>SGI</b> &mdash; and his chip is <b>in this museum</b></li>
    </ul>`},

  // CROSS-LINK to the museum's SGI Onyx (Yeager's R10000)
  {cls:"ccard", html:`<div class="ek">Just down the room</div>
    <h2>Two machines, one designer</h2>
    <div class="cimg"><img src="__R10000__" alt="The MIPS R10000 processor"></div>
    <div class="cimcap">MIPS R10000</div>
    <ul class="blist">
      <li><b>Ken Yeager</b> architected this 3280 in New Jersey</li>
      <li>Then he designed the <b>MIPS R10000</b> chip at SGI</li>
      <li>It powers the <b>SGI Onyx</b> on display here &mdash; that chip sits on top of it</li>
    </ul>`},

  // OPEN THE CABINET
  {cls:"img", html:`<img src="__INTERIOR__" alt="The 3280 card cage, opened">
    <div class="imgcap"><span class="k">Open it up</span>
      <p>Hundreds of boards &mdash; every wire placed by hand.</p></div>`},

  {cls:"img", hl:{top:"20%",bottom:"48%"}, html:`<img src="__INTERIOR__" alt="Upper card cage">
    <div class="imgcap"><span class="k">The processor</span>
      <p>Up top: where the calculations happened.</p></div>`},

  {cls:"img", hl:{top:"62%",bottom:"6%"}, html:`<img src="__INTERIOR__" alt="Lower card cage">
    <div class="imgcap"><span class="k">Memory &amp; control</span>
      <p>Below: where the data lived.</p></div>`},
];

function buildInto(container){
  return CARDS.map(c=>{
    const el=document.createElement('div');
    el.className='card'+(c.cls?' '+c.cls:'');
    el.innerHTML=c.html;
    if(c.bg){el.style.backgroundImage=`url("${c.bg}")`;el.style.backgroundPosition=`center ${c.pos}`;}
    if(c.hl){const b=document.createElement('div');b.className='hl';b.style.top=c.hl.top;b.style.bottom=c.hl.bottom;el.appendChild(b);}
    container.appendChild(el);
    return el;
  });
}
const display=document.getElementById('display'), mdisplay=document.getElementById('mdisplay');
const counter=document.getElementById('counter'), mcounter=document.getElementById('mcounter');
const inlineNodes=buildInto(display), modalNodes=buildInto(mdisplay);
const backs=[document.getElementById('btnBack'),document.getElementById('mBack')];
const nexts=[document.getElementById('btnNext'),document.getElementById('mNext')];
const homes=[document.getElementById('btnHome'),document.getElementById('mHome')];

let i=0;
function paint(nodes,n){nodes.forEach((el,idx)=>{el.classList.toggle('on',idx===n);el.classList.toggle('prev',idx<n);});}
function show(n){
  n=Math.max(0,Math.min(CARDS.length-1,n)); i=n;
  paint(inlineNodes,n); paint(modalNodes,n);
  const t=(n+1)+' / '+CARDS.length; counter.textContent=t; mcounter.textContent=t;
  backs.forEach(b=>b.disabled=(n===0)); nexts.forEach(b=>b.disabled=(n===CARDS.length-1));
}
function tap(b){b.classList.add('press');setTimeout(()=>b.classList.remove('press'),120);}
function go(d){const n=i+d; if(n<0||n>CARDS.length-1)return; show(n);}
nexts.forEach(b=>b.addEventListener('click',e=>{e.stopPropagation();tap(b);go(1);}));
backs.forEach(b=>b.addEventListener('click',e=>{e.stopPropagation();tap(b);go(-1);}));
homes.forEach(b=>b.addEventListener('click',e=>{e.stopPropagation();tap(b);show(0);}));

// enlarge / close
const modal=document.getElementById('modal');
function openModal(){modal.classList.add('open');modal.setAttribute('aria-hidden','false');}
function closeModal(){modal.classList.remove('open');modal.setAttribute('aria-hidden','true');}
display.addEventListener('click',openModal);
display.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();openModal();}});
document.getElementById('mclose').addEventListener('click',closeModal);
modal.addEventListener('click',e=>{if(e.target===modal)closeModal();});

document.addEventListener('keydown',e=>{
  if(e.key==='Escape'&&modal.classList.contains('open'))closeModal();
  else if(e.key==='ArrowRight')go(1);
  else if(e.key==='ArrowLeft')go(-1);
  else if(e.key==='Home'){e.preventDefault();show(0);}
});
show(0);
</script>
"""

for k, v in IMG.items():
    HTML = HTML.replace(k, v)

out = HERE / "index.html"
out.write_text(HTML, encoding="utf-8")
print(f"wrote {out}  ({out.stat().st_size/1024:.0f} KB)")
