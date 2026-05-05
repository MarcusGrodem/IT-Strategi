# Omnichannel Success in Grocery Retail
## Research Report for Coop Denmark IT Strategy

*Date: May 2026 | Research scope: Global grocery omnichannel leaders*

---

## Executive Summary

Grocery omnichannel has crossed a decisive threshold. Nearly **94% of grocery shoppers purchase both online and in-store**, and online grocery now represents 10% of global grocery sales — up 18% year-over-year. Omnichannel retailers dominate with **45.78% of market revenue**, and total online grocery is projected to reach $452 billion (25.5% of grocery sales) by 2028.

Retailers that have built the underlying digital infrastructure — loyalty data, personalization engines, flexible fulfillment, and app ecosystems — are pulling decisively away from the field. The window for strategic differentiation is now.

---

## Part 1: Who Succeeded and How

### Albert Heijn (Netherlands) — The European Benchmark

Albert Heijn (Ahold Delhaize) is widely regarded as Europe's strongest omnichannel grocery operator. Their transformation began with an explicit repositioning as a **"food and tech company"** rather than a supermarket.

**Key metrics:**
- App grew from 200,000 monthly users to **5 million monthly users** (3.5M monthly active), adding 50,000 new users per week
- Digital sales = **15% of total revenue**, outpacing all European peers
- **7 million+ active Dutch households** on the Bonuskaart loyalty program
- 16% conversion rate on loyalty program using personalized in-app messaging

**What drove success:** The Bonuskaart loyalty card — decades-old and deeply embedded in Dutch consumer behavior — was digitized into the app, creating a seamless online/in-store offer system. Sophisticated CRM with personalized push notifications, combined with the unified customer identity across all channels, enabled true individual-level marketing.

---

### Kroger (USA) — The Data Company That Sells Groceries

Kroger's story is fundamentally about **84.51°**, a dedicated data analytics subsidiary built on loyalty card data from 60+ million U.S. households.

**Key metrics:**
- Digital sales exceeded **$13 billion** in fiscal year 2024 (+10% YoY); delivery sales up 18% in Q4
- **4 billion personalized recommendations** delivered annually
- Omnichannel customers spend **3–4x more** than in-store-only customers
- Retail media revenue (Kroger Precision Marketing): **$4B+** annually at 40%+ margins

**What drove success:** Rather than buying analytics as a service, Kroger built 84.51° as a **standalone proprietary subsidiary**. All models are in-house. The data asset (60M+ household purchase histories) compounds in value annually and is monetized by selling advertising and insights to CPG brands — a self-reinforcing flywheel competitors cannot easily replicate.

**Cautionary note:** Kroger is closing 3 robotic CFCs and paying $350M to exit Ocado agreements. Over-investment in large-scale automated fulfillment (designed for predictable, batch-wave ordering) conflicted with how American consumers actually shop online for groceries (same-day, unpredictable). Build demand certainty before investing in capital-intensive fulfillment infrastructure.

---

### Tesco (UK) — AI-Powered Loyalty at Scale

Tesco operates the UK's most sophisticated loyalty ecosystem through its Clubcard, now enhanced with AI-driven gamification.

**Key metrics:**
- **289 million personalized vouchers** delivered in 2024 to 7.6 million customers (38 per customer/year)
- Up to **98% open rates** on app push notifications via Customer Data Platform
- 10% profit growth and 4% sales growth in H1 2024 driven by personalized campaigns
- "Clubcard Challenges" (AI-generated personalized tasks for up to £50 rewards): won "Best Global Loyalty Launch/Initiative" 2025

**What drove success:** The Eagle Eye platform powers AI personalization at scale. Every offer is generated, delivered, and attributed in a closed loop: CDP → personalization engine → app push → POS redemption → analytics. The result is 98% open rates — only achievable when the offer is genuinely relevant to the individual.

---

### Walmart (USA) — Physical Store as Fulfillment Engine

Walmart turned its unmatched store footprint into an omnichannel asset by treating stores as last-mile fulfillment hubs.

**Key metrics:**
- U.S. e-commerce: **18% of sales**; global e-commerce surpassed **$100 billion**
- Same-day delivery coverage: **93% of U.S. households**
- Omnichannel shoppers spend average **$1,044/month**, 3x more frequent, 13% more items per order
- Online grocery market share reached **record 37%** in Q2 2024

**What drove success:** 50%+ of online orders fulfilled from local stores, not warehouses. In-store integration: QR shelf codes, in-app aisle maps, real-time status updates. Site traffic up 30% over two years. Walmart Connect retail media generating **$4.4B annually**.

---

### ICA Gruppen (Sweden) — Nordic Personalization Leader

ICA Sverige operates as a franchise-cooperative model (stores are independently owned) — the most structurally comparable case to Coop Denmark.

**Key metrics:**
- **5+ million Stammis loyalty members**
- Offer redemption rate **quadrupled to 22–42%** after hyper-personalization deployment
- Campaign cycle compressed from 3–5 weeks to **near real-time**

**What drove success:** ICA went from 99% paper-based communications (3–5 week campaign cycles) to near-real-time personalized digital offers via a TCS-built real-time marketing data hub. The platform:
- Aggregates purchase data continuously across all franchise stores
- Enables both personalized (based on history) and goal-based offers ("buy 3 more produce items this week")
- Unified customer identity across all independently-owned stores

---

### Coop Norge (Norway) — Cooperative Paper-to-Digital Transformation

**Key metrics:**
- **86% app uptake** after trial period — cited as "global best in class" by Dunnhumby
- **70% of coupons now redeemed via app** (up from near-zero)
- 1,250+ stores; launched Omnium Order Management System (OMS) in 2025 for omnichannel order routing

**What drove success:** Cooperative members responded extremely well to digital equivalents of paper coupons. Customer segmentation and offer personalization via Dunnhumby data science drove both adoption and behavior change.

---

### Coop Denmark — Current State Baseline

Coop Danmark is Denmark's largest grocery retailer, a consumer-owned cooperative with 2 million members and 1,150+ stores.

**Current digital capabilities:**
- **1.8 million app users = 25% of Danish households**; #1 on both App Store and Google Play
- App users: **50% higher repeat purchase rates** than non-app customers
- Prepaid Food account users: **21% higher in-store spend**
- Peak daily active users: **250,000**; retention rate: **55%**
- Gamification: **24.8 million game sessions** in-app in 2020 alone

**Current tech stack:**
- SAP S/4HANA: modernized ERP foundation (deployed 2022)
- RELEX: Unified Store Portal for retail planning
- Scandit SDK: self-scanning (Scan & Betal) across 1,150 stores
- Lobyco: loyalty platform and promotions engine
- Azure: cloud (but <20% of systems currently cloud-native)
- Legacy: 50-year-old mainframe backend, decade-old POS, .NET middle layer

**Key incident (instructive):** The loyalty app launch caused checkout system failures across stores on a busy Saturday. AI-powered APM identified the cloud resource issue within 2 minutes, preventing closure of 500 stores. Monitoring is now a strategic capability, not optional.

---

### Sainsbury's (UK) — Scan-and-Go at Scale

Sainsbury's SmartShop is a 10-year-old scan-and-go program scaled to 1,400+ stores.

**Key metrics:**
- SmartShop sales up **173%** YoY
- In stores with SmartShop handsets, **30% of sales** generated through the app

---

### Lidl — Discount Format, Digital Loyalty

Even hard-discount retailers can win with digital loyalty.

**Key metrics:**
- **Lidl Plus app: 35+ million European users**
- +5.7% sales growth in Germany 2024, outperforming competitors
- Basket size lifted through targeted personalized coupons

---

### Amazon Fresh — The Cautionary Technology Tale

Amazon's Just Walk Out (JWO) frictionless checkout was removed from U.S. Fresh stores in April 2024 and replaced with Dash Carts. The JWO system relied heavily on computer vision and reportedly required large numbers of human reviewers.

**Lesson:** Technology that prioritizes novelty over customer value and operational unit economics fails at scale. Amazon is now licensing JWO to airports and stadiums — formats where the value proposition fits — while Fresh stores adopt the less capital-intensive approach.

---

## Part 2: Common Denominators of Success

### 1. The Loyalty Program as Data Foundation

Every successful case has a high-penetration loyalty program at its core — not primarily as a discount mechanism, but as **data collection infrastructure**.

- Loyalty data ties together online and offline purchase history into a **single customer view**
- Digital shift of the loyalty card (from physical card/paper to app) is the single highest-impact move
- Programs with 5M+ members and weekly active engagement represent a durable competitive moat
- Key metrics to track: offer redemption rate, app weekly active users, new user growth per week

### 2. Personalization Engine at Industrial Scale

- Moving from segment-level to **individual-level offers** is the core capability gap separating leaders from followers
- Personalized offers achieve **3x higher redemption rates** vs. generic promotions
- Digital coupons achieve **7% redemption** vs. 1% for print, cost **85% less** to distribute, and provide full attribution
- Grocers using predictive analytics for promotions report **15% higher customer satisfaction** and **20% higher loyalty participation**
- Near-real-time capability (vs. 3–5 week campaign cycles) is the standard among leaders

### 3. The App as the Convergence Point

The grocery app is where omnichannel succeeds or fails. Leading apps combine:

| Capability | Why it matters |
|---|---|
| Loyalty/rewards + real-time offer visibility | Primary reason to open the app daily |
| Scan-and-pay / self-checkout | Replaces checkout habit entirely; the app becomes the transaction |
| Digital circular / weekly deals | Eliminates paper, enables personalization |
| Meal planning + recipes | Keeps customer in ecosystem; increases basket size |
| Online ordering + click-and-collect | Fulfillment flexibility |
| Gamification | Drives frequency through engagement loops |
| Push notifications (personalized) | Tesco achieves 98% open rates — only possible with genuine relevance |

### 4. Store as Fulfillment Hub

- Leading retailers fulfill **50–80%+ of online orders from stores**, not warehouses
- Click-and-collect (BOPIS) now outpaces home delivery in shopper preference (31% vs 29%)
- Same-day / 2-hour delivery expectation is now baseline
- Dark stores (store-based micro-fulfillment) are the economical middle ground

### 5. IT Architecture: Moving Away from Monoliths

Common technology patterns among leaders:

- **Cloud-first**: Carrefour targeting 100% cloud by 2026; Coop Denmark on Azure
- **Microservices / API-first (MACH architecture)**: enables faster feature delivery, reduces integration debt
- **Modern OMS**: critical for routing orders intelligently across channels
- **ERP modernization**: SAP S/4HANA is the dominant choice
- **Real-time inventory visibility**: prerequisite for any fulfillment capability
- **Application Performance Monitoring**: non-negotiable when loyalty and POS are integrated

### 6. First-Party Data as a Profit Center (Retail Media)

The emerging strategic layer: loyalty data monetized through **Retail Media Networks**.

- Grocery first-party data is the most valuable in retail — weekly purchase frequency creates rich behavioral signals
- Data monetization through retail media adds 1–2% revenue lift at **40%+ profit margins** — far above core grocery margins
- For cooperatives specifically: retail media revenue can fund digital investment without requiring price increases for members

### 7. Organizational Integration

The most-cited failure mode: treating omnichannel as an e-commerce team project rather than an enterprise-wide operating model.

- Successful leaders integrate pricing, promotions, inventory, fulfillment, loyalty, and customer service into **one customer-facing system**
- Separate goals and metrics per channel = guaranteed siloing
- McKinsey: "omnichannel cannot be relegated to ecommerce teams alone"

---

## Part 3: IT Strategy Specifics

### Technology Stack of Leaders

| Layer | What leaders chose | Why it matters |
|---|---|---|
| ERP | SAP S/4HANA | Single source of truth for inventory, finance, supply chain |
| OMS | Omnium (Coop Norge), Manhattan Associates | Routes orders intelligently across channels |
| Loyalty platform | Eagle Eye (Tesco), Lobyco (Coop DK), Dunnhumby (Coop Norge) | Personalized offers, omnichannel redemption |
| CDP/Personalization | 84.51° (Kroger), TCS real-time hub (ICA) | Unifies customer identity across channels |
| Scan/Payment SDK | Scandit (Coop DK, others) | Reliable barcode scanning across device types |
| Cloud | Azure (Coop DK), GCP (Carrefour) | Scalability, microservices, reduced legacy dependency |
| APM/Monitoring | New Relic / Dynatrace-class tools | Critical when app failures cascade into checkout failures |
| Supply chain planning | RELEX (Coop DK) | Unified store portal, demand planning |

### The 84.51° Model — In-House Data as Strategy

Rather than buying analytics as a service, Kroger built 84.51° as a **standalone subsidiary**:
- Proprietary algorithms and models — not vendor-dependent
- Data asset (60M+ household histories) compounds in value annually
- Revenue from CPG advertising and insights funds the analytics capability
- Result: a self-reinforcing data flywheel that competitors cannot easily replicate

The key question for Coop Denmark: is the equivalent capability (Lobyco + partners) creating a proprietary data asset, or a vendor-dependent one?

### Tesco CDP + Eagle Eye Architecture

CDP aggregates all touchpoints → Eagle Eye personalization engine → AI-optimized individual offers → app push with ~100% open rates → POS redemption → attribution. The loop is closed in near-real time.

### ICA's Near-Real-Time Marketing Hub

From 3–5 week paper campaign cycles to near-real-time personalized digital offers:
- Aggregates purchase data continuously across all franchise stores
- Supports both purchase-history personalization and goal-based offer mechanics
- Eliminated weeks of campaign lead time
- Result: redemption rates 4x higher (22–42% vs. ~5–7% baseline)

---

## Part 4: Cooperative-Specific Considerations

### Structural Advantages

1. **Member data is consent-rich** — cooperative members have historically opted into data relationships more willingly; GDPR compliance is more straightforward
2. **Member loyalty is attitudinal, not just transactional** — members already have identity and financial investment in the cooperative; digital tools activate latent loyalty
3. **Trust premium** — personalization and data use is more acceptable when members understand it benefits the collective

### Structural Challenges

1. **Decentralized governance** — cooperative structure can slow IT investment decisions requiring member approval; ICA's franchise model shows the complexity of standardizing digital experiences across independently-owned stores
2. **Lower margins limit capital for digital investment** — retail media revenue can bridge this gap structurally
3. **Member engagement varies** — active members are already engaged; passive members (often representing the largest revenue pool) need different activation strategies

### Cooperative-Specific Success Patterns

- **Coop Denmark's Prepaid Food account**: members prepay into an account and spend 21% more in-store — a cooperative mechanic (members feel they're spending "already-owned" funds) that drives behavior impossible to replicate at non-cooperative retailers
- **Coop Norge**: paper-to-digital coupon transition achieved 86% app uptake in trial — cooperative members respond extremely well to digital equivalents of familiar member benefits
- **ICA Sverige**: solved the franchise/member identity challenge by unifying customer IDs across all stores regardless of ownership — the prerequisite for any cross-store personalization

---

## Part 5: Common Pitfalls to Avoid

### 1. Channel Siloing Disguised as Omnichannel
Launching an app and a website with separate inventory systems, different pricing, and no shared customer identity is not omnichannel. True omnichannel means one customer record, one inventory view, one promotion engine — regardless of channel.

### 2. Over-Investing in Expensive Automation Before the Digital Foundation Is Set
Kroger paid $350M to exit robotic CFC agreements. The CFC model assumes predictable, batch-wave ordering — not how consumers actually shop online for groceries. Build demand certainty before investing in capital-intensive fulfillment infrastructure.

### 3. Technology Novelty Over Customer Value
Amazon's Just Walk Out: frictionless checkout is appealing in theory, but the customer value proposition (saving 2–3 minutes while losing real-time receipt visibility) was insufficient. Technology must solve a problem customers actually have.

### 4. App Without Engagement Loop
Apps that only replicate the paper circular digitally have low retention. Leading apps create weekly/daily habits through real-time offer personalization (reason to open), gamification (reason to return), scan-and-pay (the app becomes the transaction), and meal planning (becomes part of the cooking workflow, not just shopping).

### 5. Integration Failures at Scale
Coop Denmark's launch incident (loyalty app causing checkout failures at 500 stores) is the clearest local example. When the loyalty app integrates with POS at 500+ stores, any cloud resource issue can cascade. APM/monitoring and DevOps practices (observability, continuous deployment) must replace traditional ITSM approaches before scaling.

### 6. Ignoring Fulfillment Economics
Online grocery is structurally low-margin. Manage this by pushing click-and-collect over home delivery (lower cost to serve), using stores as fulfillment hubs, growing basket size through personalization (offsets per-order fulfillment cost), and monetizing the digital channel through retail media.

### 7. Legacy Systems as a Handbrake
Coop Denmark's hybrid environment — 50-year-old mainframe, decade-old POS, <20% on cloud — means every new omnichannel capability must be built around legacy systems, increasing integration complexity and deployment risk. The SAP S/4HANA migration (2022) was a necessary foundation; POS modernization and expanding the cloud-native microservices layer are the logical next priorities.

---

## Part 6: Key Metrics and Benchmarks

### Spending Impact of Omnichannel
| Metric | Source |
|---|---|
| Omnichannel customers spend 3–4x more than in-store only | Kroger |
| Omnichannel customers shop 1.7x more frequently | Kroger |
| App users: 50% higher repeat purchase rates | Coop Denmark |
| Prepaid account users: 21% higher in-store spend | Coop Denmark |
| Omni-shoppers: 3x more frequent, 13% more items, $1,044/month | Walmart |
| Brands with strong omnichannel: 9.5% annual revenue increase vs. 3.4% for weak | McKinsey |

### Loyalty Program Impact
| Metric | Source |
|---|---|
| ICA offer redemption: ~5–7% → 22–42% after personalization | ICA/TCS |
| Coop Norge: 70% of coupons now redeemed via app | Dunnhumby |
| Tesco: 289M personalized vouchers in 2024; 98% push open rates | Eagle Eye |
| Albert Heijn: 16% conversion on loyalty using personalized in-app messaging | McKinsey |
| Digital coupons: 7% redemption vs. 1% print; 85% cheaper to distribute | FMI |

### App Scale Benchmarks
| Retailer | Scale |
|---|---|
| Lidl Plus | 35M+ European users |
| Albert Heijn | 5M monthly users, +50K/week |
| ICA Stammis | 5M+ members |
| Tesco Clubcard | 7.6M active users receiving personalized vouchers |
| Coop Denmark | 1.8M users = 25% of Danish households |
| Coop Norge | 86% app uptake among members |

### Market Context
- Online grocery will reach **25.5% of grocery sales** by 2028 (U.S.; Nordic markets typically 1–2 years behind)
- Click-and-collect now at **31% shopper preference** vs. 29% home delivery
- Retail media data monetization: **1–2% revenue lift at 40%+ profit margin**
- Digital grocery sales: 4% growth in 2024; projected **9.7% growth in 2025**

---

## Part 7: Strategic Implications for Coop Denmark

Based on the cross-case analysis, the following priorities emerge as highest-impact given Coop Denmark's current state:

### Foundation (Already Underway — Maintain)
- SAP S/4HANA deployment (2022) ✓
- RELEX for retail planning ✓
- Lobyco loyalty platform ✓
- Scandit for Scan & Betal ✓
- APM/monitoring capability ✓

### High-Priority Gaps vs. Leaders

1. **Personalization at individual scale** — ICA went from 5–7% to 22–42% offer redemption by switching from segment-level to individual-level offers in near-real time. The question is whether Lobyco + Coop's data infrastructure can generate true individual-level offers, or whether a CDP layer is needed.

2. **Cloud-native migration** — At <20% of systems on Azure, the current architecture creates cascading risk as the app scales. Leaders are at 30–100% cloud. POS modernization is the hardest and most impactful piece.

3. **Retail media network** — First-party data from 1.8M app users and 2M members is a highly monetizable asset. At 40%+ margins, retail media revenue can fund digital investment without member price impact.

4. **Fulfillment infrastructure** — Whether to invest in click-and-collect, dark stores, or home delivery depends on Danish market demand patterns, but the Kroger-Ocado cautionary case argues for starting with store-fulfillment and scaling only with demonstrated demand.

5. **The ICA franchise model lesson** — If Coop's cooperative structure creates barriers to standardizing digital experiences across stores, solving the governance model is a prerequisite for consistent omnichannel execution.

---

## Sources

Research draws on:
- McKinsey: "The winning formula: What it takes to build leading omnichannel operations"; "Winning with Customers: The Albert Heijn Success Formula"
- BCG: "First-Party Data Is Retail's Next Growth Engine" (2023)
- NIQ/Nielsen: "Online Grocery Sales Power Omnichannel Growth" (2026)
- FMI: Omnichannel industry research
- Dunnhumby: Coop Norge case study
- Eagle Eye: Tesco Clubcard Challenges case study
- PostNord: "E-commerce in the Nordics 2025"
- Grocery Doppio: Kroger/Walmart digital performance tracking
- Diginomica: Coop Danmark digital transformation reporting
- Scandit, Lobyco, RELEX: Coop Denmark implementation case studies
- Grocery Dive: Kroger-Ocado and Amazon Fresh reporting
- TCS: ICA Sverige hyper-personalization case study
- Internet Retailing: Coop Denmark technology vision reporting
