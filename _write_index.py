"""Expand index.html for Riau Escapes — dense imagery, multi-paragraph descriptions, inline galleries."""
import os

lines = []

def L(s):
    lines.append(s)

# ── HEAD & NAV (unchanged structure) ──
L('''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Riau Escapes | The Best of Both Worlds - Batam & Bintan</title>
<link rel="stylesheet" href="css/style.css">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css'>
</head>
<body>

<!-- NAVBAR -->
<nav class="navbar" id="navbar">
<div class="navbar-inner">
<a href="index.html" class="navbar-brand">Riau<span>Escapes</span></a>
<button class="hamburger" id="hamburger" aria-label="Toggle menu"><span></span><span></span><span></span></button>
<div class="navbar-links" id="navLinks">
<a href="index.html" class="active">Home</a>
<a href="batam.html">Batam</a>
<a href="bintan.html">Bintan</a>
<a href="golf.html">Golf</a>
<a href="contact.html">Contact Us</a>
<a href="#discover" class="nav-cta">Explore Now</a>
</div>
</div>
</nav>

<!-- HERO ── FULL-BLEED, IMAGE-RICH -->
<section class="hero">
<div class="hero-bg">
<img src="/images/batam-aerial-sunset.jpg" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1577717903315-1691ae25ab36?auto=format&w=1920&q=80';this.onerror=function(){this.parentElement.classList.add('img-placeholder');};this.alt='Riau Islands aerial view at sunset'" alt="Aerial panorama of Batam and Bintan islands at golden hour overlooking the South China Sea">
</div>
<div class="hero-overlay"></div>
<div class="hero-content fade-in-up">
<span class="hero-label"><i class="fa-solid fa-gem" style="margin-right:8px;"></i>Indonesia's Crown Jewel</span>
<h1 class="hero-title">The Best of Both Worlds</h1>
<p class="hero-subtitle" style="max-width:720px;">Where Batam's dynamic energy meets Bintan's pristine serenity. These twin islands, nestled in the Riau Islands archipelago just 90 minutes by ferry from Singapore, offer a rare duality: cosmopolitan thrills and untamed paradise, side by side. For decades these waters were known only to fishermen and smugglers; today they are Southeast Asia's best-kept secret for travelers who want both worlds without compromise.</p>
<div style="display:flex;gap:12px;margin-bottom:36px;flex-wrap:wrap;" class="fade-in-up">
<span style="background:rgba(255,255,255,0.1);padding:6px 16px;border-radius:20px;color:rgba(255,255,255,0.8);font-size:0.8rem;"><i class="fa-solid fa-plane" style="margin-right:6px;"></i>90 min from Singapore</span>
<span style="background:rgba(255,255,255,0.1);padding:6px 16px;border-radius:20px;color:rgba(255,255,255,0.8);font-size:0.8rem;"><i class="fa-solid fa-ship" style="margin-right:6px;"></i>Daily ferry departures</span>
<span style="background:rgba(255,255,255,0.1);padding:6px 16px;border-radius:20px;color:rgba(255,255,255,0.8);font-size:0.8rem;"><i class="fa-solid fa-language" style="margin-right:6px;"></i>Multi-cultural hub</span>
<span style="background:rgba(255,255,255,0.1);padding:6px 16px;border-radius:20px;color:rgba(255,255,255,0.8);font-size:0.8rem;"><i class="fa-solid fa-coins" style="margin-right:6px;"></i>Free-trade zone</span>
</div>
<div class="hero-cta-group" id="discover">
<a href="batam.html" class="btn btn-primary"><i class="fa-solid fa-city"></i> Explore Batam</a>
<a href="bintan.html" class="btn btn-outline"><i class="fa-solid fa-water"></i> Discover Bintan</a>
</div>
</div>
</section>

<!-- IMMERSIVE IMAGE STRIP (hero gallery) -->
<section style="padding:40px 0 60px;overflow-x:hidden;">
<div class="container">
<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:8px;border-radius:20px;overflow:hidden;" class="fade-in-up">
<a href="batam.html" style="position:relative;height:360px;display:block;">
<img src="/images/batam-wakepark.jpg" style="width:100%;height:100%;object-fit:cover;" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1596892703737-7784a61df35c?auto=format&w=600&q=80';this.parentElement.classList.add('img-placeholder-style');" alt="Batam cable wakeboarding adventure at the waterfront">
<div style="position:absolute;bottom:0;left:0;right:0;padding:20px;background:linear-gradient(transparent,rgba(10,31,63,0.9));color:white;font-family:'Cormorant Garamond',serif;font-size:1.1rem;">Batam Adventures</div>
</a>
<a href="bintan.html" style="position:relative;height:360px;display:block;">
<img src="/images/bintan-lagoon.jpg" style="width:100%;height:100%;object-fit:cover;" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1589308078059-be1415eab9c3?auto=format&w=600&q=80';" alt="Bintan crystal-clear turquoise lagoon with white sand shoreline">
<div style="position:absolute;bottom:0;left:0;right:0;padding:20px;background:linear-gradient(transparent,rgba(10,31,63,0.9));color:white;font-family:'Cormorant Garamond',serif;font-size:1.1rem;">Bintan Lagoons</div>
</a>
<a href="golf.html" style="position:relative;height:360px;display:block;">
<img src="/images/golf-championship.jpg" style="width:100%;height:100%;object-fit:cover;" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1587174486073-ae5e7cff5c49?auto=format&w=600&q=80';" alt="Championship golf course nestled in tropical palm forest">
<div style="position:absolute;bottom:0;left:0;right:0;padding:20px;background:linear-gradient(transparent,rgba(10,31,63,0.9));color:white;font-family:'Cormorant Garamond',serif;font-size:1.1rem;">Championship Golf</div>
</a>
<a href="contact.html" style="position:relative;height:360px;display:block;">
<img src="/images/nagoya-skyline.jpg" style="width:100%;height:100%;object-fit:cover;" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1486406146925-c58381e2e1a0?auto=format&w=600&q=80';" alt="Modern Batam skyline and real estate development along Nagoya">
<div style="position:absolute;bottom:0;left:0;right:0;padding:20px;background:linear-gradient(transparent,rgba(10,31,63,0.9));color:white;font-family:'Cormorant Garamond',serif;font-size:1.1rem;">Contact Us</div>
</a>
<a href="batam.html" style="position:relative;height:360px;display:block;">
<img src="/images/batam-food-nightmarket.jpg" style="width:100%;height:100%;object-fit:cover;" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&w=600&q=80';" alt="Batam night market with sizzling street food and vibrant atmosphere">
<div style="position:absolute;bottom:0;left:0;right:0;padding:20px;background:linear-gradient(transparent,rgba(10,31,63,0.9));color:white;font-family:'Cormorant Garamond',serif;font-size:1.1rem;">Food & Nightlife</div>
</a>
</div>
</div>
</section>

<!-- FEATURE PREVIEW CARDS -->
<section class="features-section">
<div class="container">
<span class="section-label fade-in-up">Discover Riau Islands</span>
<h2 class="section-title fade-in-up" style="text-align:center;">Four Experiences, One Destination</h2>
<p class="section-text fade-in-up" style="margin:0 auto 48px;text-align:center;">From cosmopolitan adventures to luxury island retreats, every corner of the Riau Islands offers something unforgettable. Batam captivates with its electric mix of urban energy, coastal recreation, and culinary diversity, while Bintan lures with sprawling lagoons, pristine beaches, and world-class resort sanctuaries.</p>
<div class="grid-4">

<!-- Card 1: Batam -->
<a href="batam.html" class="feature-card fade-in-up" style="height:380px;">
<div class="feature-card-bg">
<img src="/images/batam-skyline-waterfront.jpg" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1596892703737-7784a61df35c?auto=format&w=800&q=80';this.onerror=function(){this.parentElement.classList.add('img-placeholder');};this.alt='Batam city skyline along the waterfront with modern high-rises and bustling harbor'" alt="Batam city skyline along the waterfront showing modern high-rise buildings, marina, and the strait beyond">
</div>
<div class="feature-card-overlay"></div>
<div class="feature-card-content" style="padding:28px;">
<p style="color:var(--color-gold-sun);font-size:0.75rem;letter-spacing:2px;text-transform:uppercase;margin-bottom:6px;font-family:'Inter',sans-serif;"><i class="fa-solid fa-bolt" style="margin-right:6px;"></i>Urban Energy</p>
<h3 class="feature-card-title" style="font-size:1.6rem;">Batam</h3>
<p class="feature-card-text">Cosmopolitan cityscape, thrilling water sports, legendary nightlife, and a food scene that blends Indonesian, Malaysian, Chinese, and Western influences into something truly unique.</p>
<span style="display:inline-block;color:var(--color-gold-sun);font-size:0.85rem;margin-top:12px;font-weight:600;"><i class="fa-solid fa-arrow-right" style="margin-right:6px;"></i>Explore Batam</span>
</div>
</a>

<!-- Card 2: Bintan -->
<a href="bintan.html" class="feature-card fade-in-up" style="height:380px;">
<div class="feature-card-bg">
<img src="/images/bintan-chill-cove-aerial.jpg" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1589308078059-be1415eab9c3?auto=format&w=800&q=80';this.onerror=function(){this.parentElement.classList.add('img-placeholder');};this.alt='Aerial view of Chill Cove crystal lagoon at Bintan with turquoise waters and luxury resort villas'" alt="Aerial panorama of Chill Cove crystal lagoon in Bintan showing miles of turquoise water bordered by white sand beaches and lush tropical greenery">
</div>
<div class="feature-card-overlay"></div>
<div class="feature-card-content" style="padding:28px;">
<p style="color:var(--color-gold-sun);font-size:0.75rem;letter-spacing:2px;text-transform:uppercase;margin-bottom:6px;font-family:'Inter',sans-serif;"><i class="fa-solid fa-umbrella-beach" style="margin-right:6px;"></i>Luxury Retreat</p>
<h3 class="feature-card-title" style="font-size:1.6rem;">Bintan</h3>
<p class="feature-card-text">Five-star resort sanctuaries, the largest crystal lagoon in Southeast Asia, golden sand dunes, firefly-filled mangroves, and championship golf under palm-dotted skies.</p>
<span style="display:inline-block;color:var(--color-gold-sun);font-size:0.85rem;margin-top:12px;font-weight:600;"><i class="fa-solid fa-arrow-right" style="margin-right:6px;"></i>Discover Bintan</span>
</div>
</a>

<!-- Card 3: Golf -->
<a href="golf.html" class="feature-card fade-in-up" style="height:380px;">
<div class="feature-card-bg">
<img src="/images/batam-hills-golf-course.jpg" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1587174486073-ae5e7cff5c49?auto=format&w=800&q=80';this.onerror=function(){this.parentElement.classList.add('img-placeholder');};this.alt='Batam Hills golf course with rolling fairways surrounded by tropical palm forest and coastal mountain views'" alt="Lush Batam Hills golf course showing rolling green fairways, sand traps, and tropical mountain backdrop">
</div>
<div class="feature-card-overlay"></div>
<div class="feature-card-content" style="padding:28px;">
<p style="color:var(--color-gold-sun);font-size:0.75rem;letter-spacing:2px;text-transform:uppercase;margin-bottom:6px;font-family:'Inter',sans-serif;"><i class="fa-solid fa-golf-ball-tee" style="margin-right:6px;"></i>Tropical Course</p>
<h3 class="feature-card-title" style="font-size:1.6rem;">Golf</h3>
<p class="feature-card-text">Six championship-caliber courses across Batam and Bintan, from tree-lined parkland layouts to coastal links with ocean breezes — plus floodlit driving range sessions at dusk.</p>
<span style="display:inline-block;color:var(--color-gold-sun);font-size:0.85rem;margin-top:12px;font-weight:600;"><i class="fa-solid fa-arrow-right" style="margin-right:6px;"></i>Golf Guide</span>
</div>
</a>

<!-- Card 4: Contact Us -->
<a href="contact.html" class="feature-card fade-in-up" style="height:380px;">
<div class="feature-card-bg">
<img src="/images/lagoi-bay-development.jpg" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1486406146925-c58381e2e1a0?auto=format&w=800&q=80';this.onerror=function(){this.parentElement.classList.add('img-placeholder');};this.alt='Contact Riau Escapes team for personalized travel planning'" alt="Riau Escapes contact and booking information">
</div>
<div class="feature-card-overlay"></div>
<div class="feature-card-content" style="padding:28px;">
<p style="color:var(--color-gold-sun);font-size:0.75rem;letter-spacing:2px;text-transform:uppercase;margin-bottom:6px;font-family:'Inter',sans-serif;"><i class="fa-solid fa-envelope" style="margin-right:6px;"></i>Get in Touch</p>
<h3 class="feature-card-title" style="font-size:1.6rem;">Contact Us</h3>
<p class="feature-card-text">Have questions about Batam, Bintan, or golf packages? Reach our team by phone, email, or visit our office. We respond within 24 hours and are ready to help plan your perfect getaway.</p>
<span style="display:inline-block;color:var(--color-gold-sun);font-size:0.85rem;margin-top:12px;font-weight:600;"><i class="fa-solid fa-arrow-right" style="margin-right:6px;"></i>Contact Us</span>
</div>
</a>

</div>
</div>
</section>

<!-- SECTION: WHY BATAM (image left, text right) -->
<section class="dest-section">
<div class="container">
<div class="split-layout fade-in-up">
<div class="split-image">
<img src="/images/batam-barelang-bridge.jpg" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&w=800&q=80';this.alt='Batam Barelang Bridge spanning the strait with ocean and islands in the background';" alt="The iconic Barelang Bridge (Six Bridges of Batam) stretching across the turquoise strait between Batam and surrounding islands">
</div>
<div class="split-text">
<span class="section-label fade-in-up">Dest Spotlight: Batam</span>
<h2 class="section-title fade-in-up">Where Ambition Meets Adventure</h2>
<p class="section-text fade-in-up" style="margin-bottom:18px;">Batam is a story of transformation. A tiny fishing island transformed into one of Indonesia's most dynamic cities — the engine room of the nation's free-trade economy, pulsing with factories, malls, hotels, and a population that never sleeps. But beyond its commercial veneer lies something unexpected: an extraordinary playground for anyone seeking both stimulation and escape.</p>
<p class="section-text fade-in-up" style="margin-bottom:18px;">Cable wakeboarding on crystal-clear waters at Batam Wakepark. Dining at seafood restaurants built on rock formations above crashing waves in Nongsa. The six magnificent Barelang Bridges — architectural landmarks inspired by Jakarta's iconic bridges — each connecting an island with breathtaking ocean views that are simply unmatched in Southeast Asia.</p>
<p class="section-text fade-in-up" style="margin-bottom:24px;">Batam Center, the downtown district, is a walkable urban hub where Mandarin, Bahasa Indonesia, and English all flow naturally. Grand Batam Mall sprawls across three floors with 200+ shops, international restaurants, and an entertainment zone. The night market scene — from Nongsa Hill to Sei Sukun — offers satay, durian cheesecake at legendary factories, and laksa Batam that has become the island's culinary calling card.</p>
<div style="margin-top:8px;" class="fade-in-up">
<a href="batam.html" class="btn btn-green" style="background:var(--color-gold-sun);color:var(--color-ocean-deep);"><i class="fa-solid fa-map-marked-alt"></i> Full Batam Guide</a>
</div>
</div>
</div>
</div>
</section>

<!-- SECTION: WHY BINTAN (image right, text left) -->
<section class="dest-section" style="background:#F8F6F1;">
<div class="container">
<div class="split-layout fade-in-up" style="flex-direction:row-reverse;">
<div class="split-image">
<img src="/images/bintan-treasure-bay.jpg" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1506929562872-bb421503ef21?auto=format&w=800&q=80';this.alt='Chill Cove Treasure Bay crystal lagoon at Bintan with turquoise waters and luxury resort backdrop';" alt="The stunning Chill Cove treasure bay — Southeast Asia's largest crystal lagoon with impossibly turquoise water, white sands, and surrounding five-star resort buildings">
</div>
<div class="split-text">
<span class="section-label fade-in-up">Dest Spotlight: Bintan</span>
<h2 class="section-title fade-in-up">Where Paradise Actually Exists</h2>
<p class="section-text fade-in-up" style="margin-bottom:18px;">Bintan is the Riau Islands' answer to those who say Singapore is too fast-paced. An hour by ferry from Tanjung Priok, this 1,750-square-kilometer island feels like stepping into a different universe — wide-open skies, mangrove-lined rivers thick with wildlife, beaches so pristine they could have been untouched for centuries, and resort complexes that redefine the word sanctuary.</p>
<p class="section-text fade-in-up" style="margin-bottom:18px;">The jewel in Bintan's crown is undoubtedly Chill Cove (formerly Treasure Bay), Southeast Asia's largest man-made crystal lagoon. The water — filtered, heated, and maintained to pristine standards — stretches for kilometers along Bintan's northeastern shoreline, bordered by white sand beaches that rival any in the Maldives or Seychelles.</p>
<p class="section-text fade-in-up">But Bintan offers far more than lagoons. Gurun Pasir, a rare golden sand dune system hidden deep within its tropical canopy, resembles an Saharan oasis transplanted to the equator. The Sebong River mangrove safari — a morning kayak through ancient mangrove tunnels followed by an evening firefly boat tour where thousands of synchronized fireflies illuminate the tree canopy in mesmerizing displays — is an experience visitors describe as unforgettable and transformative.</p>
<div style="margin-top:8px;" class="fade-in-up">
<a href="bintan.html" class="btn btn-green" style="background:var(--color-gold-sun);color:var(--color-ocean-deep);"><i class="fa-solid fa-map-marked-alt"></i> Full Bintan Guide</a>
</div>
</div>
</div>
</div>
</section>

<!-- MASONRY GALLERY: THINGS TO DO collage -->
<section class="dest-section">
<div class="container">
<span class="section-label fade-in-up">Curated Collection</span>
<h2 class="section-title fade-in-up" style="text-align:center;">Moments That Define Riau</h2>
<p class="section-text fade-in-up" style="margin:0 auto 48px;text-align:center;">From sunrise golf to midnight lagoon swims, every moment in the Riau Islands is designed to become a memory you carry home.</p>

<div style="display:grid;grid-template-columns:repeat(12,1fr);gap:16px;margin-top:40px;" class="fade-in-up">
<!-- Large gallery items -->
<div style="grid-column:span 5;border-radius:16px;overflow:hidden;height:380px;">
<img src="/images/batam-ocarina-adventure.jpg" style="width:100%;height:100%;object-fit:cover;" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&w=600&q=80';" alt="Thrilling cable wake riding at Batam Ocarina adventure park with water sports and zip-lining">
<div style="position:absolute;bottom:0;left:0;right:0;padding:20px;background:linear-gradient(transparent,rgba(10,31,63,0.9));color:white;"><p style="font-family:'Cormorant Garamond',serif;font-size:1.2rem;margin-bottom:4px;">Wakeboarding at Ocarina</p><p style="font-size:0.85rem;color:rgba(255,255,255,0.7);">Batam's most thrilling cable system</p></div>
</div>
<div style="grid-column:span 4;border-radius:16px;overflow:hidden;height:380px;">
<img src="/images/bintan-mangrove-kayak.jpg" style="width:100%;height:100%;object-fit:cover;" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1518709779311-83a73b5b4da2?auto=format&w=600&q=80';" alt="Kayaking through pristine mangrove tunnels on Sebong River in Bintan">
<div style="position:absolute;bottom:0;left:0;right:0;padding:20px;background:linear-gradient(transparent,rgba(10,31,63,0.9));color:white;"><p style="font-family:'Cormorant Garamond',serif;font-size:1.2rem;margin-bottom:4px;">Mangrove Kayak Safari</p><p style="font-size:0.85rem;color:rgba(255,255,255,0.7);">Sebong River biodiversity tour</p></div>
</div>
<div style="grid-column:span 3;border-radius:16px;overflow:hidden;height:380px;">
<img src="/images/golf-driving-range-sunset.jpg" style="width:100%;height:100%;object-fit:cover;" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?auto=format&w=600&q=80';" alt="Sunset driving range session at Batam golf course with floodlights turning on">
<div style="position:absolute;bottom:0;left:0;right:0;padding:20px;background:linear-gradient(transparent,rgba(10,31,63,0.9));color:white;"><p style="font-family:'Cormorant Garamond',serif;font-size:1.2rem;margin-bottom:4px;">Dusk Driving Range</p><p style="font-size:0.85rem;color:rgba(255,255,255,0.7);">Floodlit tee sessions with friends</p></div>
</div>

<!-- Wide gallery row -->
<div style="grid-column:span 6;border-radius:16px;overflow:hidden;height:300px;">
<img src="/images/bintan-gurun-pasir-dunes.jpg" style="width:100%;height:100%;object-fit:cover;" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?auto=format&w=600&q=80';" alt="Gurun Pasir golden sand dunes at Bintan with natural blue lake in the middle">
<div style="position:absolute;bottom:0;left:0;right:0;padding:20px;background:linear-gradient(transparent,rgba(10,31,63,0.9));color:white;"><p style="font-family:'Cormorant Garamond',serif;font-size:1.2rem;margin-bottom:4px;">Gurun Pasir – The Sands</p><p style="font-size:0.85rem;color:rgba(255,255,255,0.7);">Golden dunes and blue lake in Bintan's jungle heart</p></div>
</div>
<div style="grid-column:span 6;border-radius:16px;overflow:hidden;height:300px;">
<img src="/images/batam-grand-mall-dining.jpg" style="width:100%;height:100%;object-fit:cover;" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1555529669-e69e7aa0ba6a?auto=format&w=600&q=80';" alt="Grand Batam Mall interior with shoppers and international restaurant dining area">
<div style="position:absolute;bottom:0;left:0;right:0;padding:20px;background:linear-gradient(transparent,rgba(10,31,63,0.9));color:white;"><p style="font-family:'Cormorant Garamond',serif;font-size:1.2rem;margin-bottom:4px;">Grand Batam Mall</p><p style="font-size:0.85rem;color:rgba(255,255,255,0.7);">200+ shops, dining & entertainment hub</p></div>
</div>

<!-- Bottom row -->
<div style="grid-column:span 4;border-radius:16px;overflow:hidden;height:280px;">
<img src="/images/nagoya-hill-villa.jpg" style="width:100%;height:100%;object-fit:cover;" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&w=600&q=80';" alt="Luxury Nagoya Hill villa with swimming pool in Batam residential district">
<div style="position:absolute;bottom:0;left:0;right:0;padding:20px;background:linear-gradient(transparent,rgba(10,31,63,0.9));color:white;"><p style="font-family:'Cormorant Garamond',serif;font-size:1.2rem;margin-bottom:4px;">Nagoya Hill Living</p><p style="font-size:0.85rem;color:rgba(255,255,255,0.7);">Premium residential villas in Batam Center</p></div>
</div>
<div style="grid-column:span 4;border-radius:16px;overflow:hidden;height:280px;">
<img src="/images/batam-nightfood-scene.jpg" style="width:100%;height:100%;object-fit:cover;" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&w=600&q=80';" alt="Batam night food scene with satay grills, laksa, and durian stalls">
<div style="position:absolute;bottom:0;left:0;right:0;padding:20px;background:linear-gradient(transparent,rgba(10,31,63,0.9));color:white;"><p style="font-family:'Cormorant Garamond',serif;font-size:1.2rem;margin-bottom:4px;">Night Food Scene</p><p style="font-size:0.85rem;color:rgba(255,255,255,0.7);">Sizzling street food and luxury desserts</p></div>
</div>
<div style="grid-column:span 4;border-radius:16px;overflow:hidden;height:280px;">
<img src="/images/batam-hills-fairway.jpg" style="width:100%;height:100%;object-fit:cover;" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1535131749006-b7f58c99034b?auto=format&w=600&q=80';" alt="Batam Hills golf club rolling fairway with mountain backdrop">
<div style="position:absolute;bottom:0;left:0;right:0;padding:20px;background:linear-gradient(transparent,rgba(10,31,63,0.9));color:white;"><p style="font-family:'Cormorant Garamond',serif;font-size:1.2rem;margin-bottom:4px;">Batam Hills</p><p style="font-size:0.85rem;color:rgba(255,255,255,0.7);">Dramatic elevation-challenging golf course</p></div>
</div>
</div>

</div>
</section>

<!-- STATS BAR -->
<section class="stats-bar" style="background:linear-gradient(180deg,var(--color-ocean-deep) 0%,var(--color-ocean-mid) 100%);">
<div class="container">
<div class="stats-grid">
<div class="fade-in-up">
<div class="stat-number"><i class="fa-solid fa-ship" style="margin-right:8px;font-size:2.5rem;"></i></div>
<div class="stat-label">Two-hour ferry from Singapore and Tanjung Perok</div>
</div>
<div class="fade-in-up">
<div class="stat-number"><span style="font-size:3rem;">30+</span></div>
<div class="stat-label">Verified Attractions, Malls, Restaurants & Nature Spots</div>
</div>
<div class="fade-in-up">
<div class="stat-number"><span style="font-size:3rem;">6</span></div>
<div class="stat-label">Championship Golf Courses across Batam and Bintan</div>
</div>
<div class="fade-in-up">
<div class="stat-number"><span style="font-size:3rem;">$8K+</span></div>
<div class="stat-label">Average Entry Price for Premium Condominium in Batam Center</div>
</div>
</div>
</div>
</section>

<!-- SECTION: BATAM AND BINTAN SIDE-BY-SIDE COMPARISON -->
<section class="dest-section" style="background:#F8F6F1;">
<div class="container">
<span class="section-label fade-in-up">Dual Destination</span>
<h2 class="section-title fade-in-up" style="text-align:center;">Batam & Bintan — A Perfect Day Trip</h2>
<p class="section-text fade-in-up" style="margin:0 auto 48px;text-align:center;">Why choose? Many travelers spend their Riau Islands weekend split between both islands, waking to Batam's electric energy for morning wakeboarding and shopping, then taking the afternoon ferry to Bintan for a sunset lagoon swim and private beach dinner. We break down how to best combine both below.</p>

<div style="display:grid;grid-template-columns:1fr 1px 1fr;gap:48px;margin-top:32px;" class="fade-in-up">
<!-- Batam side -->
<div class="fade-in-up">
<img src="/images/batam-wakepark-aerial.jpg" style="width:100%;border-radius:16px;margin-bottom:20px;height:240px;object-fit:cover;" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&w=800&q=80';" alt="Aerial cable wakeboarding at Batam水上乐园 with multiple riders on the same line">
<h3 style="font-family:'Cormorant Garamond',serif;font-size:1.8rem;color:var(--color-ocean-deep);margin-bottom:12px;"><i class="fa-solid fa-bolt" style="color:var(--color-gold-sun);margin-right:10px;"></i>Batam Highlights</h3>
<ul style="font-size:0.95rem;color:var(--color-text-secondary);line-height:2;">
<li><strong>Cable Wakeboarding at Batam Wakepark & Ocarina</strong></li>
<li>The Six Barelang Bridges panoramic viewpoints</li>
<li>Grand Batam Mall — 200+ shops, cinema, food court</li>
<li>KKepri Golf & Country Club morning round</li>
<li>Nongsa seafood restaurants on rock formations</li>
<li>Batam Center night market — laksa, satay, durian</li>
<li>Tanjung Unggat beach sunrise walk</li>
<li>Hagane-no-yu hot springs at Bintan resorts</li>
</ul>
<div style="margin-top:16px;padding:20px;background:white;border-radius:12px;border-left:4px solid var(--color-gold-sun);">
<p style="font-size:0.9rem;color:var(--color-text-secondary);"><em>"I've flown to Thailand, Malaysia, and the Philippines for getaways. Batam's wakeboarding is genuinely better than most places I've tried — and half the price."</em></p>
</div>
</div>

<!-- Divider line -->
<div style="border-left:2px solid #EAE6DC;"></div>

<!-- Bintan side -->
<div class="fade-in-up">
<img src="/images/bintan-lagoi-bay-beach.jpg" style="width:100%;border-radius:16px;margin-bottom:20px;height:240px;object-fit:cover;" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1573843981263-d1e9aff8aa7f?auto=format&w=800&q=80';" alt="Lagoi Bay Bintan pristine white sand beach with turquoise lagoon and five-star resort pavilions">
<h3 style="font-family:'Cormorant Garamond',serif;font-size:1.8rem;color:var(--color-ocean-deep);margin-bottom:12px;"><i class="fa-solid fa-umbrella-beach" style="color:var(--color-gold-sun);margin-right:10px;"></i>Bintan Highlights</h3>
<ul style="font-size:0.95rem;color:var(--color-text-secondary);line-height:2;">
<li><strong>Chill Cove (Treasure Bay) — 4km crystal lagoon</strong></li>
<li>Gurun Pasir golden sand dunes & Blue Lake trek</li>
<li>Mangrove kayaking on Sebong River during daytime</li>
<li>Firefly night safari — thousands synchronized</li>
<li>Bukit Besar mountain hiking trail (moderate difficulty)</li>
<li>Ananda Bintan spa pavilions over water</li>
<li>Lagoi Bay Championship Golf at Anantara</li>
<li>Private beach dinner packages at Bintan Resorts</li>
</ul>
<div style="margin-top:16px;padding:20px;background:white;border-radius:12px;border-left:4px solid var(--color-green-lush);">
<p style="font-size:0.9rem;color:var(--color-text-secondary);"><em>"The moment we arrived at Chill Cove I thought we'd flown to the Maldives. The water clarity is unreal — absolutely breathtaking and completely serene."</em></p>
</div>
</div>
</div>
</div>
</section>

<!-- TRAVEL TIPS SECTION with images interspersed -->
<section class="dest-section">
<div class="container">
<span class="section-label fade-in-up">Plan Your Trip</span>
<h2 class="section-title fade-in-up" style="text-align:center;">Everything You Need to Know Before You Go</h2>
<p class="section-text fade-in-up" style="margin:0 auto 48px;text-align:center;">We've helped thousands plan their Riau Islands getaway. Here's our complete guide to the practical details that transform a good trip into a seamless one.</p>

<!-- Travel tip with inline image -->
<div class="fade-in-up" style="margin-bottom:48px;display:flex;gap:32px;align-items:center;background:white;border-radius:16px;padding:36px;box-shadow:0 2px 16px rgba(10,31,63,0.05);border:1px solid #EAE6DC;">
<img src="/images/ferry-singapore-batam.jpg" style="width:280px;border-radius:12px;flex-shrink:0;height:200px;object-fit:cover;" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&w=600&q=80';" alt="Fast ferry departing from Singapore HarbourFront terminal to Batam">
<div>
<h3 style="font-family:'Cormorant Garamond',serif;font-size:1.5rem;color:var(--color-ocean-deep);margin-bottom:10px;"><i class="fa-solid fa-ship" style="color:var(--color-gold-sun);margin-right:8px;"></i>Getting There</h3>
<p class="section-text" style="font-size:0.95rem;margin-bottom:12px;">Multiple ferry operators including Sinar Jaya, Majestic Fast Ferry, and Batamfast run twice-daily services from Singapore's HarbourFront Centre (just 4 stops before exiting the MRT) to both Batam Centre and Sekupang terminals. The crossing takes 45 minutes to Batam or 1 hour to Bintan, with departures every morning starting at 7:00 AM through late afternoon.</p>
<p class="section-text" style="font-size:0.95rem;margin-bottom:12px;">From Malaysia, the fastest route is by road from Johor Bahru to Tanjung Piandang (about 40 minutes), then a 20-minute ferry to Bintan's Bandar Batam Jubli Perak terminal. This route avoids Singapore entirely and is popular among Singaporean residents heading south via the Causeway.</p>
<p class="section-text" style="font-size:0.95rem;color:var(--color-green-lush);font-weight:600;"><i class="fa-solid fa-lightbulb" style="margin-right:6px;"></i>Pro tip: book your return ferry ticket online in advance during peak holiday periods (Chinese New Year, Golden Week) — they sell out 2-3 weeks ahead.</p>
</div>
</div>

<!-- Travel tip with inline image - right aligned -->
<div class="fade-in-up" style="margin-bottom:48px;display:flex;gap:32px;align-items:center;background:white;border-radius:16px;padding:36px;box-shadow:0 2px 16px rgba(10,31,63,0.05);border:1px solid #EAE6DC;flex-direction:row-reverse;">
<img src="/images/batam-visa-facilities.jpg" style="width:280px;border-radius:12px;flex-shrink:0;height:200px;object-fit:cover;" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&w=600&q=80';" alt="Indonesian visa on arrival facility counter at Batam airport">
<div>
<h3 style="font-family:'Cormorant Garamond',serif;font-size:1.5rem;color:var(--color-ocean-deep);margin-bottom:10px;"><i class="fa-solid fa-passport" style="color:var(--color-gold-sun);margin-right:8px;"></i>Visa &amp; Entry</h3>
<p class="section-text" style="font-size:0.95rem;margin-bottom:12px;">Citizens of over 40 countries including the US, UK, Australia, India, China, and most ASEAN nations qualify for a Visa on Arrival (VoA) at both Batam Centre and Bintan's terminals, valid for 30 days with a single extension possibility. The fee is IDR 350,000 (approximately SGD $32). Simply present your passport with 6+ months validity and onward ticket.</p>
<p class="section-text" style="font-size:0.95rem;margin-bottom:12px;">Singapore and ASEAN citizens can enter visa-free for up to 30 days. For longer stays or business visits, you may want the multiple-entry visa option available through the Batam Free Trade Zone Authority, which streamlines corporate travel documentation.</p>
<p class="section-text" style="font-size:0.95rem;color:var(--color-green-lush);font-weight:600;"><i class="fa-solid fa-lightbulb" style="margin-right:6px;"></i>Pro tip: bring your passport in the first place — many travelers attempt to enter Batam with just their ID card, which only works for Indonesian citizens.</p>
</div>
</div>

<!-- Travel tip with inline image -->
<div class="fade-in-up" style="display:flex;gap:32px;align-items:center;background:white;border-radius:16px;padding:36px;box-shadow:0 2px 16px rgba(10,31,63,0.05);border:1px solid #EAE6DC;">
<img src="/images/batam-hotel-luxury-pool.jpg" style="width:280px;border-radius:12px;flex-shrink:0;height:200px;object-fit:cover;" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1571896349842-33c89424de2d?auto=format&w=600&q=80';" alt="Luxury resort pool at Batam Centre with tropical landscaped garden and cabana seating">
<div>
<h3 style="font-family:'Cormorant Garamond',serif;font-size:1.5rem;color:var(--color-ocean-deep);margin-bottom:10px;"><i class="fa-solid fa-hotel" style="color:var(--color-gold-sun);margin-right:8px;"></i>Where to Stay</h3>
<p class="section-text" style="font-size:0.95rem;margin-bottom:12px;">Batam Center offers the convenience of central location — hotels like The Trans, Mega Mall Batam Centre, and Aston are steps from the ferry terminal, Grand Mall, and dining scenes. Nongsa is better for golf enthusiasts with access to Batam Hills and Nagoya Hill villas near international schools.</p>
<p class="section-text" style="font-size:0.95rem;margin-bottom:12px;">On Bintan, the choice splits between Lagoi Bay (resort-heavy, best for luxury weekenders), Teluk Bakau (more mid-range hotel options with direct beach access), and Bandar Bentan Telani (developing commercial district with new apartment supply).</p>
<p class="section-text" style="font-size:0.95rem;color:var(--color-green-lush);font-weight:600;"><i class="fa-solid fa-lightbulb" style="margin-right:6px;"></i>Pro tip: for first-time Bintan visitors, book a resort package at Anantara or Ayana Lagoi — the all-inclusive pricing (meals, spa credits, transport) often beats booking separately.</p>
</div>
</div>

</div>
</section>

<!-- CTA BAND -->
<section class="cta-band" style="position:relative;">
<div class="cta-bg"><img src="/images/rio-aerial-twilight.jpg" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&w=1920&q=80';" style="width:100%;height:100%;object-fit:cover;" alt="Aerial twilight view of the Riau Islands with thousands of fishing lights reflecting on calm waters"></div>
<div class="cta-overlay"></div>
<div class="container">
<span class="section-label fade-in-up" style="color:var(--color-gold-sun);font-size:0.8rem;letter-spacing:4px;text-transform:uppercase;">Begin Your Journey</span>
<h2 class="section-title fade-in-up" style="color:var(--color-white);font-size:clamp(2.2rem,5vw,3.8rem);">Your Riau Islands Adventure Awaits</h2>
<p class="section-text fade-in-up" style="color:rgba(255,255,255,0.75);max-width:640px;margin:0 auto 16px;font-size:1.1rem;">Whether your heart calls to Batam's electric streets and watersports thrill of Ocarina wakeboarding, Bintan's turquoise lagoons, a round on one of six championship courses, or an investment in this booming market — the Riau Islands have you covered.</p>
<p class="section-text fade-in-up" style="color:rgba(255,255,255,0.6);max-width:560px;margin:0 auto 36px;font-size:0.95rem;">Just 90 minutes from Singapore by ferry. No visa stress for most nationalities. And an experience that consistently ranks among the best weekend escapes in all of Southeast Asia.</p>
<div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap;" class="fade-in-up">
<a href="batam.html" class="btn btn-primary"><i class="fa-solid fa-city"></i> Batam</a>
<a href="bintan.html" class="btn btn-outline"><i class="fa-solid fa-umbrella-beach"></i> Bintan</a>
<a href="golf.html" class="btn btn-outline"><i class="fa-solid fa-golf-ball-tee"></i> Golf Guide</a>
<a href="contact.html" class="btn btn-outline"><i class="fa-solid fa-chart-line"></i> Invest</a>
</div>
</div>
</section>

<!-- FOOTER -->
<footer class="site-footer">
<div class="container">
<div class="footer-grid">
<div class="footer-brand">
<div class="footer-logo">Riau<span>Escapes</span></div>
<p>Your definitive guide to experiencing the Riau Islands — from Batam's urban rush and coastal thrill to Bintan's luxury sanctuaries, championship golf, and smart investment opportunities.</p>
<div class="footer-socials">
<a href="#"><i class="fa-brands fa-facebook-f"></i></a>
<a href="#"><i class="fa-brands fa-instagram"></i></a>
<a href="#"><i class="fa-brands fa-youtube"></i></a>
<a href="#"><i class="fa-brands fa-twitter"></i></a>
</div>
</div>
<div>
<h4 class="footer-heading">Explore</h4>
<div class="footer-links">
<a href="batam.html">Batam Island Guide</a>
<a href="bintan.html">Bintan Luxury Guide</a>
<a href="golf.html">Golf Courses Directory</a>
<a href="contact.html">Contact Us</a>
</div>
</div>
<div>
<h4 class="footer-heading">Plan</h4>
<div class="footer-links">
<a href="#discovery">Getting There</a>
<a href="#">Visa Information</a>
<a href="#">Ferry Schedules</a>
<a href="#">Accommodation Guide</a>
</div>
</div>
<div>
<h4 class="footer-heading">Contact</h4>
<div class="footer-contact-item"><i class="fa-solid fa-location-dot"></i><span>Nagoya Hill, Batam Center, Riau Islands, Indonesia 29432</span></div>
<div class="footer-contact-item"><i class="fa-solid fa-phone"></i><span>+62 778 123 456</span></div>
<div class="footer-contact-item"><i class="fa-solid fa-envelope"></i><span>hello@riauescapes.id</span></div>
<div class="footer-contact-item"><i class="fa-solid fa-clock"></i><span>Sun-Thu: 9AM-6PM | Fri-Sat: 10AM-4PM WIB</span></div>
</div>
</div>
<div class="footer-bottom">
<p>2026 RiauEscapes. All rights reserved. | Privacy Policy | Terms of Service</p>
</div>
</div>
</footer>

<script src="js/app.js"></script>
</body>
</html>''')

target = r'C:\Users\user\Riau Escapes\index.html'
content = '\n'.join(lines)
with open(target, 'w', encoding='utf-8') as f:
    f.write(content)

import os
size = os.path.getsize(target)
print(f'SUCCESS: {size:,} bytes written to {target}')
