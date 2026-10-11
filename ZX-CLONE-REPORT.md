# Reference reconstruction — delta report

**Outcome: STATIC IMPLEMENTATION COMPLETE — RENDERED FIDELITY UNVERIFIED (mode V3).**
No Fidelity Score is given. This session had no Shopify store credentials or CLI, so the theme
was never uploaded or rendered. Functional gates (add to cart, variant switching, cart, search,
checkout) are **UNVERIFIED** until the theme is previewed on a store.

- Mode: **B**, reference reconstruction. The layout, spacing, type scale and colour system come from
  the reference. Its brand name, logo, photography, product data, founder quote and signature are
  **not** copied. All copy is placeholder text you can edit.
- Reference: public storefront, measured with headless Chromium at 1440px and 390px (E3 computed
  styles) for the homepage. The reference product and collection URLs returned 404 at measurement
  time, so those pages were built from the screenshots you supplied (E6).
- Host: Shopify **Horizon 4.1.4** (theme blocks, `{% stylesheet %}` idiom). The full Horizon base is
  now in this repo, so the branch is a complete uploadable theme.

## Measured tokens (reference, 1440px)

| Token | Value | Source |
|---|---|---|
| Ink (all text) | `#3A080A` | computed style |
| Announcement / badge strip | `#FDE8E0` | computed style |
| Badge text | `#6E2132`, 14px condensed uppercase | computed style |
| Sale price | `#E41929` | pixel sample |
| Image tile background | `#F5F5F5` | pixel sample |
| Section title | serif 28px / 30px, 24px bottom padding, centred | computed style |
| Product card | 250px wide, 8px gap, 1:1 tile, 24px badge strip, 44px outlined CTA (1px ink, 16px condensed bold uppercase) | computed style |
| Page gutter | 32px | computed style |
| Category tiles | 4 × 294px, 16px gap, centred, 16px caption | computed style |
| Letter spacing | 0.5px throughout | computed style |

## Section coverage

| Page | Reference element | Build | Tier |
|---|---|---|---|
| Global | Blush announcement bar | Horizon `header-announcements` configured | L0 |
| Global | Centred logo, locale left, icons right, uppercase menu row below | Horizon `header` configured | L0 |
| Home | Full-bleed hero, script heading, rose CTA on right | `zx-hero-banner` | L4 |
| Home | Shop By Category, 4 tiles | `zx-category-tiles` | L4 |
| Home | Product rail with arrows + "Shop …" link | `zx-product-rail` | L4 |
| Home | Pink promo banner, left text | `zx-promo-banner` | L4 |
| Home | Holiday Magic tiles on grey band | `zx-category-tiles` (band on) | L4 |
| Home | Shop Best Sellers rail | `zx-product-rail` | L4 |
| Home | "Legendary … For A Reason" video panel + pillars | `zx-legendary` | L4 |
| All | 6-up service icon strip | `zx-service-strip` | L4 |
| All | 3 link columns + newsletter + social, quote band, payment icons, legal | `zx-footer` | L4 |
| Collection | Title, intro, sub-category thumbnails | `zx-collection-hero` | L4 |
| Collection | 4-column grid, promo tiles in the grid, sort, filters, pagination | `zx-main-collection` | L4 |
| Product | Thumbnails left + main image | Horizon `_product-media-gallery` (carousel, thumbnails left) | L1 |
| Product | Badge, uppercase title, subtitle, price with installments | `zx-product-badge`, Horizon text/price, `zx-product-field` | L1/L3 |
| Product | Shade swatches, add to bag, sticky bar | Horizon `variant-picker`, `buy-buttons`, sticky add-to-cart | L0 |
| Product | Promo box, "Discover the magic" list, accordions, exclusives | `zx-promo-box`, `zx-feature-list`, Horizon `accordion` + `zx-product-field` | L3 |
| Product | Use It With rail | `zx-product-rail` (product recommendations) | L4 |

## Deviation register

| # | Item | Reason | Cost |
|---|---|---|---|
| D1 | Fonts: Helvetica Neue LT / Vanitas are licensed fonts → Inter (body), Archivo Narrow (condensed), Playfair Display (serif) | Licensing; Shopify font library only. `helvetica_n4` is deprecated (theme-check) | Medium: serif headings are the most visible difference |
| D2 | Wishlist hearts omitted | No wishlist backend; a static heart would fake a feature | Low |
| D3 | Card "Add to bag" posts to `/cart/add` and lands on the cart page. It does not open the drawer | Horizon's drawer is driven by a promise-based `@shopify/events` API; a native form is the safe functional choice | Low-medium |
| D4 | Product page: "Smooth it. Blur it." image carousel and product video omitted | No content source; an empty video block would ship a placeholder | Low |
| D5 | Loyalty coins line omitted | Needs a loyalty app (not installed) | Low |
| D6 | Service strip and announcement copy are neutral ("Delivery & Returns — see our shipping policy"), not the reference's offers | Free delivery, free samples and loyalty are business promises with no verified source | Low (structure identical) |
| D7 | Founder quote, signature and imagery are placeholders | Brand assets and copy can't be reused | Low (structure identical) |
| D8 | Accordion rows read `custom.highlights`, `custom.ingredients`, `custom.how_to_use` metafields; they show a neutral fallback when the metafield is empty | No fabricated product data | None |

## Modification ledger

- **Added (additive):** the full Horizon 4.1.4 base, 9 `zx-` sections, 6 `zx-` blocks, 3 `zx-` snippets.
- **Replaced (store-facing config):** `templates/index.json`, `templates/collection.json`,
  `templates/product.json`, `sections/footer-group.json`. The previous Kidsora versions are in git
  history at commit `fe9f707`. Revert with `git checkout fe9f707 -- <file>`.
- **Configured:** `sections/header-group.json` (Horizon header/announcement settings only).
- **Deep-merged:** `config/settings_data.json` = Horizon defaults + the tokens above (fonts, palette,
  radius 0, uppercase buttons, blush sale badge). Every select value was checked against
  `settings_schema.json`.
- **Untouched:** all Horizon core Liquid/JS/CSS. The old `kidsora-*` sections are kept, unreferenced.

## Verification run here

- `@shopify/theme-check-node` (latest): **0 errors**. Remaining warnings: `ValidScopedCSSClass` on
  the shared `zx-` classes, which are defined once in `snippets/zx-brand-styles.liquid` on purpose,
  plus 7 warnings already present in stock Horizon.
- All template JSON parses. Section and block types resolve.

## Assets checklist (your content)

| Slot | Spec |
|---|---|
| Hero desktop / mobile | 2880×1100 (≈2.6:1) / 1170×1560 (3:4); keep the right ~45% clear for the heading on desktop |
| Category & Holiday tiles | 8 square images, ≥800×800 |
| Promo banner | 2880×820, text area on the left 45% |
| Legendary panel | 16:9 MP4 (muted loop) or image ≥1400px wide |
| Collection sub-category thumbs | square ≥240×240 |
| Grid promo tiles | portrait ≥700×1100 |
| Footer quote band | 2 images ≥800×600 + transparent signature PNG |
| Product media | square (1:1) packshots on light grey/white for the reference look |
| Logo | SVG or PNG, upload in Header → Logo |
| Product badges | `custom.badge` metafield (single-line text) or a `badge:New!` tag |

## Boundary actions (for you)

1. **Permission:** connect this repo/branch to your store (Online Store → Themes → Add theme →
   Connect from GitHub) or upload a zip of the branch. It installs as an **unpublished** theme.
2. **Publishing:** preview it and publish only once you've approved it. I never publish.
3. **Private decision:** replace the placeholder copy (announcement, hero, promo, service strip,
   founder quote) with your real offers and policies, and confirm the collection handles used on the
   homepage and collection header (`new-in`, `best-sellers`, `baby-0-3y`, `sets`,
   `blankets-swaddles`, `diaper-bags`, `footwear-accessories`).
4. **Capability:** once it's on a store, run a preview pass to check add-to-cart, variant swatches,
   filters and the recommendations rail. That render is what would allow a scored V1 verification.
