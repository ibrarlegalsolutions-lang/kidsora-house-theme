# Insaf Fabrics: Umar Fabrics-style rebuild of Dawn 15.5.0: QA report

**Outcome: IMPORT-READY.** Not FULLY TESTED: I had no preview of the new theme, so nothing has been checked in a browser yet (see §5).

- ZIP: `insaf-fabrics-dawn-umar-style-v1.zip`, 394 files, 1,067,740 bytes
- SHA-256: `035ee4ba20a5301c2482f65990ca3cafc1a969d3d923bb9e314071ab723afb94`
- Source: `theme_export__insaffabricsofficial-com-dawn__25SEP2026-0446pm.zip` (left unchanged, SHA-256 `46a97492…`)
- Mode: SINGLE_REFERENCE. The only reference was 3 screenshots of Umar Fabrics (collection, product page, homepage). I had no live site to inspect, so all sizes are estimated from the screenshots, and hover and scroll behaviour was not seen.

## 1. What each reference section became
| Reference element | How it was built |
|---|---|
| Tan announcement bar | Dawn announcement bar using the new tan colour scheme `scheme-3` (#D2B48C, sampled from the screenshot) |
| Logo row with a full-width tan menu band | Header set to logo position `top-left`. The band is scoped CSS in `assets/zx-storefront.css`. Its colours are in **Theme settings › Storefront style** |
| Centred uppercase section titles with lines | CSS on Dawn titles (featured collection, collection list, multicolumn, related products) and the new sections. Can be turned off |
| 4-column portrait product cards with a full-width outlined **ADD TO CART** | Dawn card with `quick_add: standard`, centred card text, portrait image ratio |
| Black **SHOW MORE** button under grids | Dawn "View all" button (solid) |
| Two-image lifestyle banner | New section **Dual image banner** (`zx-dual-banner`) |
| "Shop by brand" / "Wedding wear" tabbed product grids | New section **Collection tabs** (`zx-collection-tabs` + `zx-tabs.js`). Accessible tablist that works with the arrow keys. Used twice: *Shop by collection* and *Winter collection* |
| Google Map with a "Find a store" button | New section **Store map** (`zx-store-map`). Google Maps embed built from the address setting |
| Breadcrumbs on collection and product pages | New section **Breadcrumbs** (`zx-breadcrumbs`) |
| Product page: availability, title, price, qty, solid ADD TO CART, outlined BUY IT NOW, green WhatsApp button, Description/Shipping/Order & Returns accordions | Native Dawn blocks plus CSS that swaps the button styles. WhatsApp button = snippet `zx-whatsapp-order` rendered by a custom-Liquid block. Shipping and returns text reuses the store's own FAQ copy |
| Dark 4-column footer with newsletter | Dawn footer on dark `scheme-4` (#232323), newsletter on, new "Policies" link list |
| Floating WhatsApp chat button | Snippet `zx-whatsapp-float` in the layout; on/off in Storefront style |
| Instagram / TikTok feeds | **Not built.** These need an app. Add them as app blocks |

## 2. Files
Added: `assets/zx-storefront.css`, `assets/zx-collection-tabs.css`, `assets/zx-tabs.js`, `assets/zx-icon-whatsapp.svg`, `sections/zx-collection-tabs.liquid`, `sections/zx-dual-banner.liquid`, `sections/zx-store-map.liquid`, `sections/zx-breadcrumbs.liquid`, `snippets/zx-whatsapp-order.liquid`, `snippets/zx-whatsapp-float.liquid`.
Edited: `layout/theme.liquid` (stylesheet, body classes, float button), `config/settings_schema.json` (new "Storefront style" group), `config/settings_data.json` (colour schemes 1/3/4/5 added, heading font Poppins 600, centred cards, WhatsApp settings), `sections/header-group.json`, `sections/footer-group.json`, `templates/index.json`, `templates/collection.json`, `templates/product.json`, and 31 storefront locale files (added `general.breadcrumbs.*` with English as the fallback).
EComposer app files: not touched.

## 3. Tests run
| Check | Result |
|---|---|
| Static suite (JSON, schemas, template types, references, Liquid balance, CSS, JS syntax, locale parity, orphans) | PASS: 0 new errors. The 7 pre-existing errors are all in EComposer app files |
| `shopify theme check` 4.8.2 | 16 errors, the same 16 as the original theme (EComposer files). 1 new warning: `OrphanedSnippet` on `zx-whatsapp-order`. It is a false positive, because the snippet is called from the custom-Liquid block in `product.json` |
| Package check: re-extract, file parity, static re-check, Theme Check on the extracted copy | PASS |
| Rendered visual comparison against the reference | NOT VERIFIED: no preview available |
| Functional QA (menus, quick add, tabs, cart, WhatsApp links, map) | NOT VERIFIED: no preview available |

## 4. Known gaps and follow-ups
1. **The Dual image banner is added but hidden.** It needs two images: Customize › Home › Dual image banner › add images › show the section. It is hidden so empty placeholders don't appear on the live site.
2. Collection-tab handles were copied from the collections your current homepage already uses (`luxury-formals`, `barosha-silk`, `ambose-silk`, `printed-marina`, `lawn`, `velvet`, `palachi`, `china-pati-pure-silk`). Change the tabs in the editor.
3. The footer "Policies" column uses the menu handle `footer`. Create that menu in Navigation, or pick another one.
4. The tan menu band only shows on desktop (≥990px). On mobile Dawn uses its drawer menu.
5. On the reference, the Add to cart button also shows the price. This build does not.
6. Instagram and TikTok feeds need an app.

## 5. Needs checking in a browser (after upload)
Menu band and dropdowns, the button colours on product pages, the quick-add modal for products with several variants, tab switching, the WhatsApp links (number `923215096308`, from your footer), and the map embed at 390, 768 and 1440 px.

## 6. Store setup after import
Online Store › Themes › Add theme › Upload zip › leave it **unpublished** › Customize. Check Theme settings › Storefront style (colours and WhatsApp), then go through §4.

## 7. Rollback
Your original ZIP is unchanged. To roll back, re-upload it or keep your current live theme published.
