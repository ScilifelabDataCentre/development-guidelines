---
last_reviewed: 2026-11-02
---

# Accessibility

[Accessibility regulations](../regulations/README.md#web-accessibility-directive-wad)

> [!NOTE]
> We use the [SciLifeLab brand colours](https://www.scilifelab.se/community-pages/resources/visual-identity/) in our services, but we need to keep accessibility in mind. Other services may be bound by the design restrictions of the backing host university or funding agency.

## Web Content Accessibility Guidelines (WCAG)

WCAG are a set of guidelines for making the web more accessible. The WCAG standards are versioned. The Act on Accessibility to Digital Public Services ("DOS-lagen", see [regulations/README.md](../regulations/README.md#web-accessibility-directive-wad)) requires compliance with WCAG 2.1 level AA [^1].

[How to meet WCAG](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.1&levels=aaa&hidesidebar=true)

[^1]: [Myndigheten för digital förvaltning](https://www.digg.se/webbriktlinjer/lagar-och-krav/det-har-ar-en-301-549-och-wcag). English page (less information): [Agency for Digital Government](https://www.digg.se/webbriktlinjer/about-webbriktlinjer).

## How to make your service compliant with WCAG

1. **Manual testing (always).** No automated tool is a replacement for visual inspection. Always review new or changed UI through the lens of accessibility.
2. **Spot-check with tools (table below).**
3. **Automate in CI (GitHub Actions) with [Pa11y](https://github.com/pa11y/pa11y) (once the initial issues are fixed).** Pa11y performs some automated checks against the specified website or HTML file. If improving the accessibility of an existing application, you will likely get many initial failures, which is why you should be manually testing and using the tools first. Example:
   [Pa11y workflow in Pathogens Portal](https://github.com/ScilifelabDataCentre/pathogens-portal/blob/develop/.github/workflows/pa11y_test.yaml)

| Tool                                                                           | How to use                                                       |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| [WAVE](https://wave.webaim.org/)                                               | Submit a URL to their website or use the browser extension.      |
| Screen reader, e.g. [NVDA](https://www.nvaccess.org/download/)                 | Install locally to test the experience of using the application. |
| Contrast checker, e.g. [siegemedia](https://www.siegemedia.com/contrast-ratio) | Choose background and text colours and get the contrast ratio.    |

## Tips

- Play around with the text colour (e.g. black vs white).
- In addition to checking the ratio number using the tools listed above, zoom out the page as much as possible or take physical steps away from the monitor.

## Further reading

- [Inclusive Design Principles](https://inclusive.microsoft.design/)
- [What is accessibility?](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/What_is_accessibility)
