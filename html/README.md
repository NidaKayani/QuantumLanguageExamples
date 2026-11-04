# HTML + CSS examples

500 web pages written as Quantum `.sa` files, 20 in each of 25 topics. Each
page is a complete HTML document with its CSS in a `<style>` element.

A `.sa` file that starts with `<!DOCTYPE html>`, an HTML comment or an HTML
tag is compiled by Quantum's HTML front-end. It checks the markup the way an
HTML validator does, checks every stylesheet with the CSS front-end, and
prints the document as a browser builds it.

```bash
qrun 10_flexbox/03_justify_content_center.sa        # print the compiled page
qrun --strict 10_flexbox/03_justify_content_center.sa  # any problem is a compile error
qrun --test examples                                # run every example, these included
```

The pages compile with no errors and no warnings. Errors are things like an
unclosed element, an unknown property, a length with no unit or a misspelled
pseudo-class. The test runner fails a page that has any error.

## Topics

| Folder | What it shows |
| --- | --- |
| `01_text_elements` | headings, paragraphs, quotes, code, abbreviations, ruby, character references |
| `02_lists` | every list-style type, nesting, counters, description lists, custom markers |
| `03_links_navigation` | link states, navbars, breadcrumbs, pagination, tabs, dropdown and mega menus |
| `04_tables` | captions, spans, sticky headers, calendars, invoices, heatmaps (several generated from data) |
| `05_forms` | login, sign-up, validation styles, pickers, sliders, toggles, star ratings |
| `06_box_model` | padding, borders, radius, shadows, overflow, box-sizing, logical properties |
| `07_colors` | palettes in hex, rgb, hsl and hwb, named colours, color-mix, system colours |
| `08_typography` | type scales, line height, decoration, shadows, columns, drop caps, vertical text |
| `09_backgrounds_gradients` | linear, radial and conic gradients, patterns, blend modes, glass |
| `10_flexbox` | every justify-content and align-items value, wrapping, growing, common layouts |
| `11_grid` | tracks, areas, spans, dense packing, subgrid, dashboards, magazine layouts |
| `12_positioning` | relative, absolute, fixed and sticky; badges, tooltips, modals, ribbons |
| `13_selectors` | nth-child formulas, attribute selectors, combinators, `:is`, `:where`, `:has` |
| `14_pseudo_elements` | `::before`, `::after`, `::marker`, `::selection`, counters, decorations |
| `15_transitions` | timing functions, hover effects, delays, accordions |
| `16_animations` | loaders, bounces, typewriters, marquees, shimmer, orbits |
| `17_transforms` | 2D and 3D transforms, perspective, flip cards, a cube |
| `18_responsive` | media and container queries, fluid type, dark mode, reduced motion, print |
| `19_custom_properties` | ten themes, fallbacks, scoping, `@property`, `:has()` toggles |
| `20_components` | buttons, cards, alerts, tabs, toasts, pricing cards, timelines, dialogs |
| `21_page_layouts` | landing, blog, portfolio, docs, dashboard, shop, resume, 404 and more |
| `22_media_svg` | images, video, audio, SVG shapes, paths, icons and charts drawn from data |
| `23_semantics_accessibility` | landmarks, labels, skip links, live regions, focus styles, alt text |
| `24_data_visualization` | bar, column, stacked, pie, donut, gauge, heatmap, waffle and Gantt charts |
| `25_css_art_games` | chess, sudoku, dice, a piano, a clock, a solar system, pixel art |

Pages that use pictures load them from `picsum.photos`. Everything else is
plain HTML and CSS, with no scripts and no build step.
